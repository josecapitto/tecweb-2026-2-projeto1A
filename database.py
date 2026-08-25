import sqlite3

class Database:
    def __init__(self, nome_banco):
        if '.db' not in nome_banco:
            nome_banco += '.db'
        self.nome_banco = nome_banco
        self.conn = sqlite3.connect(nome_banco)

        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")
        self.conn.commit()
    
    def add(self, note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}')")
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        notes = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            notes.append(Note(id=id, title=title, content=content))
        return notes

    def update(self, entry):
        self.conn.execute(
            "UPDATE note SET title = ?, content = ? WHERE id = ?",
            (entry.title, entry.content, entry.id)
        )
        self.conn.commit()
    
    def delete(self, id):
        self.conn.execute(
            "DELETE FROM note WHERE id = ?",
            (id,)
        )
        self.conn.commit()

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''