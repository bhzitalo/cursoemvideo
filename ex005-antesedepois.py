# Exercício 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

# Recebe um número inteiro digitado pelo usuário
numero = int(input("Digite um número? "))

# Exibe o antecessor e o sucessor ao usuário
print(f"Você digitou o número {numero}")
print(f"Seu antecessor é {numero - 1}")
print(f"Seu sucessor é {numero + 1}")
