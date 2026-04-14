conn = sqlite3.connect("BANCO_DE_DADOS.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota INTEGER
    )""")
print(f"\n\033[2m--==|[ NOVO ALUNO ]|==--\033[0m\n")
while True:
    novo_aluno = str(input(f"\033[1mNome do novo aluno (Máx. 20 Caractéres): \033[0m"))
    if len(novo_aluno) > 20:
        print(f"\n\033[2;31M !CARACTÉRES EXCEDIDOS (Tente abreviações)! \033[31m\n")
        continue
    else:
        break
while True:
    try:
        nota_novo_aluno = int(input(f"\033[1mNota do novo aluno: \033[0m"))
        break
    except ValueError:
        print(f"\n\033[2;31M !DIGITE UM NÚMERO VÁLIDO! \033[31m\n")
cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?, ?)", (novo_aluno, nota_novo_aluno))
conn.commit()
print(f"--==| \033[32m{novo_aluno}\033[0m com nota [{nota_novo_aluno}] foi \033[32madicionado\033[0m no BANDO DE DADOS |==--\n")
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()
id = "[ID]"
nam = "[NOME]"
nota = "[NOTA]"
print("≣"*42)
print(f"\033[1m{id:<4}| {nam:<20}  | {nota:<10} |\033[0m")
for aluno in alunos:
    id_aluno, novo_aluno, nota_novo_aluno = aluno
    print(f"{id_aluno:<4} | {novo_aluno:<20} | { nota_novo_aluno:<10} |")
print("≣"*42)
conn.close()
