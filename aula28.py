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
#idade = int(input('qual a sua idade: '))
print(f'seu nome é :{nome}!')
print(f'seu nome invertido fica: {nome[:-7]}')

