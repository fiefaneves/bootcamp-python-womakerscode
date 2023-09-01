# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 100

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10

# Crie uma instância da classe carro.
carro = Carro('Preto', 'Ford')

# Faça o carro "andar" utilizando os métodos da sua classe.
carro.ligar()
carro.acelerar()
print('CARRO LIGADO')
print('O carro está ligado? {}'.format(carro.ligado))
print('O carro está com que velocidade? {} km/h'.format(carro.velocidade))

# Faça o carro "parar" utilizando os métodos da sua classe.
carro.desacelerar()
carro.desligar()
print('CARRO DESLIGADO')
print('O carro está com que velocidade? {} km/h'.format(carro.velocidade))
print('O carro está ligado? {}'.format(carro.ligado))