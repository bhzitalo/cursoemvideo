# Exercício 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Recebe o valor do produto
preco = float(input("Digite o valor do produto: "))

# Calcula o novo preço com 5% de desconto
novo_preco = preco - (preco * 5 / 100)

# Exibe o resultado
print(f"O novo preço com 5% de desconto é R$ {novo_preco:.2f}")
