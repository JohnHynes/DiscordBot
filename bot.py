import discord
from discord.ext.commands import Bot

TOKEN = 'NzQxMzAzMjg4NDUxOTU2Nzc2.Xy1mfA.RXGHTWPPnid63b0Qp7SDhTCB-wI'

BOT_PREFIX = "!"

#bot = Bot(command_prefix=BOT_PREFIX)

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(BOT_PREFIX + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
