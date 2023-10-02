#1
'''def calculo_dolar_americano():
    dolar_americano = dinheiro / 4.91
    return dolar_americano

def calculo_peso_argentino():
    peso = dinheiro / 0.02
    return peso

def calculo_dolar_australiano():
    dolar_australiano = dinheiro / 3.18
    return dolar_australiano

def calculo_dolar_canadense():
    dolar_canadense = dinheiro / 3.64
    return dolar_canadense

def calculo_franco_suico():
    franco = dinheiro / 0.42
    return franco

def calculo_euro():
    euro = dinheiro / 5.36
    return euro

def calculo_libra_esterlina():
    libra = dinheiro / 6.21
    return libra

dinheiro = float(input('Insira o valor em reais: '))
print(f'Você pode comprar em cada moeda:\n Dólar Americano: {calculo_dolar_americano()} dolares;\n Peso argentino: {calculo_peso_argentino()} pesos;\n Dólar Australiano: {calculo_dolar_australiano()} dolares;\n Dólar Canadense: {calculo_dolar_canadense()} dolares;\n Francp Suiço: {calculo_franco_suico()} francos;\n Euro: {calculo_euro()} euros;\n Libra esterlina: {calculo_libra_esterlina()} libras.')'''

#2
'''def aluguel():
    valor1 = 80 * dias
    valor2 = 0.2 * km_rodados
    total = valor1 + valor2
    return total

km_rodados = float(input('Informe a quantidade de quilômetros(km) rodados pelo veículo alugado: '))
dias = int(input('Informe a quantidade de dias que o veículo foi alugado: '))
print(f'O preço a pagar é: R${aluguel()}.')'''

#3
'''def novo_salario():
    if salario <= 1000.0:
        reajuste = salario * 1.2
    elif 1000.0 < salario <= 2800.0:
        reajuste = salario * 1.1
    elif 2800 < salario:
        reajuste = salario * 1.05
    else:
        print('Erro: valor informado inválido.')
    return reajuste

salario = float(input('Informe seu salário atual: '))
print(f'Seu novo salário é: R${novo_salario()}.')'''

#4
'''def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('Valor inválido. Digite um número inteiro válido.')

numero = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número: {numero}')'''
