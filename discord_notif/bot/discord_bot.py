# discord_bot.py
from discord.ext import commands
import discord
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

async def send_message_to_general_channel(content, general_channel_id):
    
    try:
        general_channel = bot.get_channel(general_channel_id)
        if general_channel is None:
            raise ValueError("No se pudo encontrar el canal #general")

        # Enviar el mensaje al canal #general
        await general_channel.send(content)
    except Exception as e:
        print(e)
        raise ValueError(f"Error al enviar el mensaje: {str(e)}")
