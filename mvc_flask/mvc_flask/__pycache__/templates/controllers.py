from flask import Blueprint, render_template
from models import tarefas

tarefa_controller = Blueprint("tarega", __name__)

@tarefa_controller.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)