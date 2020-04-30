from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/mnist')
def mnist_prediction():
    return None


@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.frombuffer(r.data, np.uint8)  # an array of size 572
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # do some fancy processing here....
    '''
    # write image to file, for double check
    test_file_output = 'test_data/received.png'
    cv2.imwrite(test_file_output, img)
    '''

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1],
                                                               img.shape[0])
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
