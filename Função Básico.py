# -*- coding: UTF-8 -*-

def SOMA(a,b):
	print("Somando os Valores:",a,"+",b,"=",a+b)
	return a+b #caso seja necessário armazenar o resultado de uma função ou usa-lo de outra forma

SOMA(5,6)

arquivo = open("arquivo.txt") #Ao abrir um arquivo é importante especificar o método, "w" "a" "r" #o método "a" permite adicionar conteúdo sem apagar o anterior

linhas =  arquivo.readlines() #Lê linha por linha e armazena em um Array 
#Lê o arquivo inteiro linhas.arquivo.read() 

for linha in linhas:
	print(linha)

novo_arquivo = open("criando_um_arquivo.txt","a") #Criando um novo arquivo

novo_arquivo.write("Escrevendo dentro do arquivo áã\n") #Escrevendo dentro do arquivo

novo_arquivo.close() #Fechando o arquivo