# ------------------------------------------------- Default libraries ------------------------------------------------ #
import json
import os

# ----------------------------------------------- Third Party Libraries ---------------------------------------------- #
import discord
from dotenv import load_dotenv

# --------------------------------------------------- Local modules -------------------------------------------------- #
import src.modules.stoic_tip as stoic_tip

# ------------------------------------------ Default initialisation routine ------------------------------------------ #

load_dotenv()                                                               # Cargamos las variables de entorno del .env

SECRET = os.getenv("DISCORD_SECRET")                                        # Obtenemos el token de discord
store = json.load(open('./stoic_tips.json', 'r'), encoding='utf-8')         # Cargamos el json

intents = discord.Intents.default()                                         # Objeto que define los intents de discord
intents.message_content = True                                              # Activamos el intent de mensajes

client = discord.Client(intents=intents)                                    # Objeto de discord

# ------------------------------------------------------ Events ------------------------------------------------------ #

@client.event
async def on_ready():                                                       # Evento al conectar y estar listo
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):                                              # Evento al recibir un mensaje
    if message.author == client.user:                                       # Si el mensaje es nuestro, abortamos
        return
    if message.content.startswith('!info'):                                 # Sección helpme, TODO: AMPLIAR
        await message.channel.send('GIGACHAD is now here')
    if message.content.startswith('!tip'):                                  # Sección de tips
        tip = stoic_tip.get_random_tip(store.get('tips'))
        await message.channel.send(tip)

# ------------------------------------------------------ Main ------------------------------------------------------- #
client.run(SECRET) 
