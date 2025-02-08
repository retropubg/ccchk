import importlib
import sys
import asyncio

from ubb import Ubot
from ubb.modules import ALL_MODULES
from telethon import events

for module_name in ALL_MODULES:
    imported_module = importlib.import_module(f"ubb.modules.{module_name}")



@client.on(events.NewMessage(pattern="/alive"))
async def alive(event):
    await event.reply("Yes, I'm alive!")

    async with Ubot:
        # Run the client until Ctrl+C is pressed, or the client disconnects
        print('Your bot is alive .alive to check\n'
              '.help to check command list\n'
              '(Press Ctrl+C to stop this)')
        Ubot.run_until_disconnected()
        

if __name__ == '__main__':
    asyncio.run(main())
