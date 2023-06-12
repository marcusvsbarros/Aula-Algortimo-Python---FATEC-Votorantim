""" EXERCÍCIO 7 - AULA 7

Faça um programa que calcule os 10 primeiros números da sequencia de Fibonacci
"""

def calcularFibonacci(n):
    fibonacci = [0, 1]

    for i in range(2, n):

        proximo = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(proximo)

    return fibonacci

n = 10
resultado = calcularFibonacci(n)
print(resultado)
