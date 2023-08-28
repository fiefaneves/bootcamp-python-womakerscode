#funções

'''def soma(): #definição da função soma
    calculosoma = numero1 + numero2
    print(f'O resultado da soma é {calculosoma}')

def subtracao():
    calculosub = numero1 - numero2
    print(f'O resultado da subtração é {calculosub}')
    multiplicacao() #chamando uma função dentro de outra

def multiplicacao():
    calculomulti = numero1 * numero2
    print(f'O resultado da multiplicação é {calculomulti}')

numero1 = int(input('Digite o primeiro número: ')) #parametros
numero2 = int(input('Digite o segundo número: '))
soma() #chamada da função
subtracao()'''

#parametros

'''def soma(numero1,numero2): 
    calculosoma = 10 + 8
    print(f'O resultado da soma é {calculosoma}')
    
numero1 = int(input('Digite o primeiro número: ')) 
numero2 = int(input('Digite o segundo número: '))
soma(numero1,numero2) '''

#manipulação de arquivos

'''numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
mult = numero1 * numero2

#abertura de arquivo
file = 'arquivo.txt'

#abertura para escrita
arquivo_escrita = open(file, "w")
arquivo_escrita.write(f'O resultado da multiplicação é {mult}')
arquivo_escrita.close() #para abrir o arquivo novamente é preciso fechar

#abertura somente para leitura
arquivo_leitura = open(file, "r")
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()

#abertura de arquivos binarios
arquivo_binario = open(file, "wb")'''

#tratamento de exceções
def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('Erro: Impossível dividir um valor por zero.')
    except TypeError as e:
        print(f'Erro: Impossível dividir um valor por um texto.\nDetalhes: {e}')
    else:
        print('Sem exceções.')

#divisao(10,2) #imprime resultado
#divisao(10,0)  #imprime erro 
divisao(10, 'texto') #imprime erro