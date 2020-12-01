import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Bağlandı: {bot.user.name}({bot.user.id})")

@bot.command()
async def adin(ctx):
    await ctx.send("Nagini")

    async def sahibin(ctx):
    await ctx.send("Flamius")

    async def cataldil(ctx):
    await ctx.send("SSShaieee Assaaha")
    
    async def malmisin(ctx):
    await ctx.send("düzgün konuş. Deneme")

if __name__ == "__main__":
    bot.run(TOKEN)
