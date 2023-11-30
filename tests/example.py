# This example requires the 'message_content' intent.
import os
import discord
import logging
from os.path import join, dirname
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

# Discord Client
client = discord.Client(intents=intents)

# Logging Handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('DISCORD_TOKEN'), log_handler=handler, log_level=logging.DEBUG)
