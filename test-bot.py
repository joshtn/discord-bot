import discord
from token_info import my_token

client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("What up! bot is ready to mingle. Woop")

client.run(my_token)
