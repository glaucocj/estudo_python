lista1 = [1,2,3,4,5,6]
lista2 = ["a","b","c","d","e"]

print (lista1[3])

for item in lista2:
	print (item)

tamanho_da_lista = len(lista2)

print (tamanho_da_lista)

lista1.append(7) #adiciona um item a lista

print (lista1)

if "d" in lista2:
	print ("Está na lista")
else: print ("Não está na lista")

del lista2[1:3] #deleta itens da lista dentro do intervalo especificado [:] <--- Deleta tudo

print (lista2)