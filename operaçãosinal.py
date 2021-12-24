n1 = float(input("Digite o número:"))
sinal = input("Digite o sinal:")
n2 = float(input("Digite o número:"))
resultado = 0
print(n1,sinal,n2)

sinais =["+","-","*","/"]

if sinal == "+":
    resultado = n1+n2
elif sinal == "-":
    resultado = n1-n2
elif sinal == "*":
    resultado = n1*n2
else:
    try:
        resultado = n1/n2
    except:
        print("Divisão por Zero")

print(resultado)

