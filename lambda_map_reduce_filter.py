from functools import reduce

# Possuem um retorno implícito
f = (lambda a, b: a*b)
print(f(5, 2))

# Isto também funciona
# ‘autoexecutadas’ sem precisar a chamada.
print((lambda a, b: a*b)(2, 3))

# Em conjunto de outras funções como map, reduce e
# filter lambda mostra toda sua utilidade

# map(função aplicada, lista de elementos)
# map serve para aplicar uma função a cada um dos elementos da lista
# Assim é retornado o dobro deles com a operação: x*2, e como a
# operação irá nos retornar um MAP OBJETCT utilizamos o metodo list p
# ara voltar a ter um array.

items = [1, 2, 3, 4, 5]
double = list(map(lambda x: x*2, items))
print(double)

# interando dicionários com a map
accounts = [
    {
        'name': 'João',
        'balance': 100
    },
    {
        'name': 'Nádia',
        'balance': 2000
    }
]

print(list(map(lambda x: x['balance'] > 100, accounts)))


# reduce() outra função nativa do python, ela vai aplicar uma
# função em TODOS OS VALORES
# passados em forma de lista, e RETORNA APENAS UM VALOR

# reduce(funcao_aplicada,lista_de_elementos)

soma = reduce((lambda x, y: x+y), [1, 2, 3, 4])
print(soma)


# maior numero de uma lista com o reduce

lista = [12, 43, 3224, 3, 123, 438, 999, 13, 44, 1000]
maior = reduce((lambda x, y: x if(x > y) else y), lista)
print(maior)

# a função filter() filtra os elementos passados na função,
# de acordo com a função passada como primeiro argumento.

# filter(funcao_aplicada,lista_de_elementos)
lista_pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_pares))
print(numeros_pares)

lista_menor = range(-5, 5)
menor_que_zero = list(filter((lambda x: x < 0), lista_menor))
print(menor_que_zero)


# map(): aplicar uma função em cada um dos elementos de uma lista;
# reduce(): aplicar uma função nos elementos da lista, reduzindo a um elemento só;
# filter(): filtrar elementos de uma lista por meio de uma função;
