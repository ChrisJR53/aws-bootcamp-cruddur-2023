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

