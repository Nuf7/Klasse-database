class Film:
    def __init__(self, id, title, genre, director, year):
        self.id = id
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year

    def __str__(self):
        return (
            f"Film:\n"
            f"  ID: {self.id}\n"
            f"  Titel: {self.title}\n"
            f"  Genre: {self.genre}\n"
            f"  Instruktør: {self.director}\n"
            f"  År: {self.year}"
        )
