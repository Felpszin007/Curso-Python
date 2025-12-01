# CÓDIGO DA AULA 3: Operadores

# 1. Operadores Aritméticos
a = 10
b = 3
soma = a + b      # 13
resto = a % b     # 1 (resto de 10 / 3)
potencia = a ** 2 # 100

print(f"Soma: {soma}, Resto: {resto}, Potência: {potencia}")

# 2. Operadores de Comparação (retornam True ou False)
e_igual = (a == 10) # True
e_diferente = (a != b) # True
e_maior = (a > 15) # False

print(f"É igual a 10? {e_igual}, É diferente de b? {e_diferente}")

# 3. Operadores Lógicos (combinam resultados booleanos)
tem_permissao = True
e_admin = False

# Usa 'and': só é True se AMBAS forem True
pode_acessar_tudo = tem_permissao and e_admin # False

# Usa 'or': é True se PELO MENOS UMA for True
pode_acessar = tem_permissao or e_admin # True

# Usa 'not': inverte o valor
nao_e_admin = not e_admin # True

print(f"Pode acessar tudo? {pode_acessar_tudo}")