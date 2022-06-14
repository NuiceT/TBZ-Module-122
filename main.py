import os
import string
import requests
import smtplib as mail
from dotenv import load_dotenv


def sendMail(subject: string, message: string):
    try:
        smtp = mail.SMTP_SSL(host=os.getenv("SMTP_HOST"), port=os.getenv("SMTP_PORT"))
        smtp.ehlo()
        smtp.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
        msg = str(
            "From: <{}>\nTo: <{}>\nMIME-Version: 1.0\nContent-type: text/html\nSubject: {}\n\n{}"
        )
        smtp.sendmail(
            os.getenv("MAIL_SENDER"),
            os.getenv("MAIL_RECIPIENT"),
            msg.format(
                os.getenv("MAIL_SENDER"), os.getenv("MAIL_RECIPIENT"), subject, message
            ).encode("utf-8"),
        )
        print("Successfully sent E-Mail")
        smtp.quit()
    except mail.SMTPException:
        print("Error: Unable to send E-Mail")


def main():
    response = requests.get(
        url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    ).json()
    sendMail(
        "Wöchentlicher Bitcoin Preis",
        "<h1>" + str(response["bitcoin"]["usd"]) + "</h1>",
    )


if __name__ == "__main__":
    load_dotenv()
    main()
