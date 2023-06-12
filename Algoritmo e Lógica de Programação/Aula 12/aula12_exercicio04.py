"""  EXERCÍCIO 4 - AULA 12

Construa uma função que retorne o MDC de dois números inteiros passados por parâmetro"""

# Declaração
def calcularMdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Exemplo de uso da função:
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
mdc = calcularMdc(numero1, numero2)
print("O MDC entre", numero1, "e", numero2, "é:", mdc)
