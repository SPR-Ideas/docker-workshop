from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    """Just simple hello world program."""
    return {"message": "Helloworld"}
