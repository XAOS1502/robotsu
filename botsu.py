import time# =================================== for the ping! to work
import discord# ================================ because this bot is meant to run on? air? no, Discord
start_time = time.time()# ====================== something else for the ping!
from discord.ext import commands# ============== without this, most commands will not work, try it out
# ============================================== you have to import these if you want bot to work, just do it

description = "Robotsu, Discord bot coded by XΛOS <@!323578534763298816> and Lin² <@!324040201225633794>"# === This was at the top of help
bot_prefix = ['Robotsu ', 'robotsu ', '_']# ==== notice the next line, it also works with mention
bot = commands.Bot(command_prefix=commands.when_mentioned_or("Robotsu ", "robotsu ", "_"), description=description)
bot.remove_command('help')# ==================== Because the help got too long

# ================ cogs that are used, 
# and the reason the help is so long
# also, they serve to organise the
# commands and know where things are...
# ================ 
bot.load_extension("cogs.interactive")# ======== commands that work w/o mention to say something to a member with Kaomoji
bot.load_extension("cogs.misc")# =============== numbers, pseudo-calc, urban, choices
bot.load_extension("cogs.funtimes")# =========== commands rigged af! don't take the results too seriously
bot.load_extension("cogs.prediction")# ========= drop the 8ball, these predictions are scary-accurate, or not
bot.load_extension("cogs.administrative")# ===== a good way to remind f*ktards the 10 rules of the server
bot.load_extension("cogs.extracommands")# ====== commands from other botos, not sure why people like these...
bot.load_extension("cogs.mods")# =============== useful commands for Moderators, not sure what to write there though
bot.load_extension("cogs.ayuda")# ============== since help got so effin big, I divided them into categories with Embeds
bot.load_extension("cogs.dere")# =============== another request from a friend, to have ALL the deredere types

@bot.event
async def on_ready():# =========================================== Does anybody ever read these?
    print(discord.__version__)# ================================== version, just so you remember what you installed
    print('     ε=ε=ε=ε=┏(;^o^)┛')# ============================== RUN DOS, RUN
    print('誰かがこれを読んでいますか？')# ============================ Not sure what it says, or if it is even correct
    print('ロボつ²ト名 : {} alpha'.format(bot.user.name))# ========= gets the name from the API
    print('クライアント ID : {}'.format(bot.user.id))# ============== gets the bot user ID
    print('ロボつ²トバージョン : 0.6 「2017年 8月 21日」')# ============ I keep updating the date, when I remember to do it
    print('クリエイター :「XΛOS」#1502')# ============================ the person behind the code
    print('ロボつ²トがオンラインになりました 。。。')# ================== more random stuff
    print(' ')# =================================================== silence, because we all need some
    print('    (∩｀-´)⊃━☆ﾟ.*･｡ﾟ      「魔法の解放!」')# ============== let the magick begin
    print(' ')# =================================================== space, because we all need some
    print('-> ロードコア')# ========================================= something else
    print('--> ロボつ²ト同期が完了しました')# ========================== some more else
    print('---> ロボつ²トモード起動')# ================================ and last else
    await bot.change_presence(game=discord.Game(type=0, name='with light'))# ====>Shows as Playing with light
    with open("logs/restart.txt", "a") as file:# ================ Useful, or not. I like to keep count of restarts
        file.write("\nRobotsu is very sorry he had to restart")# ================ and he should be

# ================================================================
# ================= SERVER MANAGER COMMANDS
# ================================================================
@bot.command(pass_context=True, hidden=True)
async def mute(ctx, user):# ====================================== Okay, haven't made it work yet...
    """Command to mute a user without kicking"""# ================ this is what used to appear in the help page, rip-help
    text_overwrite = discord.PermissionOverwrite()# ============== 
    text_overwrite.send_messages = False# ======================== 
    voice_overwrite = discord.PermissionOverwrite()# ============= 
    voice_overwrite.speak = False# =============================== 
    for channel in ctx.message.server.channels:# ================= 
        if channel.type == discord.ChannelType.text:# ============ 
            await bot.edit_channel_permissions(channel, user, text_overwrite)
        elif channel.type == discord.ChannelType.voice:# ========= 
            await bot.edit_channel_permissions(channel, user, voice_overwrite)
        else:
            continue# ============================================ okay, all these blanks are because I don't know what's goin on

@bot.command(pass_context=True, hidden=True)
async def unmute(self, ctx, user:discord.Member=None):# ========== Also needs fixing, because reasons
    """Command to mute a user without kicking"""# ================ stuff for the help page, rip help
    text_overwrite = discord.PermissionOverwrite()# ============== 
    text_overwrite.send_messages = True# ========================= 
    voice_overwrite = discord.PermissionOverwrite()# ============= 
    voice_overwrite.speak = True# ================================ 
    for channel in ctx.message.server.channels:# ================= 
        if channel.type == discord.ChannelType.text:# ============ 
            await bot.edit_channel_permissions(channel, user, text_overwrite)
        elif channel.type == discord.ChannelType.voice:# ========= 
            await bot.edit_channel_permissions(channel, user, voice_overwrite)
        else:
            continue# ============================================ and again, not sure why this doesn't work

@bot.command(pass_context=True, name="kick", hidden=True, description="Robotsu can kick a member, they'll be able to join with an invite")
async def kick(ctx, user: discord.Member = None):# ================ Haven't tried it, don't want to kick members just yet
    """Kicks the mentioned member from the server."""# ============ 
    if ctx.message.author.server_permissions.kick_members == True:# 
        if user != None:# ========================================= 
            embed = discord.Embed(colour=0x5de316)# =============== 
            embed.add_field(name="­", value="{0} has kicked {1} for {2}".format(ctx.message.author.mention, user.mention, reason))
            await bot.say(embed=embed)# =========================== this is to send the Embed above as message in the channel
            await bot.kick(user)# ================================= 
        else:
            embed = discord.Embed(title="You need to specify user first", value="­", colour=0x5de316)
            await bot.say(embed=embed)# =========================== same as the above Embed, just different content, duh
    else:
        await bot.say("You don't have permissions to kick anybody, try `kickme` command instead.")

@bot.command(pass_context=True, hidden=True)# ==================== the hidden is to hide it from help page, rip help
async def ban(ctx, user: discord.Member = None):# ================ might have used it a few days back, forgot it was here
    """Very self explanatory"""# ================================= innit mate?
    if ctx.message.author.server_permissions.ban_members == True:# I believe this requires MS perms
        await bot.ban(user)
    else:
        await bot.say("You have no permission to ban any users")# = This is everyone else in server

# ================================
# WELCOME AND FAREWELL MESSAGES
# ================================
@bot.event
async def on_member_join(member):# ================================ I like to keep track of who joins, when
    serverchannel = member.server.default_channel# ================ it goes into the first General-channel, there might be way to change for a different channel, just too lazy to do it
    server = member.server# ======================================= because you only want to count members in your server
    count = len(server.members)# ================================== this gives the right number
    msg = "**Welcome __{0}__ to {1}. We now have `{2}` members.**".format(member.mention, server, count)
    await bot.send_message(serverchannel, msg)# =================== might change and make Embed later... no promises though

@bot.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel# ================ it also goes into the first General-channel
    server = member.server# ======================================= read above
    count = len(server.members)# ================================== read above
    msg = "**And now, {0}'s watch has ended.\nHold the door, Hodor.\nWe are left with {1} members in {2}**.".format(
        member.mention, count, server)# =========================== because I cried when he held the door... still do
    await bot.send_message(serverchannel, msg)# =================== same for this one, Embed would be nice

@bot.command(hidden=True, description="Robotsu finds out when a member joined the Discord guild")
async def joindate(member: discord.Member):# ====================== tells you when a member joined
    await bot.say("{0.name} joined in {0.joined_at}".format(member))

# ================================================================= because it is good to remember who helped when the rest laughed
@bot.command(pass_context=True, name="credits", description="Robotsu alpha is brought to you because of the following support")
async def credits(ctx):# ========================================== if your name isn't here, is because you didn't help
    embed = discord.Embed(title="Robotsu Beta version 0.6 - Credits", colour=discord.Colour(0x2196f3), description="**ロボつ²** is the first Bot made by <@!323578534763298816>, but it has grown from **alpha stage** to **beta** with the support and guidance of many expert individuals.")
    embed.add_field(name="Sincere thanks to:", value="Maximilian\nMiguel\nZey\nMei\nTyler\nLesbisch\nLin Lin\nAndrija", inline=True)
    embed.add_field(name="in alphabetical order", value="<@!271238766323171328>\n<@!109353460524191744>\n<@!114941315417899012>\n<@!87600987040120832>\n<@!183389299524239361>\n<@!131950684785475584>\n<@!324040201225633794>\n<@!339378386080104450>", inline=True)
    await bot.say(embed=embed)# =================================== thank you guys and girls!

# ================ Simple command to send notes to self in DM, at least it is useful to me
@bot.event
async def on_message(message):# =================================== don't really know why I used on_message here... not so clean
    if message.content.startswith.lower()("note to self"):# ======= really like .lower(), otherwise might miss the chance to DM users
        await bot.say('Note sent in a DM!')# ====================== after sending DM, it writes a note, to let you know command worked
        await bot.send_message(message.author, message.content.replace('note to self ', ''))
    await bot.process_commands(message)# ========================== not sure how this works, but it does, magick!

@bot.command(pass_context=True, name="embed")# ==================== want to have a message in Embed? no, fu!
async def embed(ctx, *, message:str):# ============================ not sure who suggested this, anyhow, it works as requested
    """Command for Embedding your text
    it deletes your original message
    and quotes your name"""# ====================================== another long and nice description for the help, rip help
    try:
        await bot.delete_message(ctx.message)# ==================== this is to avoid having same message twice in search
    except:
        pass
    embed = discord.Embed(title="{0} wrote:".format(ctx.message.author.display_name), colour=discord.Colour(0x2a6e81), description="{0}".format(message))
    await bot.say(embed=embed)# =================================== the Embed that was promised, now shatap!

# ================================
# MESSAGE ON COMMAND ERROR
# ================================
@bot.event
async def on_command_error(error, ctx):# ========================== this sends the error report directly into the chat channel
    if isinstance(error, commands.CommandNotFound):# ============== when there's a typo or a command from another bot
        return
    if isinstance(error, commands.DisabledCommand):# ============== read
        await bot.send_message(ctx.message.channel, "This command has been disabled")
        return
    if isinstance(error, checks.dev_only):# ======================= very clear one
        await bot.send_message(ctx.message.channel, "This command can only be ran by the bot developers")
        return
    if isinstance(error, checks.owner_only):# ===================== this is me, only I can run it! Mwahaha kukuku
        await bot.send_message(ctx.message.channel, "This command can only be ran by the bot owner")
        return
    if isinstance(error, checks.not_nsfw_channel):# =============== haven't used this one yet...
        await bot.send_message(ctx.message.channel, "This command can only be ran in NSFW enabled channels. It must either be named `nsfw` or the name must start with `nsfw-`")
        return
    if isinstance(error, checks.not_server_owner):# =============== since I have the bot and I'm the bot owner also, not sure how this works for normals
        await bot.send_message(ctx.message.channel, "Only the server owner (`{}`) can use this command".format(ctx.message.server.owner))
        return
    if isinstance(error, checks.no_permission):# ================== out of luck my friend
        await bot.send_message(ctx.message.channel, "You do not have permission to use this command".format(ctx.message.server.owner))
        return
    if ctx.message.channel.is_private:# =========================== I know you all have tried, but commands only work in servers, nor inside your inbox dude!
        await bot.send_message(ctx.message.channel, "An error occured while trying to run this command, this is most likely because it was ran in a private message channel. Please try running this command on a server.")
        return

    # ============================================================= in case the bot failed to send a message to the channel, the try except pass statement is to prevent another error
    try:
        await bot.send_message(ctx.message.channel, error)
    except:
        pass
    log.error("An error occured while executing the {} command: {}".format(ctx.command.qualified_name, error))

# ================================================================= Token
bot.run('TOKEN_GOES_HERE_BUT_DO_NOT_SHARE_IT')
# ================================================================= just do us all a favour, and don't share your token, thanks.
