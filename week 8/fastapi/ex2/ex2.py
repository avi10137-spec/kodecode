from fastapi import FastAPI
import uvicorn
app = FastAPI()
from datetime import datetime
@app.get("/")
def home():
    return  {"service": "my-api", "version": "1.0"}
@app.get("/users/admin")
def get_admin():
    return {"role": "admin", "access": "full"}


@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id":user_id,"name":"avi","email":"avi11@gmail.com"}

@app.get("/calc/{a}/{op}/{b}")
def get_calculate(a,op,b):
    dikt_function={"add":lambda c,d:c+d,
                   "sub":lambda c,d:c-d,
                   "multi":lambda c,d:c*d,
                   "div":lambda c,d:c/d}
    result=dikt_function[op](int(a),(b))
    try:
        return {"operation":op,"result":result}
    except ZeroDivisionError as e:
        return {"exeption":e}
@app.get("/status")
def get_status():
    return {"ex2":datetime.now()}



if __name__=="__main__":
    uvicorn.run("ex2:app", host="127.0.0.1", port=8001, reload=True)
