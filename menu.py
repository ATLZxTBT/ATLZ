
import sqlite3

conn = sqlite3.connect("BANCO DE DADOS")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota INTEGER
    )"""
)

print(f"\n\033[2m--==|[ NOVO ALUNO ]|==--\033[0m\n")
novo_aluno = str(input(f"\033[1mNome do novo aluno: \033[0m"))
while True:
    try:
        nota_novo_aluno = int(input(f"\033[1mNota do novo aluno: \033[0m"))
        break
    except ValueError:
        print(f"\n\033[2;32M !DIGITE UM NÚMERO VÁLIDO! \033[32m\n")

cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?, ?)", (novo_aluno, nota_novo_aluno))

conn.commit()

print(f"--==|[{novo_aluno} com nota [{nota_novo_aluno}] foi \033[32madicionado\033[0m no BANDO DE DADOS]|==--\n")

cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()


print("-"*30)


for aluno in alunos:
        print(aluno)

conn.close()
