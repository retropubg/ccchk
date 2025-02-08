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

# Ensure the session string is in quotes
session_string = "1AZWarzoBuzNJWNorfHYXZ90MdAnfUQCm4iCKKJljv-0nPTy0uIU7ybVpkT-2xRQIgV8uJ9zFyJ_ZAWKywRifGqAZQNh_usm2nLRV9e5KLADI-jgqlOeuh2fv1OZyS0M9F80GlaZLyxIsro3x3e4AZYeV9iExgCo4DRACblvsZu2eVxl-32tBOkZjzZhslRpBke5a2nHs8BvNuU8u66LktQVXJzXCWknfDuEBohJLP7I2sFcymkDPRcC3b_4bJfSUk6w9rFVC23wVM5pDllecTL9mE9lieDrTa2JpU9a9pzROWtpEwfIgWlfYz1-wlxEz-t2bIij1XXOR4EFikia6LYhP_kzn-so="

# Correctly initialize the TelegramClient
Ubot = TelegramClient(StringSession(session_string), 26043952, "96b8dea447ef580b5b75b01ccc3ab710", auto_reconnect=False)
