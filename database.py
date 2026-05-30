import sqlite3


def initialize_database():

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        category TEXT,
        priority TEXT,
        summary TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_email_analysis(
    sender,
    subject,
    category,
    priority,
    summary
):

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO emails
        (
            sender,
            subject,
            category,
            priority,
            summary
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            sender,
            subject,
            category,
            priority,
            summary
        )
    )

    conn.commit()
    conn.close()


initialize_database()