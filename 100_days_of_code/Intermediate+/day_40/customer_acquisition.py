from urllib import response
import requests
from data import CSV_USER_ID

ENDPOINT = f"https://api.sheety.co/{CSV_USER_ID}/flightDeals/users"

def user_registration():
    print("----- Registration -----\n")
    first_name = input("Insert your first name:\n").title()
    last_name = input("Insert your last name:\n").title()
    email = input("Insert your email:\n").lower()
    confirm_email = input("Confirm again your email:\n").lower()

    if email == confirm_email: 
        upload_user_data(first_name, last_name, email)
        print("\n🛩 Welcome to Flight Deal Finder! 🛩\n") 
    else:
        print("\nEmails don't match.\n")


def upload_user_data(first_name, last_name, email):
    user_data = {
            'user': {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
    response = requests.post(url=ENDPOINT, json=user_data)
    response.raise_for_status()

user_registration()