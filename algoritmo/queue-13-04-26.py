import queue
from queue import Queue

fila = queue.Queue()

fila2 = Queue(maxsize=1)
fila2.put(23)
fila2.put(13)
fila.put(78)
print(list(fila2.queue))
fila2.get()
print(list(fila2.queue))

if fila2.empty():
    print("A fila está vazia!")
else: 
    print("A fila tem algo!")

if fila2.full():
    print("A fila tem algo!")

else:
    print("A fila está vazia!")