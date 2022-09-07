const { Client, GatewayIntentBits, EmbedBuilder,ActivityType } = require("discord.js")
const fetch = require("node-fetch")
const keepAlive = require("./server")

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMessageReactions,
    ]
})

const subreddits = [
    "https://meme-api.herokuapp.com/gimme/dankindianmemes",
    "https://meme-api.herokuapp.com/gimme/memes",
    "https://meme-api.herokuapp.com/gimme/dankmemes",
    "https://meme-api.herokuapp.com/gimme/cursedindiancomments",
]

const reactions = ["😂", "😐", "👍", "👎"]

async function get_data() {
    const subreddit = subreddits[Math.floor(Math.random() * subreddits.length)]
    let data = await fetch(subreddit)
    let Meme = await data.json()
    while (Meme.nsfw) {
        data = await fetch(subreddit)
        Meme = await data.json()
    }
    return Meme
}

async function get_meme() {
    const data = await get_data()
    const color = '#' + (Math.random() * 0xFFFFFF << 0).toString(16);
    const embed = new EmbedBuilder()
        .setColor(color)
        .setTitle(data.title)
        .setImage(data.url)
        .setFooter({
            text: "The meme was shared solely for entertainment purposes."
        })
    return embed
}


client.on("ready", () => {
    client.user.setPresence({
      activities: [{ name: "parth kabra orz", type: ActivityType.Playing }]
    });
})

client.on("messageCreate", async (msg) => {

    if (msg.author.username == client.user.username) {
        return
    }

    const text = msg.content.toLowerCase()

    if (text === ";getmeme") {

        const meme = await get_meme()
        await msg.channel.send({
            embeds: [meme]
        }).then((message) => {

            reactions.forEach((reaction) => {
                message.react(reaction)
            })

        }).catch(async () => {

            await msg.channel.send("```yaml\nThe request failed due to an error. Please try again.```")

        })
    }

})

keepAlive()
client.login(process.env["TOKEN"])