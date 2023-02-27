# Week 1 — App Containerization

## Required Homework

### Weekly Videos
All videos in todo list watched.

### Remember to Commit Your Code
Code was committed after the streamed video, and subsequently thereafter as instructed in Gitpod. Commits on my repo can be seen as proof:

![Code Comitted](/journal/resources/images/week1/commit_proof.PNG)

### Containerize Application (Dockerfiles, Docker Compose)
#### Backend
The respective Dockerfile was added to both the backend and frontend directories on the repo:

![Dockerfile](/journal/resources/images/week1/docker_files.PNG)

The backend Dockerfile was then used to build Docker image, which was then used to create a container:

![Docker Container](/journal/resources/images/week1/docker_build_run.PNG)

I tested the container was running with ```$ docker ps``` and that the image was present with ```$ docker images```:

![Docker Test](/journal/resources/images/week1/docker_ps_images.PNG)

The above image also shows my use of the command ```$ curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json"``` which successfully returned the required data from the flask app.

I then tested that the same information could be accessed through my browser:

![Backend Success](/journal/resources/images/week1/backend_success.PNG)

I then used ```$ docker stop {CONATIANER_ID}``` to stop the container, and ```$ docker image rm backend-flask --force``` to remove the image it had created:

![Docker Remove Image](/journal/resources/images/week1/docker_rm_image.PNG)

#### Frontend
I ran the following commands to install npm into the frontend directory:
```
$ cd frontend-react-js
$ npm i
```

I then used ```$ docker build -t frontend-react-js ./frontend-react-js``` to build the frontend image (Frontend Dockerfile was added as in the "Backend" section):

![NPM Install](/journal/resources/images/week1/docker_frontend_build_run.PNG)

I then successfully tested that I could load the frontend react app in my browser:

![Frontend Success](/journal/resources/images/week1/frontend_success.PNG)

#### Docker Compose
I then created the ```docker-compose.yml``` file at the root of my project:

![Docker Compose File](/journal/resources/images/week1/docker_compose_file.PNG)

To test the Docker compose file was working I accessed it in my browser (Screenshot taken after implementing Notifications):

![Docker Compose Success](/journal/resources/images/week1/docker_compose_success.PNG)

### Document the Notification Endpoint for the OpenAI Document

I added the documentation for the Notification endpoint in the OpenAI document and tested it worked in the preview:

![OpenAI Documentation](/journal/resources/images/week1/openapi_documentation.PNG)

### Write a Flask Backend Endpoint for Notifications

For the backend of the app I added the service "notifications_activities" with pre-loaded data to view in the app, and added a route to the "api/activites/notifications" api:

![Flask Backend](/journal/resources/images/week1/app_and_service_page.PNG)

