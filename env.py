import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "27221429").strip()
API_HASH = os.getenv("API_HASH", "60f1725be1c059a2523c1b90d53c7808").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5944412356:AAHM0I8tHNyzLaRgG0_Dw4EswzH9H2jX0Co").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://wlsmwilr:ceW_SpKwa5WUaIMtN9AkHulCiiJ3Mkxc@jelani.db.elephantsql.com/wlsmwilr").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "botsmasterc")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
