from discord.ext import commands

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def on_message(self, message):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    @commands.command(name='echo')
    async def on_message(self, message):
        msg = '{0.message.content}'.format(message)
        await message.channel.send(msg[5:])



def setup(bot):
  bot.add_cog(BasicCog(bot))