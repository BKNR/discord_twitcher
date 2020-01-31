#!/usr/bin/env python3

import os, sys
import asyncio
import random

import discord
from discord.ext import commands

# This file will have the discord bot functions. Look at discord.py documentation
# Currently absolutely barebones functionality

dirname, pyfilename = os.path.split(os.path.abspath(sys.argv[0]))
tfilename = os.path.join(dirname, 'token.txt')
with open(tfilename) as token_file:
    token = token_file.read().strip()


STREAMERS = dict()
bot = commands.Bot(command_prefix='$')

class Streamer:
    def __init__(self, member):
        self.member = member
        self.streaming = False
        self.msg = None


async def stream_loop():
    while(True):
        for server in bot.guilds:
            for member in server.members:
                if isinstance(member.activity, discord.activity.Streaming):
                    if member.activity.game == "Just Chatting":
                        await twitch_things(member)
                    else:
                        # Streaming a wrong game
                        STREAMERS[member.guild.id][member.id].streaming = False
                        STREAMERS[member.guild.id][member.id].msg = None

                else:
                    # Not streaming
                    STREAMERS[member.guild.id][member.id].streaming = False
                    STREAMERS[member.guild.id][member.id].msg = None

        await asyncio.sleep(120)


# This needs to be done in the twitch things module, when it's made properly
async def twitch_things(member):
    streamer = STREAMERS[member.guild.id][member.id]
    channel = discord.utils.get(member.guild.text_channels, name='striimihommia')
    embed = stream_embed(member.activity)
    if streamer.streaming == False:
        msg = await channel.send(embed=embed, delete_after=300)
        streamer.streaming = True
    else:
        msg = await streamer.msg.edit(embed=embed, delete_after=300)
    streamer.msg = msg

def stream_embed(stream):
    color = random.randint(0, 0xFFFFFF)
    embed = discord.Embed(title=f'{stream.twitch_name.capitalize()} is streaming {stream.game}',
            colour=color,
            url=stream.url,
            description=stream.name
            )

    return embed


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for guild in bot.guilds:
        streamerdict = dict()
        for member in guild.members:
            streamerdict[member.id] = Streamer(member)
        STREAMERS[guild.id] = streamerdict
    bot.loop.create_task(stream_loop())


@bot.event
async def on_member_join(member):
    STREAMERS[member.guild.id][member.id] = Streamer(member)


@bot.command()
async def list_servers(ctx):
    print(servers)

bot.run(token)
