#Criar sistema que simule um banco, a classe deve ter um método saque, depósito e transferencia
    #Propriedades nome do proprietario da conta, saldo e etc

class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        
    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor
        
c1 = Banco('Andrade', 750.00)
#print(c1.saldo)
c1.sacar(50.0)
#print(c1.saldo)
c1.depositar(50.0)
#print(c1.saldo)
c2 = Banco('Arisio', 0)
c1.transferir(c2,50)
print(c1.saldo)
print(c2.saldo)
