from database import Database
from film import Film

def main():
    db = Database()

    print("\n--- Tilføjer film ---")
    db.insert(Film(None, "Matrix", "Sci-Fi", "Wachowski", 1999))

    print("\n--- Viser alle film ---")
    movies = db.load_all()
    for m in movies:
        print(m, "\n")

    print("\n--- Søger efter 'Matrix' ---")
    hits = db.search("Matrix")
    for h in hits:
        print(h, "\n")

    print("\n--- Opdaterer film ---")
    if hits:
        film_id = hits[0].id
        updated = Film(film_id, "The Matrix", "Science Fiction", "Wachowski", 1999)
        db.update(film_id, updated)

    print("\n--- Film efter opdatering ---")
    movies = db.load_all()
    for m in movies:
        print(m, "\n")

    print("\n--- Sletter film ---")
    if hits:
        db.delete(hits[0].id)

    print("\n--- Film efter sletning ---")
    movies = db.load_all()
    for m in movies:
        print(m, "\n")

if __name__ == "__main__":
    main()
