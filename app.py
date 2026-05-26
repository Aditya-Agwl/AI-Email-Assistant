from email_processor import analyze_email

sample_email = """
Hi Aditya,

We would like to schedule your interview for next Tuesday at 3 PM.

Please confirm your availability.

Best,
HR Team
"""

result = analyze_email(sample_email)

print(result)