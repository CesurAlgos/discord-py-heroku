import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Bağlandı: {bot.user.name}({bot.user.id})")

@bot.command()
async def Adin_ne(ctx):
    await ctx.send("Nagini")

    async def Sahibin_kim(ctx):
    await ctx.send("Flamius")

    async def Catal_dili_konus(ctx):
    await ctx.send("SSShaieee Assaaha")
    
    async def malmısın(ctx):
    await ctx.send("düzgün konuş.")

if __name__ == "__main__":
    bot.run(TOKEN)
