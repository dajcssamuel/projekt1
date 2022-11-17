import sqlite3

con = sqlite3.connect("pizza.db")
print("Database opened successfully")

con.execute(
    "create table Pizzak (id INTEGER PRIMARY KEY AUTOINCREMENT, nev TEXT NOT NULL, leiras TEXT UNIQUE NOT NULL, meret INTEGER NOT NULL, ar INTEGER NOT NULL)")

print("Table created successfully")

con.close()