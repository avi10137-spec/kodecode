from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/ping")
def get_ping():
    return {"status":"pong"}

@app.get("/greet/{name}")
def get_greet(name):
    return {"message":f"welcome,{name}!"}

if __name__ == "__main__":
    uvicorn.run("ex1:app", host="127.0.0.1", port=8001, reload=True)