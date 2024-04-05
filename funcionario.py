from bibliotecasup3 import *

def adicionar_item(item):
    lista_funcionario.append(item)

def buscar_funcionario(self):
    for item in lista_funcionario:
        if item.nome == self.nome:
            return item
    return None

def mostrar_catalogo():
    for item in lista_funcionario:
        print(item.exibir_info_funcionario())


catalogo = []
emprestado = []
estoque = 0

sair = False
while sair == False:
    print('Menu')
    print('Escolha uma das opções.')
    print('[1] Cadastrar item.')
    print('[2] Emprestar item')
    print('[3] Devolver item')
    print('[4] Exibir o catálogo')
    print('[5] Sair')

    opcao = input()
    match opcao:
        case '1':
            print('Qual item você quer cadastrar?')
            print('[1] Livro')
            print('[2] Revista')
            print('[3] Jornal')

            opcao2 = input()
            print('Informações da publicação:')
            quantidade = 0
            titulo = input('Informe o título:')
            editora = input('Informe a editora:')

            match opcao2:
                case '1':
                    autor = input('Informe o autor:')
                    ediçao = input('Informe a edição:')
                    ano = input('Informe o ano de publicação:')
                    quantidade = int(input('Informe a quantidade que você quer cadastrar:'))
                    livro = Livro(titulo, editora, autor, ediçao, ano, quantidade, 0)
                    estoque += 1
                    if estoque-1 != 0:
                        repetir = False
                        for x in catalogo:
                            if titulo == x.titulo and ediçao == x.ediçao:
                                x.quantidade += quantidade
                                repetir = True
                        if repetir == False:
                            adicionar_item(livro)
                    else: 
                        adicionar_item(livro)

                case '2':
                    ediçao = input('Informe a edição:')
                    quantidade = input('Informe a quantidade que você quer cadastrar:')
                    revista = Revista(titulo, editora, ediçao, quantidade, 0)
                    estoque += 1
                    if estoque-1 != 0:
                        repetir = False
                        for x in catalogo:
                            if titulo == x.titulo and ediçao == x.ediçao:
                                x.quantidade += quantidade
                                repetir = True
                        if repetir == False:
                            adicionar_item(revista)
                    else: 
                        adicionar_item(revista)

                case '3':
                    data = input('Informe a data de publicação:')
                    quantidade = input('Informe a quantidade que você quer cadastrar:')
                    jornal = Jornal(titulo, editora, data, quantidade, 0)
                    estoque += 1
                    if estoque-1 != 0:
                        repetir = False
                        for x in catalogo:
                            if titulo == x.titulo:
                                x.quantidade += quantidade
                                repetir = True
                        if repetir == False:
                            adicionar_item(jornal)
                    else: 
                        adicionar_item(jornal)

        case '2':
            z = input('Qual item você quer emprestar?')
            nome = input('Nome do cliente que vai alugar: ')
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

        case '3':
            z = input('Qual item você quer devolver?')
            nome = input('Nome do cliente que vai devolver: ')
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

        case '4':
            print('Catálogo:')
            mostrar_catalogo()

        case '5':
            print('Saindo...')
            sair = True