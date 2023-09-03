import sqlite3

conexao = sqlite3.connect('banco-de-dados')
cursor = conexao.cursor()

#Crieumatabelachamada"alunos"comosseguintescampos:id(inteiro),nome(texto),idade(inteiro)ecurso(texto)
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#Insirapelomenos5registrosdealunosnatabelaquevocêcriounoexercícioanterior
''''cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1,"Adriano", 20, "Geografia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2,"Bruna", 18, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3,"Carla", 25, "História")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4,"Diana", 22, "Arquitetura")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5,"Eduardo", 30, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6,"Fernando", 19, "Engenharia")')'''


#ConsultasBásicas
#Selecionartodososregistrosdatabela"alunos".
'''dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)'''

#Selecionaronomeeaidadedosalunoscommaisde20anos
'''dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for alunos in dados:
    print(alunos)'''

#Selecionarosalunosdocursode"Engenharia"emordemalfabética
'''dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for alunos in dados:
    print(alunos)'''

#Contaronúmerototaldealunosnatabela
'''dados = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in dados:
    print(alunos)'''

#AtualizaçãoeRemoção
#Atualizeaidadedeumalunoespecíficonatabela
#cursor.execute('UPDATE alunos SET idade=21 WHERE id=1')

#RemovaumalunopeloseuID
#cursor.execute('DELETE FROM alunos WHERE id=6')

#CriarumaTabelaeInserirDados
#Crieumatabelachamada"clientes"comoscampos:id(chaveprimária),nome(texto),idade(inteiro)esaldo(float).
#cursor.execute('CREATE TABLE clientes(id SERIAL PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
#Insiraalgunsregistrosdeclientesnatabela
'''cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Alberto", 37, 1500)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Bruna", 22, 10500)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Carolina", 32, 500)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (10, "George", 40, 400)')'''

#ConsultaseFunçõesAgregadas
#Selecioneonomeeaidadedosclientescomidadesuperiora30anos
'''dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
for clientes in dados:
    print(clientes)'''

#Calculeosaldomédiodosclientes
'''dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
for clientes in dados:
    print(clientes)'''

#Encontreoclientecomosaldomáximo
'''dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')
for clientes in dados:
    print(clientes)'''

#Contequantosclientestêmsaldoacimade1000
'''dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
for clientes in dados:
    print(clientes)'''

#AtualizaçãoeRemoçãocomCondições
#Atualizeosaldodeumclienteespecífico
#cursor.execute('UPDATE clientes SET saldo=12000 WHERE id=2')

#RemovaumclientepeloseuID
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (10, "Wallace", 50, 15000)')
#cursor.execute('DELETE FROM clientes WHERE id=10')

#JunçãodeTabelas
#Crieumasegundatabelachamada"compras"comoscampos:id(chaveprimária),cliente_id(chaveestrangeirareferenciandooiddatabela"clientes"),produto(texto)evalor(real)
#cursor.execute('CREATE TABLE compras(id SERIAL PRIMARY KEY, cliente_id INT REFERENCES clientes(id), produto VARCHAR(100), valor REAL);')

#Insiraalgumascomprasassociadasaclientesexistentesnatabela"clientes".
'''cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 1, "Armário", 100.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2, "Boneca", 150.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (7, 3, "Casa", 200.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (9, 10, "Dado", 250.00)')'''

#Escrevaumaconsultaparaexibironomedocliente,oprodutoeovalordecadacompra
'''dados = cursor.execute('SELECT * FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for clientes in dados:
    print(clientes)'''

conexao.commit()
conexao.close