from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras

IMG_HEIGHT = 28
IMG_WIDTH = 28

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
mnist_model = keras.models.load_model('mnist_tf_model')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/mnist', methods=['POST'])
def mnist_prediction():
    r = request
    # print(r)
    # print(r.data)
    img = None
    # convert string of image data to uint8
    # this should succeed when the request is made from Python clinet
    nparr = np.frombuffer(r.data, np.uint8)  # an array of size 572
    # print(nparr)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    # do some fancy processing here....
    '''
    # write image to file, for double check
    test_file_output = 'test_data/received.png'
    cv2.imwrite(test_file_output, img)
    '''
    # convert to tf tensor.
    # Source: https://stackoverflow.com/questions/40273109/convert-python-opencv-mat-image-to-tensorflow-image-data
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb_tensor = tf.convert_to_tensor(img_rgb)
    # Use `convert_image_dtype` to convert to floats in the [0,1] range.
    normalized_rgb_tensor = tf.image.convert_image_dtype(rgb_tensor, tf.float32)
    img_grey = tf.image.rgb_to_grayscale(normalized_rgb_tensor)
    # print(img_grey)
    small_batch = tf.expand_dims(img_grey, 0)
    pred_prob = mnist_model.predict(small_batch)[0]
    pred_label = pred_prob.argmax(axis=-1)
    print(pred_label)

    # build a response dict to send back to client
    response = {'message': 'Image received. Size={}x{}. label={}'.format(img.shape[1],
                                                               img.shape[0],
                                                               pred_label)
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200,
                    mimetype="application/json")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
