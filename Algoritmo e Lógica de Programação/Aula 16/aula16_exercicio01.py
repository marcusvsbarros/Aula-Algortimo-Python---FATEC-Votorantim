# Declaração
pessoas = []


while True:
    sobrenome = input("Digite o sobrenome da pessoa (ou pressione <Enter> para sair): ")
    if not sobrenome:
        break

    idade = input("Digite a idade da pessoa: ")
    while not idade.isdigit():
        print("Idade inválida. Digite novamente.")
        idade = input("Digite a idade da pessoa: ")

    altura = input("Digite a altura da pessoa em centímetros: ")
    while not altura.isdigit(): 
        print("Altura inválida. Digite novamente.")
        altura = input("Digite a altura da pessoa em centímetros: ")

    peso = input("Digite o peso da pessoa em kg: ")
    while not peso.isdigit():
        print("Peso inválido. Digite novamente.")
        peso = input("Digite o peso da pessoa em kg: ")


    pessoas.append({"sobrenome": sobrenome, "idade": int(idade), "altura": int(altura), "peso": int(peso)})

pessoas.sort(key=lambda x: x["sobrenome"])

# Output
print("Listagem das pessoas:")
for pessoa in pessoas:
    print("Sobrenome:", pessoa["sobrenome"])
    print("Idade:", pessoa["idade"])
    print("Altura:", pessoa["altura"], "cm")
    print("Peso:", pessoa["peso"], "kg")
    print()

# Média
totalPessoas = len(pessoas)
somaIdades = sum([pessoa["idade"] for pessoa in pessoas])
mediaIdade = somaIdades / totalPessoas

somaAlturas = sum([pessoa["altura"] for pessoa in pessoas])
mediaAltura = somaAlturas / totalPessoas

somaPesos = sum([pessoa["peso"] for pessoa in pessoas])
mediaPeso = somaPesos / totalPessoas

# Output - Média
print("Resumo:")
print("Média de idade:", mediaIdade)
print("Média de altura:", mediaAltura, "cm")
print("Média de peso:", mediaPeso, "kg")
