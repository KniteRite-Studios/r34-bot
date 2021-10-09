import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

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
     await message.channel.send('https://th.bing.com/th/id/OIP.gCTsc0R3s9lwBsiyktkhgAAAAA?w=156&h=159&c=7&r=0&o=5&dpr=1.88&pid=1.7')
  
 

  if message.author == client.user:
    return

  if message.content.startswith('$embed'):
   embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
  embedVar.add_field(name="Field1", value="hi", inline=False)
  embedVar.add_field(name="Field2", value="hi2", inline=False)
  await message.channel.send(embed=embedVar)
client.run("ODk1Nzg1MzE3OTM4OTAxMDkz.YV9nFg.DvP-gR2DALs6f0UjXbnB2kb9QT0")