import os
import logging
import yaml

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['26043952']))
API_HASH = os.getenv('API_HASH', CONFIG['96b8dea447ef580b5b75b01ccc3ab710'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['dump_id'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['AQGNZjAAdMbax-pTI7YPEhNmELkkfqoAFvtfIZHzgt-fSp_58726NLA70cQ9U25SwfMQBwVT829xp6xmQmxtFuV1_96c0qsjYj2HJCo25SlD54dn_Su5HDaf_OTDBsKAlW2nPo4wsOpHEbNfiEedclj9wuj6S97f3AZnajoIBP-z1Xf5-PmgUaaV6qms7rip6bLY-TjJLrtmT_R-JUcwU8dOHNHEAGVuQoRiikEex5TcVEdnXdnSBP7su6k2XcF4bJYDYq7juEa9Ovka8K_IZxbCc4Ll170bTdHt52OYafSfaX5taC_eFFWHWi1eLjxBhBB_SNeckxK9bC5sV-mKFyxnmQLlkAAAAAHP0O-hAA'])

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
