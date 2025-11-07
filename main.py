from database import Database

db = Database()

# Opret ny film
db.insert("Inception", "Sci-Fi", "Christopher Nolan", 2010)

# Vis alle film
print("Alle film:")
print(db.load_all())

# Søg efter film
print("\nSøgning efter 'Inception':")
print(db.search("Inception"))
