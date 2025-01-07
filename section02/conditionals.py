"""
Estruturas Condicionais:
    - if, else, elif

Estruturas Lógicas: 
    - and, or, not, is

Operadores unários:
    - not
Operadores binários:
    - and, or, is
"""

idade = int(input('Qual sua idade? '))

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
