""" EXERCÍCIO 3-2 - AULA 5

Faça um programa que receba o preço líquido de um produto e o seu código de origem e mostre a sua procedência e o preço final, 
calculado pelo imposto relativo a sua procedência. A procedência obedece a tabela a seguir:

Código Origem    -  Procedência     -    % Imposto
    1                   Sul                  11%
    2                   Norte                13%
    3                   Nordeste              9%
    4                   Centro-Oeste         12%
    5                   Sudente              18%
"""

preco = float(input("Digite o preço líquido do produto: "))
codigo = int(input("Digite o código de origem do produto: "))

imposto = 0

if codigo == 1:
    procedencia = "Sul"
    imposto = 0.11
elif codigo == 2:
    procedencia = "Norte"
    imposto = 0.13
elif codigo == 3:
    procedencia = "Nordeste"
    imposto = 0.09
elif codigo == 4:
    procedencia = "Centro-Oeste"
    imposto = 0.12
elif codigo == 5:
    procedencia = "Sudeste"
    imposto = 0.18
else:
    procedencia = "Origem desconhecida"

total = preco + (preco * imposto)

print("Procedência:", procedencia)
print("Preço Final:", total)