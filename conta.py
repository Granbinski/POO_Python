

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Initializing")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
