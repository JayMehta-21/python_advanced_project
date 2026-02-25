from database import (
    create_table
)

from service import(
    update_client_status,
    create_client,
    add_interaction,
)

def main():

    create_table()

    while True:

        print(".......CRM System.......")
        print("""
    1️⃣. Add client 
    2️⃣. Add Interaction
    3️⃣. Update Status
    4️⃣. View Records
    5️⃣. Exit
    """)
        
        choice=input("Choose from menu : ")

        if choice=="1":
            name=input("Enter the name of client :")
            phone=input("Client phone no : ")
            email=input("Client email :")

            try :
                create_client(name,phone,email)
                print("Client added Successfully")
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")
        elif choice=="2":

            client_id=int(input("Enter the Client Id :"))
            type=input("Enter the way of Interaction :")
            note=input("Leave some note :")

            try :
                add_interaction(client_id,type,note)
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")

        elif choice=="3":
            client_id=int(input("Enter the Client Id :"))
            new_status=input("Enter the Updated Status : ")

            try:
                update_client_status(client_id,new_status)
            except ValueError as e :
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")
                
        elif choice=="4":
            pass
        elif choice=="5":
            print("Goodbye!")
            break
        else :
            print("Choose from Menu only")