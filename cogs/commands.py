from discord.ext import commands


class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def on_message(self, message):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)



def setup(bot):
  bot.add_cog(BasicCog(bot))