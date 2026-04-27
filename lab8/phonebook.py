import psycopg2
from connect import get_connection

def insert_or_update():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
                conn.commit()
                print("Success: Contact saved.")
    except Exception as e:
        print(f"Database Error: {e}")

def search():
    pattern = input("Search term: ").strip()
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                # We are calling V3 here to bypass the old error
                cur.execute("SELECT * FROM search_contacts_v3(%s)", (pattern,))
                rows = cur.fetchall()
                if not rows:
                    print("No contacts found.")
                else:
                    print(f"\n{'ID':<5} | {'Name':<20} | {'Phone':<15}")
                    print("-" * 45)
                    for r in rows:
                        print(f"{r[0]:<5} | {r[1]:<20} | {r[2]:<15}")
    except Exception as e:
        print(f"Database Error: {e}")

def paginate():
    try:
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_contacts_paginated_v3(%s, %s)", (limit, offset))
                rows = cur.fetchall()
                print(f"\n{'ID':<5} | {'Name':<20} | {'Phone':<15}")
                print("-" * 45)
                for r in rows:
                    print(f"{r[0]:<5} | {r[1]:<20} | {r[2]:<15}")
    except Exception as e:
        print(f"Database Error: {e}")

def delete():
    value = input("Enter name or phone to delete: ").strip()
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact(%s)", (value,))
                conn.commit()
                print("Contact deleted.")
    except Exception as e:
        print(f"Database Error: {e}")

def bulk_insert():
    try:
        n = int(input("How many contacts: "))
        names, phones = [], []
        for i in range(n):
            names.append(input(f"Name {i+1}: ").strip())
            phones.append(input(f"Phone {i+1}: ").strip())
        
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))
                conn.commit()
                print("Bulk insert completed.")
    except Exception as e:
        print(f"Database Error: {e}")

def menu():
    while True:
        print("\n" + "="*20)
        print("   PHONEBOOK MENU")
        print("="*20)
        print("1. Insert/Update")
        print("2. Search")
        print("3. Pagination")
        print("4. Delete")
        print("5. Bulk Insert")
        print("6. Exit")
        
        choice = input("\nChoose: ")
        if choice == "1": insert_or_update()
        elif choice == "2": search()
        elif choice == "3": paginate()
        elif choice == "4": delete()
        elif choice == "5": bulk_insert()
        elif choice == "6": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    menu()