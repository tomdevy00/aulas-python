"""
faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. caso usuario não digite um numero
inteiro, informe que não é um numero inteiro

"""

try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Isso não é um número inteiro válido.")
"""
"""
'''faça um programa que pergunte a hora ao usuario e, baseando-se no horario 
descrito, exiba a saudação apropriada.Ex
bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""
entrada = input('digite a hora em numeros inteiros:  ')'''

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('bom dia')
    elif hora >= 12 and hora <= 17:
        print('boa tarde')
    elif hora >= 18 and hora <= 23:
         print('boa noite')
except:
         print('não conheço essa hora')


         """
Faça um programa que peça o primeiro nome ao usuario. se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 letras e 6 letras, ecreva
"Seu nome é normal"; maior que 6 ecreva "Seu nome é muito grande"
         """

nome = input('digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if   tamanho_nome <= 4:
        print('seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('seu nome é normal')
    else:
        print('seu nome é muito grande')
   
   
        

    
    




    






