import discord
from discord.ext import commands
import asyncio
import yt_dlp

intents = discord.Intents.all()
# Define the bot's command prefix
bot = commands.Bot(command_prefix='!',intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to join a voice channel
@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

# Command to leave a voice channel
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Command to play a song from YouTube using yt-dlp
@bot.command()
async def play(ctx, *, song_query):
    voice_client = ctx.voice_client

    if not ctx.author.voice:
        await ctx.send("You must be in a voice channel to use this command.")
        return

    if not voice_client:
        # Join the voice channel using the join command
        command = bot.get_command('join')
        await ctx.invoke(command)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
    }

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    try:
        info = ydl.extract_info(f"ytsearch1:{song_query}", download=False)
        if 'entries' in info:
            url = info['entries'][0]['url']

            # Debugging messages
            print(f"Bot is_playing: {voice_client.is_playing()}")
            
            if voice_client.is_playing():
                await ctx.send("The bot is already playing music.")
            else:
                voice_client.stop()
                voice_client.play(discord.FFmpegPCMAudio(url))
        else:
            await ctx.send("No search results found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


bot.run('MTE1NDc3MzM5MjEzODk2OTIxMA.GPqNQP.cktcq3EOFMxaUxjPqQsmU770BYQpIQD-fh--8U')
