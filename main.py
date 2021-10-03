import json
import discord
import asyncio

with open('config.json', 'r') as config:
    get = json.load(config)
token = get['token']
client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f"GroupChannel leaver is now activating on {client.user} ...")
    await asyncio.sleep(2)
    for gc in client.private_channels:
        if isinstance(gc, discord.GroupChannel):
            try:
                await gc.leave()
                print(f'Successfull: {gc.name}')
            except:
                print(f'Failed: {gc.name}')
    print(f"GroupChannel leaver has finished!")

client.run(token, bot=False)
