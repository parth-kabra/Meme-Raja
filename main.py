import discord
import requests
import random
from dotenv import load_dotenv
import os
from app import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

subreddits = [
    "IndianMeyMeys", 
    "programmingmemes", 
    "IndianDankMemes"
]

def get_random_meme():
    subreddit = random.choice(subreddits)
    url = f"https://www.reddit.com/r/{subreddit}/random.json"
    headers = {"User-Agent": "Discord Bot"}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    url = json_data[0]["data"]["children"][0]["data"]["url"]
    if is_image_url(url):
        return [url, subreddit]
    else:
        return get_random_meme()

def is_image_url(url):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    return any(url.endswith(ext) for ext in image_extensions)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if(message.content == "!meme"):
        meme = get_random_meme()
        em = discord.Embed(
            title=f"Meme from {meme[1]}",
            color=0xff0000,
            description="The purpose of sharing this meme is solely for entertainment and it is not intended to hurt anyone's feelings in any way. Please do not take offense."
        )
        em.set_image(url = meme[0])
        await message.channel.send(embed = em)

keep_alive()
client.run(os.environ.get("KEY"))
#मीम राजा