#This code has been created by Kartik The Great
#in honour of himself being the singlest person alive

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
from time import time

def randnum():
    rand = str(round(time(),7))
    rand2 = str(rand[::-1])
    return rand2[0]

#intends and prefix commands .....................................
intents = discord.Intents.all()
client=commands.Bot(command_prefix ='&',intents=intents)

#showing that the bot has started..................................
@client.event
async def on_ready():
    print("Started")
    
#status command .................................................
@client.command()
async def status(ctx):
    await ctx.send("This bot is under construction . Please wait patiently")

#show commands command ............................................   
@client.command()
async def commands(ctx):
    await ctx.send("status\nowners\nconnect\nleave\nplay\npause\nresume\nstop")

#owners command ...................................................
@client.command()
async def owners(ctx):
    await ctx.send("This is an initiative set by amateurs")     

#connect command .....................................................
@client.command(pass_context=True)
async def connect(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
      
    else:
        await ctx.send("Connect to the voice channel first")
 
#leave command .......................................................       
@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the voice channel")
    else:
        await ctx.send("I am already disconnected")

#pause command ...........................................................
@client.command(pass_context=True)
async def pause(ctx):
    if (ctx.author.voice):
      voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
      if voice.is_playing():
         voice.pause()
      else:
         await ctx.send("The voice is already paused")
    else:
        await ctx.send('Please connect to voice channel first')
        
#stop command ............................................................
@client.command(pass_context=True)
async def stop(ctx):
    if (ctx.author.voice):
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        voice.stop()
        await ctx.send("The voice has been stopped") 
    else:
        await ctx.send("Please connect to the voice channel first")
                 
#resume command ..........................................................       
@client.command(pass_context=True)
async def resume(ctx):
    voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
    if (ctx.author.voice):
        if voice.is_paused():
          voice.resume()
        else:
          await ctx.send("The voice is already running")  
    else:
        await ctx.send("Please connect to the voice channel first")

#Truth game .................................................(Upgrade it on a daily basis)
@client.command(pass_context=True)
async def truth(ctx):
    a="Do you have a girlfriend?"
    b="Who was your first kiss?"
    c="Who do you have crush on?"
    d="What's the most embarrassing moment of your life?"
    e="What's your favourite sport?"
    f="When was the last time you cried?"
    g="What's your biggest fear? (not philosophical)"
    h="Your best ever pickup line?"
    i="Who is your comfort character?"
    j="What's your weird fantasy?"
    l1=[a,b,c,d,e,f,g,h,i,j]
    await ctx.send(l1[randnum])

#Dare game.............................................................(Upgrade it on a daily basis)
@client.command(pass_context=True)
async def dare(ctx):
    a="Dance with your underwear in your hand"
    b="Sing a song on the top of your lungs from your window"
    c="Put on a frock on your neck and dance on Hotel California"
    d="Call a random number and talk like you are their previous reincarnation's partner"
    e="Show your weirdest photo available"
    f="Jump on your bed thrice and shout MarcoPolo"
    g="Speak out your will as if your funeral is tomorrow"
    h="Put your craziest clip online"
    i="Kiss an item from your room (tongue involved)"
    j="Balance a steel utensil on your nose and walk around for 30 seconds."
    l2=[a,b,c,d,e,f,g,h,i,j]
    await ctx.send(l2[randnum])

#token key ..............................................................
client.run("MTE1NDc3MzM5MjEzODk2OTIxMA.GPqNQP.cktcq3EOFMxaUxjPqQsmU770BYQpIQD-fh--8U")  #Important 