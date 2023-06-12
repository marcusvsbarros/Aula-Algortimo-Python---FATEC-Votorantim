'''  EXERCÍCIO 1 - AULA 12

Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro passado por parâmetro for par, e F (falso) se não.
Implemente sua função em um programa completo.
'''

# Declaração
def verificar_par(numero):
    if numero % 2 == 0:
        return "Verdadeiro"
    else:
        return "Falso" 


numero = int(input("Digite um número inteiro: "))
resultado = verificar_par(numero)

# Output
print("O número é par? Resposta:", resultado)
