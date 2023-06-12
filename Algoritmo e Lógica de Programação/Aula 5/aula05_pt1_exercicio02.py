""" EXERCÍCIO 2-1 - AULA 5

Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem que segue a tabela abaixo. 
Para alunos de exame, calcule e mostre a nota que deverá ser tirada no exame para aprovação, considerando que a média do exame é 6,0 
(e que a média após o exame é resultado da média aritmética entre a nota do exame e a média antes do exame)

0,0 e <3,0 Reprovado
>= 3,0 e < 7,0 Exame
>=7,0 e <=10,0 Aprovado
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 3.0:
    print("Reprovado")
elif media < 6.0:
    print("Exame")
    notaExame = 10 - media
    print("Nota necessária no exame: ", notaExame)
else:
    print("Aprovado")