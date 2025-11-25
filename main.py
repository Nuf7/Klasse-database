from database import Database
from film import Film

def print_menu():
    print("\n--- FILM MENU ---")
    print("1. Vis alle film")
    print("2. Søg film")
    print("3. Tilføj film")
    print("4. Opdater film")
    print("5. Slet film")
    print("6. Afslut")

def main():
    db = Database()

    while True:
        print_menu()
        choice = input("Vælg en mulighed: ")

        # 1. Vis alle film
        if choice == "1":
            movies = db.load_all()
            print("\n--- ALLE FILM ---")
            for m in movies:
                print(m, "\n")

        # 2. Søg film
        elif choice == "2":
            term = input("Indtast søgeord: ")
            hits = db.search(term)
            print("\n--- SØGERESULTAT ---")
            for h in hits:
                print(h, "\n")

        # 3. Tilføj film
        elif choice == "3":
            title = input("Titel: ")
            genre = input("Genre: ")
            director = input("Instruktør: ")
            year = int(input("År: "))

            db.insert(Film(None, title, genre, director, year))
            print("Film tilføjet!")

        # 4. Opdater film
        elif choice == "4":
            movie_id = int(input("ID på den film du vil opdatere: "))
            film = db.load(movie_id)

            if film is None:
                print("Film blev ikke fundet.")
            else:
                print("Efterlad tomt felt for at beholde nuværende værdi.")
                title = input(f"Ny titel ({film.title}): ") or film.title
                genre = input(f"Ny genre ({film.genre}): ") or film.genre
                director = input(f"Ny instruktør ({film.director}): ") or film.director
                year = input(f"Nyt år ({film.year}): ") or film.year

                updated = Film(movie_id, title, genre, director, int(year))
                db.update(movie_id, updated)
                print("Filmen er opdateret!")

        # 5. Slet film
        elif choice == "5":
            movie_id = int(input("ID på film der skal slettes: "))
            db.delete(movie_id)
            print("Film slettet (hvis ID fandtes).")

        # 6. Afslut
        elif choice == "6":
            print("Farvel!")
            break

        else:
            print("Ugyldigt valg – prøv igen.")

if __name__ == "__main__":
    main()
