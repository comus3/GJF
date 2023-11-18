import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getpass import getpass  # Used for securely entering your password
import os

user_Mail = ""#PLACE YOUR MAIL HERE


def sendEmail(recipient_email,subject,password = None):
    def returnEmailMsg():
        # Specify the path to the text file within the "output" folder
        file_path = "output/email.txt"
        # Initialize an empty string variable to store the contents
        file_contents = ""
        # Try to open the file and read its contents
        try:
            with open(file_path, "r",encoding="utf-8") as file:
                file_contents = file.read()
        except FileNotFoundError:
            print("EMAIL: The file does not exist.")
        except Exception as e:
            print("EMAIL: An error occurred:", e)

        # Check if the file_contents variable contains the string from the file
        if file_contents:
            return file_contents
        else:
            print("EMAIL: No content found in the file.")

    # Sender's email address and password
    sender_email = user_Mail
    if password == None or password == "":password = getpass("Enter your Gmail password: ")
    message = returnEmailMsg()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain',"utf-8"))
    
    # Add attachments
    attachment_files = ["output/CPC-CV.pdf", "output/CPC-Motiv.pdf"]  # File paths
    for file_path in attachment_files:
        with open(file_path, "rb") as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(file_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        msg.attach(part)

    # Establish a connection to the Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the connection
        server.quit()

        print("EMAIL: Email sent successfully!")
        return 0

    except smtplib.SMTPException as e:
        print(f"EMAIL: Email sending failed. Error: {e}")
        return 1

    # Note: If you have 2-Step Verification enabled on your Google account, you may need to generate an "App Password" for the script.
