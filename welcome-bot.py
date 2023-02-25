#import
import discord
from discord.ext import commands
import colour
import json
#intents
intents = discord.Intents.all()
intents.message_content

# loading our config file
with open("config.json", "r", encoding='utf-8') as data:
    config = json.load(data)


client=commands.Bot(command_prefix=config["PREFIX"] ,intents = intents)


#on_ready
@client.event
async def on_ready():
    print(f"bot is online")


@client.event
async def on_member_join(member: discord.Member):
    try:
        channel = client.get_channel(config["ID_WELCOME_CHANNLE"])
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url=member.display_avatar)
            embed.add_field(name="Welcome" ,value=f"**Hi,{member.mention} Welcome to {member.guild.name}\n Thanks for join**", inline=False)
            embed.set_thumbnail(url=member.display_avatar)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

@client.event
async def on_member_remove(member : discord.Member):
    try:
        channel = client.get_channel(config["ID_LEAVE_CHANNLE"])
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url=member.display_avatar)
            embed.add_field(name="Good Bye", value=f"**{member.mention} left us.**", inline=False)
            embed.set_thumbnail(url=member.display_avatar)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

client.run(config["TOKEN"])

#code by ahmad_carabit
