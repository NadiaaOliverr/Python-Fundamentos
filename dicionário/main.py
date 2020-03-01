#O que é um dicionário ? {chave: valor}
#É possível acessar um dicionário pelo nome dele e o nome da chave
#A chave não precisa necessariamente de ser uma string
#Não é possível colocar listas como chave do dicionário, mas pode ter um valor correspondente a uma chave que é uma lista
#Pode ter um dicionário dentro de outro
#A ordem de como um dicionário está organizado não é tão importante assim, pois, você tem acesso ao elemento pela chave, então não importa se a chave está no começo ou fim.


#Criar Listas: []
#Criar Tuplas: ()
#Criar Dicionários: {}

contato = {'Nome': 'Pedro', 'Telefone': 319956734,'Celular': 3165342345 , 'Email': 'pedro.henrique@ufv.br'}
# print(contato['Nome'])

# contato_2 = {4.77: 'O que é isso?!!!'}
# print(contato_2[4.77])

# contato_3 = {11: [4,5,6]}
# print(contato_3[11])

# #Um dicionário dentro de outro
# dicionario_de_contatos = {'Contato1': contato}
# print(dicionario_de_contatos['Contato1'])

# contato['Endereco'] = ['Av. Paulista']

# #Em um dicionário a gente consegue guardar:
# #   -Integer, Float, Dicionário, Str, Tuplas, Listas, lambdas 

# # (lambda x,y: x+y)(1,2)

# dic = {'Lambda': lambda x: x+1}
# print(dic['Lambda'](3))

# for chaves in contato:
#     print(chaves)
    
# print(len(contato)) #número de chaves do dicionário

def get(dic, key, valor=None):
    if key in dic:
        return dic[key]
    else:
        return valor

print(get(contato,'Nome'))
print(get(contato,'Nadia', 88888))
