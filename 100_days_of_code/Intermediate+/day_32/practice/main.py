import smtplib
import random
import datetime as dt
from data import EML, PWD, DST, HOST_SERVER

if dt.datetime.now().weekday() == 0: #Monday
    try:
        with open("./quotes.txt") as file:
            quotes = file.readlines()
    except FileNotFoundError:
        print("File not found. Please provide a valid file path")
    else:
        chosen_quote = random.choice(quotes)
        try:
            with smtplib.SMTP(HOST_SERVER) as connection:
                connection.starttls()
                connection.login(user=EML, password=PWD)
                connection.sendmail(from_addr=EML, to_addrs=DST, msg=f"Subject:Motivational Monday\n\n{chosen_quote}")
        except smtplib.SMTPAuthenticationError:
            print("Error Found. Confirm SMTP settings and/or authentication information.")
        else:
            print("\nMotivational quote was sent!\n")
