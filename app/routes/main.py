from flask import Blueprint
from app.controllers.main import index

main_bp = Blueprint('main', __name__)

main_bp.route('/', methods=['GET'])(index)
