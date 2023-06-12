""" EXERCÍCIO 4 - AULA 4

Faça um algoritmo que receba a data de nascimento de uma pessoa e a data atual e mostre sua idade em anos, meses, semanas e dias
"""

# Inputs, determinando / como separador
diaNascimento, mesNascimento, anoNascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").split('/')
diaAtual, mesAtual, anoAtual = input("Digite a data atual (dd/mm/aaaa): ").split('/')

# Cálculo em anos
idadeAnos = int(anoAtual) - int(anoNascimento)

# Calcular a diferença de meses
idadeMeses = int(mesAtual) - int(mesNascimento)

# Cálculo em meses
idadeAnos -= idadeMeses // 12
idadeMeses = idadeMeses % 12

# Calcular em semanas
totalDiasNascimento = int(diaNascimento) + int(mesNascimento) * 30 + int(anoNascimento) * 365
totalDiasAnoAtual = int(diaAtual) + int(mesAtual) * 30 + int(anoAtual) * 365
idadeSemanas = (totalDiasAnoAtual - totalDiasNascimento) // 7

# Calcular em dias
idadeDias = (totalDiasAnoAtual - totalDiasNascimento) % 7

# Output
print("Idade:")
print("Anos:", idadeAnos)
print("Meses:", idadeMeses)
print("Semanas:", idadeSemanas)
print("Dias:", idadeDias)
