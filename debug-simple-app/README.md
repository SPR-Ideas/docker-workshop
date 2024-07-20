# Debugging Task 
This Project contains a web app with its docker file.But when developer tries to run the container, it exits with  a `exit code 1` it fails.Can you find the issue with the container make the container available up running.
```shell
$ docker ps -al
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS                     PORTS     NAMES
d687a27d6fdb   sample-app   "uvicorn main:app --…"   3 seconds ago   Exited (1) 2 seconds ago             mycontainer

```

## Simple Web App

This is a sample FastAPI project that responds with the message "hello-world" when you access the default route `/`.

## Building the Docker Image

Navigate to the `helloworld` directory and build the Docker image with the following commands:

```shell
$ cd debug-simple-app/
$ docker build -t sample-app .
```

## Running the container
```shell
$ docker run -it -d --name mycontainer sample-app
```

