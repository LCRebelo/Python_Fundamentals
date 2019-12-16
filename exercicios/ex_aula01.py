# dada a string 

#string = "Não deixe o barulho da opinião dos outros abafar sua voz interior. \
#E mais importante, tenha a coragem de seguir seu coração e sua intuição. \
#Eles de alguma forma já sabem o que você realmente quer se tornar. \
#Tudo o mais é secundário."

#print(string)

# conte quantas letras a tem no texto
#print(string.count('r'))

# mude todas as letras o para s
#print(string.replace('o', 'O'))

# divida o texto em uma lista colocando virgulas nos espaços
#print(string.split(' '))



#frutas = ['abacaxi']
#print(frutas)
#frutas.append('laranja')
#frutas.append('uva')
#print(frutas)
#print(frutas[2])
#frutas.pop(2)
#print(frutas)
#frutas.remove('abacaxi')
#print(frutas)

#lista = [[1,2],[1,5,6],[4,5,6],'abacaxi',160.6]
#print (lista[2][2])


#dada a lista abaixo:

#lista = ['Corinthians', [1, 2, 3, 4, 5] ,
#         'Palmeiras', 'São Paulo', 
#        [10, 11, 12, 13, 14],'Flamengo', 'Vasco']



# print 3, 13, Vasco
#print(lista[1][2], lista[4][3], lista[-1])

# print 5, São Paulo, 14
# print(lista[1][-1], lista[3], lista[4][-1])

# mude o valor de 4 para 40
#lista[1][-2] = 40
# mude o valor de 14 para 150
#lista [-3][-1] = 150
#print(lista)

#lista = ['d','c','a']
#print(lista)
#lista.sort(reverse=True)
#lista.sort(reverse=False)
#print(lista)
#lista.reverse()
#print(lista.)

#imutavel=(1,2,3,4,5)
#print(imutavel[2])
#imutavel[2] = 10


dados = {

    'cidades': {
        'saopaulo': {
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 12.18
        },
        'riodejaneiro': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'população': 6.32
        },
        'minasgerais': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 20.87

        }
    }
}


# imprima a quantiddade de municipios de minas
#print('total de municípios',dados['cidades']['minasgerais']['municipios'])

# imprima a quantidade de municipios do rio

#print(dados['cidades']['riodejaneiro']['municipios'])

# imprima o nome e população de são paulo em milhoes

#print('Cidade:',dados['cidades']['saopaulo']['nome'],'Ṕopulação em milhões:', dados['cidades']['saopaulo']['população'])

#print(dados.values())
#print(dados.keys())


#novo_dict=dict(nome='Renato',sobrenome='Barbosa', idade='26')




#nome= imput("")

#Nome2= "teste"

#print('O valor de nome2 é {} e {} e mais {}', format ... )

#print(f'O nome digitado foi {nome}')


#for


# faça um for que imprima o nome de cada pessoa da lista e com a mensagem 'bem-vindo {}'

Nomes=['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']

# faça um for que imprima o nome de cada pessoa da lista e com a mensagem 'bem-vindo {}'

#print('Lista de presença')
#for nome in Nomes:
#    print('Bem vindo:', nome.capitalize())


impar = []

for num in range(20):
    if num % 2 == 0:
        continue
    impar.append(num)

print (impar)

