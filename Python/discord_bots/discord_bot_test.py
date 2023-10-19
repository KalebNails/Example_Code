#Kaleb Nails

import subprocess
import discord

intents = discord.Intents.all()  # This sets up a default set of intents
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


        if message.content.lower() == 'ifconfig':#'ip?':
            try:
                ipconfig_txt = str(subprocess.getstatusoutput(f'ifconfig'))
                #I am so very dyslexic, it took me like 10 minutes to figure out i swapped / for \ and i even specifically checked if i did
                ipconfig_txt = ipconfig_txt.replace(r'\n','\n')
                await message.channel.send(ipconfig_txt)

            except Exception as e:
                await message.channel.send(f"An error has occurred: {str(e)}")



        if message.content.lower() == 'traceroute':#'ip?':
            try:
                ipconfig_txt = str(subprocess.getstatusoutput(f'traceroute 1.2.3.4')) #This is for when you have a router in a subnet with a port foward, you can traceroute to a static IP in the network to see the routers IP
                #I am so very dyslexic, it took me like 10 minutes to figure out i swapped / for \ and i even specifically checked if i did
                ipconfig_txt = ipconfig_txt.replace(r'\n','\n')
                await message.channel.send(ipconfig_txt)

            except Exception as e:
                await message.channel.send(f"An error has occurred: {str(e)}")


client.run('YOUR AUTH CODE')
