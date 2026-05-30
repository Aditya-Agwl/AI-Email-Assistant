import sqlite3


def get_finance_emails():

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT sender, subject, priority
        FROM emails
        WHERE category='finance'
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_high_priority_emails():

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT sender, subject
        FROM emails
        WHERE priority='high'
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def count_categories():

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT category, COUNT(*)
        FROM emails
        GROUP BY category
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_interview_emails():

    conn = sqlite3.connect("emails.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT sender, subject, summary
        FROM emails
        WHERE category='interview'
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

finance_emails = get_finance_emails()

for email in finance_emails:
    print(email)

print(count_categories())