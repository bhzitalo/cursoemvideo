# Exercício 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Recebe os dados do usuário
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta (1 litro para cada 2 m²)
tinta = area / 2

# Exibe os resultados
print(f"A área da parede é de {area:.2f} m².")
print(f"Você precisará de {tinta:.2f} litros de tinta para pintá-la.")
