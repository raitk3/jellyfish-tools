"""Experimental things"""

from discord import app_commands
from discord.ext import commands
import logging
from helpers.emoji import Emoji

class RacePlan(commands.Cog, name='RacePlan'):
    """Experimental stuff that most likely won't work"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logger = logging.getLogger("CattoBotto.raceplan")
        self.last_sent = None
        self.emoji = Emoji()

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info('Race planner tools are loaded')
        
    @commands.command(hidden=True)
    async def race(self, ctx):
        await ctx.send("Hi!")

async def setup(bot):
    await bot.add_cog(RacePlan(bot))