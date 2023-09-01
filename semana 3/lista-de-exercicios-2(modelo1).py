# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod

class BaseBancoDelas(ABC):
    def __init__(self, nome, tipo, telefone, rendamensal):
        self.nome = nome
        self._tipo = tipo
        self._telefone = telefone
        self.rendamensal = rendamensal
        self.saldo = 0
        self.operacoes = []

    @abstractmethod
    def depositar(self):
        pass

    def sacar(self):
        pass

    def chequeespecial(self):
        pass

class BancoDelas(BaseBancoDelas):
    def __init__(self, nome, tipo, telefone, rendamensal):
        super().__init__(nome, tipo, telefone, rendamensal)

    def chequeespecial(self):
        if self._tipo == 'Feminino':
            print('Você tem direito a um cheque especial!')
        elif self._tipo == 'Masculino':
            print('Você não tem direito a um cheque especial.')
        else:
            print('Erro. Não foi possível analisar se você tem direito ao cheque especial.')
            
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        self.operacoes.append(f"Depósito: +R${valor}")
        print(f'Você depositou R${valor}, seu saldo é de R${self.saldo}.')

    def sacar(self, valor):
        if self._tipo == 'Feminino':
            self.saldo = self.saldo - valor
            if self.saldo < -self.rendamensal:
                print('Você não tem saldo suficiente para realizar esse saque.')
            else:
                self.operacoes.append(f"Saque: -R${valor}")
                print(f'Você sacou R${valor}, seu saldo agora é de R${self.saldo}.')
        elif self._tipo == 'Masculino':
            if self.saldo < valor:
                print('Você não tem saldo suficiente para realizar esse saque.')
            else:
                self.saldo = self.saldo - valor
                self.operacoes.append(f"Saque: -R${valor}")
                print(f'Você sacou R${valor}, seu saldo agora é de R${self.saldo}.')
        else:
            print('Erro. Não foi possível completar a operação.')

pessoa1 = BancoDelas('Fernanda', 'Feminino', 97487692, 1000)
pessoa1.depositar(1000)
pessoa1.sacar(1500)

pessoa2 = BancoDelas('Carlos', 'Masculino', 96635050, 10000)
pessoa2.depositar(10000)
pessoa2.sacar(10000)
pessoa2.sacar(10)