# Debugging Task

This project includes a web app with its Dockerfile. However, when developers try to run the container, it shows that it is running, but they are unable to access the container from their local machines even after mapping the ports.

## Steps to Reproduce the issues

1. Pull the image from the registry:
    ```shell
    docker pull pradeepragul/amd-build
    ```

2. Run the container and map the ports:
    ```shell
    docker run -it -p 8000:8000 pradeepragul/amd-build
    ```

3. The output shows:
    ```shell
    INFO:     Started server process [1]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```

## Expected Behavior

You should be able to access the web app via your browser at `http://127.0.0.1:8000`.
``` &#8203;:citation[oaicite:0]{index=0}&#8203;
