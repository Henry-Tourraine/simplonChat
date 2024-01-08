from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import app

app.mount("/public", StaticFiles(directory="public", html = True), name="public")
app.mount("/", StaticFiles(directory="uml", html = True), name="uml")


@app.get("/api")
async def root():
    return {"message": "Hello World"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)