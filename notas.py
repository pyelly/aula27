#LER ENTRADAS DO USUÁRIO
cont = 0
escolha_usuario = int(input())
while cont < escolha_usuario:
     nome = input()#ARMAZENAR o nome do aluno
     nota1 = float(input()) #4 notas do aluno
     nota2 = float(input())
     nota3 = float(input())
     nota4 = float(input())

     faltas = int(input())
     #calculo da media
     media = (nota1+nota2+nota3+nota4)/4

     #LOGICA DA SITUAÇÃO
     if faltas > 31:
        situacao = "Reprovado por falta"
    elif media >= 8:
        situacao = "Aprovado"
    elif media >= 5: #recuperação
        recuperacao = float(input()) #ler a nota da prova de recuperação
        if recuperacao >= (10-media):
            situacao = "aprovado(a) na recuperação"
        else:
            situacao = "reprovado(a) na recuperação"
    else:
        situacao = "reprovado(a) por media"
    #relatorio
    print("nome",nome)
    print("notas:",nota1,nota2,nota3,nota3,nota4)
    print("faltas:",faltas)
    print("situação do aluno(a):", situacao)
    cont = cont+1
