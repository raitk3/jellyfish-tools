#!/bin/python3
import asyncio
import os
import sys

from discord import Game, Intents, version_info
from discord.ext import commands
from dotenv import load_dotenv
from helpers.data import Data

from modules.logger.logger import Logger

class MainBot():
    def __init__(self, *args) -> None:
        self.dev = self.parse_args()
        self.logger = Logger(self.dev)
        self.bot = self.init_bot()
        self.data = Data(self.bot)
    
    def init_bot(self, dev = False):
        """Initialise the Discord interface"""
        # Needs actual permissions to be set
        PERMISSIONS = '8'
        intents = Intents.default()
        intents.message_content = True
        description = '''Rait wanted to do a bot, so uhh...here it is!'''
        prefix = 'jf?' if dev else 'jf.'
        help_cmd = commands.DefaultHelpCommand(show_parameter_descriptions=False)
        return commands.Bot(command_prefix=prefix, 
                            description=description,
                            intents=intents,
                            permissions=PERMISSIONS,
                            help_command=help_cmd,
                            activity=Game(name=f"{prefix}stoobid" if dev else f"{prefix}smørt"))
    
    def find_token(self):
        """Locate the discord token for the bot to run."""
        load_dotenv()
        token = os.getenv("DISCORD_TOKEN")
        if token is None:
            raise Exception("No token found, please add a token to .env as `DISCORD_TOKEN` and try again.")
        return token
    
    def parse_args(self, *args):
        dev = False
        for argument in args:
            if argument in ["--debug", "--dev", "-d"]:
                dev = True
        return dev
    
    async def load_modules(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                cog_name = filename[:-3]
                if cog_name in ['experimental', 'debug'] and not self.dev:
                    continue
                self.logger.info(f"Loading module {cog_name}")
                await self.bot.load_extension(f'cogs.{cog_name}')

    
    async def main(self, *args):
        dev = False
        self.logger.info("Jellyfish started...")
        self.logger.info(f"discord.py version: {version_info}")
        try:
            token = self.find_token()
        except Exception as e:
            self.logger.error(e)
            return
        @self.bot.event
        async def on_ready():
            try:
                await self.bot.tree.sync()
            except Exception as e:
                self.logger.error(e)
        await self.load_modules()
        await self.bot.start(token)


if __name__ == '__main__':
    args = sys.argv
    main_bot = MainBot(args)
    asyncio.run(main_bot.main(args))
