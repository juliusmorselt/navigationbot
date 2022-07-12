import discord
import creds
from discord.ext import commands

client = commands.Bot(command_prefix='/')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Yes BITCH IM ONLINE!! as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content == "hello":
            await message.channel.send('sup')



client = MyClient()
client.run(creds.BOT_TOKEN)