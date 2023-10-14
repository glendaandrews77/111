from flask import Flask, request
from app.database import task

app = Flask(__name__)


@app.get("/tasks")
def get_all_tasks():
    tasks = task.scan()
    out = {
        "task": tasks,
        "ok": True,
    }
    return out
@app.get("/tasks/{pk}")
def get_task_by_id(pk: int):
    single_task = task.select_by_id(pk)
    if not single_task:
        return {"ok": False, "message": "Not found"}, 404
    else:   
        out = {
            "ok": True,
            "task": single_task
        }
    return out


@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    out ={
        "ok": True,
        "message": "Success"
    }
 
    return"", 201

@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update_by_id(pk, task_data)
    return"",204

@app.delete("/tasks/int:pk>")
def delete_task(pk):
    task.delete(pk)
    return"", 204


