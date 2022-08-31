import discord
from keep_alive import keep_alive
from wrapper import get_meme
from random import randint
import asyncio

intent = discord.Intents.default()
intent.message_content = True
client = discord.Client(intents=intent)
reactions = ["😂", "😐", "👍", "👎"]

async def share_meme(msg):
    
    meme = get_meme()
    title = meme.title;    

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    
    color = discord.Color.from_rgb(r, g, b)
    
    embed=discord.Embed(title=title, color=color)
    embed.set_image(url = meme.url)
    
    Meme = await msg.channel.send(embed = embed)

    for reaction in reactions:
        await Meme.add_reaction(reaction)

@client.event
async def on_message(msg):
    if (msg.author == client.user):
        return

    text = msg.content
    if (text == ";getmeme"):
        await share_meme(msg)


keep_alive()
discord_task = asyncio.create_task(client.run("token"))