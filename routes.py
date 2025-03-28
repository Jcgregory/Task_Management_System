from flask import request, jsonify
from config import app, db
from models import Task

@app.route('/')  
def home():
    return "Hello, Flask is working!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks])

@app.route('/tasks', methods=['POST'])  
def add_task():
    data = request.json  
    if not data or 'title' not in data:  
        return jsonify({"error": "Title is required"}), 400  

    new_task = Task(title=data['title'], completed=data.get('completed', False))
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task Added", "id": new_task.id}), 201  

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)   
    data = request.json
    task.title = data.get('title', task.title)  
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({"message": "Task Updated"})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task Deleted"})

@app.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    Task.query.delete()
    db.session.commit()
    return jsonify({"message": "All Tasks Deleted"})


if __name__ == '__main__':
    print('Flask is working')
    app.run(debug=True)
