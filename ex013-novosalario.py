# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Recebe o salário atual do usuário
salario = float(input("Digite o salário atual: "))

# Calcula e exibe o ovo salário
novo_salario = salario + (salario * 0.15)
print(f"Novo salário: R${novo_salario:.2f}")