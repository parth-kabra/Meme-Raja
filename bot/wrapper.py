from praw import Reddit
from random import choice

client_id = "XXX"
client_secret = "XXX"
user_agent = "XXX"

valid_extensions = [".gif", ".png", ".jpg"]

reddit = Reddit(
    client_id = client_id,
    client_secret = client_secret,
    user_agent = user_agent
)

subreddit = reddit.subreddit("dankmemes").hot(limit = 1000)

memes = list()

for meme in subreddit:
    url = meme.url
    extension = url[url.rfind('.'):].lower()
    if extension not in valid_extensions:
        continue
    memes.append(meme)

def get_meme():
    meme = choice(memes)
    return meme
