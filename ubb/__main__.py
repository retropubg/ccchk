import importlib
import sys
import asyncio

from ubb import Ubot
from ubb.modules import ALL_MODULES
from telethon import TelegramClient

for module_name in ALL_MODULES:
    imported_module = importlib.import_module(f"ubb.modules.{module_name}")




async def main():
 Ubot.start()
    print("Bot is running...")
 Ubot.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
        

