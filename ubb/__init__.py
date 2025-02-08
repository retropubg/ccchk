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
session_string = "1AZWarzoBuxcfU1NuhKl6b6K_4yM7J5Pl9rUz_VZWjOJIuCxpRN2RLk2FYcs6T84WqMIZOmP7GWfQV1AmgSnkifVmg8yFGt05dfQpWq88TJuEZHktJPQntcAp37It0PFMhbBZzqgKApJW2IfW-P5ZyoZ33BswDtI5jv9qBtwD7PWpZ4GZzYvAGfTGDcjxfKVYZID74JgNwvdAU1Y8Bg3H_5e3elLGN4HxpAo05IgbA3YldU7M7zjwU2HTqpAlAphGQ7UdEfSkWn9sK93G03JskQXtkHSeRkLP8K10S836ZbWeZZ9DVGhyXJ5nIjbJIA-9j0i-MZClr0qSxY_rFmP9db3SZuDl7Sc="

# Correctly initialize the TelegramClient
Ubot = TelegramClient(StringSession(session_string), 26043952, "96b8dea447ef580b5b75b01ccc3ab710", auto_reconnect=False)
