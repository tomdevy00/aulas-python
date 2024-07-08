'''
Exercicio
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
se nome e idade forem digitados:
exiba:
    seu nome é {nome}
    seu nome invertido é {nome invertido}
    se nome contem  (ou não) espaços
    seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
se nada for digitado em nome ou idade:
   exiba "Desculpe, voce deixou campos vazios."
 '''

nome = input('qual o seu nome: ')
idade = int(input('qual a sua idade: '))
if nome and idade:
    print(f'seu nome é :{nome}!')
    print(f'seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome NÃO contem espaços.')
    
    print(f'a quantidade de letras para o meu nome são: {len(nome)} letras!')
    print(f'a primeira letra do meu nome é: {nome[0]}')
    print(f'a ultima letra do meu nome é: {nome[-1]}')
else:
    print("desculpe, voce deixou oos campos vazios.!")


