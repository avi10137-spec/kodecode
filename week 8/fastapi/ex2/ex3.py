from fastapi import FastAPI
import uvicorn
app = FastAPI()
grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}
@app.get("/students")
def get_student():
    list_student=[]
    for g in grades.values():
        list_student.append(g)
    return list_student

@app.get("/student/top")
def get_top_student():
    list_grades=list(grades.values())
    maxi=list_grades[0]
    for g in list_grades:
        if g["grade"]>maxi["grade"]:
            maxi=g
    return maxi
@app.get("/students/average")
def get_average():
    list_grades=list(grades.values())
    sumi=0
    for grade in list_grades:
        sumi+= grade["grade"]
    average=len(list_grades)/sumi
    return average









if __name__=="__main__":
    uvicorn.run("ex3:app", host="127.0.0.1", port=8001, reload=True)