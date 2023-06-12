""" EXERCÍCIO 5 - AULA 7

Elabore um algoritmo que simule uma contagem regressiva de 10 minutos, ou seja, 
mostre 10:00 e então 9:59, 9:58, ..., 9:00; 8:59, 8:58, até 0:00.
"""

import time
import os

totalSegundos = 10 * 60  # 10 minutos em segundos

for segundosRestantes in range(totalSegundos, -1, -1):
    minutos = segundosRestantes // 60
    segundos = segundosRestantes % 60
    
    os.system("cls")
    print(f"{minutos:02d}:{segundos:02d}")
    time.sleep(1)  # Aguarda 1 segundo antes de exibir o próximo valor

print("Contagem regressiva concluída!")
