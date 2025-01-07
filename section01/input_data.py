"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo "str", também conhecido como String
"""

# Entrada de dados
nome = input('Qual é o seu nome? ') # Input -> Entrada

print(f'Seja bem-vindo(a) {nome}')

idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
print(f'O(A) {nome} tem {idade} anos')

print(f'O(A) {nome} nasceu em {2025 - idade}')
