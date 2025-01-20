nome = (input('Digite seu nome: '))
anonasc = float (input('Digite seu ano de nascimento: '))

idade = 2025 - anonasc

if anonasc > 2025:
    print ('Idade não encontrada')
else:
    print (f'{nome}, sua idade em 2025 é: {idade}')

