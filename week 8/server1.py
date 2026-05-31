from fastapi import FastAPI
import uvicorn
app=FastAPI()





@app.get("/items/{item_id}")
def get_item(item_id:int):
    return {"item_id":item_id}


if __name__ == "__main__":
    uvicorn.run("server1:app", host="127.0.0.1", port=8000, reload=True)

