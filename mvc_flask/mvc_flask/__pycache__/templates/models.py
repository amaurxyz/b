from typing import Any

class Tarefa:
    def __init__ (self, id, descricao, concluido = False):
        self.id = id
        self.descricao = descricao
        self.concluido = concluido

tarefas = []

def add_tarefas(descricao):
    id = len(tarefas) + 1
    nova_tarefa = tarefas(id, descricao)
    Tarefa.append(nova_tarefa)
