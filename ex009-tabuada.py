# Exercício 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

# Recebe um número do usuário
print("=-="*10)
multiplicador = int(input("Digite um número: "))
print("=-="*10)

# Exibe a tabuada na tela do usuário
contador = 1

print(f"Tabuada de {multiplicador}: ")

while contador <= 10:
    print(f"{multiplicador} x {contador} = {multiplicador * contador}")
    contador = contador + 1
