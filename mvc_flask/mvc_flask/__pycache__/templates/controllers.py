from flask import Blueprint, render_template
from models import tarefas

tarefa_controller = Blueprint("tarega", __name__)

@tarefa_controller.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@tarefa_controller.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    add_tarefa(descricao)
    return redirect(url_for('tarefa.index'))
