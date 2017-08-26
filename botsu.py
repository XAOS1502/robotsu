import datetime
import time  # =================================== for the ping! to work
import discord  # ================================ because this bot is meant to run on? air? no, Discord
import asyncio
start_time = time.time()  # ====================== something else for the ping!
from discord.ext import commands  # ============== without this, most commands will not work, try it out
# ============================================== you have to import these if you want bot to work, just do it

description = "Robotsu, Discord bot coded by XΛOS <@!323578534763298816> and Lin² <@!324040201225633794>"  # === This was at the top of help
bot_prefix = ['Robotsu ', 'robotsu ', '_']  # ==== notice the next line, it also works with mention
bot = commands.Bot(command_prefix=commands.when_mentioned_or("Robotsu ", "robotsu ", "_"), description=description)
bot.remove_command('help')  # ==================== Because the help got too long

# ================ cogs that are used, 
# and the reason the help is so long
# also, they serve to organise the
# commands and know where things are...
# EDIT: I might change some of them
# ================ 
bot.load_extension("cogs.interactive")  # ======== commands that work w/o mention to say something to a member with Kaomoji
bot.load_extension("cogs.misc")  # =============== numbers, pseudo-calc, urban, choices
bot.load_extension("cogs.funtimes")  # =========== commands rigged af! don't take the results too seriously
bot.load_extension("cogs.prediction")  # ========= drop the 8ball, these predictions are scary-accurate, or not
bot.load_extension("cogs.administrative")  # ===== a good way to remind f*ktards the 10 rules of the server
bot.load_extension("cogs.extracommands")  # ====== commands from other botos, not sure why people like these...
bot.load_extension("cogs.mods")  # =============== useful commands for Moderators, not sure what to write there though
bot.load_extension("cogs.ayuda")  # ============== since help got so effin big, I divided them into categories with Embeds
bot.load_extension("cogs.dere")  # =============== another request from a friend, to have ALL the deredere types

@bot.event
async def on_ready():  # =========================================== Does anybody ever read these?
    print(discord.__version__)  # ================================== version, just so you remember what you installed
    print('     ε=ε=ε=ε=┏(;^o^)┛')  # ============================== RUN DOS, RUN
    print('誰かがこれを読んでいますか？')  # ============================ Not sure what it says, or if it is even correct
    print('ロボつ²ト名 : {} alpha'.format(bot.user.name))  # ========= gets the name from the API
    print('クライアント ID : {}'.format(bot.user.id))  # ============== gets the bot user ID
    print('ロボつ²トバージョン : 0.6 「2017年 8月 21日」')  # ============ I keep updating the date, when I remember to do it
    print('クリエイター :「XΛOS」#1502')  # ============================ the person behind the code
    print('ロボつ²トがオンラインになりました 。。。')  # ================== more random stuff
    print(' ')  # =================================================== silence, because we all need some
    print('    (∩｀-´)⊃━☆ﾟ.*･｡ﾟ      「魔法の解放!」')  # ============== let the magick begin
    print(' ')  # =================================================== space, because we all need some
    print('-> ロードコア')# ========================================= something else
    print('--> ロボつ²ト同期が完了しました')  # ========================== some more else
    print('---> ロボつ²トモード起動')  # ================================ and last else
    await bot.change_presence(game=discord.Game(type=0, name='with light'))  # ====>Shows as Playing with light
    with open("logs/restart.txt", "a") as file:  # ================ Useful, or not. I like to keep count of restarts
        file.write("\nRobotsu is very sorry he had to restart")  # ================ and he should be

# ================================================================
# ================= SERVER MANAGER COMMANDS
# ================================================================
@bot.command(pass_context=True)  # ================================= required shit, won't work without it, just don't ask
async def mute(ctx, user: discord.Member=None, reason: str=None):  # ==== here's the stuff needed for the command to work
    """Command to mute a user, needs a reason  # =================== rip help description
    Example: Robotsu mute @member_name for NSFW images"""  # ======= this command requires a reason after mention
    text_overwrite = discord.PermissionOverwrite()  # ============== Ok, so, there's no need to remove roles, just overwrite perms
    text_overwrite.send_messages = False  # ======================== this is magick! well, not really
    for channel in ctx.message.server.channels:  # ================= they won't be able to write
        if ctx.message.author.server_permissions.manage_server:# = only for Mods or Admins, so other people cannot mute everyone else
            await bot.edit_channel_permissions(channel, user, text_overwrite)# ==== the action takes place, sparks fly everywhere
            embed = discord.Embed(title="\N{ZIPPER-MOUTH FACE} Mute Successful", colour=discord.Colour(0xc0329b),
                                  description=f"**{ctx.message.author.display_name}** has muted **{user}**\nReason: *{reason}*")
        else:  # ==================================================== for everyone who isn't Mod or Admin
            embed = discord.Embed(title="Mute Unsuccessful", colour=discord.Colour(0xe74c3c),
                                  description="You haven't permission to mute anybody")
    await bot.say(embed=embed)  # =================================== and another nice Embed with the result

@bot.command(pass_context=True)  # ================================== again, don't ask
@commands.has_permissions(manage_server=True)  # ==================== now, we want the mute to be lifted only by Mods and Admins
async def unmute(ctx, user:discord.Member=None):  # ================= notice there's no reason string here, we don't need one
    """Command to unmute that spammer, use wisely"""  # ============= rip help descriptions, why did I write so many?
    text_overwrite = discord.PermissionOverwrite()  # =============== gotta change what was altered before
    text_overwrite.send_messages = True  # ========================== and now they will be able to write again
    embed = discord.Embed(title="\N{FLUSHED FACE} Unmute Successful", colour=discord.Colour(0x9b59b6),
                          description=f"Say thanks to **{ctx.message.author.display_name}** for removing the Mute and, remember to behave {user.mention}")
    for channel in ctx.message.server.channels:  # ================== since only works for Mods and Admins, no need of an if statement
        await bot.edit_channel_permissions(channel, user, text_overwrite)
    await bot.say(embed=embed)  # =================================== and vam! another awesome Embed

@bot.command(pass_context=True, name="kick", hidden=True)  # ======== finally kick command is fully working
@commands.has_permissions(manage_server=True)
async def kick(ctx, user: discord.Member=None, *, reason: str=None):
    """Kicks member, needs mention and reason."""
    if ctx.message.author.server_permissions.kick_members == True:
        if user != None:
            embed = discord.Embed(colour=0xe67e22)
            embed.add_field(name="\N{CRAB}" , value="{0} kicked {1} because: {2}".format(ctx.message.author.display_name, user.display_name, reason))
            await bot.say(embed=embed)
            await bot.kick(user)
        else:
            embed = discord.Embed(title="First you need to mention user", value="Then a reason", colour=0xd35400)
            await bot.say(embed=embed)
    else:
        await bot.say("You haven't permission to kick anybody, try command `kickme` instead.")

@bot.command(pass_context=True, hidden=True)  # ==================== the hidden is to hide it from help page, rip help
async def ban(ctx, user: discord.Member = None):  # ================ might have used it a few days back, forgot it was here
    """Very self explanatory"""  # ================================= innit mate?
    if ctx.message.author.server_permissions.ban_members == True:  # I believe this requires MS perms
        await bot.ban(user)
    else:
        await bot.say("You have no permission to ban any users")  # = This is everyone else in server

# ================================
# WELCOME AND FAREWELL MESSAGES
# ================================
@bot.event
async def on_member_join(member):  # ================================ I like to keep track of who joins, when
    serverchannel = member.server.default_channel  # ================ it goes into the first General-channel, there might be way to change for a different channel, just too lazy to do it
    server = member.server  # ======================================= because you only want to count members in your server
    count = len(server.members)  # ================================== this gives the right number
    msg = "**Welcome __{0}__ to {1}. We now have `{2}` members.**".format(member.mention, server, count)
    await bot.send_message(serverchannel, msg)  # =================== might change and make Embed later... no promises though

@bot.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel  # ================ it also goes into the first General-channel
    server = member.server  # ======================================= read above
    count = len(server.members)  # ================================== read above
    msg = "**And now, {0}'s watch has ended.\nHold the door, Hodor.\nWe are left with {1} members in {2}**.".format(
        member.mention, count, server)  # =========================== because I cried when he held the door... still do
    await bot.send_message(serverchannel, msg)  # =================== same for this one, Embed would be nice

@bot.command(hidden=True, description="Robotsu finds out when a member joined the Discord guild")
async def joindate(member: discord.Member):  # ====================== tells you when a member joined
    await bot.say("{0.name} joined in {0.joined_at}".format(member))

# =================================================================== because it is good to remember who helped when the rest laughed
@bot.command(pass_context=True, name="credits", description="Robotsu alpha is brought to you because of the following support")
async def credits(ctx):  # ========================================== if your name isn't here, is because you didn't help
    embed = discord.Embed(title="Robotsu Beta version 0.6 - Credits", colour=discord.Colour(0x2196f3), description="**ロボつ²** is the first Bot made by <@!323578534763298816>, but it has grown from **alpha stage** to **beta** with the support and guidance of many expert individuals.")
    embed.add_field(name="Sincere thanks to:", value="Maximilian\nMiguel\nZey\nMei\nTyler\nLesbisch\nLin Lin\nAndrija", inline=True)
    embed.add_field(name="in alphabetical order", value="<@!271238766323171328>\n<@!109353460524191744>\n<@!114941315417899012>\n<@!87600987040120832>\n<@!183389299524239361>\n<@!131950684785475584>\n<@!324040201225633794>\n<@!339378386080104450>", inline=True)
    await bot.say(embed=embed)  # =================================== thank you guys and girls!

# ================ Simple command to send notes to self in DM, at least it is useful to me
@bot.event
async def on_message(message):  # =================================== don't really know why I used on_message here... not so clean
    if message.content.startswith.lower()("note to self"):  # ======= really like .lower(), otherwise might miss the chance to DM users
        await bot.say('Note sent in a DM!')  # ====================== after sending DM, it writes a note, to let you know command worked
        await bot.send_message(message.author, message.content.replace('note to self ', ''))
    await bot.process_commands(message)  # ========================== not sure how this works, but it does, magick!

@bot.command(pass_context=True, name="embed")  # ==================== want to have a message in Embed? no, fu!
async def embed(ctx, *, message:str):  # ============================ not sure who suggested this, anyhow, it works as requested
    """Command for Embedding your text
    it deletes your original message
    and quotes your name"""  # ====================================== another long and nice description for the help, rip help
    try:
        await bot.delete_message(ctx.message)  # ==================== this is to avoid having same message twice in search
    except:
        pass
    embed = discord.Embed(title="{0} wrote:".format(ctx.message.author.display_name), colour=discord.Colour(0x2a6e81), description="{0}".format(message))
    await bot.say(embed=embed)  # =================================== the Embed that was promised, now shatap!

# ================================
# MESSAGE ON COMMAND ERROR
# ================================
@bot.event
async def on_command_error(error, ctx):  # ========================== this sends the error report directly into the chat channel
    if isinstance(error, commands.CommandNotFound):  # ============== when there's a typo or a command from another bot
        return
    if isinstance(error, commands.DisabledCommand):  # ============== read
        await bot.send_message(ctx.message.channel, "This command has been disabled by the server owner")
        return
    if isinstance(error, checks.dev_only):  # ======================= very clear one
        await bot.send_message(ctx.message.channel, "This command can only be ran by **XAOS1502**")
        return
    if ctx.message.channel.is_private:  # =========================== I know you all have tried, but commands only work in servers, nor inside your inbox dude!
        await bot.send_message(ctx.message.channel, "An error occurred while trying to run this command,\n"
                                                    "robotsu's commands don't run in a private messages channel.\n"
                                                    "Please try running this command on a server where he's member.")
        return
    try:
        await bot.send_message(ctx.message.channel, error)
    except:
        pass
    log.error("An error occurred while executing the {} command: {}".format(ctx.command.qualified_name, error))

# ================================
# WORDS IN MSG w/o PREFIX
# ================================
@bot.event
async def on_message(message):
    if "(╯°□°）╯︵ ┻━┻" in message.content:
        EmbedFlip = discord.Embed()
        EmbedFlip.title = "{0}".format(message.author.display_name)
        EmbedFlip.colour = discord.Colour(0xbb94de)
        EmbedFlip.description = "{0}".format(random.choice(flipping_tables))
        await bot.send_message(message.channel, embed=EmbedFlip)

    if message.content.startswith("plzpm me"):
        await bot.say('I sent you a DM!')
        await bot.send_message(message.author, message.content.replace('plzpmme ', ''))
    await bot.process_commands(message)

    if message.content.startswith("I love you"):
        EmbedLuv = discord.Embed(colour=discord.Colour(0xf6a3bf), description="We have some (ღˇ◡ˇ(ᵕ◡ᵕෆ) love birds here.")
        await bot.send_message(message.channel, embed=EmbedLuv)

    if message.content.startswith("Happy Birthday"):
        EmbedBd = discord.Embed()
        EmbedBd.title = "🎂"
        EmbedBd.colour = discord.Colour(0xff5a93)
        EmbedBd.description = "ღゝ◡╹)ノ♡✯ℋᵅᵖᵖᵞ ℬⁱʳᵗᑋᵈᵃᵞ✯ **{}**\nfrom **robotsu**\nwith love.".format(message.author.display_name)
        await bot.send_message(message.channel, embed=EmbedBd)

    if message.content.lower() in spam_list:
        EmbedSpam = discord.Embed(colour=discord.Colour(0xed1163), description="Not nice.")
        await bot.send_message(message.channel, embed=EmbedSpam)

    await bot.process_commands(message)

# ================================
# LIST OF COMMAND LISTS
# ================================
spam_list = [
    "who wants nudes",
    "want nudes",
    "send me nudes",
    "see nudes",
    "is naked",
    "her naker",
    "my dick"
]
flipping_tables = [
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ ︵ ┻━┻\n*tablerus-repellus!*",
    "┻━┻ ︵ ┐( ˘ㅅ˘)┌ \nMeh, that table passed far away!",
    "(╯°□°)╯︵ ┻━┻\nTake this back!",
    "┻━ ︵ ¯\\(｡･益･)┌┛ ︵ ━┻\nTable destroyed!",
    "(ノ `Д´)ノ ┬─┬\nWhy you? Take this!",
    "┬─┬ ノ( º _ ºノ)\nBetter luck next time!",
    "╰(⇀ᗣ↼‶)╯ ︵ ┻━┻\n**robotsu** ducked that one",
    "︵ ┻━┻ . .･ヾ(。￣□￣)ﾂ\n**robotsu** ran faster than sound!",
    "!(ﾉ｀◎´)ﾉ ︵ ┻━┻\nTable bounced back at you!",
    "(つ•̀ω•́)つ ︵┬─┬\nNothing can touch **robotsu**",
    "ヽ( ･∀･)ﾉ┌┛︵ ┻━┻\n**robotsu** kicked the table back at you!",
    "┻━┻ ︵ (ノ`Д´)ノ\n**robotsu** dove away!",
    "ヾ(ﾟ∀ﾟ○)ﾂ三ヾ(●ﾟ∀ﾟ)ﾉ\nRunning zig-zag so no table can hit him",
    "┬─┬ ヾ(･д･ヾ)\nTables bow down to **robotsu**'s feet",
    "╭(°ㅂ°)╮┻━┻ ︵╰(°ㅂ°)╯\nWhich one am I? Confusion spell.",
    "┬─┬﻿ ノ( ゜-゜ノ)\nStop messing around with tables and go back to school",
    "(｀´)ゞ ((┻━┻))\nTelekinesis counter-attack",
    "(〜￣っ￣)〜 ︵┻━┻\nLOL, no use trying again...",
    ".·´¯`(>▂\nHow could you hit **robotsu**?"
]

# =================================================================== Token
bot.run('TOKEN_GOES_HERE_BUT_DO_NOT_SHARE_IT')
# =================================================================== just do us all a favour, and don't share your token, thanks.
