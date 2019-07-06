#Import / prefix
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

#Events

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Ping Pong"))
    print("Bot is online.")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#TestEvent
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Hello'):
        await message.channel.send('Hello ' + f'{message.author.display_name}' + '!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!What is your gender?'):
        await message.channel.send('01000010 01101001 01101110 01100001 01110010 01111001')

client.run("NTk2MDYxNTIxNTIwNDkyNTUz.XR4VpA.GwGym2Wsn69pmNdCWxZoyPwsNUo")

#Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping {round(client.latency * 1000)}ms')

#Ghostping command
@client.command()
async def gping(ctx):
    await ctx.channel.purge(limit=1)

#Clear
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run("NTk2MDYxNTIxNTIwNDkyNTUz.XR4VpA.GwGym2Wsn69pmNdCWxZoyPwsNUo")
