import discord
import os
import asyncio
import datetime

from discord.ext import commands

client = commands.Bot(
    command_prefix='.',
    self_bot=True)


@client.event
async def on_ready():
    print(f'{client.user} Is now Online.')


client.run(os.getenv("TOKEN"), bot=False)

#If you are hosting on repl.it Make sure to go on environmental veriables and add new secreat with name "TOKEN" and then in 
#value give your token and click on run this is to prevent other users to acess your token 
#WITH LOVE MADE BY AAYAN :P