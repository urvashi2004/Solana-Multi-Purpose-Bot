import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

intents = discord.Intents.all()
client=commands.Bot(command_prefix ='&',intents=intents)

@client.event
async def on_ready():
    print("Started")

@client.command()
async def status(ctx):
    await ctx.send("This bot is under construction. Please wait patiently")

@client.command()
async def owners(ctx):
    await ctx.send("This is an initiative set by.............")     #needed

@client.command(pass_context=True)
async def connect(ctx):
    if (ctx.author.voice):
        channel=ctx.message.author.voice.channel
        await channel.connect()
        
    else:
        await ctx.send("Connect to the voice channel first")

@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the voice channel")
    else:
        await ctx.send("I am already disconnected")

client.run("MTE1NDc3MzM5MjEzODk2OTIxMA.GPqNQP.cktcq3EOFMxaUxjPqQsmU770BYQpIQD-fh--8U")  #Important