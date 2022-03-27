from InstagramBot import InstagramBot
from dotenv import load_dotenv
import os

os.system("clear")
load_dotenv()

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

bot = InstagramBot(CHROMEDRIVER_PATH)

bot.login()
bot.find_followers()
bot.follow()