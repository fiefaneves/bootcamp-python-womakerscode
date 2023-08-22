#1
'''alunos = 1
media_alunos = []

while alunos <= 10:
    print(f"Aluno {alunos}:")
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    nota4 = float(input('Digite a nota 4: '))

    media = (nota1 + nota2 + nota3 + nota4)/4

    media_alunos.append(media)
    alunos += 1

alunos_aprovados = 0
for media in media_alunos:
    if media >= 7.0:
        alunos_aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 é: {alunos_aprovados}")'''

'''
medias = []

for i in range(10):  # Vai pedir as notas de 10 alunos
    print(f"Aluno {i + 1}:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    
    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media)

alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 é: {alunos_aprovados}")'''

#2
'''nome = input('Digite o seu nome: ')
nome_maiusculo = nome.upper() #Converte o nome para letras maiúsculas
nome_invertido = nome_maiusculo[::-1] #Inverte o nome
print("Nome de trás para frente:", nome_invertido)'''

#3
'''def todos_valores_emitidos(dicionario):
    for valor in dicionario.values():
        if valor is None:
            return False
    return True

meu_dicionario = {'chave1': 10, 'chave2': 'abc', 'chave3': None, 'chave4': None}

resultado = todos_valores_emitidos(meu_dicionario)
print(resultado)'''

#4
'''def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (sim/não): ").lower()
    if resposta == "sim":
        return True
    elif resposta == "não":
        return False
    else:
        print("Resposta inválida. Responda com 'sim' ou 'não'.")
        return fazer_pergunta(pergunta)

def classificar_participacao(respostas):
    num_respostas_positivas = respostas.count(True)
    
    if num_respostas_positivas == 2:
        return "Suspeita"
    elif 3 <= num_respostas_positivas <= 4:
        return "Cúmplice"
    elif num_respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"

#Faz as perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []
for pergunta in perguntas:
    respostas.append(fazer_pergunta(pergunta))

classificacao = classificar_participacao(respostas)
print("Classificação:", classificacao)'''
