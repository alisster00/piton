'''
1. Clase CuentaBancaria:
    - Atributos: titular, saldo
    - Métodos: depositar(cantidad), retirar(cantidad) y mostrar_saldo().
'''

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        deposito = 700
        self.saldo += deposito
        print(f"{self.titular} ha depositado: {deposito}. Saldo: {self.saldo}")

    def retirar(self):
        retiro = 400
        self.saldo -= retiro
        print(f"{self.titular} ha retirado: {retiro}. Saldo: {self.saldo}")

    def mostrar_saldo(self):
        print(f"{self.titular} posee: {self.saldo} de saldo")

cliente = CuentaBancaria("José", 1200)

cliente.mostrar_saldo()
cliente.depositar()
cliente.retirar()


