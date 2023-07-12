import discord
import os
import requests
import json
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

predictions = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definetly.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

def get_prediction():
    return(predictions[random.randrange(0,20)])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$magic8':
        print('We have recieved a request for a prediction')
        predict = get_prediction()
        await message.channel.send(predict)

client.run(TOKEN)