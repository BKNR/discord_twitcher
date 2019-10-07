# Discord Twitcher

**Table of contents**

* [What is this?](#What-is-this?)
* [How to participate](#How-to-participate)
* [Specs](#Specs)

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
8. ???
9. Profit!

# Specs

This bit will have specs.
