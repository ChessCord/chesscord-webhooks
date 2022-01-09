import discord
import asyncio

client = discord.Bot(command_prefix="c-w!", intents=discord.Intents().all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="new webhooks..."))
    print("Bot is ready")

def send_msg(content, embed):
    channel = client.get_channel(928901869772873788)
    asyncio.run(channel.send(content, embed=embed))
