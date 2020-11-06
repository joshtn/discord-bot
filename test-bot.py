import discord
import time
from token_info import my_token
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot online..')


@bot.event
async def on_raw_reaction_add(payload):
    print(f"hello {payload.emoji.name}")


@bot.event
async def on_reaction_remove(reaction, user):
    print(f"{user.display_name} removed reaction {reaction.emoji.name}")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def pom(ctx, minutes):
    try:
        t = int(minutes) * 60
        if t <= 0:
            await ctx.send('Negative number not accepted!')
            print("neg num")
            raise BaseException

        message = await ctx.send(f'Timer: {t}')
        await message.add_reaction('❌')

        while True:
            mins = t // 60
            secs = t % 60
            if t == 0:
                await message.edit(content='🍅 COMPLETE!')
                break

            await message.edit(content='🍅 {:02d}:{:02d}'.format(mins, secs))
            time.sleep(1)
            t -= 1

        await ctx.send(f'{ctx.author.mention}, BRR countdown finished!')
    except ValueError:
        await ctx.send('You must enter a number!')


bot.run(my_token)
