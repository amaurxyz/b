id=-1
listafuncionario=[]
listacliente=[]
lista_usuario = []
lista_usuario_cliente = []

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
         for i in listafuncionario:
             print(i)

    def criar_listausuario(self, nome):
        for i in listafuncionario:
            if hasattr(Funcionario, nome):
                l_nome = getattr(Funcionario, nome)
                lista_usuario.append(l_nome)
                
    def alterar_cadastro(self):
        if usuario_logado == adm:
            print("Lista de funcionários:")
            for x in listafuncionario:
                print(x)

            y = input("Qual o nome do funcionário que deseja excluir do sistema?\n")
            for i in listafuncionario:
                if i.nome == y:
                    funcionario_encontrado = y
                    sla=0
                    break
            if sla==0:
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
            for func in listafuncionario:
                print(func)

        elif operacao == "4":
            Funcionario.alterar_cadastro()
            
        elif operacao == "5":
            #chmr menu
            pass
        else: 
            while resposta!= "sim"  :
             resposta = input("Deseja fazer outra operação? (sim/não)\n")

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

