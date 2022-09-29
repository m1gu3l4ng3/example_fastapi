from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    """
    Endpoint to return hello
    """
    return {"Hello": "World"}
