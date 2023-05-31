import discord
from discord.ext import commands
import os, random
bot = commands.Bot(command_prefix="@" , intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Вы зашли как {bot.user}")

@bot.command()
async def protection(ctx):
    with open(f'C:/Users/user/Desktop/memebot/images/з.jpg', "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def aaa(ctx):
    with open(f'C:/Users/user/Desktop/memebot/images/з.jpg', "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTEwNTg4MzEzNTc0NjUxOTE5Mg.G7jxqp.3sp1QBUYcXOZOSlxxspPuZI25c2iEu9fdBm3tw")




