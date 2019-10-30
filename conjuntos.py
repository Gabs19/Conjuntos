cores = {'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'preto_e_branco' : '\033[7;30m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m',
         'lilas' : '\033[35m',
         'fim' : '\033[m'}


import random
elementos = {'1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
elemento = list(elementos)
conjunto_a = []
conjunto_b = []

for i in range(5):
    elemento_a = random.choice(elemento)
    conjunto_a.append(elemento_a)

for i in range(5):
    elemento_b = random.choice(elemento)
    conjunto_b.append(elemento_b)

uniao = []
intersecao = []
complemento_a = []
complemento_b = []

for i in conjunto_a:
    if i in conjunto_b:
        intersecao.append(i)
    else:
        complemento_b.append(i)

for i in conjunto_b:
    if i not in conjunto_a:
        complemento_a.append(i)


#uniao.extend(conjunto_b)
#uniao.extend(conjunto_b)

for i in conjunto_a:
    if i not in uniao:
        uniao.append(i)

for i in conjunto_b:
    if i not in uniao:
        uniao.append(i)

union = list(sorted(set(uniao)))
print(f'{cores["lilas"]}-=-{cores["fim"]}'*25)
print(f'{cores["vermelho"]}Conjunto A:{cores["amarelo"]} {conjunto_a} {cores["fim"]}')
print(f'{cores["vermelho"]}Conjunto B:{cores["amarelo"]} {conjunto_b} {cores["fim"]}')
print(f'{cores["vermelho"]}Uniao dos conjuntos A e B:{cores["amarelo"]} {union} {cores["fim"]}')
print(f'{cores["vermelho"]}Intersecao dos conjuntos A e B:{cores["amarelo"]} {intersecao} {cores["fim"]}')
print(f'{cores["vermelho"]}Complemento de B:{cores["amarelo"]} {complemento_b} \n{cores["vermelho"]}Complemento de A: {cores["amarelo"]}{complemento_a}')
print(f'{cores["lilas"]}-=-{cores["fim"]}'*25)