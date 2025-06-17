# Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

# Recebe uma distância do usuário
distancia = float(input("Digite uma distância em metros: "))

# Exibe a resposta ao usuário
print(f"Convertendo {distancia} metros em:")
print(f"Centímetros: {distancia * 100}")
print(f"Milímetros: {distancia * 1000} ")