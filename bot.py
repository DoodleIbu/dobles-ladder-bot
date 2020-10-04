import os

from discord import Member
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

class Team(commands.Converter):
    async def convert(self, ctx, argument):
        return argument

@bot.command(name='challenge')
async def challenge(ctx, challenging_team: Team, defending_team: Team, court: str):
    await ctx.send('{} has challenged {} on {}!'.format(challenging_team, defending_team, court))

@bot.command(name='team')
async def team(ctx, team: Team):
    await ctx.send('{} is a team'.format(team))

@bot.command(name='join')
async def join(ctx, member: Member):
    requesting_user = ctx.author
    await ctx.send('{} and {} would like to join'.format(requesting_user, member))

bot.run(TOKEN)
