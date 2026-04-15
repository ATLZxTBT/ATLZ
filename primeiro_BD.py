import sqlite3

conn = sqlite3.connect("BANCO_DE_DADOS.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota INTEGER
    )""")
while True:
    print(f"\n\033[1;32m--==| SERVIDOR |==--\033[0m\n")
    print(f"\033[1;32m[1] Alunos\n[2] Adicionar aluno\n[3] Remover aluno\n[4] Alterar nota\033[0m\n\033[31m[5] Encerrar sessão\033[0m\n")
    opcao = int(input(f"\033[2m: \033[0m"))

    # Mostar tabela
    if opcao == 1:
        print(f"\n\033[1m| ALUNOS |\033[0m")
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        id = "[ID]"
        nam = "[NOME]"
        nota = "[NOTA]"
        print("≣"*42)
        print(f"\033[1m{id:<4} | {nam:<20} | {nota:<10} |\033[0m")
        for aluno in alunos:
            id_aluno, novo_aluno, nota_novo_aluno = aluno
            print(f"{id_aluno:<4} | {novo_aluno:<20} | { nota_novo_aluno:<10} |")
        print("≣"*42)

    # Adicionar aluno
    elif opcao == 2:
        print(f"\n\033[1m| NOVO ALUNO |\033[0m")
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

    # Remover aluno
    elif opcao == 3:
        print(f"\n\033[1m| REMOVER ALUNO |\033[0m")
        remover = int(input("ID do aluno: "))
        cursor.execute("SELECT * FROM alunos WHERE id = ?", (remover,))
        alunos = cursor.fetchone()

        if alunos:
            print(f"\n\033[1;32mREMOVENDO {alunos[1]}\033[0m\n")
            cursor.execute("DELETE FROM alunos WHERE id = ?", (remover,))
            conn.commit()
            print("Aluno removido!")
        else:
            print(f"\033[1;31mID NÃO ENCONTRADO!\033[0m")
    
    # Alterar nota
    elif opcao == 4:
        print(f"\n\033[1m| ALTERAR NOTA |\033[0m")
        nova_nota = int(input("ID do aluno: "))
        cursor.execute("SELECT * FROM alunos WHERE id = ?", (nova_nota,))
        alunos = cursor.fetchone()

        if alunos:
            print(f"Aluno: {alunos[1]} - Nota: {alunos[2]}\n")
            change = int(input("Nova nota: "))
            cursor.execute("UPDATE alunos SET nota = ? WHERE id = ?", (change, nova_nota,))
            conn.commit()
            print(f"\033[1;32mNota atualizada com sucesso!\033[0m")
        else:
            print(f"\033[1;31mID NÃO ENCONTRADO!\033[0m")
    
    # Sair
    elif opcao == 5:
        break
