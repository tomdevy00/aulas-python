"""
Repetiçoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

"""
condição = True


while condição:
    nome = input('qual o seu nome: ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')