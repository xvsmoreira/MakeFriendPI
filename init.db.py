import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO pets (foto, nome, idade, historia, tutor, telefone, cep, rua, numero, complemento, bairro, cidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('foto','Caramelo', '5','icone brasileiro','Pedro','967670000','08574300','Rua nao existe','155','nao tem','jd marisa','itaqua'))

cursor.execute("INSERT INTO pets (foto, nome, idade, historia, tutor, telefone, cep, rua, numero, complemento, bairro, cidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('foto','Hawk', '6','icone brasileiro','Pedro','967670000','08574300','Rua nao existe','155','nao tem','jd marisa','itaqua'))

cursor.execute("INSERT INTO pets (foto, nome, idade, historia, tutor, telefone, cep, rua, numero, complemento, bairro, cidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('foto','Teste', '10','teste','teste','967670000','08574300','Rua teste','155','nao tem','jd marisa','itaqua'))

connection.commit()
connection.close()