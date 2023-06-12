""" EXERCÍCIO 1-2 - AULA 5

FAZER UM PROGRAMA QUE RECEBA DOIS NÚMEROS E EXECUTE AS OPERAÇÕES LISTADAS A SEGUIR DE ACORDO COM A ESCOLHA DO USUÁRIO:
1. Média entre os números digitados
2. Diferença do maior pelo menor
3. Produto entre os números digitados
4. Divisão do primeiro pelo segundo
"""

n1 = int(input("Digite o primeiro número: "))

n2 = int(input("Digite o segundo número: "))

media = ((n1 + n2)/2)
diferenca = n1 - n2
produto = n1 * n2
divisao = n1 / n2

print(f"A média entre os valores digitado é {media:.2f}")
print(f"A diferença entre os valores digitado é {diferenca:.2f}")
print(f"O produto entre os valores digitado é {produto:.2f}")
print(f"A divisão entre os valores digitado é {divisao:.2f}")
