#1- a)

# numeros = [0, 0, 0, 0, 0]

# for i in range(5):
#     numeros[i] = float(input("Digite um número qualquer: "))

# for i in range(5):
#     print(numeros[i])

#1- b) Isso geraria erro de sintaxe, porque o while precisa de uma condição completa, ou seja, uma variável sendo comparada.

#1- c) Não funcionaria corretamente. Porque a lista já foi criada com tamanho fixo de 5 posições.

#1- d) Nem sempre sabemos quantos dados o usuário vai inserir. O código fica pouco reutilizável. Qualquer mudança exige editar o código manualmente

2 

l = [1,2,3]
x = 0
while x < 3:
    print(l[x])
    x +=1

#a) A variável x termina com valor 3.

#b)Não necessariamente. Neste caso específico, sim, coincide (3 elementos → x termina em 3), mas isso é coincidência.

#c) O código não mostraria todos os elementos. O while continua limitado a x < 3. Mesmo com 6 elementos, só percorre os índices 0, 1 e 2

#d) 

# l = [7,8,9,10,11,12]
# x = 0
# for item in l:
#     print(item)
#     x += item

#3-

A = ["mouse", "teclado", "monitor", "estabilizador"]
B = ["memória", "cpu", "ssd", "chipset", "rom"]

C = []

for itemA in A :
    C.append(itemA) 

for itemB in B :
    C.append(itemB) 

print(C)

#4- 

A = ['Python', 'Java', 'C', 'PHP', 'JavaScript', 'Dart']
B = ['C++', 'Python', 'Java', 'Julia', 'Go', 'JavaScript']

C = list(set(A + B))

print(C)