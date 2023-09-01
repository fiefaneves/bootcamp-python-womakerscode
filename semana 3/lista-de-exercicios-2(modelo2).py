from abc import ABC, abstractmethod

#modelo 2

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

class ContaCorrente(ABC):
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

class ContaMulher(ContaCorrente):
    def __init__(self, clientes):
        super().__init__(clientes)
        self.cheque_especial = -clientes[0].renda_mensal

    def sacar(self, valor):
        if self.saldo - valor >= self.cheque_especial:
            self.saldo -= valor
            self.operacoes.append(f'Saque: -{valor}')
        else:
            print('Saldo insuficiente.')

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito: +{valor}')

class ContaHomem(ContaCorrente):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(f'Saque: -{valor}')
        else:
            print('Saldo insuficiente.')

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito: +{valor}')

cliente1 = Cliente('Fernanda', '81997487692', 1000)
cliente2 = Cliente('Carlos', '81996635050', 10000)

conta_mulher = ContaMulher([cliente1])
conta_homem = ContaHomem([cliente2])

conta_mulher.depositar(1000)
conta_mulher.sacar(1500)
print(f'Saldo da conta: {conta_mulher.saldo}')
print(f'Operações da conta: {conta_mulher.operacoes}')

conta_homem.depositar(10000)
conta_homem.sacar(10000)
conta_homem.sacar(10)
print(f'Saldo da conta: {conta_homem.saldo}')
print(f'Operações da conta: {conta_homem.operacoes}')
