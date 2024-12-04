#LER ENTRADAS DO USUÁRIO
cont = 0
escolha_usuario = int(input("digite quantos alunos vc quer cadastrar"))#variavel que guarda quantas vezes o codigo vai rodar
alunos = [] #lista que guardara todos os alunos cadrastados
while cont < escolha_usuario:
     nome = input("digite o nome do aluno")#ARMAZENAR o nome do aluno
     nota1 = float(input("digite a nota1 do aluno")) #4 notas do aluno
     nota2 = float(input("digite a nota2 do aluno"))
     nota3 = float(input("digite a nota3 do aluno"))
     nota4 = float(input("digite a nota4 do aluno"))

     faltas = int(input())
     #calculo da media
     media = (nota1+nota2+nota3+nota4)/4

     #LOGICA DA SITUAÇÃO
     if faltas > 31:
        situacao = "Reprovado por falta"
     elif media >= 8:
        situacao = "Aprovado"
     elif media >= 5: #recuperação
        recuperacao = float(input("digite nota do aluno(a) da recuperação")) #ler a nota da prova de recuperação
        if recuperacao >= (10-media):
            situacao = "aprovado(a) na recuperação"
        else:
            situacao = "reprovado(a) na recuperação"
     else:
       situacao = "reprovado(a) por media"
       #enviar os dados do aluno para a lista (alunos)
       alunos.append([nome,faltas,media,situação])
    #relatorio
     print(alunos)
