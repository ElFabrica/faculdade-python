from queue import PriorityQueue

fila = PriorityQueue()
fila.put((2, "Ler livro"))
fila.put((2, "Ler livro"))
fila.put((2, "Ler livro"))
fila.put((2, "Ler livro"))
while not fila.empty():
    fila.get()