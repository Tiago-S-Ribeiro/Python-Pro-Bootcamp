from GoogleSheetFiller import GoogleSheetFiller
from FormFillerBot import FormFillerBot
from Remax import FindRemaxListings
from dotenv import load_dotenv
import os

os.system("clear")
load_dotenv()

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

method = input("\n\"Comprar\" ou \"Arrendar\"? ").lower()
price = int(input("\nMaximum Price? "))
region = input("\nRegion (Porto, Braga, Viana do Castelo, Aveiro)? ").title()

remax = FindRemaxListings(region, price, method)
all_listings = remax.find_listings()

bot = FormFillerBot(CHROMEDRIVER_PATH)
bot.fill_google_form(all_listings)

sheet = GoogleSheetFiller()
sheet.transfer_data_to_sheet(all_listings)