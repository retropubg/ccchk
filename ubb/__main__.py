import importlib
import sys
import asyncio

from ubb import Ubot
from ubb.modules import ALL_MODULES
from telethon import events

for module_name in ALL_MODULES:
    imported_module = importlib.import_module(f"ubb.modules.{module_name}")



api_id = 26043952  # Replace with your actual API ID
api_hash = "96b8dea447ef580b5b75b01ccc3ab710"
client = TelegramClient("1AZWarzoBuxcfU1NuhKl6b6K_4yM7J5Pl9rUz_VZWjOJIuCxpRN2RLk2FYcs6T84WqMIZOmP7GWfQV1AmgSnkifVmg8yFGt05dfQpWq88TJuEZHktJPQntcAp37It0PFMhbBZzqgKApJW2IfW-P5ZyoZ33BswDtI5jv9qBtwD7PWpZ4GZzYvAGfTGDcjxfKVYZID74JgNwvdAU1Y8Bg3H_5e3elLGN4HxpAo05IgbA3YldU7M7zjwU2HTqpAlAphGQ7UdEfSkWn9sK93G03JskQXtkHSeRkLP8K10S836ZbWeZZ9DVGhyXJ5nIjbJIA-9j0i-MZClr0qSxY_rFmP9db3SZuDl7Sc=", api_id, api_hash)

async def main():
    await Ubott.start()
    print("Bot is running...")
    await Ubot.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
        

