from typing import Any
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs import COMMANDS
import os

load_dotenv()

class AIBot(commands.AutoShardedBot):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if True:
            super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        print(COMMANDS)
        for cog in COMMANDS:
            cog_name = cog.split('.')[-1]
            discord.client._log.info(f"Loaded Command {cog_name}")
            await self.load_extension(f"{cog}")
        print('If syncing commands is taking longer than usual you are being ratelimited')
        await self.tree.sync()
        discord.client._log.info(f"Loaded {len(self.commands)} commands")

bot = AIBot(command_prefix=[], intents=discord.Intents.all(), help_command=None)


TOKEN = str(os.getenv('DISCORD_TOKEN'))

if TOKEN is None:
    print("\033[31mLooks like you haven't properly set up a Discord token environment variable in the `.env` file. (Secrets on replit)\033[0m")
    print("\033[33mNote: If you don't have a Discord token environment variable, you will have to input it every time. \033[0m")
    TOKEN = input("Please enter your Discord token: ")

bot.run(TOKEN, reconnect=True)
