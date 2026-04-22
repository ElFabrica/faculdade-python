# ======================================
# ATIVIDADE: SISTEMA BANCÁRIO (POO)
# ======================================

from datetime import datetime


# ======================================
# Classe Conta
# ======================================
class Conta:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0
        self.historico = []
        self.tipo = "Standard"

    def depositar(self, valor):
        if (valor>0):
            self.saldo += valor
            self.historico.append(f"{self.titular} ; {datetime.now()} - Depósito: +R${valor} ; Saldo:R${self.saldo}")
        else:
            print("Valor inválido!")


    def sacar(self, valor):
        if (valor<=self.saldo):
            self.saldo -= valor
            print("flag")
            self.historico.append(f"{self.titular} ; {datetime.now()} - Saque: -R${valor} ; Saldo:R${self.saldo}")

        else:
            print("Saldo insuficiente!")


    def consultar_saldo(self):
        return self.saldo

    def exibir_historico(self):
        for h in self.historico:
            print(h)

# ======================================
# Classe ContaCorrente
# ======================================
class ContaCorrente(Conta):
    def __init__(self, titular, numero, limite=500):
        super().__init__(titular, numero)
        self.limite = limite

# ======================================
# Classe Banco
# ======================================
class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular):
        self.conta_numero = len(self.contas) + 1
        self.conta = ContaCorrente(titular, self.conta_numero)
        self.contas[self.conta_numero] = self.conta
   


    def buscar_conta(self, numero):
        return self.contas.get(numero)



    def transferir(self, origem, destino, valor):
        origem.sacar(valor)
        destino.depositar(valor)

    # def emprestimo(self, valor_emprestimo):



# ======================================
# TESTE DO SISTEMA
# ======================================

banco = Banco()

# Criar contas
banco.criar_conta("João")
banco.criar_conta("Maria")
print(banco.contas[2].titular)

# Buscar contas
conta1 = banco.buscar_conta(1)

conta2 = banco.buscar_conta(2)

print(conta1.consultar_saldo())
conta1.depositar(1000)
print(conta1.consultar_saldo())
conta1.depositar(200)
print(conta1.consultar_saldo())
conta1.sacar(400)
print(conta1.consultar_saldo())

banco.transferir(conta1, conta2, 300)
conta1.exibir_historico()
conta2.exibir_historico()



# Realizar operações
# TODO: testar depósito, saque e transferência

# conta1.depositar(1000)
# conta1.sacar(200)
# banco.transferir(1, 2, 300)

# conta1.consultar_saldo()
# conta2.consultar_saldo()

# conta1.exibir_historico()
# conta2.exibir_historico()