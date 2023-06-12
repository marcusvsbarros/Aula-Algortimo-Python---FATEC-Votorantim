"""  EXERCÍCIO 1 - AULA 11

Faça um algoritmo que carregue uma tupla de 10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo deve escrever a mesma tupla, na ordem inversa de entrada.
"""

# Declaração
tupla = []
for i in range(10):
    elemento = int(input("Digite um elemento inteiro: "))
    tupla.append(elemento)

tuplaInversa = tuple(reversed(tupla))

# Output
print("Tupla na ordem inversa:")
for elemento in tuplaInversa:
    print(elemento)
