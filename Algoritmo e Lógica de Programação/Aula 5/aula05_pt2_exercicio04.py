""" EXERCÍCIO 4-2 - AULA 5

Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verificar se é um 
triângulo eqüilátero, isósceles ou escaleno.
Se eles não formarem um triângulo, escrever uma mensagem.

Considerar que:

•O comprimento de cada lado de um triângulo é menor que a soma dos outros
dois lados;
•Chama-se eqüilátero o triângulo que tem três lados iguais;
•Chama-se isósceles o triângulo que tem o comprimento de dois lados iguais;
•Chama-se escaleno o triângulo que tem os três lados diferentes;
"""

a = float(input("Digite o lado A: "))

b = float(input("Digite o lado B: "))

c = float(input("Digite o lado C: "))

if a<=0 or b<=0 or c<=0 :
   print("Lados nulos ou negativos nao sao aceitos.")
   quit()

if a>=b+c or b>=c+a or c>=a+b :
   print("Triangulo inexistente.")
   quit()

if a==b and b==c :
   print("Triangulo equilatero.")

elif a==b or b==c or c==a :
   print("Triangulo isosceles.")

else:
   print("Triangulo escaleno.")