import os
import discord
from dotenv import load_dotenv
from pic2pic import pic2pic

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
    	for name in client.guilds:
    		print(name, '\n')
    	if guild.name == GUILD:
            break
    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

  
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id == "DISCORD CHANNEL ID" and message.attachments:
        for attachment in message.attachments:
            image_url = attachment
            pic2pic(image_url)
            file = discord.File("PATH TO YOUR IMAGE FILE", filename="gen_image.png")
            await message.channel.send(file=file)

