from fastapi import FastAPI, Request
from time import time

app = FastAPI()


def write_log(content):
    """Write logs to a txt file."""
    with open("log.txt", "a") as fp:
        fp.write(f"[{time()}]: {content} \n")


@app.get("/")
def hello_world(req: Request):
    """Just simple hello world program."""
    write_log(req.client.host)
    return {"message": "Helloworld"}
