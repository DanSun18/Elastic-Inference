# Elastic-Inference
Term Project for ECE 590: Data Analytics at Scale in the Cloud. The project deploys a pre-trained CNN model for MNIST, aceepts picuters from the MNIST dataset, and returns a label prediction. It is configured to run on Google App Engine. 

## Deploying the project

Create a new project. 

Clone the repository into your Cloud environment.

Create a virtual environment in Google Cloud Shell with  ```virtualenv --python python3 ~/envs/e_inf ```

Activate the virtual environment by ```source  ~/envs/e_inf/bin/activate```

Change current directory to your clone of this repostiroy. Head into the `app` folder

Install the necessary dependencies with ```pip install -r requirements.txt``` or ```make install```

Run the app in Cloud Shell with ```python main.py```

### Previewing the app

While the app is running on Cloud Shell, you can access it by clicking the Web Preview button. 

### Deploying to App Engine
Create an application with ```gcloud app create```. (You may not need to do this step if you have created an app on Google App Engine before.)

#### Build a docker image by running the following command

Get project id by running ```gcloud config get-value project```

Run ```gcloud builds submit --tag gcr.io/[project-id]/mnist-pred-image``` or whatever image name you want to give it. You can verify it is added with ```gcloud container images list```

Deploy the app with ```gcloud app deploy --image-url=gcr.io/[project-id]/mnist-pred-image``` (These steps are taken because simply running ```gcloud app deploy``` resulting in Cloud Build to fail because of memory issues ```OSError: [Errno 12] Cannot allocate memory```).

Note: you may wish to disable the application when you are done with it. 

## Running Load Test

Go to ```test/```, run ```pip install -r requirements-test.txt```. (If you are on MS Windows run ```pip install locustio``` instead)

Go to ```../load_test```. Start the locust server by running ```./start_locust.sh``` (verified on Linux only)

### Running on multiple processes
Link: https://docs.locust.io/en/stable/quickstart.html

Running too many requests can saturate a CPU. Therefore you can run on multiple processes:

Start the master by typing ```locust  --master```.

Start as many slaves as you want by typing ```locust --slave```

Head to http://127.0.0.1:8089 to the Web UI. (On MS Windows you'd have to set firewall to open that port before starting Locust)

## Helpful Links

Project Link: https://noahgift.github.io/cloud-data-analysis-at-scale/projects.html#team-project

Boilerplate code from https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard_python37/hello_world

How to send and receive images with Flask: https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594

MNIST dataset as jpg: https://www.kaggle.com/scolianni/mnistasjpg/data
