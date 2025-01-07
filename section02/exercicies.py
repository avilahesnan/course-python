# 1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
numero1: int = int(input('Digite o primeiro número: '))
numero2: int = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'O primeiro número é o maior: {numero1}')
elif numero1 < numero2:
    print(f'O segundo número é o maior: {numero2}')
else:
    print('Os números são iguais')

# 2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
from math import sqrt

num: int = int(input('Digite um número: '))

if num >= 0:
    raiz: float = sqrt(num)
    print(f'A Raiz quadrada de {num} é: {raiz}')
else:
    print('O número digite é inválido')

# 3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
numero: int = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')
