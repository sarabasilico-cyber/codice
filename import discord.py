import discord
from discord.ext import commands
from bot_logic import flip_coin, gen_emodji, gen_pass

# La variabile intents contiene i permessi del bot
intents = discord.Intents.default()
intents.message_content = True

# Crea il bot usando la classe commands.Bot
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f"Abbiamo fatto l'accesso come {bot.user}")


@bot.command()
async def ciao(ctx):
    await ctx.send("Ciao!")


@bot.command()
async def arrivederci(ctx):
    await ctx.send("\U0001f642")


@bot.command()
async def smile(ctx):
    await ctx.send(gen_emodji())


@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())


@bot.command()
async def password(ctx):
    await ctx.send("La tua password: " + gen_pass(30))


@bot.command()
async def comandi(ctx):
    await ctx.send(
        "**I comandi disponibili sono:**\n"
        "- Lancio moneta: `$coin`\n"
        "- Genera password: `$password`\n"
        "- Emoji casuale: `$smile`\n"
        "- Benvenuto: `$ciao`\n"
        "- Arrivederci: `$arrivederci`\n"
        "- Mostra i comandi: `$comandi`"
    )


# Gestisce i comandi non riconosciuti
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "**Comando non riconosciuto. I comandi disponibili sono:**\n"
            "- Lancio moneta: `$coin`\n"
            "- Genera password: `$password`\n"
            "- Emoji casuale: `$smile`\n"
            "- Benvenuto: `$ciao`\n"
            "- Arrivederci: `$arrivederci`\n"
            "- Mostra i comandi: `$comandi`"
        )
    else:
        raise error


bot.run("MTU1OTI2MDM3MzE0NjkzMTM2Mw.GqHoFH.0vrSPSQ_2VLayunbts-_Tc5pIsJniUVd7rfW0o")