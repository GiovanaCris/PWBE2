#EXERCÍCIO 1:
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print (f'{numero} é Par!')

else:
    print (f'{numero} é Ímpar!')

#EXERCÍCIO 2:
nome = (input('Digite o nome do aluno: '))

nota1 =  float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite terceira nota: '))
nota4 = float(input('Digite quarta nota: '))
nota5 = float(input('Digite quinta nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if media >= 5:
    print ('ALUNO APROVADO! ')

elif media > 2.5 and media < 5:
    print ("RECUPERAÇÃO! ")

elif media < 2.5:
    print ('REPROVADO! ')