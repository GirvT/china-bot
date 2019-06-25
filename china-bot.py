import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "NTYwNTAzMzMyMTk2NTgxMzc2.D305YA.TPHrxwl5_2kf757UQZXQqp_RwAI"
bot = commands.Bot(command_prefix="G-")
greatFirewall = list()

@bot.event
async def on_ready():
    print('Glory to China!')
    f = open("china.txt", "r",  encoding="utf8")
    for line in f:
        greatFirewall.append(line.rstrip('\n').lower())
    f.close()

@bot.event
async def on_message(message):
    if message.channel.name == 'peoples-republic-of-china':
        for wordsThatDontExist in greatFirewall:
            if wordsThatDontExist in message.content.lower():
                await message.delete()
                await message.channel.set_permissions(message.author, read_messages=True, send_messages=False)
    else:
        create_republic = True
        for channel in message.guild.channels:
            if channel.name == 'peoples-republic-of-china':
                    create_republic = False
        if (create_republic):
            await message.guild.create_text_channel('People\'s Republic of China')
    

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

bot.run(TOKEN)