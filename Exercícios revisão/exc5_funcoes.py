#EXERCÍCIO 1:
# def inverter_string(s):
#     palavra = input('Digite uma palavra: ')
#     palavra_invertida = ''.join(reversed(palavra))
#     print (palavra_invertida)
# print (inverter_string(s))

#EXERCÍCIO 1 (PROF):    
# def inverter_string(s):
#     invertido = ''
#     for i in s:
#         invertido = i + invertido
#     print (invertido)
# inverter_string ("Luana")

#EXEMPLO 2 (PROF):
# def inverter_string(s):
#     invertido = ''
#     for i in range(len(s), 0, -1):
#         invertido += s[i]
# print (invertido)


#EXERCÍCIO 2:
def contar_caracteres(s):
    dicionario = {}
    for i in s:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    print (dicionario)

contar_caracteres("Gustavo Bruno")