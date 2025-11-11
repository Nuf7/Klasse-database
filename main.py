from database import Database

db = Database()

def menu():
    while True:
        print("\n--- Film Database ---")
        print("1. Vis alle film")
        print("2. Søg film")
        print("3. Tilføj film")
        print("4. Opdater film")
        print("5. Slet film")
        print("0. Afslut")

        valg = input("Vælg en mulighed: ")

        if valg == "1":
            print(db.load_all())

        elif valg == "2":
            term = input("Søg efter titel: ")
            print(db.search(term))

        elif valg == "3":
            title = input("Titel: ")
            genre = input("Genre: ")
            director = input("Instruktør: ")
            year = input("År: ")
            db.insert(title, genre, director, year)
            print("Film tilføjet!")

        elif valg == "4":
            movie_id = input("Indtast ID på film, der skal opdateres: ")
            new_title = input("Ny titel (tryk Enter for at springe over): ") or None
            new_genre = input("Ny genre (tryk Enter for at springe over): ") or None
            new_director = input("Ny instruktør (tryk Enter for at springe over): ") or None
            new_year = input("Nyt år (tryk Enter for at springe over): ") or None
            db.update(movie_id, new_title, new_genre, new_director, new_year)
            print("Film opdateret!")

        elif valg == "5":
            movie_id = input("Indtast ID på film, der skal slettes: ")
            db.delete(movie_id)
            print("Film slettet!")

        elif valg == "0":
            print("Farvel 👋")
            break

        else:
            print("Ugyldigt valg – prøv igen.")

if __name__ == "__main__":
    menu()
