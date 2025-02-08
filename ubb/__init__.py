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
Ubot = TelegramClient(StringSession(1AZWarzsBux0cAwohXalqVXlck2QmUAPtpPcv4bhoxuDJoHPn1sDFsDsGwH-yU4MQgE0_0kXx_OpnUhwY2ZDhkEBEUtuzm-zcPBHqMviPAxK8JJ0X1fQP6RWG3LN41Y2QeTPvh9zMe9Pb27KewmYH-WXaOf_uxrcEIhLsHnYvHGwZ-oUgq0mz_6blnkd6RJZoY28l1M41ELmTzNclA-B7BXnG40MKQMdKMvd2JaDNxkVTOEpmGGaHELcqK-86JviXUXtc7kKopXBMtQTcZ8ybmmGnzzLKAZA1WqXqHbDhEqH4gOkxG5E8e8L0Ul2IknEgqMxCVartXI-InIigIedXcpkD6kRarwE=), 26043952, 96b8dea447ef580b5b75b01ccc3ab710, auto_reconnect=False)
