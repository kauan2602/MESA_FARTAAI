
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("mesafartai.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            endereco TEXT,
            latitude REAL,
            longitude REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            alimento TEXT NOT NULL,
            quantidade REAL NOT NULL,
            unidade TEXT NOT NULL,
            validade TEXT,
            status TEXT DEFAULT 'disponivel',
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doacao_id INTEGER,
            ong_id INTEGER,
            distancia REAL,
            status TEXT DEFAULT 'pendente',
            FOREIGN KEY (doacao_id) REFERENCES doacoes(id),
            FOREIGN KEY (ong_id) REFERENCES usuarios(id)
        )
    """)

    cursor.execute("""
        SELECT id FROM usuarios
        WHERE nome = ?
    """, ("ONG Prato Quente",))

    if cursor.fetchone() is None:
        cursor.execute("""
            INSERT INTO usuarios
            (nome, tipo, endereco, latitude, longitude)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "ONG Prato Quente",
            "ong",
            "São Paulo",
            -23.612,
            -46.781
        ))

    cursor.execute("""
        SELECT id FROM usuarios
        WHERE nome = ?
    """, ("ONG Abrigo Esperança",))

    if cursor.fetchone() is None:
        cursor.execute("""
            INSERT INTO usuarios
            (nome, tipo, endereco, latitude, longitude)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "ONG Abrigo Esperança",
            "ong",
            "São Paulo",
            -23.625,
            -46.795
        ))

    conexao.commit()
    conexao.close()

    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco()
