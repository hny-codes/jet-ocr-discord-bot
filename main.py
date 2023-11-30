# This example requires the 'message_content' intent.
import os
import discord
import logging
import importlib
from image_util import parse_image
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands

# Load environmental variables
load_dotenv()

# Discord Intents
intents = discord.Intents.default()
intents.message_content = True

# Logging Handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Bot utility
bot_desc = 'Test bot'
bot = commands.Bot(command_prefix='$', description=bot_desc, intents=intents)

# On Ready Event
@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')
  print(f'Login ID: {str(bot.user.id)}')
  await bot.change_presence(activity=discord.Game('$help for more'))

@bot.command()
async def hello(ctx):
  """ Basic command that says hi back """
  await ctx.send('Hi!')

@bot.command()
async def text(ctx, lang='en'):
  try:
    attachment = ctx.message.attachments[0]
    text = parse_image(attachment, lang)
    await ctx.send(text)
  except Exception as e:
    await ctx.send(f'Error! ${e}')

bot.run(os.getenv('DISCORD_TOKEN'))