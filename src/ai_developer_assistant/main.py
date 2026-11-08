from fastapi import FastAPI

app = FastAPI(title="AI Developer Assistant")


@app.get("/")
def read_root():
    return {"message": "AI Developer Assistant is running"}