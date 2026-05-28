import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def authenticate_gmail():

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)

    return service

def get_unread_emails():

    service = authenticate_gmail()

    results = service.users().messages().list(
        userId="me",
        labelIds=["UNREAD"],
        maxResults=5
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for message in messages:

        msg = service.users().messages().get(
            userId="me",
            id=message["id"]
        ).execute()

        payload = msg.get("payload", {})

        headers = payload.get("headers", [])

        subject = ""
        sender = ""

        for header in headers:

            if header["name"] == "Subject":
                subject = header["value"]

            elif header["name"] == "From":
                sender = header["value"]

        body = ""

        def extract_body(payload):

            data = payload.get("body", {}).get("data")

            if data:
                return base64.urlsafe_b64decode(
                    data.encode("UTF-8")
                ).decode("utf-8", errors="ignore")

            parts = payload.get("parts", [])

            for part in parts:

                if part.get("mimeType") == "text/plain":

                    data = part.get("body", {}).get("data")

                    if data:
                        return base64.urlsafe_b64decode(
                            data.encode("UTF-8")
                        ).decode("utf-8", errors="ignore")

            return ""

        body = extract_body(payload)

        email_info = {
            "id": msg["id"],
            "thread_id": msg["threadId"],
            "subject": subject,
            "from": sender,
            "snippet": msg.get("snippet", ""),
            "body": body
        }

        emails.append(email_info)

    return emails