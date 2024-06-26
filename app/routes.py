from flask import current_app as app, request, jsonify, render_template
from app.models import Todo
from app import db

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'content': todo.content,
        'is_done': todo.is_done
    } for todo in todos])

@app.route('/todo/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'content': todo.content,
        'is_done': todo.is_done
    })

@app.route('/todo', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = Todo(
        title=data['title'],
        content=data['content'],
        is_done=data.get('is_done', False)
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({
        'id': new_todo.id,
        'title': new_todo.title,
        'content': new_todo.content,
        'is_done': new_todo.is_done
    }), 201

@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    todo = Todo.query.get_or_404(id)

    if 'title' in data:
        todo.title = data['title']
    if 'content' in data:
        todo.content = data['content']
    if 'is_done' in data:
        todo.is_done = data['is_done']

    db.session.commit()
    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'content': todo.content,
        'is_done': todo.is_done
    })

@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

@app.route('/')
def index():
    return render_template('todos.html')
