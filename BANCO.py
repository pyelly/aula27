#CADASTRO DE USUÁRIO E SENHA
saldo = 0.0
while True:
    #MENU PRINCIPAL
    print("Bem vindo! \n Digite 1. cadastrar 2.login 3.Encarrar")
    #LER A ESCOLHA DO USUÁRIO
    escolha_menu = int(input())

    #SE O USUARIO ESCOLHER CADASTRO
    if escolha_menu ==1:
        #cria um usuario e uma senha com tipo string
        usuario = input("crie um nome de usuario ")
        senha = input("crie uma senha ")
    elif escolha_menu == 2: #se usuario escolher login
        #comparar as inf. cadastradas com uma leitura
        login_usuario = input("Digite seu usuario ")
        login_senha = input("digite sua senha ")
        if login_usuario == usuario and login_senha == senha:
            print("LOGIN REALIZADO COM DIVAÇÃO")
            #SE LOGIN CORRETO, ENTRA NO 
            #MENU PRINCIPAL DO APP
        while True: #EQUANTO QUE EXIBIRA O MENU PRINCIPAL
            print("1. DEPOSITO 2. SACAR 3. EXTRATO 4. ENCERRRAR")
            escolha_principal = int(input())
            if escolha_principal ==1: #se usuario escolher desposito
                #LE O VALOR A SER DEPOSITADO
                valor_deposito = float(input("Digite o valo do deposito "))
                saldo = saldo + valor_deposito #ATUALIZA O VALOR
                print("NOVO SALDO É " , saldo)
                valor_saque = float(input("digite o valor do saque"))
                senha_saque = input("Digite sua senha: ")
                if senha_saque == senha: # se senha correta
                    saldo = saldo - valor_saque #subtrai o valor do saldo
                else:
                    print("Senha incorreta")
            elif escolha_principal == 3: #Se usuario escolhar pix
                valor_pix = float(input("digite o valor do pix "))
                senha_pix = input("digite sua senha")
                if senha_pix == senha:
                    saldo = saldo - valor_pix
        else:
            print("senha incorreta")
    elif escolha_principal == 4: #se usuario escolher vizualizar
        senha_extrato = input("digite sua senha ")
        if senha_extrato == senha:
            print("extrato: ", saldo)
        else:
            print("senha incorreta")
    elif escolha_principal == 5: #encerrar
        senha_encerrar = input("digite sua senha")
        if senha_encerrar == senha:
            break
        else:
            print("Senha incorreta")


    else:
            print("USUÁRIO OU SENHA INCORRETOS")