from gmail_reader import get_unread_emails
from email_processor import analyze_email
from database import save_email_analysis

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

    save_email_analysis(
        sender=email["from"],
        subject=email["subject"],
        category=result["category"],
        priority=result["priority"],
        summary=result["summary"]
    )

    print(result)