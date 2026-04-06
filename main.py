import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load rahasia dari .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Setup Bot dengan prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Login berhasil sebagai {bot.user}')
    
    # Load semua file di dalam folder cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Modul {filename} berhasil dimuat.')

if __name__ == '__main__':
    bot.run(TOKEN)