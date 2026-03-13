import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

CITY = os.getenv("CITY", "Stockholm")
JOB_API_URL = os.getenv("JOB_API_URL")

keywords_raw = os.getenv("KEYWORDS", "DevOps")
KEYWORDS = [k.strip() for k in keywords_raw.split(",")]
