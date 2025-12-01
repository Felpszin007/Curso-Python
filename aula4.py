# CÓDIGO DA AULA 4: Condicionais (if/elif/else)

nota = 75

# 1. O bloco 'if' testa a primeira condição
if nota >= 90:
    print("Excelente! Você tirou A.")
# 2. O bloco 'elif' (else if) testa a próxima condição SE a anterior for False
elif nota >= 70:
    print("Bom! Você tirou B.")
# 3. Podemos ter vários 'elif'
elif nota >= 50:
    print("Satisfatório! Você tirou C.")
# 4. O bloco 'else' executa se TODAS as condições acima forem False
else:
    print("Reprovado. Você precisa estudar mais.")

# Exemplo com Operadores Lógicos
idade = 18
carteira_motorista = True

if idade >= 18 and carteira_motorista:
    # Este bloco só executa se AMBAS as condições forem True
    print("Você pode dirigir legalmente.")
else:
    print("Você não pode dirigir.")