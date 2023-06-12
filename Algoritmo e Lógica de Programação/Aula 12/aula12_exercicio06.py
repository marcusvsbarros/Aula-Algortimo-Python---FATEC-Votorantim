"""  EXERCÍCIO 6 - AULA 12

Crie uma função que receba como parâmetro 3 números interios (representando horas, minutos e segundos). 
A função deve converter em segundos.

Por exemplo: 2 h, 40 min e 10 segundos 
correspondem a 9.610 segundos."""


# Declaração
def converterSegundos(horas, minutos, segundos):
    totalSegundos = (horas * 3600) + (minutos * 60) + segundos
    return totalSegundos

# Input
entrada = input("Digite o tempo no formato (hh:mm:ss): ")

horas, minutos, segundos = map(int, entrada.split(":"))
resultado = converterSegundos(horas, minutos, segundos)


# Output
print(f"{horas:02d}:{minutos:02d}:{segundos:02d} correspondem a {resultado} segundos.")


