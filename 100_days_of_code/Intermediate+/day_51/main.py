from dotenv import load_dotenv
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import os

os.system("clear")
load_dotenv()

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
PROMISED_DOWNLOAD = os.getenv('PROMISED_DOWNLOAD')
PROMISED_UPLOAD = os.getenv('PROMISED_UPLOAD')

bot = InternetSpeedTwitterBot(CHROMEDRIVER_PATH)

bot.get_internet_speed()

if float(bot.download) < float(PROMISED_DOWNLOAD) and float(bot.upload) < float(PROMISED_UPLOAD):
    bot.tweet_at_provider()