import discord
import asyncio
from token_info import my_token
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot online..')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def pom(ctx, seconds):
    try:
        second = int(seconds) * 60
        if second <= 0:
            await ctx.send('Negative number not accepted!')
            print("neg num")
            raise BaseException

        message = await ctx.send(f'Timer: {second}')

        while True:
            second -= 1
            if second == 0:
                await message.edit(content='Ended!')
                break

            await message.edit(content=f'Timer: {second}')
            await asyncio.sleep(1)

        await ctx.send(f'{ctx.author.mention}, Brrr countdown ended!')
    except ValueError:
        await ctx.send('You must enter a number!')


bot.run(my_token)
