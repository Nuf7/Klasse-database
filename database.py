import sqlite3
from pathlib import Path

Base_dir = Path(__file__).resolve().parent
DB_FILE = Base_dir / "Movies.db"

DB_FILE = "Movies.db"

# Denne klasse håndterer al kommunikation med databasen 'Movies.db'.
# Den sørger for at oprette forbindelse, køre forespørgsler og hente eller indsætte data.
class Database:
   
    # Denne metode opretter og returnerer en forbindelse til databasen.
    # row_factory sættes til sqlite3.Row, så data kan tilgås som ordbøger,
    # hvilket gør det lettere at arbejde med resultaterne i Python.
    def _connect(self):
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn

    # Denne metode bruges til at udføre ændrende forespørgsler som
    # INSERT, UPDATE eller DELETE. Efter udførsel gemmes ændringerne
    # med commit(), og forbindelsen lukkes igen.
    def _execute(self, query, params=()):
        conn = self._connect()
        try:
            conn.execute(query, params)
            conn.commit()
        finally:
            conn.close()

    # Denne metode bruges til at køre SELECT-forespørgsler og hente data fra databasen.
    # Resultaterne omdannes til en liste af ordbøger, så de er nemme at arbejde med.
    def _run_query(self, query, params=()):
        conn = self._connect()
        try:
            cur = conn.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()
        return [dict(row) for row in rows]



    # Finder film, hvor titlen indeholder det søgte ord.
    # Søgetermen indsættes i et LIKE-udtryk for at finde delvise match.
    def search(self, term):
        query = "SELECT * FROM movies WHERE title LIKE ?"
        return self._run_query(query, (f"%{term}%",))

    # Henter en enkelt film ud fra dens ID.
    # Hvis filmen ikke findes, returneres None.
    def load(self, movie_id):
        query = "SELECT * FROM movies WHERE id = ?"
        result = self._run_query(query, (movie_id,))
        return result[0] if result else None

    # Henter alle film fra databasen og returnerer dem som en liste.
    def load_all(self):
        query = "SELECT * FROM movies"
        return self._run_query(query)

    # Indsætter en ny film i databasen med titel, genre, instruktør og årstal.
    def insert(self, title, genre, director, year):
        query = "INSERT INTO movies (title, genre, director, year) VALUES (?, ?, ?, ?)"
        self._execute(query, (title, genre, director, year))
    
    # Opdaterer en eksisterende film baseret på ID.
    # Felter kan opdateres individuelt efter behov.
    def update(self, movie_id, title=None, genre=None, director=None, year=None):
        fields = []
        params = []

        if title is not None:
            fields.append("title = ?")
            params.append(title)
        if genre is not None:
            fields.append("genre = ?")
            params.append(genre)
        if director is not None:
            fields.append("director = ?")
            params.append(director)
        if year is not None:
            fields.append("year = ?")
            params.append(year)

        if not fields:
            return  # Intet at opdatere

        query = f"UPDATE movies SET {', '.join(fields)} WHERE id = ?"
        params.append(movie_id)
        self._execute(query, params)

    # Sletter en film ud fra dens ID.
    def delete(self, movie_id):
        query = "DELETE FROM movies WHERE id = ?"
        self._execute(query, (movie_id,))
