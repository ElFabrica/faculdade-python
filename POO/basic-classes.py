class Carro:
  def _init_(self):
    self.tipo = "carro"
    

  def getIdeitificador(self):
    return self.identificador

  def setIdentificador(self, identificador):
    self.identificador = identificador

  def setProprietario(self, name):
    self.proprietario = name

  def getProprietario(self):
    return self.proprietario

  def setColor(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def getVelocidadeMaxima(self):
    vel = 2 * self.identificador
    return vel

  def listCars(self):
    return {
        "id":self.getIdeitificador(),
        "name": self.getProprietario(),
        "color": self.getColor(),
        "maxValocity": self.getVelocidadeMaxima()
    }

  def printAll(self):
    print(self.getIdeitificador())
    print(self.getProprietario())
    print(self.getColor())
    print(self.getVelocidadeMaxima())


veiculo1 = Carro()
veiculo1.setIdentificador(100)
veiculo1.setProprietario("João")
veiculo1.setColor("azul")

veiculo2 = Carro()
veiculo2.setIdentificador(110)
veiculo2.setProprietario("Maria")
veiculo2.setColor("verde")

veiculo3 = Carro()
veiculo3.setIdentificador("007")
veiculo3.setProprietario("Arthur")
veiculo3.setColor("Prata")



print(veiculo1.listCars())
print(veiculo2.listCars())
print(veiculo3.listCars())

print("______________________________________")

print(veiculo1.printAll())