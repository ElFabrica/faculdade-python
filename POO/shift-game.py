import random


# Classe base

class Personagem:

    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.__vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        dano = random.randint(1, self.ataque)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0


    def esta_vivo(self):
        return self.__vida > 0


    def mostrar_status(self):
        print(f"{self.nome} - Vida: {self.__vida}")



# Classe Guerreiro

class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=25)

    def ataque_especial(self, alvo):
        dano = random.randint(20, 40)
        print(f"💥 {self.nome} usou ATAQUE PESADO em {alvo.nome} causando {dano}!")
        alvo.receber_dano(dano)
class Orc(Personagem):

    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=25)

    def ataque_especial(self, alvo):
        dano = random.randint(20, 40)
        print(f"💥 {self.nome} usou ATAQUE PESADO em {alvo.nome} causando {dano}!")
        alvo.receber_dano(dano)

# Classe Mago

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=30)
        self.mana = 100

    def magia(self, alvo):
        if self.mana >= 20:
            dano = random.randint(25, 50)
            self.mana -= 20
            print(f"🔥 {self.nome} lançou magia em {alvo.nome} causando {dano}!")
            alvo.receber_dano(dano)
        else:
            print("❌ Mana insuficiente!")

# Função de batalha

def batalha(jogador, inimigo):
    turno = 1
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        jogador.mostrar_status()
        inimigo.mostrar_status()
        print("\nEscolha sua ação:")
        print("1 - Ataque normal")
        if isinstance(jogador, Guerreiro):
            print("2 - Ataque especial")
        elif isinstance(jogador, Mago):
            print("2 - Magia")
        escolha = input("Opção: ")

        # Ação do jogador
        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            if isinstance(jogador, Guerreiro):
                jogador.ataque_especial(inimigo)
            elif isinstance(jogador, Mago):
                jogador.magia(inimigo)
        else:
            print("Opção inválida!")

        # Verifica se inimigo morreu
        if not inimigo.esta_vivo():
            print(f"\n🏆 {jogador.nome} venceu!")
            break

        # Turno do inimigo
        print("\n👾 Turno do inimigo!")
        inimigo.atacar(jogador)
        if not jogador.esta_vivo():
            print(f"\n💀 {jogador.nome} foi derrotado!")
        turno += 1

# Execução

print("🎮 Escolha seu personagem:")
print("1 - Guerreiro")
print("2 - Mago")

opcao = input("Digite: ")
nome = input("Nome do personagem: ")

if opcao == "1":
    jogador = Guerreiro(nome)
elif opcao == "2":
    jogador = Mago(nome)
else:
    print("Opção inválida! Usando Guerreiro padrão.")
    jogador = Guerreiro(nome)

# Inimigo automático

inimigo = Orc("Orc")

# Iniciar batalha

batalha(jogador, inimigo)