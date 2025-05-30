import csv
import smtplib
import datetime
from email.message import EmailMessage

datum = datetime.datetime.today().strftime('%m.%Y')
email_1 = "********@gmail.com"
heslo = "*************"
zprava = "Vyplatní lístek {datum}\n\nVýplatní lístek {datum}."

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email_1, password=heslo)
    with open('kontakty.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for cislo, email, soubor in reader:
            msg = EmailMessage()
            msg["Subject"] = f"Vyplatní lístek {datum}"
            msg["From"] = email_1
            msg["To"] = email
            msg.set_content(f"Výplatní lístek {datum}.", charset="utf-8")
            with open(soubor, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=soubor)
            connection.send_message(msg)