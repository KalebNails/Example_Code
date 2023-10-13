#Kaleb Nails
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

        if message.content == 'ip?':

            try:
                # Try to open and read the content of the file
                with open('Dummy_ip.txt', 'r') as file:
                    file_content = file.read()
                await message.channel.send(file_content)

            except FileNotFoundError:
                # If the file is not found, send an error message
                await message.channel.send("An error has occurred. 'Dummy_ip.txt' is not available.")
                
            except Exception as e:
                await message.channel.send(f"An error has occurred: {str(e)}")


client.run('YOUR AUTH CODE')
