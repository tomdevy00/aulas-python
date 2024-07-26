"""
Iterando syrings com while
"""
#      012345678910111213141516171819
# nome ='everton fernandes de oliveira' # Iteraveis
#      1110987654321
nome = 'everton fernandes'
indice  = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    
novo_nome += '*'
print(novo_nome)

