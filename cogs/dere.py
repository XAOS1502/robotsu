import discord

from discord.ext import commands

class Dere:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def dere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xe46ba2))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Tsundere", value="Deredere (デレデレ) means lovey dovey.")
		embed.add_field(name="Available Types", value="tsundere\nyandere\ndandere\nkuudere\nderedere\nhimedere\noujidere\nkamidere\nundere\nmayadere\nbodere\nhinedere\nsadodere\nbakadere\nhajidere\nkanedere\nnyandere\nutsundere")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def tsundere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xf30707))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Tsundere", value="The tsundere is one of the most popular types. They switch between a tsun (harsh) state and dere (love struck) state. You’ll know if a character is tsundere if they keep saying “baka” or they try to cover up a good deed.")
		embed.add_field(name="Tsundere (Type A)", value="Type A: The “tsun” state is their default personality. They tend to verbally and physically abuse their object of desire, get embarrassed when complimented, and use “baka” as every other word.\nPopular examples: Louise Françoise Le Blanc de La Vallière (The Familiar of Zero) / Chitoge Kirisaki (Nisekoi) / Taiga Aisaka (Toradora!)")
		embed.add_field(name="Tsundere (Type B)", value="Type B: The “dere” state is their default personality. They have a friendly public face and are usually generous. Their “tsun” state appears when their love interests does something to upset them (usually something perverted).\nIn short, Type A tends to be off-putting with everyone until a love interest breaks their shell, while Type B tends to be friendly with everyone except for their love interest due to not knowing how to express their feelings.\nPopular examples: Winry Rockbell (Fullmetal Alchemist) / Yamada (B Gata H Kei) / Levy McGarden (Fairy Tale)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def yandere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xbb4d0d))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Yandere", value="The Yandere (ヤンデレ) type refers to a character who starts out nice and sweet but eventually becomes dark and obsessive over the one they love. They become stalkers and use violence on, and possibly even murder, any person who gets close to their love interest — even if they’re too shy to simply speak with that person they have a crush on.\nThis word is a portmanteau of Yanderu (やんでる) which means to be mentally or emotionally ill and Deredere (デレデレ) which means lovey dovey.")
		embed.add_field(name="ヤンデレ", value="Yandere characters are really sweet on the outside. They range from being cheerful and friends with others, or can be really shy. A bond with the main character will form quickly.\nHowever, their friendly nature masks a dark side. Yandere characters are very possessive and controlling. Most will kill the people around their love interest or will isolate them from society. They do not take rejection well (which has a 90% chance of happening).\nPopular examples: Yuno Gasai (The Future Diary) / Anna Nishikinomiya (Shimoneta) / Lindo (Dance with Devils)")
		await self.bot.say(embed=embed)
		 
	@commands.command(pass_context=True)
	async def dandere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xce1eee))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Dandere", value="The Dandere (だんデレ) type refers to a character who is often silent and to themselves. It may be due to shyness or just because they’re the quiet type. However, when alone with the person they are attracted to, they usually come out of their shell and become more loving.\nThis word is a compound of Danmari (だんまり) which means silent and Deredere (デレデレ) which means lovey dovey.\nQuiet, shy, and harmless. Dandere characters typically wear glasses and are always buried in books. However, they can become talkative when around their love interest.\nPopular examples: Urara Shiraishi (Yamada-kun and the Seven Witches) / Shiori Shinomiya (The World God Only Knows) / Onodera Kosaki (Nisekoi)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def kuudere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x038dc5))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Kuudere", value="The Kuudere (クーデレ), sometimes written Coodere or Kūdere, type refers to a character who is often cold, blunt, and cynical. They may seem very emotionless on the outside, but on the inside they’re very caring — at least when it comes to the ones they love.\nThis word is a compound of Cool (クール) and Deredere (デレデレ) which means lovey dovey.\nEmotionless, cold, and distant. On the rare occasional that a kuudere does speak, they tend to be very blunt and cynical. A blank face and a flat voice is a must. Despite their icy nature, kuudere characters are capable of caring and forming romantic bonds.\nPopular examples: Eucliwood Hellscythe (Is this a Zombie?) / Kanade Tachibana (Angel Beats!) / Mashiro Shiina (The Pet Girl of Sakurasou)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def deredere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xff791d))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Deredere", value="The Deredere (デレデレ) type refers to a character who is completely kind, happy, and energetic. No matter what may happen, they quickly revert to their cheerful self.\nThis may be the only character type that doesn’t have any abbreviation with the base Deredere (デレデレ) word, although the definition isn’t simply lovey dovey like the other types.\nThe most cheeful, hyper, and loving of the “-dere” archetypes. Deredere characters are constantly smothering their love interests with affection.\nPopular examples: Lala Satalin Deviluke (To LOVE-Ru) / Belldandy (Ah! My Goddess) / Otome Arisugawa (Aikatsu!)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def himedere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xd40197))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Himedere", value="The Himedere (ひめデレ) type refers to a character who wishes to be treated like a princess by the person she loves, even if they aren’t royalty in actuality.\nThis word is a compound of Hime (ひめ / 姫) which means princess and Deredere (デレデレ) which means lovey dovey.\nThis archetype is restricted to female characters. They want to be treated like a princess by everyone, even if they are not actual royalty. Himedere characters may act stuck up as a mask to hide insecurities. The classic “ohoho” laugh is their favorite weapon.\nPopular examples: Erina Nakiri (Shokugeki no Souma) / Mio Aoyama (The World God Only Knows) / Eri Sawachika (School Rumble)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def oujidere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x6654de))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Oujidere", value="The Oujidere (おうじデレ) type refers to a character who wishes to be treated like a prince by the person he loves, even if they aren’t royalty in actuality.\nThis word is a compound of Ouji (おうじ / 王子) which means prince and Deredere (デレデレ) which means lovey dovey.\nThe male version of himedere. They want to be treated like a prince, even if they are not royalty. Usually they have sharp eyes and crazy awesome fashion.\nPopular examples: Lelouch Lamperouge (Code Geass) / Ciel Phantomhive (Black Butler) / Ayato Sakamaki (Diabolik Lovers)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def kamidere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xafd90f))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Kamidere", value="The Kamidere (かみデレ) type refers to a character with a god complex. They’re highly arrogant and proud, and aren’t afraid to speak their minds and show everyone how right they are.\nThis word is a compound of Kami (かみ / 神) which means God and Deredere (デレデレ) which means lovey dovey.\nArrogant, proud, and sporting a god complex. They believe everyone should treat them as divine beings, and will force their views on everyone.\nPopular examples: Mio Isurugi (MM!) / Light Yagami (Death Note) / Satsuki Kiryuuin (Kill la Kill)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def undere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x0be590))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Undere", value="The Undere (ウンデレ) type refers to a character who says yes to pretty much everything the one they love says. They agree as much as possible to become as close as they can to their love interest.\nThis word is a compound of Un (ウン) which is a short way Japanese people say Yes and Deredere (デレデレ) which means lovey dovey.\nA relatively obscure character type. The undere combines the deredere, dandere, and a sprinkle of yandere. These character always say “yes” (un) to their loved ones as a way to stay close to them.\nPopular examples: Misa Amane (Death Note) / Minami Kotori (Love Live!)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def mayadere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x430a4e))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Mayadere", value="The Mayadere (まやデレ) type refers to a character who is often a dangerous antagonist of a series, but switches sides after falling in love with another character. The character may remain deadly and unpredictable for the protagonist or other main character in the Anime or Manga.\nI do not know the origins of the word Mayadere, as Maya doesn’t translate into anything.\nThey are characters who begin the series as an antagonist. Mayadere will fall in love with the main character, but that does not mean they will switch sides and are willing the kill their love interest if they feel betrayed.\nPopular examples: Esdeath (Akame ga Kill!) / Golden Darkness (To LOVE-Ru) / Illyasviel von Einzbern (Fate/stay Night: Unlimited Blade Works)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def bodere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xb23a3a))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Bodere", value="A relatively new type of character. The bodere combines the violent nature of the tsundere with the shyness of the dandere. Bodere characters are usually shy around the opposite sex and lash out to hide their embarrassment.\nPopular example: Mahiru Inami (Working!!)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def hinedere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x17b69e))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Hinedere", value="Takes the icy nature of the kuudere and combines it with the arrogant attitude of the kamidere. Hinedere characters are very cynical and sarcastic, but will show their soft side when a character breaks through their shell.\nThey are a new archetype and may see more popularity if the anime’s cynical trend continues.\nPopular example: Hachiman Hikigaya (OreGairu)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def sadodere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x530606))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Sadodere", value="Sadistic characters that get off on toying with characters on an emotional and physical level. If they find a love interest, they better be a masochist who can take a beating.\nPopular examples: Nemesis (To LOVE-Ru) / Kurumi Tokisaki (Date A Live) / Kirihime Natsuno (Dog & Scissors)")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def bakadere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xe59a10))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Bakadere", value="The Bakadere (ばかデレ) type refers to a character who is very clumsy and stupid. They’re a very innocent and sweet person for the most part, but their stupidity outshines their other positives.\nThe word is a compound of Baka (ばか) which means stupid or moron and Deredere (デレデレ) which means lovey dovey.")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def hajidere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0xad539a))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Hajidere", value="The Hajidere (はじデレ) type refers to a character who is very nervous and embarrassed around their crush. They will easily blush near their love interest, and might even feint from being so bashful.\nThis word is a compound of Haji (はじ / 恥) which means embarrassment and Deredere (デレデレ) which means lovey dovey.")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def kanedere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x18641e))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Kanedere", value="The Kanedere (かねデレ) type refers to a character who is attracted to others with money or status. They’re the anime and manga equivalent of a gold digger.\nThis word is a compound of kane (かね / 金) which means money and Deredere (デレデレ) which means lovey dovey.")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def nyandere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x54ee0e))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Nyandere", value="The Nyandere (ニャンデレ) type refers to a character who has many cat like attributes. Often times they add “nyan” in their sentences. They might even be part cat and part human. See also: Nekomimi.\nThe word is a compound of Nyan (ニャン) which is a Japanese onomatopoeia for a cat sound, and Deredere (デレデレ) which means lovey dovey.")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def utsudere(self, ctx):
		"""Anime Dere types"""
		embed = discord.Embed(colour=discord.Colour(0x494d6e))
		embed.set_footer(text="Coded by 「XΛOS」#1502")
		embed.add_field(name="Utsudere", value="The Utsudere (うつデレ) type refers to a character who is often sad and depressed. There is a reason for the character’s despair such as being bullied at school. Even if their life improves, they are often wary of other characters’ motives.\nThis word is a compound of Utsu (うつ / 鬱) which means depression and Deredere (デレデレ) which means lovey dovey.")
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(Dere(bot))
