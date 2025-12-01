# CÓDIGO DA AULA 6: Strings

texto = "  python é divertido  "

# 1. Acessando caracteres (Indexação)
# A contagem começa em 0 (P=0, Y=1, T=2...)
primeiro_caractere = texto[2] # 'p' (ignorando os espaços iniciais)

# 2. Fatiamento (Slicing) - pega uma parte da string
fatia = texto[3:9] # do índice 3 até o 8 (o 9 é exclusivo): "thon é"

# 3. Concatenação e Repetição
saudacao = "Olá, " + "usuário."
separador = "-" * 10 # Cria "----------"

print(f"Primeiro caractere: {primeiro_caractere}, Fatia: '{fatia}', Saudação: {saudacao}")

# 4. Métodos de String
texto_limpo = texto.strip()      # Remove espaços: "python é divertido"
texto_maiusculo = texto_limpo.upper() # "PYTHON É DIVERTIDO"

print(f"Texto em maiúsculo: {texto_maiusculo}")

# 5. F-Strings (Formatação) - a forma preferida no Python moderno
versao = 3
print(f"Estamos a aprender a versão {versao} do Python.")