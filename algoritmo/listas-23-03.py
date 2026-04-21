dados = [1,2,3,"segunda", 3.14, "PIT", "10.50"]

# print(dados)
# print(len(dados))
# print(dados[3])
# print(dados[2:5]) #Percorre um intervalo
# num = 1,2
# print(type(num)) #Mostra o tipo de dados tupla
# print(type(dados)) #Mostra o tipo de dados array
dados.extend(["Programação", 3, "prova", 56.78]) #adiciona mais de um item no array
dados.append("last item") #Adiciona um item ao final da lista

# print(dados)

del dados[4] #remove especificamente este elemento
valuePoped = dados.pop() #Remove o item da lista e retorna o valor removido. Remove o ultimo item caso não passe o index da posição

dados.remove("PIT") #remove o item que eu repassar o valor

print(dados)