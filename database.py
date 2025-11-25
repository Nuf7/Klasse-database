import sqlite3
from film import Film

DB_FILE = "Movies.db"


class Database:

    def _connect(self):
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn

    def _execute(self, query, params=()):
        conn = self._connect()
        try:
            conn.execute(query, params)
            conn.commit()
        finally:
            conn.close()

    def _run_query(self, query, params=()):
        conn = self._connect()
        try:
            cur = conn.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()
        return rows

    
    # CRUD – OOP version
   

    def search(self, term):
        query = "SELECT * FROM movies WHERE title LIKE ?"
        rows = self._run_query(query, (f"%{term}%",))
        return [Film(r["id"], r["title"], r["genre"], r["director"], r["year"]) for r in rows]

    def load(self, movie_id):
        query = "SELECT * FROM movies WHERE id = ?"
        rows = self._run_query(query, (movie_id,))
        if not rows:
            return None
        r = rows[0]
        return Film(r["id"], r["title"], r["genre"], r["director"], r["year"])

    def load_all(self):
        query = "SELECT * FROM movies"
        rows = self._run_query(query)
        return [Film(r["id"], r["title"], r["genre"], r["director"], r["year"]) for r in rows]

    def insert(self, film: Film):
        query = """
            INSERT INTO movies (title, genre, director, year)
            VALUES (?, ?, ?, ?)
        """
        self._execute(query, (film.title, film.genre, film.director, film.year))

    def update(self, movie_id, film: Film):
        query = """
            UPDATE movies
            SET title = ?, genre = ?, director = ?, year = ?
            WHERE id = ?
        """
        self._execute(query, (film.title, film.genre, film.director, film.year, movie_id))

    def delete(self, movie_id):
        query = "DELETE FROM movies WHERE id = ?"
        self._execute(query, (movie_id,))
