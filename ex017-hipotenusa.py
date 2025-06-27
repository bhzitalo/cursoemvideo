# Exercício 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

# Lê os catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcula a hipotenusa
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Mostra o resultado
print(f"A hipotenusa mede {hipotenusa:.2f}")
