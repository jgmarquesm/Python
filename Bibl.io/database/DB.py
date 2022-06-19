# coding: UTF-8
import os

try:
    import sqlite3 as sql
except ImportError:
    os.system("pip install sqlite3")
    import sqlite3 as sql


class DataBaseBiblioteca:

    def __init__(self, database="Biblioteca.db"):
        self.connection = sql.connect(f"{database}")
        self.cursor = self.connection.cursor()
        print("Banco de dados iniciado com sucesso.")

    def create_table(self, table_name="Livros"):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS '{table_name}'(id TEXT PRIMARY KEY NOT NULL, Título TEXT, "
            "Volume TEXT, Escritores TEXT, Edição TEXT, Ano INTEGER, Editora TEXT, ISBN INTEGER, Qtd Pgs INTEGER, "
            "Gêneros TEXT, Idioma_Original TEXT, Idioma TEXT, Tradutores TEXT, Tipo Capa TEXT)")
        self.connection.commit()

    def read_table_all(self, table_name="Livros", ordered="DESC"):
        self.cursor.execute(f"SELECT * FROM '{table_name}' ORDER BY '{ordered}'")

    def read_table_like(self, condition, like, table_name="Livros", colunm="*", ordered="DESC"):
        self.cursor.execute(
            f"SELECT '{colunm}' FROM '{table_name}' WHERE '{condition}' LIKE '%{like}%' ORDER BY '{ordered}'")

    def update_table(self, colunm, new_value, condition_value, table_name="Livros", condition="None", ordered="DESC"):
        conditionals = (
            "id", "Título", "Volume", "Escritores", "Edição", "Ano", "Editora", "ISBN", "Qtd Pgs", "Gêneros",
            "Idioma_Original", "Idioma", "Tradutores", "Tipo Capa")
        if condition not in conditionals:
            print(f"ERRO. A coluna {condition} não existe.")
        elif condition in conditionals:
            if isinstance(new_value, str) and isinstance(condition_value, str):
                self.cursor.execute(
                    f"UPDATE '{table_name}' SET '{colunm}' = '{new_value}' WHERE '{condition}' = '{condition_value}' "
                    f"ORDER BY '{ordered}'")
                self.connection.commit()
            elif isinstance(new_value, str) and isinstance(condition_value, int) or isinstance(condition_value, float):
                self.cursor.execute(
                    f"UPDATE '{table_name}' SET '{colunm}' = '{new_value}' WHERE '{condition}' = {condition_value} "
                    f"ORDER BY '{ordered}'")
                self.connection.commit()
            elif isinstance(new_value, int) or isinstance(new_value, float) and isinstance(condition_value, str):
                self.cursor.execute(
                    f"UPDATE '{table_name}' SET '{colunm}' = {new_value} WHERE '{condition}' = '{condition_value}' "
                    f"ORDER BY '{ordered}'")
                self.connection.commit()
            elif isinstance(new_value, int) or isinstance(new_value, float) and isinstance(condition_value, int) or \
                    isinstance(condition_value, float):
                self.cursor.execute(
                    f"UPDATE '{table_name}' SET '{colunm}' = {new_value} WHERE {condition} = {condition_value} "
                    f"ORDER BY '{ordered}'")
                self.connection.commit()
            else:
                print(f"ERRO. Verifique se estas entradas estão corretas: {condition_value}; {new_value}")

    def delete_table(self, condition, condition_value, table_name="Livros"):
        if isinstance(condition_value, int) or isinstance(condition_value, float):
            self.cursor.execute(f"DELETE FROM '{table_name}' WHERE '{condition}' = {condition_value}")
            self.connection.commit()
        elif isinstance(condition_value, str):
            self.cursor.execute(f"DELETE FROM '{table_name}' WHERE '{condition}' = '{condition_value}'")
            self.connection.commit()
        else:
            print(f"ERRO. Verifique se a entrada {condition_value} está correta.")

    def insert_Livros(self, id_code, title, vol, writer, ed, year, editor, isbn, pages, gender, languague, idioma,
                      translater, capa):
        self.cursor.execute(
            f"INSERT INTO Livros VALUES({id_code}, '{title}', '{vol}', '{writer}', '{ed}', {year}, '{editor}', {isbn},"
            f" {pages}, '{gender}', '{languague}', '{idioma}', '{translater}', '{capa}')")
        self.connection.commit()

    def new_backup_DB(self, path=r"D:\backups\BACKUP DB-BIBLIOTECA.bak", database="Biblioteca.db"):
        self.cursor.execute(f"BACKUP DATABASE '{database}' TO DISK '{path}'")

    def att_existing_backup_DB(self, path=r"D:\backups\BACKUP DB-BIBLIOTECA.bak", database="Biblioteca.db"):
        self.cursor.execute(f"BACKUP DATABASE '{database}' TO DISK '{path}' WITH DIFFERENTIAL")
