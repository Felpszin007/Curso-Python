# CÓDIGO DA AULA 9: Funções

# 1. Função simples sem parâmetros e sem retorno
def saudacao():
    """Esta função imprime uma saudação na tela."""
    print("Seja bem-vindo(a) ao Python!")

# Chamada da função
saudacao()

# 2. Função com parâmetros
def somar(num1, num2):
    """Esta função soma dois números e imprime o resultado."""
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")

# Chamada da função com argumentos
somar(15, 7)

# 3. Função com retorno (return)
def calcular_area_quadrado(lado):
    """Esta função calcula e RETORNA a área de um quadrado."""
    area = lado * lado
    return area

# Chamada da função e armazenamento do resultado
tamanho_lado = 5
area_calculada = calcular_area_quadrado(tamanho_lado)

print(f"A área de um quadrado de lado {tamanho_lado} é: {area_calculada}")