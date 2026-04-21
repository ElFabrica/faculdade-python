value = []

for i in range(4):
    value.append(float(input(f"valor {i}: ")))
    
media = ((sum(value)/4))

if(media<7):
    print("Reprovado")

if(media>=7):
    print("Aprovado")