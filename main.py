import discord
import time
import requests
client = discord.Client()

client.run("Token")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


url = "https://rule34.xxx/index.php?page=post&s=list&tags=user%3akniterite+spunow_+"

r = requests.get(url)
with open('responsecompare.txt', 'w') as file:
    file.write(r.text)
time.sleep(30)

f1 = open("response.txt", "r")
f2 = open("responsecompare.txt", "r")

i = 115
for line1 in f1:
    i += 1

    for line2 in f2:

        # matching line1 from both files
        if line1 == line2:
            # print IDENTICAL if similar
            print("Line ", i, ": IDENTICAL")
        else:
            r = requests.get(url)
        with open('response.txt', 'w') as file:
            file.write(r.text)
            embedVar = discord.Embed(title="Title",
                                     description="Desc",
                                     color=0x00ff00)
    embedVar.add_field(
        name="Field1",
        value=
        "A new Rule34 Spunow Post has been uploaded! (or there was a server crash and my bot broke lol)",
        inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    embedVar.set_thumbnail(url="https://rule34.xxx/images/header3c.png")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('Test Recieved. Command Works!')

    if message.author == client.user:
        return

    if message.content.startswith('$image'):
        await message.channel.send(
            'https://th.bing.com/th/id/OIP.gCTsc0R3s9lwBsiyktkhgAAAAA?w=156&h=159&c=7&r=0&o=5&dpr=1.88&pid=1.7'
        )

    if message.author == client.user:
        return

    if message.content.startswith('$embed'):
        embedVar = discord.Embed(title="Title",
                                 description="Desc",
                                 color=0x00ff00)
        embedVar.add_field(name="Field1", value="Embed Test)", inline=False)
        embedVar.add_field(name="Field2",
                           value="Bot made by KniteRite Studios",
                           inline=False)
    await message.channel.send(embed=embedVar)

    if message.author == client.user:
        return

    if message.content.startswith('$about'):
        await message.channel.send(
            'Rule34 Update Bot made by KniteRite Studios. Posts when spunow uploads on rule34!'
        )
