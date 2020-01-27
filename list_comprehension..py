#Abordagem normal
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
        

#Usando listas de compreensão
pares = [x for x in inteiros if x % 2 == 0]
print(pares)
