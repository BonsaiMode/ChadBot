import discord
import json
import os

from dotenv import load_dotenv

import stoic_tip

load_dotenv()                                                                   # Cargamos las variables de entorno del .env

SECRET = os.getenv("DISCORD_SECRET")                                            # Obtenemos el token de discord
store = json.load(open('./stoic_tips.json', 'r'), encoding='utf-8')             # Cargamos el json

intents = discord.Intents.default()                                             # Objeto que define los intents de discord
intents.message_content = True                                                  # Activamos el intent de mensajes

client = discord.Client(intents=intents)                                        # Objeto de discord

@client.event
async def on_ready():                                                           # Evento que se ejecuta cuando el bot se conecta y esta listo
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):                                                  # Evento que se ejecuta cuando se recibe un mensaje
    if message.author == client.user:
        return

    if message.content.startswith('!info'):
        await message.channel.send('GIGACHAD is now here')
    if message.content.startswith('!tip'):
        await message.channel.send(stoic_tip.stoic_tip(store.get('tips')))
        
client.run(SECRET) 

