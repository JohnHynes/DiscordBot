import discord
from discord.ext import commands

TOKEN = 'NzQxMzA3Nzk3NDg0MDc3MTA3.Xy1qrw.kxkQTNlxEWkof05PyRIzDQU982g'

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