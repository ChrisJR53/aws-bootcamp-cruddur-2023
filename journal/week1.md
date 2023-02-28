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
For the backend of the app I added the service "notifications_activities" with pre-loaded data to view in the Flask app, and added a route to the "api/activites/notifications" api:

![Flask Backend](/journal/resources/images/week1/app_and_service_page.PNG)

### Write a React Page for Notifications
I added the react page for notifications and added an import link to the page in the React app:

![React Page](/journal/resources/images/week1/notification_add_to_app.PNG)

### Run DynamoDB Local Container and ensure it works
I first installed the DymnamoDB table and then initialised a test table with the following commands:
```
$ aws dynamodb create-table \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD
```

Then I created an item in the table with:
```
$ ws dynamodb put-item \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}}' \
    --return-consumed-capacity TOTAL  
```

These commands came from [100 Days of Cloud](https://github.com/100DaysOfCloud/challenge-dynamodb-local) and successfully created a table and item in DynamoDB for me:

![Install DynamoDB](/journal/resources/images/week1/dynamodb_create_table.PNG)

I then tried useing a few basic commands to test it was functioning correctly:

![DynamoDB Test](/journal/resources/images/week1/dynamodb_table_usage.PNG)

### Run Postgres Container and ensure it works
I installed the Postgres client into my Gitpod workspace by adding the following lines to the gitpod initialization file:
```
  - name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
```

I then logged into the Postgres table and tested some basic commands:

![Postgres Table](/journal/resources/images/week1/postgres_table_usage.PNG)

## Homework Challenges
### Push and tag an image to DockerHub
I downloaded the Github repo to my desktop and then built the images for the frontend react app and backend flask app on WSL 2. Using ```$ docker images``` I was able to view all the images on my local machine:

![WSL2 Docker Images](/journal/resources/images/week1/external_docker.PNG)

Below you can also see the images in Docker Desktop as well:

![Docker Desktop](/journal/resources/images/week1/docker_desktop.PNG)

I used the command ```$ docker tag 41e19adb0b0c chrisjrobinson/backend-flask``` to tag the image with my personal Docker Hub account name and then used ```$ docker push chrisjrobinson/backend-flask``` to push the image to my Docker Hub account (The previous commands were reproduced to uppload the frontend-react-js image as well):

![Docker Tag and Push](/journal/resources/images/week1/docker_hub_tag_push.PNG)

Here you can see the images successfully uploaded to my Docker Hub account:

![Docker Hub Proof](/journal/resources/images/week1/docker_hub_proof.PNG)

### Learn how to install Docker on your local machine and get the same containers running outside of Gitpod / Codespaces
I installed [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) on my local machine and used the ```$ docker compose up``` command in WSL 2 to build the environment for the containers:

![Docker Desktop Compose Up](/journal/resources/images/week1/docker_local.PNG)

Initially I couldn't access the frontend or backend apps at all until I changed the ```FRONTEND_URL``` to ```0.0.0.0:3000``` and the ```BACKEND_URL``` to ```0.0.0.0:4567``` in the docker-compose.yml file:

![Compose File Change](/journal/resources/images/week1/docker_local_changes.PNG)

This allowed me to access the frontend app running locally:

![Frontend Local](/journal/resources/images/week1/docker_local_frontend.PNG)

As well as the backend locally, adding the suffix ```/api/activites/home``` to the URL:

![Backend Local](/journal/resources/images/week1/docker_local_backend.PNG)

However as you can see in my local frontend app screenshot 2 images above, I couldn't get the frontned to comunicate with the backend locally, which is why I classed this homework challenge as only a partial success.
