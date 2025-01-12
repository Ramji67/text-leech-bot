import os

API_ID    = os.environ.get("API_ID", "28088290")
API_HASH  = os.environ.get("API_HASH", "6998f2c585fdce65ac72dfa23d02b6ec")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7721614203:AAEWpy9Qj8cmkf1rJGGasdHF4Qp2_z4Wzw8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
