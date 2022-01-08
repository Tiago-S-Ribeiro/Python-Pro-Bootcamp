import smtplib
import random
import datetime as dt
import pandas
from data import EML, PWD, DST, HOST_SERVER
birthday_person = ""
data_dict = None

def send_email(letter):
  try:
    with smtplib.SMTP(HOST_SERVER) as connection:
      connection.starttls()
      connection.login(user=EML, password=PWD)
      connection.sendmail(from_addr=EML, to_addrs=DST, msg=f"Subject:Happy Birthday\n\n{letter}")
  except smtplib.SMTPAuthenticationError:
    print("Error Found. Confirm SMTP settings and/or authentication information.")
  else:
    print("\nMessage sent!\n")

def write_letter():
  try:
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
      letter = file.read()
  except FileNotFoundError:
    custom_letter = f"Have a joyous day {birthday_person.strip()}.\n\nTiago"
  else:
    custom_letter = letter.replace("[NAME]", birthday_person.strip())
  finally:
    send_email(custom_letter)

def check_birthday():
  global birthday_person
  cur_month = dt.datetime.now().month
  cur_day = dt.datetime.now().day

  for item in data_dict:
    if item["month"] == cur_month and item["day"] == cur_day:
      birthday_person = item["name"]
      write_letter()
      
#-----------------------------------------------------------
try:
  data = pandas.read_csv("./birthdays.csv")
except FileNotFoundError:
  print("File not found.")
else:  
  data_dict = data.to_dict(orient="records")
  check_birthday()
