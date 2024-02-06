from genericpath import exists
import discord
import json
import os
import comms

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} on duty!')

    async def on_message(self, msg):
        print(f'Message from {msg.author}: {msg.content}')
        if msg.content.startswith(PREFIX):
            await comms.commHandler(msg)
        
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
