import time
import discord
start_time = time.time()
from discord.ext import commands

description = "Robotsu, Discord bot coded in Python by XΛOS and Lin²"
bot_prefix = ['Robotsu ', 'robotsu ', '_', '?tag ']
bot = commands.Bot(command_prefix=commands.when_mentioned_or("Robotsu ", "robotsu ", "_", "?tag "), description=description)
bot.remove_command('help')# ================ Because the help got too long

# ================ cogs that are used
bot.load_extension("cogs.interactive")
bot.load_extension("cogs.misc")
bot.load_extension("cogs.funtimes")
bot.load_extension("cogs.misc")
bot.load_extension("cogs.prediction")
bot.load_extension("cogs.administrative")
bot.load_extension("cogs.extracommands")
bot.load_extension("cogs.mods")
bot.load_extension("cogs.ayuda")
bot.load_extension("cogs.dere")

@bot.event
async def on_ready():# ================ Does anybody read these?
    print(discord.__version__)
    print('     ε=ε=ε=ε=┏(;^o^)┛')
    print('誰かがこれを読んでいますか？')
    print('ロボつ²ト名 : {} alpha'.format(bot.user.name))
    print('クライアント ID : {}'.format(bot.user.id))
    print('ロボつ²トバージョン : 0.6 「2017年 8月 21日」')
    print('クリエイター :「XΛOS」#1502')
    print('ロボつ²トがオンラインになりました 。。。')
    print(' ')
    print('    (∩｀-´)⊃━☆ﾟ.*･｡ﾟ      「魔法の解放!」')
    print(' ')
    print('-> ロードコア')
    print('--> ロボつ²ト同期が完了しました')
    print('---> ロボつ²トモード起動')
    await bot.change_presence(game=discord.Game(type=0, name='with light'))
    with open("logs/restart.txt", "a") as file:# ================ Useful, or not
        file.write("\nRobotsu is very sorry he had to restart")

# ================================
# SERVER MANAGE COMMANDS
# ================================
@bot.command(pass_context=True, hidden=True)
async def mute(ctx, user):
    """Command to mute a user without kicking"""
    text_overwrite = discord.PermissionOverwrite()
    text_overwrite.send_messages = False
    voice_overwrite = discord.PermissionOverwrite()
    voice_overwrite.speak = False
    for channel in ctx.message.server.channels:
        if channel.type == discord.ChannelType.text:
            await bot.edit_channel_permissions(channel, user, text_overwrite)
        elif channel.type == discord.ChannelType.voice:
            await bot.edit_channel_permissions(channel, user, voice_overwrite)
        else:
            continue

@bot.command(pass_context=True, hidden=True)
async def unmute(self, ctx, user:discord.Member=None):
    """Command to mute a user without kicking"""
    text_overwrite = discord.PermissionOverwrite()
    text_overwrite.send_messages = True
    voice_overwrite = discord.PermissionOverwrite()
    voice_overwrite.speak = True
    for channel in ctx.message.server.channels:
        if channel.type == discord.ChannelType.text:
            await bot.edit_channel_permissions(channel, user, text_overwrite)
        elif channel.type == discord.ChannelType.voice:
            await bot.edit_channel_permissions(channel, user, voice_overwrite)
        else:
            continue

@bot.command(pass_context=True, name="kick", hidden=True, description="Robotsu can kick a member, they'll be able to join with an invite")
async def kick(ctx, user: discord.Member = None):
    """Kicks the mentioned member from the server."""
    if ctx.message.author.server_permissions.kick_members == True:
        if user != None:
            embed = discord.Embed(colour=0x5de316)
            embed.add_field(name="­", value="{0} has kicked {1} for {2}".format(ctx.message.author.mention, user.mention, reason))
            await bot.say(embed=embed)
            await bot.kick(user)
        else:
            embed = discord.Embed(title="You need to specify user first", value="­", colour=0x5de316)
            await bot.say(embed=embed)
    else:
        await bot.say("You don't have permissions to kick anybody, try `kickme` command instead.")

@bot.command(pass_context=True, hidden=True)
async def ban(ctx, user: discord.Member = None):
    """Very self explanatory"""
    if ctx.message.author.server_permissions.ban_members == True:
        await bot.ban(user)
    else:
        await bot.say("You have no permission to ban any users")

# ================================
# WELCOME AND FAREWELL MESSAGES
# ================================
@bot.event
async def on_member_join(member):
    serverchannel = member.server.default_channel# ================ It goes into the first General channel
    server = member.server
    count = len(server.members)
    msg = "**Welcome __{0}__ to {1}. We now have `{2}` members.**".format(member.mention, server, count)
    await bot.send_message(serverchannel, msg)

@bot.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel# ================ It goes into the first General channel
    server = member.server
    count = len(server.members)
    msg = "**And now, {0}'s watch has ended.\nHold the door, Hodor.\nWe are left with {1} members in {2}**.".format(
        member.mention, count, server)
    await bot.send_message(serverchannel, msg)

# ================ Says when a member joined
@bot.command(hidden=True, description="Robotsu finds out when a member joined the Discord guild")
async def joindate(member: discord.Member):
    await bot.say("{0.name} joined in {0.joined_at}".format(member))

# ================ Because it is good to remember who helped
@bot.command(pass_context=True, name="credits", description="Robotsu alpha is brought to you because of the following support")
async def credits(ctx):
    embed = discord.Embed(title="Robotsu Beta version 0.6 - Credits", colour=discord.Colour(0x2196f3), description="**ロボつ²** is the first Bot made by 「XΛOS」#1502, but it has grown from **alpha stage** to **beta** with the support and guidance of many expert individuals.")
    embed.add_field(name="Thanks to:", value="Maximilian\nMiguel F\nZey\nMei\nTyler\nLesbisch™\nLin Lin\nAndrija", inline=True)
    embed.add_field(name=":small_orange_diamond:", value="**Irae/Clockwork#9860\nAnthsoul#6929\nzeyla#5479\nmei#5429\nTrain#1115\nLesbisch#8111\nLin²#5427**\nRetardedKid#2405", inline=True)
    await bot.say(embed=embed)

# ================ Simple command to rend notes to self
@bot.event
async def on_message(message):
    if message.content.startswith.lower()("note to self"):
        await bot.say('Note sent in a DM!')
        await bot.send_message(message.author, message.content.replace('note to self ', ''))
    await bot.process_commands(message)

# ================ Want to have a message in Embed?
@bot.command(pass_context=True, name="embed")
async def embed(ctx, *, message:str):
    """Command for Embedding your text
    it deletes your original message
    and quotes your name"""
    try:
        await bot.delete_message(ctx.message)
    except:
        pass
    embed = discord.Embed(title="{0} wrote:".format(ctx.message.author.display_name), colour=discord.Colour(0x2a6e81), description="{0}".format(message))
    await bot.say(embed=embed)

# ================================
# MESSAGE ON COMMAND ERROR
# ================================
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.DisabledCommand):
        await bot.send_message(ctx.message.channel, "This command has been disabled")
        return
    if isinstance(error, checks.dev_only):
        await bot.send_message(ctx.message.channel, "This command can only be ran by the bot developers")
        return
    if isinstance(error, checks.owner_only):
        await bot.send_message(ctx.message.channel, "This command can only be ran by the bot owner")
        return
    if isinstance(error, checks.not_nsfw_channel):
        await bot.send_message(ctx.message.channel, "This command can only be ran in NSFW enabled channels. It must either be named `nsfw` or the name must start with `nsfw-`")
        return
    if isinstance(error, checks.not_server_owner):
        await bot.send_message(ctx.message.channel, "Only the server owner (`{}`) can use this command".format(ctx.message.server.owner))
        return
    if isinstance(error, checks.no_permission):
        await bot.send_message(ctx.message.channel, "You do not have permission to use this command".format(ctx.message.server.owner))
        return
    if ctx.message.channel.is_private:
        await bot.send_message(ctx.message.channel, "An error occured while trying to run this command, this is most likely because it was ran in a private message channel. Please try running this command on a server.")
        return

    # In case the bot failed to send a message to the channel, the try except pass statement is to prevent another error
    try:
        await bot.send_message(ctx.message.channel, error)
    except:
        pass
    log.error("An error occured while executing the {} command: {}".format(ctx.command.qualified_name, error))

#===== Token
bot.run('TOKEN_GOES_HERE_BUT_DO_NOT_SHARE_IT')
