import discord
import dotenv
import os
from discord.ext import commands
from dotenv import load_dotenv
import openai 

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents);


openai.api_key = os.getenv('apikey')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='OpenApi', url='https://www.twitch.tv/hoodie4546'))
    print(f'Bot Status is Spiced up ! {bot.user.name}')
    print(f"{bot.user.name} is Ready For Ai Chating!")
    print(f"{bot.user.name} is connected to Open Ai Api!")
 


@bot.event
async def on_message(message):
    if message.channel.id == 1113365746219749477 and not message.author.bot:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=message.content,
            temperature=0.7,
            max_tokens=50
        )
        await message.channel.send(response.choices[0].text)


bot.run(os.getenv('Token'))