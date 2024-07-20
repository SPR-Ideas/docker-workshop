# Logger App

This is a FastAPI-based web application that logs the details of clients visiting the website into a `log.txt` file. This specific use case requires persistent storage rather than container built-in storage since container storage is not persistent and all files are removed once the container restarts.

## Features

- Logs client visits to `log.txt`
- Uses persistent storage to ensure logs are not lost on container restart

## Prerequisites

- Docker installed on your machine

## Building the Docker Image

To build the Docker image for the Logger App, follow these steps:

1. Navigate to the project directory:
    ```shell
    cd logger-app/
    ```

2. Build the Docker image:
    ```shell
    docker build -t logger-app .
    ```

## Running the Docker Container with Persistent Storage

To run the Docker container and ensure that the logs are stored persistently, you need to attach a volume to the container. Follow these steps:

1. Create a directory on your host machine to store the logs:
    ```shell
    mkdir -p /path/to/your/log/directory
    ```

2. Run the Docker container with the volume attached:
    ```shell
    docker run -d -p 8000:8000 -v /path/to/your/log/directory:/app/logs --name logger-container logger-app
    ```

## Accessing the Application

Once the container is running, you can access the application in your web browser at:
http://localhost:8000
