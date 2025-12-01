# CÓDIGO DA AULA 5: Laços (for/while)

# 1. Laço 'for' com a função range()
# range(5) gera uma sequência de números: 0, 1, 2, 3, 4
print("--- Contagem com 'for' ---")
for i in range(5):
    print(f"Contagem: {i}")

# 2. Laço 'for' iterando sobre uma lista de itens (veremos listas depois!)
frutas = ["Maçã", "Banana", "Cereja"]
print("\n--- Listando frutas com 'for' ---")
for fruta in frutas:
    print(f"Eu gosto de {fruta}")


# 3. Laço 'while'
contador = 0
print("\n--- Contagem com 'while' ---")
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1 # O 'incremento' é crucial para evitar laços infinitos

# 4. Exemplo de 'break'
for numero in range(10):
    if numero == 5:
        print("Encontrado o 5, parando o laço com break.")
        break # Para o loop completamente
    print(numero)