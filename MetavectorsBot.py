import discord
from discord.ext import commands

TOKEN = "OTUwMjY5MzQ2NjMzMTA1NDE4.YiWdSw.CtHUT2PHmk9XE6SoNYUlOvOOYFU"

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.command()
async def help_list(ctx):
    if ctx.author.guild_permissions.administrator == True:
        await ctx.send("1)official_links\n2)rules\n3)faq\n4)social_media")

@client.command()
async def official_links(ctx):
    embed = discord.Embed (
        title = "Metavectors: Official Links",
        colour = 0xe1bc52
    )

    embed.set_image(url="https://pbs.twimg.com/profile_banners/1493503990612512770/1645346092/1500x500")
    embed.add_field(name="\u200b", value="Twitter: https://twitter.com/metavectors", inline=False)
    embed.add_field(name="\u200b", value="Instagram: https://www.instagram.com/metavectors/", inline=False)
    embed.add_field(name="\u200b", value="Discord: https://discord.gg/PfdVbW9VAJ", inline=False)
    embed.add_field(name="\u200b", value="Website: https://metavectors.ga/", inline=False)
    embed.add_field(name="\u200b", value="Opensea: https://opensea.io/metavectors", inline=False)
    embed.add_field(name="\u200b", value="Rarible: https://rarible.com/metavectors/owned", inline=False)

    if ctx.author.guild_permissions.administrator == True:
        await ctx.send(embed=embed)

@client.command()
async def rules(ctx):
    embed = discord.Embed (
        title = "Metavectors: Rules",
        description="All members of any rank or role are expected to adhere to a basic\nrules outlined below. Failure to comply will result in your\nimmediate removal from Whitelist Shop Discord.",
        colour = 0xe1bc52
    )

    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1495320401580367872/L_4HGlgW_400x400.jpg")
    embed.add_field(name="\u200b", value="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯", inline=False)
    embed.add_field(name="\u200b", value="✅ Be respectful to all community members, no abuse, harassment, sexism, racism, or hate speech will be tolerated", inline=False)
    embed.add_field(name="\u200b", value="✅ Do not spam, advertise, shill, or post referral links.", inline=False)
    embed.add_field(name="\u200b", value="✅ No NSFW, politics, or sensitive content.", inline=False)
    embed.add_field(name="\u200b", value="✅ Do not imperonate staff members.", inline=False)
    embed.add_field(name="\u200b", value="✅ Keep discussions in the appropriate channel, if you feel there is no channel for your topic, let us know and we can get it added", inline=False)
    embed.add_field(name="\u200b", value="✅ Leave all the moderation to the staff. See someone breaking a rule? Send a message to a moderator.", inline=False)
    embed.add_field(name="\u200b", value="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯", inline=False)

    if ctx.author.guild_permissions.administrator == True:
        await ctx.send(embed=embed)

@client.command()
async def faq(ctx):
    embed = discord.Embed (
        title = "Metavectors: Frequently Asked Questions",
        colour = 0xe1bc52
    )

    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=False)
    embed.add_field(name="Test", value="Test", inline=False)
   
   
    if ctx.author.guild_permissions.administrator == True:
        await ctx.send(embed=embed)

@client.command()
async def roadmap(ctx):
    embed = discord.Embed (
        title = "Metavectors: Roadmap",
        description="This is just the beginning! There is more to come.👀",
        colour = 0xe1bc52
    )

    embed.set_image(url="https://pbs.twimg.com/media/FNTjCCCWUAAdkzD?format=jpg&name=large")
    embed.add_field(name="\u200b", value="📌1. Launching the Meta Vectors Modern Website/ Landing page - Will Launch on the 2nd of March 2022.📝", inline=False)
    embed.add_field(name="\u200b", value="📌2. Presales of the Meta Vectors NFT collection - OGs ,Whitelists and 19 Giveaways will be distributed accordingly during this stage.👀👀", inline=False)
    embed.add_field(name="\u200b", value="📌3. Main MetaVectors NFT Mint Launch - A total of 8889 NFTs will be Launched with a max of 1 NFTs to be minted per Whitelist wallet at 50% off and 2 NFTs per OGs wallet at 20% off. 😯", inline=False)
    embed.add_field(name="\u200b", value="📌4. MetaFi Dapp Launch - Meta Vectors is not like any other NFT Projects out there where their project utility lies in a delusional promise of a metaverse game .MetaFi will be the first dApp of its kind focused on adding a new steady utility to NFTs making them  not only to be seen as a trading commodity but an income generator for the NFT owner. The MetaFi dApp will be a crypto Lending and borrowing protocol with the use of NFTs as collateral , giving NFT owners the liquidity they need without selling off their NFTs. ⛔🎰", inline=False)
    embed.add_field(name="\u200b", value="📌5. MetaFi Dapp Marketing intergration - Due to the increase in niche specific NFT investors users on our MetaFi Dapp ,we will integrate NFT project marketing where NFT art creators can directly display and promote there project to NFT investors and Traders reducing the time and money spent on marketing a new NFT project. 🙏😏", inline=False)
    embed.add_field(name="\u200b", value="《-----------------------------------------------------------------------------------------》", inline=False)
    embed.add_field(name="\u200b", value="🤯We at Meta Vectors are planning to entirely change the NFT space by building MetaFi a NFT Finance tech startup with borrowing and lending of crypto with NFTs as collateral, MetaFi Fund a NFT insurance firm and to make NFTs a real world utility product. 😏💰📈", inline=True)
    embed.set_footer(text="Metavectors", icon_url="https://pbs.twimg.com/profile_images/1495320401580367872/L_4HGlgW_400x400.jpg")
    if ctx.author.guild_permissions.administrator == True:
        await ctx.send(embed=embed)

client.run(TOKEN)