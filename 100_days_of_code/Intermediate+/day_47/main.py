from dotenv import load_dotenv
from twilio.rest import Client
from bs4 import BeautifulSoup
import requests
import smtplib
import os

os.system("clear")
load_dotenv()

RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
RECEIVER_PHONE = os.getenv('RECEIVER_PHONE')
CALLER_PHONE = os.getenv('CALLER_PHONE')
HOST_SERVER = os.getenv('HOST_SERVER')
PRODUCT_URL = os.getenv('PRODUCT_URL')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
USER_AGENT = os.getenv('USER_AGENT')
LANGUAGE = os.getenv('LANGUAGE')
PASSWORD = os.getenv('PASSWORD')
ACC_SID = os.getenv('ACC_SID')
EMAIL = os.getenv('EMAIL')
LOWEST_PRICE = 9

headers = { "User-Agent": USER_AGENT, "Accept-Language": LANGUAGE }
#------------------------------------------------------------------

def send_email(product, url):
  try:
    print("Sending...")
    with smtplib.SMTP(HOST_SERVER) as connection:
      connection.starttls()
      connection.login(user=EMAIL, password=PASSWORD)
      connection.sendmail(from_addr=EMAIL, to_addrs=RECEIVER_EMAIL, msg=f"Subject:Price Drop Alert!\n\nThe product '{product}' just dropped below 9€!\n Visit {url} to purchase it.".encode('utf-8'))
  except smtplib.SMTPAuthenticationError:
    print("Error Found. Confirm SMTP settings and/or authentication information.")
  else:
    print("\nMessage sent!\n")
#------------------------------------------------------------------

def send_text_message(message):
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages.create(body=message, from_=CALLER_PHONE, to=RECEIVER_PHONE)
    print(message.status)
#------------------------------------------------------------------

response = requests.get(PRODUCT_URL, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "lxml")

price_tag = soup.find(name="span", id="price").getText()
title_tag = soup.find(name="span", id="productTitle").getText().strip()

price = float(price_tag.split()[0].strip().replace(",", "."))

if price < LOWEST_PRICE:
    send_email(title_tag, PRODUCT_URL)
    send_text_message(f"\n----------------\n'{title_tag}' just dropped below {LOWEST_PRICE}€ on Amazon.es.\n----------------\nVisit:\n{PRODUCT_URL}")