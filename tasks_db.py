import json
import os

filename = "./tasks.json"   #   Run on No IDE   #
# filename = "./DevSecOps/python/tasks_API/tasks.json"   #   Ubuntu   #
# filename = 'C:\\Users\\Stas\\Desktop\\DevOps\\DevSecOps\\python\\tasks_API\\tasks.json'   #   Windows   #
# pathlib

# Check if Json file exsist, if not create it.
def ensure_file_exists():
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump({ "next_task_id":1, "tasks":[  ]}, file)

ensure_file_exists()


# Get all tasks
def get_all_tasks():
    with open(filename, "r") as file:
        data = json.load(file)
        return data

# Get single task
def get_single_task(task_id):
    tasks = get_all_tasks()
    for task in tasks["tasks"]:
            if task['id'] == task_id:
                return json.dumps(task)              
    return json.dumps({"message": "Task not found, This slot ia empty"})

# Add new task
def add_new_task(new_task):
    tasks = get_all_tasks()
    
    title = new_task.get('title')
    details = new_task.get('details')
    if title is None or details is None:
        return json.dumps({"error": "Title and details are required fields."})
    task_id = tasks["next_task_id"]
    tasks["next_task_id"] +=1
    task = {'id': task_id, 'title': title, 'details': details}
    tasks["tasks"].append(task)
    with open(filename, "w") as file:
        json.dump(tasks, file)
    return json.dumps({"message": f"Task number {task_id} was added"})


# Update existing task
def update_task(task_id, data):
    with open(filename, "r") as file:
        tasks = json.load(file)
    for task in tasks["tasks"]:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['details'] = data.get('details', task['details'])
            with open(filename, "w") as file:
                json.dump(tasks, file)
            return task
    return None

# Delete existing task
def delete_task(task_id):
    with open(filename, "r") as file:
        tasks = json.load(file)
    for task in tasks["tasks"]:
        if task['id'] == task_id:
            tasks["tasks"].remove(task)
            with open(filename, "w") as file:
                json.dump(tasks, file)
            return task
    return None

