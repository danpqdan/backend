import os
import sqlite3

class Conexao:
    def __init__(self, db_name="filme.db"):
        self.db_folder = os.getenv("DB_FOLDER", "./data")
        os.makedirs(self.db_folder, exist_ok=True) 
        self.db_file = os.path.join(self.db_folder, db_name)
        self.db = None
        self.connect()

    def connect(self):
        print(f"Conexão estabelecida com o banco: {self.db_file}")
        self.db = sqlite3.connect(self.db_file)

    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            ano INTEGER
            )
        ''')
        self.db.commit()
        self.db.close()

    def fechar(self):
        if self.db:
            self.db.close()
            print("Conexão encerrada.")


    def gravar(self, sql, params=None):
        try:
            cursor = self.db.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            self.db.commit()
            print("Gravação bem-sucedida.")
        except sqlite3.Error as e:
            print(f"Erro ao gravar no banco: {e}")
            return False
        return True

    def consultar_um(self, sql, params=None):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, params or [])
            response = cursor.fetchone()
            return response
        except sqlite3.Error as e:
            print(f"Erro ao consultar no banco: {e}")
            return None

    def consultar_lista(self, sql, params=None):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, params or [])
            response = cursor.fetchall()
            return response
        except sqlite3.Error as e:
            print(f"Erro ao consultar no banco: {e}")
            return None
