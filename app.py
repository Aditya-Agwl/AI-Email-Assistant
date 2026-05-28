from gmail_reader import get_unread_emails
from email_processor import analyze_email

emails = get_unread_emails()

for i, email in enumerate(emails):

    print(f"\n========== EMAIL {i+1} ==========\n")

    email_content = f"""
    Sender:
    {email['from']}

    Subject:
    {email['subject']}

    Body:
    {email['body']}
    """

    email_content = email_content[:5000]
    result = analyze_email(email_content)

    print(result)