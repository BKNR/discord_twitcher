#!/usr/bin/env python3

import os, sys
import asyncio

import discord
from discord.ext import commands

#This file will have the discord bot functions. Look at discord.py documentation

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
                print(user.activities)
        await asyncio.sleep(1)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for server in bot.guilds:
        servers.append(server.id)

@bot.command()
async def list_servers(ctx):
    print(servers)

bot.loop.create_task(print_users())
bot.run(token)
