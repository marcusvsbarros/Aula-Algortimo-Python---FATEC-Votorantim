"""  EXERCÍCIO 7 - AULA 9

Faça um algoritmo que armazenará os 10
primeiros números primos acima de 100. Ao
final, o algoritmo deve mostrar os valores
desse vetor."""

# Declaração
primos = []
numero = 101


while len(primos) < 10:
    verificaPrimo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            verificaPrimo = False
            break

    if verificaPrimo:
        primos.append(numero)

    numero += 1

# Output
print("Os 10 primeiros números primos acima de 100 são:")
for numeroPrimo in primos:
    print(numeroPrimo)
