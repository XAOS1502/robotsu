import discord
from discord.ext import commands

import asyncio
import random

description = "Robotsu alpha, coded in Python3 and released by XΛOS and Lin² for Discord"
bot_prefix = ['Robotsu ', 'robotsu ', '_']
bot = commands.Bot(command_prefix=commands.when_mentioned_or("Robotsu ", "robotsu ", "_"), description=description)
#bot.remove_command('help')
#make sure to remove help after having created one
bot.load_extension("cogs.dere")
#loads the file <mycog> from the folder <cogs>

@bot.event
async def on_ready():
    print(discord.__version__)
    print('     ε=ε=ε=ε=┏(;^o^)┛')
    print('誰かがこれを読んでいますか？')
    print('ロボつ²ト名 : {} alpha' .format(bot.user.name))
    print('クライアント ID : {}' .format(bot.user.id))
    print('ロボつ²トバージョン : 0.3 「2017年 7月 21日」')
    print('         ------')
    print('クリエイター :「XΛOS」#1502')
    print('ロボつ²トがオンラインになりました 。。。')
    print(' ')
    print('    (∩｀-´)⊃━☆ﾟ.*･｡ﾟ      「魔法の解放!」')
    print(' ')
    print('-> ロードコア')
    print('--> ロボつ²ト同期が完了しました')
    print('---> ロボつ²トモード起動')
    await bot.change_presence(game=discord.Game(name='type _ball'))

#================================
# Reaction Poll
#================================
@bot.command(aliases = ['ask', 'drawstraw'], name="poll", pass_context=True, description='Robotsu helps you ask other members, write :\nrobotsu poll <question or idea>')
async def poll(ctx):
        await bot.add_reaction(ctx.message, '👍')
        await bot.add_reaction(ctx.message, '👎')
        await bot.add_reaction(ctx.message, '🤷')

#================================
# Picks between multiple choices
#================================
@bot.command(aliases = ['choose', 'select'], description='Robotsu helps you choose between two or more things, separate them with a space')
async def pick(*choices : str):
    await bot.say(random.choice(choices))

#================================
# SUPER BASIC calculator
#================================
@bot.command(aliases = ['+', 'sum', 'addition'], description='Robotsu alpha can add two numbers separated by space')
async def add(left : int, right : int):#Adds two consecutive numbers
    await bot.say(left + right)

@bot.command(aliases = ['-', 'rest', 'subs'], description='Robotsu alpha can substract two numbers separated by space')
async def substract(left : int, right : int):#Substracts two consecutive numbers
    await bot.say(left - right)

@bot.command(aliases = ['*', 'x', 'multiplicate'], description='Robotsu alpha can multiply two numbers separated by space')
async def multiply(left : int, right : int):#Multiplies two consecutive numbers
    await bot.say(left * right)

@bot.command(aliases = ['/', 'into'], description='Robotsu alpha can divide two numbers separated by space')
async def divide(left : int, right : int):#Divides two consecutive numbers
    await bot.say(left / right)

#================================
# SERVER MANAGE
#================================
@bot.command(pass_context=True, name="mute", description="Robotsu helps to mute users without kicking or banning them")
async def mute(ctx, member: discord.Member):
    """Mutes the mentioned member in this channel."""
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await asyncio.sleep(1)

@bot.command(pass_context=True, name="kick", description="Robotsu can kick a member, they'll be able to join with an invite")
async def kick(ctx, user: discord.Member = None):
    """Kicks the mentioned member from the server."""
    if ctx.message.author.server_permissions.kick_members == True:
        if user != None:
            embed = discord.Embed(colour=0x5de316)
            embed.add_field(name="­",
                            value="{} has kicked {} for {}".format(ctx.message.author.mention, user.mention, reason))
            await bot.say(embed=embed)
            await bot.kick(user)
        else:
            embed = discord.Embed(title="You need to specify user first", value="­", colour=0x5de316)
            await bot.say(embed=embed)
    else:
        await bot.say("You don't have permissions to kick anybody, try `kickme` command instead.")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member=None):
    if ctx.message.author.server_permissions.ban_members==True:
        await bot.ban(user)
    else:
        await bot.say("You have no permission to ban any users")

#================================
# TESTING RANDOM COMMANDS
#================================
@bot.command(aliases = ['seem', 'is'], pass_context=True, name='seems', description='Robotsu alpha is cute and adorable')
async def seems(ctx):
    await bot.say("Robotsu is cute")

#========== bot commands extra labels
@bot.command(pass_context=True, name='8ball', description='Robotsu alpha does not do 8balls')
async def ball(ctx):
    await bot.say("robotsu don't have 8ball, try `robotsu prediction`")

@bot.command(aliases = ['fortune', 'predict', 'astrobotsu'], pass_context=True, name='prediction', description='Robotsu alpha will include future prediction forecast for your questions')
async def prediction(ctx):
    await bot.say("```Hello there,\nmy Dev XAOS is working hard to bring PREDICTION to you\nso you can enjoy asking questions about your future,\nthank you for your patience.```")
#========== End of bot commands


#================================
# WELCOME AND FAREWELL MESSAGES
#================================
@bot.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    server = member.server
    count = len(server.members)
    msg = "**Welcome __{0}__ to {1}. We now have `{2}` members.**".format(member.mention, server, count)
    await bot.say(serverchannel, msg)

@bot.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    server = member.server
    count = len(server.members)
    msg = "**And now, {0}'s watch has ended.\nHold the door, Hodor.\nWe are left with {1} members in {2}**.".format(member.mention, count, server)
    await bot.say(serverchannel, msg)

#================ Says when a member joined
@bot.command(description="Robotsu finds out when a member joined the Discord guild")
async def joindate(member : discord.Member):
    await bot.say("{0.name} joined in {0.joined_at}".format(member))


#===== Beginning of secret token
bot.run('token')
#===== End of secret token
