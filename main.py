# This example requires the 'message_content' intent.
import os
import discord
import logging
import importlib
from image_util import parse_image
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

# Load environmental variables
load_dotenv()

# Discord Intents
intents = discord.Intents.default()
intents.message_content = True

# Logging Handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Bot utility
bot_desc = 'Taking the text out of your images, done easy!'
bot = commands.Bot(command_prefix='$', description=bot_desc, intents=intents)
bot.remove_command('help')

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

@bot.event
async def on_command_error(ctx, error):
  """ Catch non-existing bot commands """
  if isinstance(error, CommandNotFound):
    await ctx.send('Command doesn\'t exist!')

@bot.command()
async def help(ctx):
  """Display a list of available commands to use"""
  help_text = f"""
  ```{bot_desc}\n\nCommands\n\t$text - I will take in an image and grab the text from it for you!\n\n👀Don\'t forget to attach an image along with this command! I can read even Japanese!\n\nExample: $text ja```"""
  
  await ctx.send(help_text.strip())

@bot.command()
async def text(ctx, lang='en'):
  """ Takes in an image and returns text """
  try:
    attachment = ctx.message.attachments[0]
    text = parse_image(attachment, lang)
    await ctx.send(text)
  except Exception as e:
    await ctx.send(f'Error! ${e}')

bot.run(os.getenv('DISCORD_TOKEN'))