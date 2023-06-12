""" EXERCÍCIO 3 - AULA 4

Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual e mostre:
a) A idade dessa pessoa em anos;
b) A idade dessa pessoa em meses;
c) A idade dessa pessoa em dias;
d) A idade dessa pessoa em semanas.
"""

# inputs
anoNascimento = int(input("Digite seu ano de nascimento(AAAA): "))
anoAtual = int(input("Digite o ano atual(AAAA): "))

# Calculo em anos
anos = anoAtual - anoNascimento
print(f"Você possui a idade de {anos} anos.")

# Cálculo em meses
mesesanoAtual =  anoAtual * 12
mesesanoNascimento = anoNascimento * 12
meses = mesesanoAtual - mesesanoNascimento
print(f"Ou {meses} meses.")

# Cálculo em dias
diasanoAtual =  anoAtual * 365
diasanoNascimento = anoNascimento * 365
dias = diasanoAtual - diasanoNascimento
print(f"Totalizando {dias} dias.")

# Cálculo em semanas
semanasanoAtual = diasanoAtual // 7
semanasanoNascimento =diasanoNascimento // 7
semanas = semanasanoAtual - semanasanoNascimento
print(f"Sendo {semanas} semanas.")