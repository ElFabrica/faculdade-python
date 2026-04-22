# class Bird:
#     def sound(self):
#         return "Tweet"
    
# class Dog:
#     def sound(self):
#         return "Bark"
    
# def make_sound(animal):
#     print(animal.sound())

# bird = Bird()
# dog = Dog()

# # make_sound(bird)
# # make_sound(dog)

#Polimorfismo com perímetro e área

# class Quadrado:
#     def __init__(self, lado):
#         self.lado = lado

#     def perimetro(self):
#         print(f"o perímetro é: {self.lado *4}")

#     def area(self):
#         print(f"o area é: {self.lado**2}")

# class Triangulo:
#     def __init__(self, lado, altura):
#         self.lado = lado
#         self.altura = altura

#     def perimetro(self):
#         print(f"o perímetro é: {self.lado *3}")

#     def area(self,):
#         print(f"o area é: {(self.lado * self.altura)/2}")

# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio

#     def perimetro(self):
#         print(f"o perímetro é: {2 * self.raio *3.14}")

#     def area(self):
#         print(f"o area é: {3.14 * self.raio}")

    
# def calcula_pedimetro(object):
#     print(object.perimetro())

# def calcula_area(object):
#     print(object.area())
    
# quadrado = Quadrado(3)
# triangulo = Triangulo(2,4)
# circulo = Circulo(4)

# calcula_pedimetro(quadrado)
# calcula_area(triangulo)

class Pagamento:
    def __init__(self):
         self.valor = 0.0

    def start(self):
        self.metodo_pagamento()

    def metodo_pagamento(self):
        self.metodo = input("Digite o método de pagamento: ")
        self.valor_pago()

    def valor_pago(self):
        self.valor = float(input("Digite o valor: "))
        self.processar_pagamento()

    def processar_pagamento(self):
        if self.metodo == "Cartão":
            print(f"Pagamento processado com sucesso! R$: {self.valor}") 
        elif self.metodo == "Pix":
            print(f"Pagamento do pix processado com sucesso! R$: {self.valor}")
        elif self.metodo == "Boleto":
            print(f"Pagamento do Boleto processado com sucesso! R$: {self.valor}")
             
pg1 = Pagamento()

pg1.start()


