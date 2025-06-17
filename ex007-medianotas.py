# Exercício 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Recebe as notas do usuário
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

# Exibe o resultado da soma e da média a usuário
print(f"Sua nota total é {nota1 + nota2 + nota3 + nota4}")
print(f"Sua média é {(nota1 + nota2 + nota3 + nota4) / 4}")

# Podia usar uma variavel para registrar a soma das notas e uma pra guardar o valor da média

