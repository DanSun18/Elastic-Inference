from locust import HttpLocust, TaskSet, between, constant
import json

def index(l):
    response = l.client.get("/")
    print(response.text)
    print('-------------------')
    # print(response.text)

def mnist(l):
    img_file = '../test_data/img_1.jpg'
    img = open(img_file, 'rb').read()
    response = l.client.post("/mnist", data=img)
    print(response.text)
    # print(json.loads(response.text))

class UserBehavior(TaskSet):
    # tasks = {index: 1}
    tasks = {mnist: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = constant(30)