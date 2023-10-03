import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord_py_wavelink import WavelinkMixin

bot = Bot(command_prefix='!')

# Mix the Wavelink features into the bot
bot.add_cog(WavelinkMixin(bot))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    player = ctx.voice_client

    if player and player.channel:
        await player.disconnect()

    await ctx.invoke(bot.get_command('connect'))

@bot.command()
async def play(ctx, *, query):
    player = ctx.voice_client

    if not player:
        await ctx.invoke(bot.get_command('join'))

    track = await bot.wavelink.get_tracks(f'ytsearch:{query}')

    if not track:
        return await ctx.send('No tracks found.')

    player.play(track[0])

bot.run('YOUR_BOT_TOKEN')






bot.run('MTE1NDc3MzM5MjEzODk2OTIxMA.GPqNQP.cktcq3EOFMxaUxjPqQsmU770BYQpIQD-fh--8U')
