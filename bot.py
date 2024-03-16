import discord
import os
from discord.ext import commands
from src import qaran
from dotenv import load_dotenv

load_dotenv()

# Discord bot token
TOKEN = os.getenv('TOKEN')

# Discord client with intents
intents = discord.Intents.default()
intents.message_content = True 
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!randomverse'):
        content = message.content.split()
        editions = content[1:] if len(content) > 1 else ['quran-uthmani', 'en.asad']
        random_ayahs = qaran.get_random_ayah(editions)
        for edition, verse in random_ayahs.items():
            await message.channel.send(f'[{edition}] {verse}')

if __name__ == "__main__":
  client.run(TOKEN)
