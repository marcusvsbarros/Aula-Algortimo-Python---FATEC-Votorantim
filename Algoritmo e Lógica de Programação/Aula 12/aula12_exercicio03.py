"""  EXERCÍCIO 3 - AULA 12

Faça uma função que determine se um ano qualquer, no formato AAAA, é bissexto.
A função retorna 1 se o ano é bissexto e 
0(zero) se não"""

# Declaração
def verificarBissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True 
            else:
                return False 
        else:
            return 1  
    else:
        return 0  

ano = int(input("Digite um ano no formato AAAA: "))
resultado = verificarBissexto(ano)

# Output
if resultado:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

