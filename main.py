import nextcord, config, os
from nextcord.ext import commands
from nextcord import Embed

bot = commands.Bot(command_prefix='#', intents=nextcord.Intents.default())

@bot.event
async def on_ready():
    print("-------------------------")
    print(f"{bot.user} is online...")
    print("-------------------------")

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")

bot.run(config.TOKEN)