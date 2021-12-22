dicio = {"G":"Glauco"} #chave:conteúdo

print (dicio["G"])

dicio_completo = {1:"A",2:"B",3:"C"}

print (dicio_completo) #exibindo o dicionário completo

for chave in dicio_completo: #exibindo o dicionário completo, item a item
	print (dicio_completo[chave]+" - CHAVE "+str(chave))

for i in dicio_completo.items(): #impressão em formato do tupla existem tbm os métodos *.values() e *.keys()
	print (i)


