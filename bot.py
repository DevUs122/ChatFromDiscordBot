# pip install nextcord
import nextcord
from nextcord.ext import commands
import os
import time


print("MUST HAVE TURNED ALL THE INTENTS ON IN THE BOT SETTINGS")
time.sleep(1)
print("To do that go to : https://discord.com/developers/applications/")
intents = nextcord.Intents.all()
intents.members = True

token = input("What's your bot's token? [You can check our code that we **DO NOT** store discord bot token] : ")
prefix = input("Bot prefix? : ")
bot_status = input("What should be the bot's status? : ")
print("After the bot is online, do the command, prefixdo_that, [EG: !do_that, $do_that]")

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
  print("Your bot is online")
  await client.change_presence(activity=nextcord.Game(name=bot_status))

@client.command()
async def send_message(ctx):
    message = input("What's the message that you want to send? : ")
    await ctx.send(message)


client.run(token)
