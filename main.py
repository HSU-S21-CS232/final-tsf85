import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('hi')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Sup dickface!")

client.run(os.environ['TOKEN'])
