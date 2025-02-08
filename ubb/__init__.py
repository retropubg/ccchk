import os
import logging
import yaml
from telethon import TelegramClient

# Logging setup
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

# Load config
CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['api_id']))  # Correct key name
API_HASH = os.getenv('API_HASH', CONFIG['api_hash'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['dump_id'])
BOT_TOKEN = os.getenv('BOT_TOKEN', CONFIG['bot_token'])  # Use bot token instead of session

# Correctly initialize the TelegramClient
Ubot = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)
