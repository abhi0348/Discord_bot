import discord
import random

from discord import user

TOKEN='ODg1NjM3NTE0NzU1NDY5MzMz.YTp8NQ.M32XpXj_Zqokvqjd0nbUE5Iup94'

client = discord.Client()

@client.event 
async def on_ready():
       print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
       username =str(message.author).split('#')[0]
       user_message=str(message.content)
       channel=str(message.channel.name)
       print(f'{username}:{user_message}({channel})')

       if message.author == client.user:
              return 
       if message.channel.name =='general':
            if user_message.lower()=='bye':
                   await message.channel.send(f'Khuda hafiz piggie!')
                   return 
            elif user_message.lower()=='hello':
                   await message.channel.send(f'Salam walekum piggie!')
                   return
            elif user_message.lower()=='how are you':
                   await message.channel.send(f'Sab khariyat !')
                   return 
 
client.run(TOKEN)            