import discord
from discord.ext import commands

TOKEN = 'NzQxMzAzMjg4NDUxOTU2Nzc2.Xy1mfA.P8nYNnA_xcNq1xUWBNGlIp1YLUc'

BOT_PREFIX = "!"

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.load_extension('cogs.commands')
    print('------')

bot.run(TOKEN)
