from queue import PriorityQueue
import queue


fila = PriorityQueue()
system = True
while system:
    try:
        print("Welcome to basic of the service system. Select the option 1 to service start, 2 to run the service and 3 to finish the service")
        optionNumber = int(input("Digite uma opção: "))
        match optionNumber:
            case 1:
                print("Digite 1 para atendimento 80+, 2 para grávidas e atendimento inclusão e 3 para atendimento geral")
                optionAttendiment = int(input("Digite a opção: "))
                match optionAttendiment:
                    case 1:
                        fila.put((1, "Atendimento 80+"))
                        print(f"Fila atual {list(fila.queue)}")
                    case 2:
                        fila.put((2, "Atendimento grávida"))
                        print(f"Fila atual {list(fila.queue)}")
                    case 3:
                        fila.put((3, "Atendimento inclusão"))
                        print(f"Fila atual {list(fila.queue)}")
                    case 4:
                        fila.put((4, "geral"))
                        print(f"Fila atual {list(fila.queue)}")
                    case _:
                        print("Opção inválida!")
            case 2:
                fila.get_nowait()
            case 3:
                system = False
                print("O sistema foi finalizado!")
            case _:
                print("Opção inválida parceiro!!")
    except queue.Empty:
        print("A fila está vazia")             
    except():
        print("Algo deu errado")

    