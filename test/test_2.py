from __future__ import print_function
import requests
import json
# import cv2

addr = 'http://localhost:8080'
test_url = addr + '/mnist'
img_file = 'test_data/img_1.jpg'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = open(img_file, 'rb').read()

'''
img = cv2.imread(img_file)
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(),
                         headers=headers)
'''
# decode response
response = requests.post(test_url, data=img, headers=headers)
print(response)
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}

response = requests.get('http://localhost:8080/')
print(response.text)
