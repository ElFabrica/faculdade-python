#QUESTÃO CLASSICA - APROVADO, PROVA FINAL E REPROVADO   

nome = input("Seu nome: ")
nota01 = float(input("Nota 01: "))
nota02 = float(input("Nota 02: "))
nota03 = float(input("Nota 03: "))
nota04 = float(input("Nota 04: "))

media = (nota01 + nota02 + nota03 + nota04 )/4

if media >=0 and media < 4:
    print(f"Sua média é {media} e está reprovado(a)!")
elif media >= 4 and media < 7:
    print(f"Sua média é: {media} e está de prova final!")
elif media >= 7:
    print(f"Sua média é: {media} e está aprovado(a)!")
else:
    print("Algo de errado não está certo")