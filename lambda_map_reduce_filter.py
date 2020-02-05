f = (lambda a,b: a*b)
print(f(5,2))

#Isto também funciona
print((lambda a,b: a*b)(2,3))

#Em conjunto de outras funções como map, reduce e 
# filter lambda mostra toda sua utilidade

#map(função aplicada, lista de elementos)
items = [1,2,3,4,5]
double = list(map(lambda x: x*2, items))
print(double)

#interando dicionários com a map
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

print(list(map(lambda x: x['balance']> 100, accounts)))