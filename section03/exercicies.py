# 1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
multiplos: int = 0
num: int  = 1

while multiplos < 5:
    if num % 3 == 0:
        print(f'{num} é múltiplo de 3')
        multiplos+= 1
    num+= 1
    
# 2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
contador: int = 10

while contador >= 0:
    print(f'{contador}...', end='')
    contador-= 1
print('FIM')

# 3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).
for n in range(0, 100001, 1000):
    print(n)
