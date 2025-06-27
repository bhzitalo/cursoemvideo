# Exercício 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# Recebe a temperatura em °C
celsius = int(input("Digite uma temperatura em °C: "))

# Converte e exibe a temperatura
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")


