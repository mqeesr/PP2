import csv
from connect import get_connection

def search_pattern():
    pattern = input("Enter pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """SELECT * FROM contacts 
           WHERE name ILIKE %s OR phone LIKE %s""",
        (f"%{pattern}%", f"%{pattern}%")
    )

    rows = cur.fetchall()

    if not rows:
        print("Nothing found")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def insert_or_update():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM contacts WHERE name=%s", (name,))

    if cur.fetchone():
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE name=%s",
            (phone, name)
        )
        print("Updated existing contact")
    else:
        cur.execute(
            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        print("Inserted new contact")

    conn.commit()
    cur.close()
    conn.close()


def insert_many():
    n = int(input("How many users: "))

    invalid = []

    conn = get_connection()
    cur = conn.cursor()

    for _ in range(n):
        name = input("Name: ")
        phone = input("Phone: ")

        if not phone.isdigit():
            invalid.append((name, phone))
            continue

        cur.execute(
            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
            (name, phone)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Invalid data:", invalid)


def get_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts ORDER BY id LIMIT %s OFFSET %s",
        (limit, offset)
    )

    rows = cur.fetchall()

    if not rows:
        print("No data")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def delete_by_value():
    val = input("Enter name or phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name=%s OR phone=%s",
        (val, val)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted if existed")


while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1 - Search by pattern")
    print("2 - Insert or update user")
    print("3 - Insert many users")
    print("4 - Show paginated")
    print("5 - Delete by name or phone")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        search_pattern()
    elif choice == "2":
        insert_or_update()
    elif choice == "3":
        insert_many()
    elif choice == "4":
        get_paginated()
    elif choice == "5":
        delete_by_value()
    elif choice == "0":
        break