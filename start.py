import os
import discord
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv("DISCORD_SECRET")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents) #Objeto de discord

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!info'):
        await message.channel.send('GIGACHAD is now here')
        
client.run(SECRET) 

