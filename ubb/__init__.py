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
API_ID = int(os.getenv('API_ID', CONFIG['26043952']))
API_HASH = os.getenv('API_HASH', CONFIG['96b8dea447ef580b5b75b01ccc3ab710'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['-1002493436016'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['1AZWarzsBux0cAwohXalqVXlck2QmUAPtpPcv4bhoxuDJoHPn1sDFsDsGwH-yU4MQgE0_0kXx_OpnUhwY2ZDhkEBEUtuzm-zcPBHqMviPAxK8JJ0X1fQP6RWG3LN41Y2QeTPvh9zMe9Pb27KewmYH-WXaOf_uxrcEIhLsHnYvHGwZ-oUgq0mz_6blnkd6RJZoY28l1M41ELmTzNclA-B7BXnG40MKQMdKMvd2JaDNxkVTOEpmGGaHELcqK-86JviXUXtc7kKopXBMtQTcZ8ybmmGnzzLKAZA1WqXqHbDhEqH4gOkxG5E8e8L0Ul2IknEgqMxCVartXI-InIigIedXcpkD6kRarwE='])

# Initialize Telegram Client
Ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH, auto_reconnect=False)
