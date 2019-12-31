#!/usr/bin/env python3

import os, sys
import asyncio

import discord
from discord.ext import commands

# This file will have the discord bot functions. Look at discord.py documentation
# Currently absolutely barebones functionality

dirname, pyfilename = os.path.split(os.path.abspath(sys.argv[0]))
tfilename = os.path.join(dirname, 'token.txt')
with open(tfilename) as token_file:
    token = token_file.read().strip()


servers = []
bot = commands.Bot(command_prefix='$', fetch_offline_members=False)

async def print_users():
    while(True):
        for server in bot.guilds:
            for user in server.members:
                for activity in user.activities:
                    if isinstance(activity, discord.activity.Streaming):
                        await twitch_things(server, activity)
        await asyncio.sleep(30)

# This needs to be done in the twitch things module, when it's made properly
async def twitch_things(server, stream):
    print(stream.details)
    # channel = discord.utils.get(server.text_channels, name='striimihommia')
    # await channel.send(stream.url)

def stream_embed():
    embed = discord.Embed(title=character['proper_name'],
            colour=0x00EAFF,
            url=character['online_webpage'],
            description=""
            )


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for server in bot.guilds:
        servers.append(server.id)
    bot.loop.create_task(print_users())

@bot.command()
async def list_servers(ctx):
    print(servers)

bot.run(token)
