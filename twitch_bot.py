import foaap, jokes, urban_dictionary
import os, json, asyncio
from dotenv import load_dotenv
from os.path import join
from twitchio.ext import commands

dir_path = os.path.dirname(os.path.realpath(__file__))
dotenv_path = join(dir_path, '.env')
load_dotenv(dotenv_path)

# credentials
TMI_TOKEN = os.environ.get('TMI_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')
BOT_NAME = os.environ.get('BOT_NAME')
BOT_PREFIX = os.environ.get('BOT_PREFIX')
CHANNEL = os.environ.get('CHANNEL')

DATA = str(os.path.dirname(os.path.realpath(__file__))) + '/data.json'
with open(DATA) as file:
    channels = json.loads(file.read())["channels"]

bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NAME,
    prefix=BOT_PREFIX,
    initial_channels=[CHANNEL, *channels]
)


#services
foaap = foaap.FOAAP()
jokes = jokes.Jokes()
urb_dict = urban_dictionary.Urban_Dict()


def split_chunks(string, length=300):
    l_str = len(string)
    r = range(0, l_str-length, length)
    return [string[i: i+length] for i in r] + [string[-(l_str % length):]]


@bot.event
async def event_ready():
    """ Runs once the bot has established a connection with Twitch """
    print(f"{BOT_NAME} is online!")


@bot.event
async def event_message(message):
    """
    Runs every time a message is sent to the Twitch chat and relays it to the
    command callbacks
    """

    # the bot should not react to itself
    if message.echo:
        return

    # relay message to command callbacks
    await bot.handle_commands(message)


@bot.command(name='join')
async def join(ctx):
    with open('backup.json', 'w') as file:
        file.write(json.dumps({"channels": channels}))
    author = ctx.message.author.name
    if ctx.channel.name == BOT_NAME and ctx.message.content == "!join":
        if author in bot._ws._channel_cache:
            await ctx.send("Channel already joined!")
        else:
            await bot.join_channels([author])
            channels.append(author)
            update = json.dumps({"channels": channels})
            with open(DATA, 'w') as file:
                file.write(update)
            await ctx.send("Channel joined!")


@bot.command(name='leave')
async def leave(ctx):
    with open('backup.json', 'w') as file:
        file.write(json.dumps({"channels": channels}))
    author = ctx.message.author.name
    if ctx.channel.name == BOT_NAME and ctx.message.content == "!leave":
        if author not in bot._ws._channel_cache:
            await ctx.send("Cannot leave a channel not joined!")
        else:
            await bot.part_channels([author])
            channels.remove(author)
            update = json.dumps({"channels": channels})
            with open(DATA, 'w') as file:
                file.write(update)
            await ctx.send("Channel left!")


@bot.command(name='fo')
async def fo(ctx):
    """
    Runs when the fo command was issued in the Twitch chat and sends a
    random fuck off quote
    """

    author = ctx.author.name
    command = ctx.message.content.strip().split()
    if len(command) == 1:
        await ctx.send(foaap.fuck_off(author))
    else:
        await ctx.send(foaap.fuck_off_more(' '.join(command[1:])))

@bot.command(name='idgaf')
async def idgafuck(ctx):
    """
    Runs when the fo command was issued in the Twitch chat and sends a
    random I don't give a fuck quote
    """

    author = ctx.author.name
    await ctx.send(foaap.idgaf(author))

@bot.command(name='joke')
async def joke(ctx):
    """
    Runs when the joke command was issued in the Twitch chat and sends a
    random dad-joke/pun
    """

    text = split_chunks(jokes.random_joke())
    for chunk in text:
        await ctx.send(chunk)
        await asyncio.sleep(1.2)


@bot.command(name='ud')
async def ud(ctx):
    """
    Runs when the ud command was issued in the Twitch chat and sends a
    random urban dictionary definition or looks for one if specified
    """

    command = ctx.message.content.strip().split()
    if len(command) == 1:
        text = split_chunks(urb_dict.random_def())
    else:
        text = split_chunks(urb_dict.search(' '.join(command[1:])))
    for chunk in text:
        await ctx.send(chunk)
        await asyncio.sleep(1.2)


if __name__ == "__main__":
    # launch bot
    bot.run()
