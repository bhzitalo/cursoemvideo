# Exercício 015: Escreva um programa que pergunte a quantidade de Km percorridos por um 
# carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Lê a quilometragem e a quantidade de dias
quilometros = float(input("Digite a quilometragem percorrida (em km): "))
diarias = int(input("Digite a quantidade de diárias: "))

# Calcula o valor total
valor_km = quilometros * 0.15
valor_dias = diarias * 60
total = valor_km + valor_dias

# Exibe o resultado ao usuário
print(f"\nQuilometragem percorrida: {quilometros:.2f} km")
print(f"Diárias: {diarias} dias")
print(f"Valor por km: R${valor_km:.2f}")
print(f"Valor por dias: R${valor_dias:.2f}")
print(f"Total a pagar: R${total:.2f}")