from smtplib import SMTP
import os


class EmailClient:

    def __init__(self):
        self.from_email = os.getenv("FROM_EMAIL")
        self.to_email = os.getenv("RECEIVER")
        self.password = os.getenv("PASSWORD")

    def send_email(self, message):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.password)
            connection.sendmail(from_addr=self.from_email, to_addrs=self.to_email, msg=f"Subject: Amazon Price Alert\n\n"
                                                                                       f"Amazon Price Alert\n\n"
                                                                                       f"{message}")
