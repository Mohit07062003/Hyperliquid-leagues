# db.py
from tinydb import TinyDB

db = TinyDB("db.json")
leagues_table = db.table("leagues")

