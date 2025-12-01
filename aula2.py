# CÓDIGO DA AULA 2: Variáveis e Tipos

# Declaração de variáveis (o Python infere o tipo automaticamente)
idade = 30           # int (Inteiro)
altura = 1.75        # float (Ponto Flutuante)
nome = "Maria Silva" # str (String/Texto)
esta_ativo = True    # bool (Booleano: True ou False)

# 1. Imprimindo os valores
print("Nome:", nome)
print("Idade:", idade)
print(f"Altura: {altura} metros")

# 2. Verificando os tipos de dados com a função type()
print("O tipo da variável 'idade' é:", type(idade))    # <class 'int'>
print("O tipo da variável 'nome' é:", type(nome))      # <class 'str'>
print("O tipo da variável 'esta_ativo' é:", type(esta_ativo)) # <class 'bool'>

# 3. Exemplo de Conversão de Tipos (Type Casting)
numero_em_texto = "45"
numero_convertido = int(numero_em_texto) # Converte a string "45" para o inteiro 45

print("Tipo original:", type(numero_em_texto))
print("Tipo convertido:", type(numero_convertido))
print("Resultado da soma após conversão:", numero_convertido + 5) # 50