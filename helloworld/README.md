# Simple Web App

This is a sample FastAPI project that responds with the message "hello-world" when you access the default route `/`.

## Building the Docker Image

Navigate to the `helloworld` directory and build the Docker image with the following commands:

```shell
$ cd helloworld/
$ docker build -t sample-app .
```

## Running the container
```shell
$ docker run -it --rm --name mycontainer sample-app
```
