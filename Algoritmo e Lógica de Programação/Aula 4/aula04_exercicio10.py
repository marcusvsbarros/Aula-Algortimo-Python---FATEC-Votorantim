""" EXERCÍCIO 10 - AULA 4

Faça um algoritmo que receba um número positivo e maior que zero, calcule e mostre:
a) O número digitado ao quadrado
b) O número digitado ao cubo
c) A raiz quadrada do número digitado

Observação:
Exp(x,y) – Calcula a potência de x elevado a y
Raizq(x) – Calcula a raiz quadrada de x
"""

numero = None

# Condição
while numero is None:
    entrada = input("Digite um número positivo e maior que zero: ")
    numero = float(entrada) if entrada.replace('.', '', 1).isdigit() else None

    if numero is None or numero <= 0:
        print("Por favor, digite um número positivo e maior que zero.")

print("O número digitado foi:", numero)

# a)
numeroaoQuadrado = (numero) ** 2
print(f"O valor ao quadrado é {numeroaoQuadrado}")

# b)
numeroaoCubo = (numero) ** 3
print(f"O valor ao cubo é {numeroaoCubo}")

# c)
numeroRaiz = (numero) ** 0.5
print(f"O valor da raiz quadrada é {numeroRaiz}")
