"""  EXERCÍCIO 2 - AULA 12

Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro passado por parâmetro for primo, e F (falso) se não.
Implemente sua função em um programa completo.
"""

# Declaração
def verificarPrimo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            return False

    return True


numero = int(input("Digite um número inteiro: "))
resultado = verificarPrimo(numero)

if resultado:
    print("O número é primo.")
else:
    print("O número não é primo.")


numerosPrimos = []
numero = 2
while len(numerosPrimos) < 50:
    if verificarPrimo(numero):
        numerosPrimos.append(numero)
    numero += 1 

# Output
print("Os 50 primeiros números primos:")
for numeroPrimo in numerosPrimos:
    print(numeroPrimo)
