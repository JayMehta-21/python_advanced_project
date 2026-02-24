import sqlite3

from database import(
    add_client,
    get_client_by_id,
    interaction
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

def add_interaction(client_id,type,note):
    
    client_detail= get_client_by_id(client_id)

    if client_detail is None:
        raise ValueError("Client not found")
    
    status= client_detail[4]

    valid_interacion={"call","email","meeting"}

    if type not in valid_interacion:
        raise ValueError("Invalid interaction type")

    try :
        interaction(client_id,type,note)
    except sqlite3.IntegrityError:
        raise ValueError("Check Contraints Failed")

def update_client_status(client_id,new_status):

    client_details= get_client_by_id(client_id)

    if client_details is None:
        raise ValueError("Client not Exists")
    
    current_status=client_details[4]

    valid_transactions={
        "lead":["contacted","converted"],
        "contacted": ["converted","lost"],
        "converted": [],
        "lost":[],
    }

    if new_status not in valid_transactions(current_status):
        raise ValueError("Invalid status transitions")