# CÓDIGO DA AULA 8: Tuplas e Dicionários

# 1. Tuplas (imutáveis)
coordenadas = (10.5, 20.7, 5.0)
primeiro_valor = coordenadas[0] # 10.5

# Tentar fazer 'coordenadas[0] = 1' geraria um erro (TypeError)
print(f"Coordenadas: {coordenadas}, Primeiro valor: {primeiro_valor}")

# 2. Dicionários (Chave: Valor)
aluno = {
    "nome": "João",
    "idade": 25,
    "curso": "Engenharia",
    "matriculado": True
}

# 3. Acessando valores (usando a chave)
nome_aluno = aluno["nome"] # "João"
print(f"O nome do aluno é: {nome_aluno}")

# 4. Adicionando/Modificando um par Chave:Valor
aluno["cidade"] = "Lisboa" # Adiciona nova chave
aluno["idade"] = 26       # Modifica o valor da chave 'idade'

print(f"Dicionário após modificação: {aluno}")

# 5. Iterando sobre chaves e valores
print("\nChaves do dicionário:")
for chave in aluno.keys():
    print(chave)

print("\nValores do dicionário:")
for valor in aluno.values():
    print(valor)