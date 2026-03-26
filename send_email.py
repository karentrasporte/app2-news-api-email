import smtplib
import ssl
from email.message import EmailMessage


def send_email(sender_email, app_password, recipient_email, subject, body):
    # Create the email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Gmail SMTP server details
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create secure SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    send_email(
        sender_email="traspo811@gmail.com",
        app_password="gludymxnthvmohff",
        recipient_email="traspo811@gmail.com",
        subject="Test Email",
        body="Hello! This is a test email sent from Python."
    )