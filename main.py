from array import array
from datetime import datetime, timedelta
from distutils.log import error
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os
import string
import requests
import smtplib as mail
import matplotlib.pyplot as plt
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)


def sendMail(subject: string, msg: string, attachment: string):
    try:
        smtp = mail.SMTP_SSL(host=os.getenv("SMTP_HOST"), port=os.getenv("SMTP_PORT"))
        smtp.ehlo()
        smtp.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))

        logging.info("Logged in with USERNAME: " + os.getenv("SMTP_USERNAME"))

        message = MIMEMultipart("mixed")
        message["From"] = "Automatic Bot <{}>".format(os.getenv("MAIL_SENDER"))
        message["To"] = os.getenv("MAIL_RECIPIENT")
        message["Subject"] = subject

        body = MIMEText(msg, "html")
        message.attach(body)

        logging.info("Attached body")

        with open(attachment, "rb") as f:
            # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
            attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header("Content-Disposition", "attachment", filename=attachment)
        message.attach(attach)

        logging.info("Attached attachment")

        smtp.sendmail(
            os.getenv("MAIL_SENDER"), os.getenv("MAIL_RECIPIENT"), message.as_string()
        )

        logging.info("Sent E-Mail to " + os.getenv("MAIL_RECIPIENT"))
        smtp.quit()
    except mail.SMTPException:
        logging.error("Error: Unable to send E-Mail")


def createFigure(dates: array, prices: int):
    plt.figure(figsize=(11.75, 8.25))
    plt.plot(dates, prices)
    plt.xlabel("Date")
    plt.ylabel("Price per unit in CHF")
    logging.info("Created figure")
    plt.savefig("report_" + dates[7] + ".pdf")
    logging.info("Saved figure")


def main():
    message = ""
    prices = []
    dates = []
    for x in range(8):
        date = datetime.today().date() - timedelta(days=x)
        response = requests.get(
            url="https://api.coingecko.com/api/v3/coins/bitcoin/history?date="
            + str(date.strftime("%d-%m-%Y"))
        ).json()
        dates.append(str(date))
        prices.append(round(response["market_data"]["current_price"]["chf"], 2))
        message += (
            "<tr><th>"
            + str(date.strftime("%d.%m.%Y"))
            + "</th><td>CHF "
            + str(
                round(
                    response["market_data"]["current_price"]["chf"],
                    2,
                )
            )
            + "</td></tr>"
        )
    logging.info("Retrieved data")
    createFigure(dates, prices)
    sendMail(
        "Wöchentlicher Bitcoin Bericht",
        "<h1>Wöchentlicher Bitcoin Bericht</h1><table>" + message + "</table>",
        "report_" + dates[7] + ".pdf",
    )


if __name__ == "__main__":
    load_dotenv()
    main()
