import csv
import sys
from connect import get_connection

CREATE_TABLE_SQL = """
DROP TABLE IF EXISTS contacts;
CREATE TABLE contacts (
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR(50)  NOT NULL,
    last_name  VARCHAR(50)  NOT NULL DEFAULT '',
    phone      VARCHAR(20)  NOT NULL UNIQUE
);
"""


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)
        conn.commit()
    print("table 'contacts' reset and ready")


def insert_from_csv(filepath: str = "contacts.csv"):

    inserted = skipped = 0
    sql = """
        INSERT INTO contacts (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT (phone) DO NOTHING
    """
    try:
        with open(filepath, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            rows = [(r["first_name"].strip(),
                     r.get("last_name", "").strip(),
                     r["phone"].strip()) for r in reader]
    except FileNotFoundError:
        print(f"file not found: {filepath}")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            for row in rows:
                cur.execute(sql, row)
                if cur.rowcount:
                    inserted += 1
                else:
                    skipped += 1
        conn.commit()

    print(f"CSV import done — inserted: {inserted}, skipped (duplicate): {skipped}")


def insert_from_console():
    print("\n─── add new contact ───")
    first_name = input("first name : ").strip()
    last_name = input("last name  : ").strip()
    phone = input("phone      : ").strip()

    if not first_name or not phone:
        print("first name and phone are required.")
        return

    sql = """
        INSERT INTO contacts (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT (phone) DO NOTHING
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (first_name, last_name, phone))
            if cur.rowcount:
                print(f"contact '{first_name} {last_name}' added.")
            else:
                print(f"phone '{phone}' already exists - contact not added.")
        conn.commit()


def update_contact():
    print("\n─── update contact ───")
    current_phone = input("enter the contacts current phone number: ").strip()

    print("what do you want to update?")
    print("1 - first name")
    print("2 - phone number")
    choice = input("choice: ").strip()

    if choice == "1":
        new_value = input("new first name: ").strip()
        sql = "UPDATE contacts SET first_name = %s WHERE phone = %s"
    elif choice == "2":
        new_value = input("new phone number: ").strip()
        sql = "UPDATE contacts SET phone = %s WHERE phone = %s"
    else:
        print("invalid choice")
        return

    if not new_value:
        print("value cannot be empty")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (new_value, current_phone))
            if cur.rowcount:
                print("contact updated successfully")
            else:
                print(f"no contact found with phone '{current_phone}'.")
        conn.commit()


def _print_contacts(rows):
    if not rows:
        print("(no contacts found)")
        return
    print(f"\n  {'ID':<5} {'First Name':<15} {'Last Name':<15} {'Phone':<20}")
    print("  " + "─" * 57)
    for row in rows:
        print(f"  {row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<20}")
    print(f"\n  {len(rows)} record(s) found.")


def query_contacts():
    print("\n─── search contacts ───")
    print("1 - by name (first or last, partial match)")
    print("2 - by phone prefix")
    print("3 - show all")
    choice = input("choice: ").strip()

    with get_connection() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                name = input("name fragment: ").strip()
                cur.execute("""
                    SELECT id, first_name, last_name, phone
                    FROM contacts
                    WHERE first_name ILIKE %s OR last_name ILIKE %s
                    ORDER BY id
                """, (f"%{name}%", f"%{name}%"))

            elif choice == "2":
                prefix = input("phone prefix: ").strip()
                cur.execute("""
                    SELECT id, first_name, last_name, phone
                    FROM contacts
                    WHERE phone LIKE %s
                    ORDER BY phone
                """, (f"{prefix}%",))

            elif choice == "3":
                cur.execute("""
                    SELECT id, first_name, last_name, phone
                    FROM contacts
                    ORDER BY id
                """)

            else:
                print("invalid choice")
                return

            rows = cur.fetchall()

    _print_contacts(rows)


def delete_contact():
    print("\n─── delete contact ───")
    print("1 - by phone number")
    print("2 - by full name (first + last)")
    choice = input("choice: ").strip()

    with get_connection() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                phone = input("phone number: ").strip()
                cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
                if cur.rowcount:
                    print(f"contact with phone '{phone}' deleted")
                else:
                    print(f"no contact found with phone '{phone}'.")

            elif choice == "2":
                first_name = input("first name: ").strip()
                last_name  = input("last name : ").strip()
                cur.execute("""
                    DELETE FROM contacts
                    WHERE first_name ILIKE %s AND last_name ILIKE %s
                """, (first_name, last_name))
                if cur.rowcount:
                    print(f"{cur.rowcount} contact(s) named '{first_name} {last_name}' deleted")
                else:
                    print(f"no contact found with name '{first_name} {last_name}'")

            else:
                print("invalid choice")
                return

        conn.commit()


menu = """
 ______________________________
|  1 — Import from CSV         |
|  2 — Add contact (console)   |
|  3 — Update contact          |
|  4 — Search / Query          |
|  5 — Delete contact          |
|  0 — Exit                    |
|______________________________|
"""

actions = {
    "1": insert_from_csv,
    "2": insert_from_console,
    "3": update_contact,
    "4": query_contacts,
    "5": delete_contact,
}


create_table()

while True:
    print(menu)
    choice = input("select option: ").strip()

    if choice == "0":
        print("bye")
        sys.exit(0)

    action = actions.get(choice)
    if action:
        try:
            action()
        except Exception as exc:
            print(f"error: {exc}")
    else:
        print("unknown option")