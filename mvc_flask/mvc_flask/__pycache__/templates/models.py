from typing import Any

class Tarefa:
    def __init__ (self, id, descricao, concluido = False):
        self.id = id
        self.descricao = descricao
        self.concluido = concluido

tarefas = []

t = Tarefas(1, "Comer")
tarefas.append(t)
t2 = Tarefas(2, "Dormir", True)
tarefas.append(t2)