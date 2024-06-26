from flask import Blueprint
from app.controllers.todos import get_todos, get_todo, create_todo, update_todo, delete_todo

api_bp = Blueprint('api', __name__)

api_bp.route('/todos', methods=['GET'])(get_todos)
api_bp.route('/todo/<int:id>', methods=['GET'])(get_todo)
api_bp.route('/todo', methods=['POST'])(create_todo)
api_bp.route('/todo/<int:id>', methods=['PUT'])(update_todo)
api_bp.route('/todo/<int:id>', methods=['DELETE'])(delete_todo)
