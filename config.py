import os
import telebot
from dotenv import load_dotenv

load_dotenv()

# bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
# chat_id = int(os.getenv("CHAT_ID"))
host_stage = str(os.getenv("HOST_STAGE"))
# int = os.getenv("QASE_PROJECT_CODE")
# token_qase = os.getenv("QASE_TESTOPS_API_TOKEN")