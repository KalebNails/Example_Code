#!/usr/bin/env python
#Kaleb Nails
#pip3 install metpy
#pip3 install dask
#pip3 install discord

import subprocess
import discord

intents = discord.Intents.all()
# This sets up a default set of intents
#reading messages is not default
client = discord.Client(intents=intents)


#this prints on bot boot up
@client.event
async def on_ready():
    print('Bot is online and ready')



@client.event
async def on_message(message):

    #This is very important and keeps the bot from infinately replying to its own messages
    if message.author == client.user:
        #print('my own message')
        return

    #This checks to see if a user asks for an IP adress
    if message.channel.name == 'whats-the-ip':# and message.content == 'ip?':
        print('correct channel')
        print('the message is: {}'.format(message.content))

#METO COMMAND
        if message.content.lower() == 'meto':#'ip?':
            try:
                python_script_path = 'discord_meteogram.py'
                await message.channel.send("Generating")
                subprocess.run(['python',python_script_path])
                #I am so very dyslexic, it took me like 10 minutes to figure out i swapped / for \ and i even specifically checked if i did

                #embed = discord.Embed(title="GRAPHS")
                #embed.set_image(url='attachment://{meteogram_image.png}')

                await message.channel.send( file=discord.File('meteogram_image.png'))
                #await message.channel.send(embed=embed, file=discord.File('meteogram_image.png'))
                #await message.channel.send( file=discord.File('meteogram_image.png'))

            except Exception as e:
                await message.channel.send(f"An error has occurred: {str(e)}")

#HELP COMMAND
        if message.content.lower() == 'help':#'ip?':
            try:
                await message.channel.send("LIST OF COMMANDS (case insensitive):\nmeto: produces a meteogram graph of today\nifconfig: will print out the contents of ifconfig from the Linux terminal\ntraceroute: will traceroute and give the bubble IP")

            except Exception as e:
                await message.channel.send(f"An error has occurred: {str(e)}")


client.run('YOURCODE')
