import discord
import os
import random
from discord.ext import commands
##from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix = 's!')
owner_id = 288156627486638090

# Cog loading
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Console messages
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('s!help | stormbot.ga'))
    print('The Storm has arrived.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

# Background Tasks
##status = cycle(['Status 1', 'Status 2'])
##@tasks.loop(seconds=10)
##async def change_status():
##    await client.change_presence(activity=discord.Game(next(status)))

# Errors
@client.event
async def on_command_error(ctx, error):
##    if isinstance(error, commands.MissingRequiredArgument):
##        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission for this command.')
    elif isinstance(error, commands.NotOwner):
        await ctx.send('You do not have permission for this command.')

# Run Bot
client.run('NDU2NjYwNjM4MjgyODA5MzQ2.XLtjQA.g4yqtQw_o0s8oMW6j4I7F78RS6o')
