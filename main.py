import discord

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('DM For Support'))
    print("Bot is ready!")

@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("**"+ message.author.display_name + "** : ")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("**"+ message.author.display_name + "** : " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("**"+ message.author.display_name + "** : ")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("**" + message.author.display_name + "** : " + mod_message)


client.run('NzkzMzcxMzkyMzcxOTgyMzY2.X-rSsA.jEs2kF_U503glmhW4rsHNAumMt8')