from hashlib import sha256
#laura
usuario_logado = None
lista_usuario=[]
lista_senha=[] 
status="não logado"

#melissa
id=-1
listafuncionario=[]
listacliente=[]
lista_usuario = []
lista_usuario_cliente = []

def verificar_login():
    if status!="logado":
        pass
    else:
        print("você deve fazer login para poder continuar")
        logar()
        

def criar_login ():  
        usuario_logado = input("digite seu nome:  \n")
        while r == 1:
            for x in lista_usuario :
                if usuario_logado == x: 
                    nova_senha=input("crie sua senha:\n")
                    criptoSenha= sha256(nova_senha.encode()).hexdigest()
                    lista_senha.append(criptoSenha)
                else:
                    print("usuario não encontrado")
                    r= -1
                    while r!=1 or r!=2:
                        r = input("digite [1] para tentar criar o login novamente \n [2] voltar para o menu")
                        if r== 2 :
                            print("chamar menu")
                        

def logar( ):
        status="não logado"
        print("digite suas informações para fazer login")
        usuario_logado = input("digite seu nome de usuario \n")
        senha = input("digite sua senha")
        while status=="não logado":
            x=len(lista_usuario)
            for y in range(x) :
                if usuario_logado == lista_usuario[y]:
                    if sha256(senha.encode()).hexdigest() == lista_senha[y]:
                        print("usuario e senha validos. Bem vindo(a) ", usuario_logado)
                        status="logado"
                        #chamar menu
                
                    else:
                        print("usuario e/ou senha invalidos. Tente novmente")
        #voltar no menu


        

catalogo = []
emprestado = []
estoque = 0

def logout(status, usuario_logado, senha):
    status="não logado"
    usuario_logado= "nenhum usuario logado"
    senha = None
    logar()

#parte da mirella
def adicionar_item(item):
    catalogo.append(item)

def buscar_item(self):
    for item in catalogo:
        if item.titulo == self.titulo:
            return item
    return None

def mostrar_catalogo():
    for item in catalogo:
        print(item.exibir_info())

def menu_geral():
    menu = int(input("Sigite para: [1] info. Livros \n [2] info. funcionários  \n[4] cadastro cliente: \n   "))
    match menu:
        case 1:
            pass
        case 2:
            menu_funcionario() 
        case 3:  
            pass


#parte da melissa
class cadastro:
    def __init__(self, nome, idade, numero, email, endereco):
        self.nome = nome
        self.idade= idade
        self.numero = numero
        self.email = email
        self.endereco = endereco

    def __repr__(self):
        return f"{self.id}\n {self.nome}\n {self.idade}\n {self.numero}\n {self.email}"

class Funcionario(cadastro):
    def __init__(self, nome, idade, numero, email, endereco, salario, turno):
        super().__init__(nome, idade, numero, email, endereco)
        self.__salario = salario
        self.__turno= turno

    @property
    def mostrar_salario(self):
        return f"O novo salário do funcionário(a) é {self.__salario}"

    @mostrar_salario.setter
    def mudar_salario(self, novo_salario):
        self.__salario = novo_salario

    @property
    def mostrar_numero(self):
        return f"O novo número do funcionário(a) é {self.__numero}"

    @mostrar_numero.setter
    def mudar_numero(self, novo_numero):
        self.__numero = novo_numero

    @property
    def mostrar_idade(self):
        return self.__idade

    @mostrar_idade.setter
    def mudar_idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def mostrar_email(self):
        return self.__email

    @mostrar_email.setter
    def mudar_email(self, novo_email):
        self.__email = novo_email

    @property
    def mostrar_turno(self):
        return self.__turno

    @mostrar_turno.setter
    def mudar_turno(self, novo_turno):
        self.__turno = novo_turno

    def cadastrarfuncionario(self):
        listafuncionario.append(self)
        #salva as variaveis novofuncionario
       
        
    def apresentar_funcionarios(self):
        #mostra a lista com todas as informações dos funcionarios
         i=len(listafuncionario)
         for i in range(0,i,1):
          print(listafuncionario[i])
          
    def criar_listausuario(self, nome):
        #funciona?
        # salva o atributo nome dentro de um vetor para usar no login
        for funcionario in listafuncionario:
            if hasattr(funcionario, nome):
                l_nome = getattr(funcionario, nome)
                lista_usuario.append(l_nome)
                

    def alterar_cadastro(self):
        if usuario_logado == adm:
            print("Lista de funcionários:")
            for x in listafuncionario:
                print(x)
            y = int(input("Qual o id do funcionário que deseja excluir do sistema?\n"))
            funcionario_encontrado = None

            for x in listafuncionario:
                if x.id == y:
                    funcionario_encontrado = x
                    break

            if funcionario_encontrado:
                z = input(f"O funcionário encontrado é: {funcionario_encontrado}. Confirma a alteração? (sim/não)\n")
                if z.lower() == "sim":
                    f = int(input("[1] - mudar número\n[2] - mudar salário\n[3] - mudar email\n[4] - turno: "))
                    if f == 1:
                        a = input("Digite o novo número do funcionário: ")
                        self.mudar_numero(a)
                    elif f == 2:
                        a = input("Digite o novo email do funcionário: ")
                        self.mudar_email(a)
                    elif f == 3:
                        a = input("Digite o novo salário do funcionário: ")
                        self.mudar_salario(a)
                    elif f == 4:
                        a = input("Digite o novo turno do funcionário: ")
                        self.mudar_turno(a)
                else:
                    print("Funcionário não encontrado.")
            else:
                print("Apenas o administrador pode mudar as informações de cadastro de funcionários.")

def removerfuncionario():
    print("Lista de funcionários:")
    for x in listafuncionario:
        print(x)
    y = int(input("Qual o id do funcionário que deseja excluir do sistema?\n"))
    funcionario_encontrado = None
    
    for x in listafuncionario:
        if x.id == y:
            funcionario_encontrado = x
            break

    if funcionario_encontrado:
        z = input(f"O funcionário encontrado é: {funcionario_encontrado}. Confirma a remoção? (sim/não)\n")
        if z.lower() == "sim":
            listafuncionario.remove(funcionario_encontrado)
            print("Funcionário removido com sucesso.")
        else:
            print("Remoção cancelada.")
    else:
        print("Funcionário não encontrado.")


def menu_funcionario():
    #aplica as funções criadas com o objeto funcionario
    resposta = "sim"
    while resposta.lower() == "sim":
        operacao=input("O que deseja fazer? Digite:\n 1 - Para adicionar novo funcionário\n 2 - Para remover\n 3 - Verificar a lista de funcionários\n 4 - alterar cadastro de funcionario\n 5- Voltar ao menu\n")

        if operacao == "1":
            aux="0"
            if aux=="0":
                aux="a"
                id= 0
            else:
                id=id+1
            #adiciona novo funcionario
            nome = input("Qual o nome do funcionário? \n exemplo -> fulano \n")
            lista_usuario.append(nome)

            while True and idade>18 and idade<=100:
                try:
                    idade=int(input("digite a idade do funcionario:\n"))
                    break
                except:
                    print("digite uma idade valida")

            numero = input("Digite o número de celular ou telefone do funcionário:\n exemplo -> 940028922\n")   
            while True:
                try:
                    numero=int(input("digite o numero de telefone ou celular do funcionario:\n"))
                    break
                except:
                    print("digite apenas os numeros")

            email = input("Digite o email do funcionário:\n fulaninho@gmail.com\n")
            
            salario= input("Digite o salário do funcionário:\n exemplo-> xxxx.xx \n")
            while True:
                try:
                    salario=float(input("digite o salario do funcionario:\n"))
                    break
                except:
                    print("digite um salarop valido")
            aux1=-1 
            while aux1<1 or aux1>3:
                aux1 = int(input("Qual o turno do funcionário? digite [1]- manhã [2]- tarde [3]- noite):\n"))
                if aux1==1:
                        turno ="manhã"
                elif aux1==2:
                        turno = "tarde"
                elif aux1==3:
                        turno="noite"
                else:
                    print("numero invalido. digite uma das opções dadas:\n")
            novo_funcionario = Funcionario(id, nome, idade, numero, email, salario, turno)
            novo_funcionario.cadastrarfuncionario()
            
        elif operacao == "2":
            #função auto-explicativa
            removerfuncionario()

        elif operacao == "3":
            #mostra a lista de funcionarios 
            print("Lista de funcionários:")
            for novo_funcionario in listafuncionario:
                print(novo_funcionario)

        elif operacao == "4":
            Funcionario.alterar_cadastro()
            
        elif operacao == "5":
            #chmr menu
            pass
        else: 
            while resposta!= "sim"  :
             resposta = input("Deseja fazer outra operação? (sim/não)\n")


#parte da melissa
class Cliente(cadastro):
    def __init__(self, nome, idade, numero, email, endereco, qtdlivro):
        super().__init__(nome, idade, numero, email, endereco)
        self.__qtdlivro = qtdlivro

    @property
    def mostrar_numero(self):
        return f"O novo número do cliente é {self.__numero}"

    @mostrar_numero.setter
    def mudar_numero(self, novo_numero):
        self.__numero = novo_numero

    @property
    def mostrar_idade(self):
        return self.__idade

    @mostrar_idade.setter
    def mudar_idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def mostrar_email(self):
        return self.__email

    @mostrar_email.setter
    def mudar_email(self, novo_email):
        self.__email = novo_email

    def cadastrarcliente(self):
        listacliente.append(self)
        #salva as variaveis novocliente
        
    def apresentar_clientes(self):
        #mostra a lista com todas as informações dos clientes
         i=len(listacliente)
         for i in range(0,i,1):
          print(listacliente[i])
          
    def criar_listausuario(self, nome):
        #funciona?
        # salva o atributo nome dentro de um vetor para usar no login
        for cliente in listacliente:
            if hasattr(cliente, nome):
                l_nome = getattr(cliente, nome)
                lista_usuario_cliente.append(l_nome)
                

    def alterar_cadastro(self):
        if usuario_logado == funcionario:
            print("Lista de clientes:")
            for m in listacliente:
                print(x)
            n = int(input("Qual o id do cliente que deseja excluir do sistema?\n"))
            cliente_encontrado = None

            for m in listacliente:
                if m.id == n:
                    cliente_encontrado = m
                    break

            if cliente_encontrado:
                z = input(f"O cliente encontrado é: {cliente_encontrado}. Confirma a alteração? (sim/não)\n")
                if z.lower() == "sim":
                    f = int(input("[1] - mudar número\n[2] - mudar idade\n[3] - mudar email\n[4] quantidade de livros "))
                    if f == 1:
                        a = input("Digite o novo número do cliente: ")
                        self.mudar_numero(a)
                    elif f == 2:
                        a = input("Digite a nova idade do cliente: ")
                        self.mudar_idade(a)
                    elif f == 3:
                        a = input("Digite o novo email do cliente: ")
                        self.mudar_email(a)
                    elif f == 4:
                        a = input("Digite o novo livro do cliente: ")
                        self.mudar_qtdlivros(a)
                else:
                    print("Cliente não encontrado.")
            else:
                print("Apenas o administrador pode mudar as informações de cadastro de clientes.")

def removercliente():
    print("Lista de clientes:")
    for m in listacliente:
        print(x)
    n = int(input("Qual o id do cliente que deseja excluir do sistema?\n"))
    cliente_encontrado = None
    
    for m in listacliente:
        if m.id == n:
            cliente_encontrado = m
            break

    if cliente_encontrado:
        z = input(f"O cliente encontrado é: {cliente_encontrado}. Confirma a remoção? (sim/não)\n")
        if z.lower() == "sim":
            listacliente.remove(cliente_encontrado)
            print("Cliente removido com sucesso.")
        else:
            print("Remoção cancelada.")
    else:
        print("Cliente não encontrado.")


def menu_cliente():
    #aplica as funções criadas com o objeto cliente
    resposta = "sim"
    while resposta.lower() == "sim":
        operacao=input("O que deseja fazer? Digite:\n 1 - Para adicionar novo cliente\n 2 - Para remover\n 3 - Verificar a lista de clientes\n 4 - alterar cadastro de cliente\n 5- Voltar ao menu\n")

        if operacao == "1":
            aux="0"
            if aux=="0":
                aux="a"
                id= 0
            else:
                id=id+1
            #adiciona novo cliente
            nome = input("Qual o nome do cliente? \n exemplo -> fulano \n")
            lista_usuario_cliente.append(nome)

            while True and idade>18 and idade<=100:
                try:
                    idade=int(input("digite a idade do cliente:\n"))
                    break
                except:
                    print("digite uma idade valida")

            numero = input("Digite o número de celular ou telefone do cliente:\n exemplo -> 940028922\n")   
            while True:
                try:
                    numero=int(input("digite o numero de telefone ou celular do cliente:\n"))
                    break
                except:
                    print("digite apenas os numeros")

            email = input("Digite o email do cliente:\n fulaninho@gmail.com\n")
        

            novo_cliente = Cliente(id, nome, idade, numero, email)
            novo_cliente.cadastrarcliente()
            
        elif operacao == "2":
            #função auto-explicativa
            removercliente()

        elif operacao == "3":
            #mostra a lista de clientes 
            print("Lista de clientes:")
            for cliente in listacliente:
                print(cliente)

        elif operacao == "4":
            Cliente.alterar_cadastro()
            
        elif operacao == "5":
            #chmr menu
            pass
        else: 
            while resposta!= "sim"  :
             resposta = input("Deseja fazer outra operação? (sim/não)\n")

#parte marcel e milela

class Publicacao:
    #classe abstrata
    def __init__(self, titulo, editora, quantidade, emprestados):
        self.titulo = titulo
        self.editora = editora
        self.quantidade = quantidade
        self.emprestados = emprestados

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

    def exibir_info(self):
        return f'Título: {self.titulo}\nEditora: {self.editora}\n'


class Livro(Publicacao):
    def __init__(self, titulo, editora, autor, ediçao, ano, quantidade, emprestados):
        super().__init__(titulo, editora, quantidade, emprestados)
        self.autor = autor
        self.ediçao = ediçao
        self.ano = ano

    def exibir_info(self):
        return super().exibir_info() + f'Autor: {self.autor}\nEdiçao: {self.ediçao}\nAno: {self.ano}\nQuantidade: {self.quantidade}\nEmprestados: {self.emprestados}'



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