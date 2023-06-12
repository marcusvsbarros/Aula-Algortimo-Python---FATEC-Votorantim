""" EXERCÍCIO 3 - AULA 7

Faça um algoritmo que leia o valor do peso e da altura de 20 pessoas. Ao final, o algoritmo deve mostrar:

- O peso médio
- A altura média
- O maior e o menor IMC

Obs: IMC (Índice de Massa Corporal) – calculado a partir da fórmula:
IMC = massa dividido por altura ao quadrado"""

participantes = 20

pesoTotal = 0
alturaTotal = 0
imcMaximo = float('-inf')
imcMinimo = float('inf')

for i in range(participantes):
    print(f"\nDados da pessoa {i+1}:")
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    pesoTotal += peso
    alturaTotal += altura

    imc = peso / (altura ** 2)
    if imc > imcMaximo:
        imcMaximo = imc
    if imc < imcMinimo:
        imcMinimo = imc

pesoMedio = pesoTotal / participantes
alturaMedia = alturaTotal / participantes

print("\nResultados:")
print("Peso médio:", pesoMedio)
print("Altura média:", alturaMedia)
print("Maior IMC:", imcMaximo)
print("Menor IMC:", imcMinimo)
