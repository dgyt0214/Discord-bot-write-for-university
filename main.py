from encodings import utf_8
from lib2to3.pgen2 import token
from turtle import end_fill
import os, json, nextcord, logging, datetime, random, time
from ssl import CHANNEL_BINDING_TYPES
import sentry_sdk
import nextcord
from nextcord.ext import commands
from nextcord.ui import *
from nextcord.ext import commands
from nextcord import TextChannel
from nextcord.utils import get
intents=nextcord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)
with open ("test.json","r",encoding='utf8') as jfile:
  jdate=json.load(jfile)

@bot.event
async def on_ready():
    print('Bot is Online')
    
@commands.is_owner()
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cod.{extension}')
    await ctx.send(f'導入{extension}成功')

@commands.is_owner()
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cod.{extension}')
    await ctx.send(f'導出{extension}成功')

@commands.is_owner()
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cod.{extension}')
    await ctx.send(f'重製{extension}成功')
    
    
    
for filename in os.listdir('./cod'):
    if filename.endswith('.py'):
        bot.load_extension(f'cod.{filename[:-3]}')
        
if __name__ == "__main__":  
    bot.run(jdate['token'])