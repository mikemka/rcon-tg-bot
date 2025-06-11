from dotenv import load_dotenv
from pathlib import Path
from os import getenv


BASE_DIR = Path(__file__).resolve().parent

DOTENV_PATH = BASE_DIR / '.env'

if DOTENV_PATH.exists():
    load_dotenv(DOTENV_PATH)

TOKEN = getenv('TG_TOKEN')

RCON_IP = getenv('RCON_IP')

RCON_PORT = int(getenv('RCON_PORT'))

RCON_PWD = getenv('RCON_PWD')

TG_ADMIN_GROUP_ID = getenv('TG_ADMIN_GROUP_ID')
