# CÓDIGO DA AULA 10: Módulos e I/O

# 1. Importando um módulo (math para matemática, random para aleatoriedade)
import math
import random

# Usando uma função do módulo math (raiz quadrada)
raiz = math.sqrt(81) # 9.0

# Usando uma função do módulo random (número inteiro aleatório entre 1 e 10)
dado = random.randint(1, 10)

print(f"Raiz quadrada de 81: {raiz}")
print(f"Número aleatório gerado: {dado}")

# 2. Entrada do Usuário (I/O)
# A função input() SEMPRE retorna uma string, então precisamos converter para int ou float se for um número.
nome_usuario = input("Digite o seu nome: ")
ano_nascimento_str = input("Digite o seu ano de nascimento: ")
ano_nascimento = int(ano_nascimento_str) # Conversão para inteiro

idade_atual = 2024 - ano_nascimento
print(f"Olá, {nome_usuario}! Você tem aproximadamente {idade_atual} anos.")

# 3. I/O Básico de Arquivos
# O modo 'w' (write) cria ou sobrescreve o arquivo. O 'with' garante que o arquivo seja fechado.
with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Linha 1: Dados do arquivo.\n")
    arquivo.write("Linha 2: Informação de teste.")

print("\nDados escritos em 'meu_arquivo.txt'")

# O modo 'r' (read) lê o conteúdo do arquivo.
with open("meu_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("\nConteúdo do arquivo:")
    print(conteudo)