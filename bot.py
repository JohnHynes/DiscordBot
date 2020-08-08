import discord
from discord.ext import commands

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

BOT_PREFIX = "!"

bot = commands.Bot(command_prefix=BOT_PREFIX)

bot.remove_command('help')

@bot.command(name='help')
async def help(message):
    msg =   '***Bot Commands***\n'\
            '**!help** : *Prints out command list*\n'\
            '**!hello** : *Says hello*\n'\
            '**!echo <msg>** : *Repeats a message back to you*\n'\
            '**!math <formula>** : *Calculated the result of <formula>*\n'\
            '**!codehelp <query>** : *Searches for <query> on StackOverflow and GitHub*\n'\
            '**!weather <city name>** optional **,<state code>** : *Gives the current weather from a given city.*\n'\
            '**!weather <zipcode>,<countrycode>** : *Gives the current weather from a given zipcode. USA = US*'
    await message.channel.send(msg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.load_extension('cogs.commands')
    print('------')

bot.run(TOKEN)
