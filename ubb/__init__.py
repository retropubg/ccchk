import os
import logging
import yaml
from telethon import TelegramClient
from telethon.sessions import StringSession

# Logging setup
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

# Load config
CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['api_id']))  # Correct key name
API_HASH = os.getenv('API_HASH', CONFIG['api_hash'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['dump_id'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['string_session'])

# Initialize Telegram Client
Ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH, auto_reconnect=False)
