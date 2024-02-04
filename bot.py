from genericpath import exists
import discord
import json
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

configData = {}

if os.path.exists(os.getcwd()+"/config.json"):
    with open("./config.json", "r+") as file:
        configData = json.load(file)
#else:
#    configTemplate = {"Token":"", "Prefix":"!"}
#    with open(os.getcwd()+"/config.json", "w+") as file    :
#        json.dump(configTemplate, file)

TOKEN = configData["Token"]
PREFIX = configData["Prefix"]

client = MyClient(intents=intents)
client.run(TOKEN)
