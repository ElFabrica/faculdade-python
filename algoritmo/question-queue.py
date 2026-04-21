import queue
from queue import Queue

fila = Queue()

validator = True

while validator:
    try:
        inputOption = int(input("Digite a opção: "))
        if(inputOption == 1 ):
            name = input("Digite seu nome: ")
            fila.put(name, block = False)
        if(inputOption == 2):
            fila.get(block = False)
        if(inputOption == 3):
            validator = False
    except queue.Full:
        print("A fila está cheia")
    except queue.Empty:
        print("A fila está vazia")

print(list(fila.queue))

print("acabou o programa")