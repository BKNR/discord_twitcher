# Discord Twitcher

**Table of contents**

* [What is this?](#What-is-this?)
* [How to participate](#How-to-participate)
* [Specs](#Specs)
* [How to add your changes](#How-to-add-your-changes)

## What is this?

This repository will be the home for the collaborative effort of Finnish Tekken scene to make a discord bot.
The goal is to make bot that shows Finnish Tekken streams that are currently live on twitch, on a specified
channel on the Discord server. Optimally the result will be a more general purpose bot, that can be used to 
show the streams for any specific game or games with tags narrowing it down. 

## How to participate

The collaboration platform, as you notice, is GitHub. If you're unfamiliar with Git and/or GitHub, I suggest you start with 
[this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and the following few pages.
The bot will be made using Python 3, [Discord.py framework](https://discordpy.readthedocs.io/en/latest/),
[Requests library](https://requests.readthedocs.io/en/master/) and [New Twitch API ("helix")](https://dev.twitch.tv/docs/api). 
The easiest way for you to have the environment necessary to participate is as follows:

1. Have a Linux machine, a macOS machine, a Windows 10 machine using [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
or a shell on a Linux machine, and be able to install software on whichever option you go with. You don't 
need root or sudo rights if your machine has the required things to build Python (https://github.com/pyenv/pyenv/wiki#suggested-build-environment). 
It might be possible to do the subsequent steps, or similar ones on purely a Windows machine, but these 
directions will not cover that (as I don't know how it's done).
2. Install [pyenv](https://github.com/pyenv/pyenv) according to the directions.
3. Install Python 3.7.4 with pyenv: ``pyenv install 3.7.4``
4. Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) according to the directions. I suggest you do the optional
step 2 as well.
5. Create a new virtual environment that uses Python 3.7.4 called dt374: ``pyenv virtualenv 3.7.4 dt374``
6. Clone this repository with ``git clone http://github.com/BKNR/discord_twitcher.git``. It has a file that automatically 
activates the virtual environment that you just made, when you navigate into the repository directory, and also
the file you need for the next step.
7. Navigate into the repo you just cloned with ``cd discord_twitcher`` and install the required python packages
with ``pip install -r requirements.txt``
8. You should register your app with Twitch (https://dev.twitch.tv/docs/api) and register as developer and make 
your own bot on Discord (https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) 
and make a discord server so that you can experiment for yourself
9. ???
10. Profit!

## Specs

I will outline some of the specs here:
* The project should have at least two python files, with one having the main bot functionalities and the 
other interfacing the twitch api. 
* The configuration of the bot should be handled as chat commands rather than be hard coded.
* Only certain people should be able to give configuration commands for the bot.
* There should be a specific channel for the bot to post in, and post nowhere else.
* The bot should be at minimum be told what game's streams to post (Tekken's game_id is 461067). Should be possible
to add multiple games.
* It should be able to narrow the amount of streams for the bot to post with tags (for the tag 'Finnish' the
tag_id is 220eb274-ab25-425b-8a9b-826103404997)
* There should be a possibility add specific streamers for the bot, and for them to ignore the tag requirements.
* All these settings should be saved somewhere.
* It should be possible to turn these settings off as well as on. You should also be able to see a list of current
settings.
* The bot should have a help command to show the possible commands.
* For these streams to be posted in discord, there should be a discord embed with info given as a response for the
Twitch API query: the stream title, the streamer's name (as a link to click to get into the stream), the stream
thumbnail, The game name, the number of viewers and either the stream starting time or the uptime.

## How to add your changes

Changes will be made as pull requests, here's how: https://help.github.com/en/articles/creating-a-pull-request
