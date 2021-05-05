import discord
from discord.ext import commands
import os
import datetime
import asyncio

emojiCheck = '\N{THUMBS UP SIGN}'
emojiLetters = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER E}", 
            "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER K}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER L}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER M}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER O}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER P}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Q}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER R}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER S}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER T}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER U}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER V}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER W}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER X}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Y}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER Z}"]

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
  print('Event Bot has entered chat.')
  

isrunning = True

@bot.command()
async def poll(ctx, question, *args):
    voters = []
    vote_counts = {}
    
    # Create poll
    options = []
    react_to_option = {}
    description = ""
    for i, arg in enumerate(args):
      description += emojiLetters[i] + " " + arg + "\n"
      options.append(arg)
      react_to_option[emojiLetters[i]] = arg
    print(react_to_option)
    # Initialize vote_counts dictionary
    for option in options:
      vote_counts[option] = 0
    print(vote_counts)
    my_poll = discord.Embed(title = question, description = description)
    message = await ctx.send(embed = my_poll)
    for i, option in enumerate(options):
      await message.add_reaction(emojiLetters[i])
    await message.add_reaction(emojiCheck)
    # Get votes
    reaction = None
    # Ensure reaction is to the poll message and the reactor is not the bot
    def check(reaction, user):
        return reaction.message.id == message.id and user.id != 797601108268155001 
        
    
    global isrunning  
    while True:
        reaction, user = await bot.wait_for('reaction_add', check = check)
        
        await message.remove_reaction(reaction, user)
        # Check if the user has already voted
        if user not in voters:
          voters.append(user)
          vote_counts[react_to_option[reaction.emoji]] += 1
          print(vote_counts)
        if isrunning == False:
          isrunning = True
          print("done")
          results = ""
          for option in vote_counts:
            results += option + ": " + str(vote_counts[option]) + "\n"
          results_message = discord.Embed(title = question, description = results)
          await message.clear_reactions()
          await ctx.send(embed = results_message)
          break
        #await asyncio.sleep(1)
 

      

@bot.command()
async def stop(ctx):
  global isrunning
  isrunning = False

@bot.command()
async def test(ctx, *args):
    print("fucking work")
    await ctx.channel.send('{} arguments: {}'.format(len(args), ', '.join(args)))

bot.run(os.environ['TOKEN'])