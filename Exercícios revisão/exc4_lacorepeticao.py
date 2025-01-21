#EXERCÍCIO 1:
numero = int (input('Digite um número positivo: '))

for i in range (0, numero+1):
    print (i)

#EXERCÍCIO 2:
m = []
while True:
    numeros = int(input('Digite um número: '))
    m.append(numeros)
    if numeros <0:
        print ('O número é negativo! ')
        break

maior = max(m)
print (f'O número maior é {maior}')