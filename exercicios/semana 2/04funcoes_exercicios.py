#1
'''def soma(n1,n2,n3):
    calculo = n1 + n2 + n3
    print(f'A soma dos três números é {calculo}')

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))
soma(n1,n2,n3)'''

#2
'''def reverso(numero):
    numero_str = str(numero) #transforma o int em str para poder reverter
    numero_invertido = numero_str[::-1]
    print(f'{numero} -> {numero_invertido}')

numero = int(input('Digite um número: '))
reverso(numero)'''

#3
'''def tempcelsius():
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = ((9 * celsius) /5) + 32
    print(f'A temperatura {celsius} em Celsius correponde a {fahrenheit} em Fahrenheit.')

def tempfahrenheit():
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = (fahrenheit- 32)* (5/9)
    print(f'A temperatura {fahrenheit} em Fahrenheit correponde a {celsius} em Celsius.')

def menu():
    escolha = input('Deseja converter a temperatura de Celsius para Fahrenheit(responda com a letra C) ou de Fahrenheit para Celsius(responda com F)? ')
    escolha_maiusculo = escolha.upper()
    if escolha_maiusculo == 'C':
        tempcelsius()
    elif escolha_maiusculo == 'F':
        tempfahrenheit()
    else:
        print('Opção inválida!')
        menu()

menu()'''