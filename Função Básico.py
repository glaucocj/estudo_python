# -*- coding: UTF-8 -*-

def SOMA(a,b):
	print("Somando os Valores:",a,"+",b,"=",a+b)
	return a+b #caso seja necessário armazenar o resultado de uma função ou usa-lo de outra forma

SOMA(5,6)

arquivo = open("arquivo.txt")

linhas =  arquivo.readlines()

for linha in linhas:
	print(linha)