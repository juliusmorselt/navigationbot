import discord
from interactions import Embed
from matplotlib.pyplot import close
import creds
import embeds
from discord.ext import commands

prefix = '/'

class MyClient(discord.Client):

    async def on_ready(self):
        print('Yow I am online as {0}!'.format(self.user))
    


    async def on_message(self, message):
        if message.author == client.user:
            return



    async def on_message(self, message):
        if message.content == prefix + 'help':
            await message.channel.send(embed=embeds.HELP_EMBED)
                


client = MyClient()
client.run(creds.BOT_TOKEN)