#This code has been created by Kartik The Great
#in honour of himself being the singlest person alive

import discord
from discord.ext import commands
from time import time
import youtube_dl
from pytube import YouTube
import yt_dlp
import datetime
import random
import os
from collections import defaultdict
from random import shuffle
import json

#intends and prefix commands .....................................
intents = discord.Intents.all()
client=commands.Bot(command_prefix ='&',intents=intents)
songs_folder = "Songs"
playlists = defaultdict(list)
current_song_index = defaultdict(int)
playlist_file = "playlists.json"

#playlist in json file....................................
if os.path.isfile(playlist_file):
    with open(playlist_file, "r") as file:
        saved_playlists = json.load(file)
        playlists.update(saved_playlists)

#save playlist ...................................
def save_playlists():
    with open(playlist_file, "w") as file:
        json.dump(playlists, file)

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
    embed=discord.Embed(title="Commands",description="status->Shows status of bot\nmusic_commands->Shows music commands\ntruth_daregame->Shows truth and dare game commands\nping->Shows the ping of the bot\ntime->Shows the time\nowners->Shows the owners")
    await ctx.send(embed=embed)

#individual command list .......................................
@client.command()
async def music_commands(ctx):
    embed=discord.Embed(title="Music Commands",description="connect->Connects to vc\npause->Pause the song\nresume->Resume the song\nstop->Stops the song \nplay (playlist_name)->Plays the playlist\ncreateplaylist (playlist_name)->Create the playlist\ndeleteplaylist (playlist_name)->Delete the playlist\nshowplaylists->Shows the total number of playlists\nshowplaylist (playlist_name)->Shows the songs in the playlist\nshowallsongs->Shows all available songs\ndeletesong (playlist_name)->Delets the song from the playlist")
    await ctx.send(embed=embed)

@client.command()
async def truth_daregame(ctx):
    embed=discord.Embed(title="Truth & Dare",description="truth->Shows a random truth\ndare->Shows a random dare")
    await ctx.send(embed=embed)

#time command .......................................................
@client.command()
async def time(ctx):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'The current time is: {current_time}')

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

#play command.............................................
@client.command()
async def play(ctx, playlist_name: str = None, song_number: int = None):
    global current_song_index

    voice_channel = ctx.author.voice.channel

    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()

    voice_client = await voice_channel.connect()

    if playlist_name:
        if playlist_name.lower() in playlists:
            selected_playlist = playlists[playlist_name.lower()]

            if song_number is not None and 1 <= song_number <= len(selected_playlist):
                song_index = song_number - 1  # Adjust for 0-based indexing
                source = os.path.join(songs_folder, selected_playlist[song_index])
                voice_client.play(discord.FFmpegPCMAudio(source))
                await ctx.send(f"Now playing: {selected_playlist[song_index]}")
            else:
                await ctx.send("Invalid song number. Please specify a valid song number.")
        else:
            await ctx.send(f"The '{playlist_name}' playlist does not exist. Use the &createplaylist command to create it.")
    else:
        await ctx.send("Please provide a playlist name as input.")


#create playlist..........................................
@client.command()
async def createplaylist(ctx, playlist_name: str):
    if playlist_name.lower() not in playlists:
        playlists[playlist_name.lower()] = []
        current_song_index[playlist_name.lower()] = 0
        await ctx.send(f"Playlist '{playlist_name}' created.")
        save_playlists()
    else:
        await ctx.send(f"The playlist '{playlist_name}' already exists.")

#add songs to playlist.........................
@client.command()
async def add(ctx, playlist_name: str, *, song_choice: str):
    if playlist_name.lower() not in playlists:
        await ctx.send(f"The playlist '{playlist_name}' does not exist. Use the &createplaylist command to create it.")
        return

    songs = [f for f in os.listdir(songs_folder) if f.endswith('.mp3')]
    if not songs:
        await ctx.send("No songs found in the 'songs' folder.")
        return

    song_choice = song_choice.lower()
    matching_songs = [song for song in songs if song_choice in song.lower()]

    if not matching_songs:
        await ctx.send(f"No songs matching '{song_choice}' found in the 'songs' folder.")
        return

    playlists[playlist_name.lower()].extend(matching_songs)
    await ctx.send(f"{len(matching_songs)} song(s) added to the '{playlist_name}' playlist.")
    save_playlists()

#Showplaylist songs ...........................................
@client.command()
async def showplaylist(ctx, playlist_name: str):
    if playlist_name.lower() not in playlists:
        await ctx.send(f"The playlist '{playlist_name}' does not exist. Use the &createplaylist command to create it.")
        return

    selected_playlist = playlists[playlist_name.lower()]

    if not selected_playlist:
        await ctx.send(f"The '{playlist_name}' playlist is empty. Use the &add command to add songs to it.")
        return

    await ctx.send(f"Current Playlist '{playlist_name}':")
    for i, song in enumerate(selected_playlist, start=1):
        await ctx.send(f"{i}. {song}")

#Delete playlists.......................
@client.command()
async def deleteplaylist(ctx, playlist_name: str):
    if playlist_name.lower() in playlists:
        del playlists[playlist_name.lower()]
        await ctx.send(f"Playlist '{playlist_name}' deleted.")
        save_playlists()
    else:
        await ctx.send(f"The playlist '{playlist_name}' does not exist.")

#Show all playlists..........................
@client.command()
async def showplaylists(ctx):
    if not playlists:
        await ctx.send("No playlists found.")
        return

    playlist_names = list(playlists.keys())
    await ctx.send(f"Total playlists: {len(playlist_names)}")
    await ctx.send("Playlist names:")
    await ctx.send("\n".join(playlist_names))

#Total songs available.................
@client.command()
async def showallsongs(ctx):
    songs = [f for f in os.listdir(songs_folder) if f.endswith('.mp3')]
    total_songs = len(songs)
    
    if total_songs > 0:
        song_list = "\n".join(songs)
        await ctx.send(f"Total songs in the 'songs' folder: {total_songs}\nSongs:\n{song_list}")
    else:
        await ctx.send("No songs found in the 'songs' folder.")

#edit playlist......................
@client.command()
async def deletesong(ctx, playlist_name: str, song_number: int=None):
    if not playlist_name:
        await ctx.send("Please provide a playlist name.")
        return

    if not song_number:
        await ctx.send("Please specify the song number to remove.")
        return

    if playlist_name.lower() not in playlists:
        await ctx.send(f"The '{playlist_name}' playlist does not exist.")
        return

    selected_playlist = playlists[playlist_name.lower()]

    if 1 <= song_number <= len(selected_playlist):
        song_index = song_number - 1
        removed_song = selected_playlist.pop(song_index)
        save_playlists()  

        await ctx.send(f"Removed song '{removed_song}' from the '{playlist_name}' playlist.")
    else:
        await ctx.send("Invalid song number. Please specify a valid song number.")

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
    shuffle(l1)
    embed=discord.Embed(title="TRUTH" , description=l1[0],color=0x44ff44)
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
    shuffle(l2)
    embed=discord.Embed(title="DARE" , description=l2[0],color=0x44ff44)
    await ctx.send(embed=embed)
    
#token key ..............................................................
client.run("MTE1NDc3MzM5MjEzODk2OTIxMA.GPqNQP.cktcq3EOFMxaUxjPqQsmU770BYQpIQD-fh--8U")  #Important 