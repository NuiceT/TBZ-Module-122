from array import array
from datetime import datetime, timedelta
from distutils.log import error
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import string
import requests
import smtplib as mail
import matplotlib.pyplot as plt
from dotenv import load_dotenv


def sendMail(subject: string, msg: string, attachment: string):
    try:
        smtp = mail.SMTP_SSL(host=os.getenv("SMTP_HOST"), port=os.getenv("SMTP_PORT"))
        smtp.ehlo()
        smtp.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))

        message = MIMEMultipart("mixed")
        message["From"] = "Automatic Bot <{}>".format(os.getenv("MAIL_SENDER"))
        message["To"] = os.getenv("MAIL_RECIPIENT")
        message["Subject"] = subject

        body = MIMEText(msg, "html")
        message.attach(body)

        with open(attachment, "rb") as f:
            # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
            attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header("Content-Disposition", "attachment", filename=attachment)
        message.attach(attach)

        smtp.sendmail(
            os.getenv("MAIL_SENDER"), os.getenv("MAIL_RECIPIENT"), message.as_string()
        )
        print("Successfully sent E-Mail")
        smtp.quit()
    except mail.SMTPException:
        print("Error: Unable to send E-Mail")


def createFigure(dates: array, prices: int):
    plt.figure(figsize=(11.75, 8.25))
    plt.plot(dates, prices)
    plt.xlabel("Date")
    plt.ylabel("Price per unit in CHF")
    plt.savefig("report_" + dates[7] + ".pdf")


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
    createFigure(dates, prices)
    sendMail(
        "Wöchentlicher Bitcoin Bericht",
        "<h1>Wöchentlicher Bitcoin Bericht</h1><table>" + message + "</table>",
        "report_" + dates[7] + ".pdf",
    )


if __name__ == "__main__":
    load_dotenv()
    main()
