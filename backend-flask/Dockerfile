FROM python:3.10-slim-buster

# Inside container create and run from directory called backend-flask
WORKDIR /backend-flask

# Outside container -> inside container
COPY requirements.txt requirements.txt

# Install python libraries inside container working directory
RUN pip3 install -r requirements.txt

# Copy files in external work dir to container work dir
COPY . .

# Set env vars inside container
ENV FLASK_ENV=development

EXPOSE ${PORT}

# Command to run flask
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]