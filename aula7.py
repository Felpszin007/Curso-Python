# CÓDIGO DA AULA 7: Listas

# Criação de uma lista
compras = ["Pão", "Leite", "Ovos", "Café"]

# 1. Acessando e modificando elementos
primeiro_item = compras[0] # "Pão"
ultimo_item = compras[-1]  # "Café"
compras[1] = "Manteiga"    # Lista é mutável: 'Leite' é substituído por 'Manteiga'

print(f"Lista inicial: {compras}")
print(f"Primeiro item: {primeiro_item}")

# 2. Métodos de Lista
compras.append("Frutas")  # Adiciona 'Frutas' ao final
compras.insert(1, "Queijo") # Insere 'Queijo' na posição 1

print(f"Lista após adicionar: {compras}")

# 3. Remover elementos
item_removido = compras.pop() # Remove e retorna o último item ('Frutas')
compras.remove("Pão")        # Remove o valor "Pão"

print(f"Lista após remover: {compras}")

# 4. Ordenação
numeros = [5, 1, 8, 2]
numeros.sort() # Ordena a lista in-place (no local): [1, 2, 5, 8]
print(f"Lista ordenada: {numeros}")