import discord
import requests, json
from discord.ext import commands

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, message):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    @commands.command(name='echo')
    async def echo(self, message, arg):
        await message.channel.send(arg)

    @commands.command(name='math')
    async def math(self, message, arg):
        try:
            await message.channel.send(eval(arg))
        except:
            await message.channel.send('Syntax Error')   

    @commands.command(name='codehelp')
    async def codehelp(self, message, arg):
        search = arg.replace(" ", "+")
        await message.channel.send('https://github.com/search?q=' + search + '&ref=simplesearch')
        await message.channel.send('https://stackoverflow.com/search?q=' + search)

    @commands.command(name='weather')
    async def weather(self, message, arg):
        api_key = "7e7928224d722fcf2ffbb1af2b4499bc"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = arg.replace(" ", "+")
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404": 
        
            # store the value of "main" 
            # key in variable y 
            y = x["main"] 
        
            # store the value corresponding 
            # to the "temp" key of y 
            current_temperature = y["temp"] 
        
            # store the value corresponding 
            # to the "pressure" key of y 
            current_pressure = y["pressure"] 
        
            # store the value corresponding 
            # to the "humidity" key of y 
            current_humidiy = y["humidity"] 
        
            # store the value of "weather" 
            # key in variable z 
            z = x["weather"] 
        
            # store the value corresponding  
            # to the "description" key at  
            # the 0th index of z 
            weather_description = z[0]["description"]
            
            msg = ( "Weather in " + arg + 
          "\n Temperature = " +
                    str((current_temperature - 273.15) * 9/5 + 32) + 
          "°F \n Atmospheric Pressure = " +
                    str(current_pressure) +
          "hPa \n Humidity = " +
                    str(current_humidiy) +
          "% \n Normal Description = " +
                    str(weather_description)).format(message)
        else: 
            msg = (" City Not Found ").format(message) 

        await message.channel.send(msg)

def setup(bot):
  bot.add_cog(BasicCog(bot))
