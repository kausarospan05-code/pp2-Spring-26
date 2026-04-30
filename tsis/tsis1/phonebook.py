# phonebook.py
import csv
import json
from datetime import datetime
from connect import connect

VALID_PHONE_TYPES = {"home", "work", "mobile"}
VALID_SORTS = {
    "name": "c.name",
    "birthday": "c.birthday",
    "date": "c.id",
}


def parse_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, "%Y-%m-%d").date()


# -------------------------------
# Contact logic
# -------------------------------
def contact_exists(cur, name):
    cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
    return cur.fetchone()


def collect_phones_from_console():
    phones = []
    while True:
        phone = input("Enter phone (leave empty to stop): ").strip()
        if not phone:
            break

        phone_type = input("Type [home/work/mobile]: ").strip().lower()
        if phone_type not in VALID_PHONE_TYPES:
            print("Invalid type.")
            continue

        phones.append((phone, phone_type))

    return phones


def create_contact_with_details(name, email, birthday, group_name, phones):
    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO contacts(name, email, birthday, group_name)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (name, email, birthday, group_name),
        )

        contact_id = cur.fetchone()[0]

        for phone, phone_type in phones:
            cur.execute(
                """
                INSERT INTO contact_phones(contact_id, phone, phone_type)
                VALUES (%s, %s, %s)
                """,
                (contact_id, phone, phone_type),
            )

        conn.commit()
        print("Contact added successfully.")

    except Exception as e:
        conn.rollback()
        print("Error while adding contact:", e)

    finally:
        cur.close()
        conn.close()


def overwrite_contact(name, email, birthday, group_name, phones):
    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE contacts
            SET email = %s,
                birthday = %s,
                group_name = %s
            WHERE name = %s
            RETURNING id
            """,
            (email, birthday, group_name, name),
        )

        row = cur.fetchone()

        if not row:
            print("Contact not found.")
            conn.rollback()
            return

        contact_id = row[0]

        cur.execute(
            "DELETE FROM contact_phones WHERE contact_id = %s",
            (contact_id,),
        )

        for phone, phone_type in phones:
            cur.execute(
                """
                INSERT INTO contact_phones(contact_id, phone, phone_type)
                VALUES (%s, %s, %s)
                """,
                (contact_id, phone, phone_type),
            )

        conn.commit()
        print("Contact overwritten successfully.")

    except Exception as e:
        conn.rollback()
        print("Error while overwriting contact:", e)

    finally:
        cur.close()
        conn.close()


def add_contact_extended():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip() or None
    birthday_input = input("Enter birthday (YYYY-MM-DD or empty): ").strip()
    group_name = input("Enter group [Family/Work/Friend/Other]: ").strip() or "Other"

    try:
        birthday = parse_date(birthday_input) if birthday_input else None
    except ValueError:
        print("Invalid date format.")
        return

    phones = collect_phones_from_console()

    if not phones:
        print("At least one phone is required.")
        return

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()
        exists = contact_exists(cur, name)
    finally:
        cur.close()
        conn.close()

    if exists:
        action = input("Contact exists. Choose [skip/overwrite]: ").strip().lower()
        if action == "overwrite":
            overwrite_contact(name, email, birthday, group_name, phones)
        else:
            print("Skipped.")
    else:
        create_contact_with_details(name, email, birthday, group_name, phones)


# -------------------------------
# Display helpers
# -------------------------------
def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return

    for row in rows:
        print("-" * 60)
        print(f"Name      : {row[1]}")
        print(f"Email     : {row[2] or '-'}")
        print(f"Birthday  : {row[3] or '-'}")
        print(f"Group     : {row[4] or '-'}")
        print(f"Phones    : {row[5] or '-'}")
    print("-" * 60)


def base_select_query(where_clause="", order_clause="ORDER BY c.name", params=()):
    query = f"""
        SELECT
            c.id,
            c.name,
            c.email,
            c.birthday,
            c.group_name,
            COALESCE(
                STRING_AGG(
                    ph.phone_type || ': ' || ph.phone,
                    ', '
                    ORDER BY ph.phone_type, ph.phone
                ),
                ''
            ) AS phones
        FROM contacts c
        LEFT JOIN contact_phones ph ON ph.contact_id = c.id
        {where_clause}
        GROUP BY c.id, c.name, c.email, c.birthday, c.group_name
        {order_clause}
    """

    conn = connect()
    if not conn:
        return []

    try:
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        return rows

    except Exception as e:
        print("Database error:", e)
        return []

    finally:
        cur.close()
        conn.close()


# -------------------------------
# Search / filter
# -------------------------------
def search_all_fields():
    query = input("Enter search text: ").strip()

    rows = base_select_query(
        """
        WHERE
            c.name ILIKE %s OR
            COALESCE(c.email, '') ILIKE %s OR
            COALESCE(c.group_name, '') ILIKE %s OR
            EXISTS (
                SELECT 1
                FROM contact_phones p
                WHERE p.contact_id = c.id
                AND p.phone ILIKE %s
            )
        """,
        params=(f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"),
    )

    print_contacts(rows)


def search_by_email():
    query = input("Enter part of email: ").strip()

    rows = base_select_query(
        "WHERE COALESCE(c.email, '') ILIKE %s",
        params=(f"%{query}%",),
    )

    print_contacts(rows)


def filter_by_group():
    group_name = input("Enter group name: ").strip()

    rows = base_select_query(
        "WHERE c.group_name = %s",
        params=(group_name,),
    )

    print_contacts(rows)


def sort_contacts():
    sort_key = input("Sort by [name/birthday/date]: ").strip().lower()

    if sort_key not in VALID_SORTS:
        print("Invalid sort option.")
        return

    rows = base_select_query(
        order_clause=f"ORDER BY {VALID_SORTS[sort_key]} NULLS LAST"
    )

    print_contacts(rows)


def paginate_navigation():
    try:
        limit = int(input("Enter page size: "))
    except ValueError:
        print("Invalid number.")
        return

    offset = 0

    while True:
        rows = base_select_query(
            order_clause=f"ORDER BY c.name LIMIT {limit} OFFSET {offset}"
        )

        print(f"\nPage offset = {offset}")
        print_contacts(rows)

        command = input("Command [next/prev/quit]: ").strip().lower()

        if command == "next":
            if rows:
                offset += limit
        elif command == "prev":
            offset = max(0, offset - limit)
        elif command == "quit":
            break
        else:
            print("Unknown command.")


# -------------------------------
# Import / Export
# -------------------------------
def export_to_json():
    filename = input("Enter JSON filename: ").strip() or "contacts_export.json"

    rows = base_select_query()

    result = []

    for row in rows:
        result.append(
            {
                "name": row[1],
                "email": row[2],
                "birthday": str(row[3]) if row[3] else None,
                "group": row[4],
                "phones": row[5],
            }
        )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"Exported to {filename}")


def import_from_json():
    filename = input("Enter JSON filename: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Import error:", e)
        return

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        for item in data:
            name = item["name"]
            email = item.get("email")
            birthday = parse_date(item["birthday"]) if item.get("birthday") else None
            group_name = item.get("group", "Other")

            phones = []
            if isinstance(item.get("phones"), list):
                for ph in item["phones"]:
                    phones.append((ph["phone"], ph.get("type", "mobile")))

            # UPSERT CONTACT
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_name)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (email)
                DO UPDATE SET
                    name = EXCLUDED.name,
                    birthday = EXCLUDED.birthday,
                    group_name = EXCLUDED.group_name
                RETURNING id
            """, (name, email, birthday, group_name))

            contact_id = cur.fetchone()[0]

            # optional: clear old phones and reinsert
            cur.execute(
                "DELETE FROM contact_phones WHERE contact_id = %s",
                (contact_id,)
            )

            for phone, phone_type in phones:
                cur.execute("""
                    INSERT INTO contact_phones(contact_id, phone, phone_type)
                    VALUES (%s, %s, %s)
                """, (contact_id, phone, phone_type))

        conn.commit()
        print("JSON import completed.")

    except Exception as e:
        conn.rollback()
        print("Import error:", e)

    finally:
        cur.close()
        conn.close()

def import_from_csv():
    filename = input("Enter CSV filename: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                phones = [(row["phone"], row.get("phone_type", "mobile"))]

                create_contact_with_details(
                    row["name"],
                    row.get("email"),
                    parse_date(row["birthday"]) if row.get("birthday") else None,
                    row.get("group", "Other"),
                    phones,
                )

        print("CSV import completed.")

    except Exception as e:
        print("CSV import error:", e)


# -------------------------------
# Extra features
# -------------------------------
def add_new_phone_to_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone: ").strip()
    phone_type = input("Enter type [home/work/mobile]: ").strip().lower()

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        row = cur.fetchone()

        if not row:
            print("Contact not found.")
            return

        contact_id = row[0]

        cur.execute(
            """
            INSERT INTO contact_phones(contact_id, phone, phone_type)
            VALUES (%s, %s, %s)
            """,
            (contact_id, phone, phone_type),
        )

        conn.commit()
        print("Phone added.")

    except Exception as e:
        conn.rollback()
        print("Add phone error:", e)

    finally:
        cur.close()
        conn.close()


def move_contact_to_group():
    name = input("Enter contact name: ").strip()
    group_name = input("Enter new group: ").strip()

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE contacts
            SET group_name = %s
            WHERE name = %s
            """,
            (group_name, name),
        )

        conn.commit()
        print("Contact moved.")

    except Exception as e:
        conn.rollback()
        print("Move error:", e)

    finally:
        cur.close()
        conn.close()


# -------------------------------
# Main menu
# -------------------------------
def main():
    while True:
        print("\n========== EXTENDED PHONEBOOK ==========")
        print("1. Add contact with extended fields")
        print("2. Search across all fields")
        print("3. Search by email")
        print("4. Filter by group")
        print("5. Sort contacts")
        print("6. Paginated navigation")
        print("7. Export to JSON")
        print("8. Import from JSON")
        print("9. Import from CSV")
        print("10. Add one more phone to contact")
        print("11. Move contact to another group")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_contact_extended()
        elif choice == "2":
            search_all_fields()
        elif choice == "3":
            search_by_email()
        elif choice == "4":
            filter_by_group()
        elif choice == "5":
            sort_contacts()
        elif choice == "6":
            paginate_navigation()
        elif choice == "7":
            export_to_json()
        elif choice == "8":
            import_from_json()
        elif choice == "9":
            import_from_csv()
        elif choice == "10":
            add_new_phone_to_contact()
        elif choice == "11":
            move_contact_to_group()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()