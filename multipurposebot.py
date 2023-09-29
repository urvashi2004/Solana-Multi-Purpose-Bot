#This code has been created by Kartik The Great
#in honour of himself being the singlest person alive

import discord
from discord.ext import commands
from time import time
from youtube_dl import YoutubeDL

#intends and prefix commands .....................................
intents = discord.Intents.all()
client=commands.Bot(command_prefix ='&',intents=intents)

#showing that the bot has started..................................
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(type=discord.ActivityType.listening,name='&commands'))
    print("Started")
    
#status command .................................................
@client.command()
async def status(ctx):
    await ctx.send("This bot is under construction . Please wait patiently")

#ping command............................................
@client.command()
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!", color=0xff6600)
    else:
        embed=discord.Embed(title="PING", description=f":ping_pong: The ping is **{round(client.latency *1000)}** milliseconds!", color=0x990000)
    await ctx.send(embed=embed)

#show commands command ............................................   
@client.command()
async def commands(ctx):
    await ctx.send("status\nowners\nconnect\nleave\ntruth\ndare\npause\nresume\nstop\nping")

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
        await ctx.send("Connected")
      
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
    j="What's your weirdest fantasy?"
    l1=[a,b,c,d,e,f,g,h,i,j]
    for i in range(0,10):
        rand = str(round(time(),7))
        rand2 = str(rand[::-1])
    embed=discord.Embed(title="TRUTH" , description=l1[int(rand2[0])],color=0x44ff44)
    await ctx.send(embed=embed)

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
    for i in range(0,10):
        rand = str(round(time(),7))
        rand2 = str(rand[::-1])
    embed=discord.Embed(title="DARE" , description=l2[int(rand2[0])],color=0x44ff44)
    await ctx.send(embed=embed)

#token key ..............................................................
client.run("MTE1NDc3MzM5MjEzODk2OTIxMA.GPqNQP.cktcq3EOFMxaUxjPqQsmU770BYQpIQD-fh--8U")  #Important 