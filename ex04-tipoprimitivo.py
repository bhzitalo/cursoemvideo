# Exercício 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Recebe uma informação do usuário
algo = input("Digite qualquer coisa: ")

# Exibe o que o usuário digitou e os tipos primitivos
print(f"Você Digitou: {algo}")
print(f"É minúsculo? {algo.islower()}")
print(f"É maiúsculo? {algo.isupper()}")
print(f"É numérico? {algo.isnumeric()}")
print(f"É alfabético? {algo.isalpha()}")
print(f"É alfanumérico? {algo.isalnum()}")
print(f"É dígito? {algo.isdigit()}")
print(f"É espaço? {algo.isspace()}")
print(f"É ASCII? {algo.isascii()}")
print(f"É imprimível? {algo.isprintable()}")
