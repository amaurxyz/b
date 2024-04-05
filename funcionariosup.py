class Funcionrio:
    #classe abstrata
    def __init__(self, nome, idade, email,telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        
    def emprestar(self):
        repetir = False
        for x in catalogo:
            if x.titulo == z:
                if x.quantidade == 0:
                    print("Não há cópias desse livro disponíveis")
                    repetir = True
                else:
                    x.quantidade -= 1
                    x.emprestados += 1
                    repetir = True
        if repetir == False:
            print("Titulo não encontrado") 
        
    def devolver(self):
        repetir = False
        for x in catalogo:
            if x.titulo == z:
                if x.emprestados == 0:
                    print("Não há cópias desse livro emprestadas")
                    repetir = True
                else:
                    x.quantidade += 1
                    x.emprestados -= 1
                    repetir = True
        if repetir == False:
            print("Titulo não encontrado")

    def exibir_info_funcionario(self):
        return f'Título: {self.titulo}\nEditora: {self.editora}\n'


class Cliente(Funcionario):
    def __init__(self, nome, idade, email,telefone):
        super().__init__(titulo, editora, quantidade, emprestados)
        self.salario= salario
        self.turno= turno


    def exibir_info(self):
        return super().exibir_info() + f'Autor: {self.autor}\nEdiçao: {self.ediçao}\nAno: {self.ano}\nQuantidade: {self.quantidade}\nEmprestados: {self.emprestados}\n'



class Revista(Publicacao):
    def __init__(self, titulo, editora, ediçao, quantidade, emprestados):
        super().__init__(titulo, editora, quantidade, emprestados)
        self.ediçao = ediçao

    def exibir_info(self):
        return super().exibir_info() + f'Edição: {self.ediçao}\nQuantidade: {self.quantidade}\nEmprestado: {self.emprestados}\n'


class Jornal(Publicacao):
    def __init__(self, titulo, editora, data, quantidade, emprestados):
        super().__init__(titulo, editora, quantidade, emprestados)
        self.data = data

    def exibir_info(self):
        return super().exibir_info() + f'Data: {self.data}\nQuantidade: {self.quantidade}\nEmprestados: {self.emprestados}\n'