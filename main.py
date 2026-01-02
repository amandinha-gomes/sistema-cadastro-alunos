import sqlite3

conexao = sqlite3.connect("alunos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso TEXT NOT NULL,
    idade INTEGER
)
""")
conexao.commit()

while True:
    print("\n=== Sistema de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        curso = input("Curso: ")
        idade = int(input("Idade: "))

        cursor.execute(
            "INSERT INTO alunos (nome, curso, idade) VALUES (?, ?, ?)",
            (nome, curso, idade)
        )
        conexao.commit()
        print("Aluno cadastrado!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        print("\nAlunos cadastrados:")
        for a in alunos:
            print(f"{a[0]} - {a[1]} | {a[2]} | {a[3]} anos")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

conexao.close()
