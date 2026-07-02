import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://katalon-demo-cura.herokuapp.com/")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
BROWSER = os.getenv("BROWSER", "chromium")
