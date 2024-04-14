from flask import Flask,request
import json
import tasks_db

app = Flask(__name__)

# get all tasks
# curl http://127.0.0.1:5000/tasks
@app.route("/tasks", methods=["GET"]) 
def get_all_tasks():
    all_tasks = tasks_db.get_all_tasks()
    # return json.dumps({'tasks': all_tasks}) 
    return all_tasks['tasks']


# get single task
# curl http://127.0.0.1:5000/tasks/{task_id}
@app.route("/tasks/<int:task_id>", methods=["GET"]) 
def get_single_task(task_id):
    task = tasks_db.get_single_task(task_id)
    return json.dumps(task)


# add new task
# curl -X POST -H "Content-Type: application/json" -d '{"title":"Add", "details":"New"}' http://127.0.0.1:5000/tasks
@app.route("/tasks", methods=["POST"])  
def add_new_task():
    data = request.json
    new_task = tasks_db.add_new_task(data)
    return json.dumps(new_task)


# Update existing task
# curl -X PUT -H "Content-Type: application/json" -d '{"title":"Item", "details":"Updated"}' http://127.0.0.1:5000/tasks/{task_id}
@app.route("/tasks/<int:task_id>", methods=["PUT"])  
def update_task(task_id):
    data = request.json
    updated_task = tasks_db.update_task(task_id, data)
    if updated_task is not None:
        return json.dumps(updated_task)
    else:
        return json.dumps({'error': 'Task not found'})
    

#  Delete task
# curl -X DELETE http://127.0.0.1:5000/tasks/{task_id}
@app.route("/tasks/<int:task_id>", methods=["DELETE"])  
def delete_task(task_id):
    deleted_task = tasks_db.delete_task(task_id)
    if deleted_task is not None:
        return json.dumps({'message': f'Task {task_id} deleted successfully'})
    else:
        return json.dumps({'error': 'Task not found'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)   