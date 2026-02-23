import sqlite3

from database import(
    add_client
)

def create_client(name,phone,email):

    if name.strip()==" ":
        raise ValueError("name should not be empty")
    if phone==" ":
        raise ValueError("phone no should not be empty")
    if email==" ":
        raise ValueError("email should not be empty")
    
    try:
        add_client(name,phone,email)
    except sqlite3.IntegrityError:
        raise ValueError("Client already exists")