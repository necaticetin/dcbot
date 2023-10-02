import discord
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"


@client.event
async def on_ready():
    print(f' Çalışmaya Hazırım {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('seni kim yaptı?'):
        await message.channel.send("beni necati yaptı")
    elif message.content.startswith('gidiyorum'):
        await message.channel.send("\U0001f642 görüşürüz")
    elif message.content.startswith('sa'):
        await message.channel.send("as")
    elif message.content.startswith('necati nerede?'):
        await message.channel.send("\U0001f642 az sonra gelecek")
        await message.author.send("necati sonra seninle ilgilenecek.")
    elif message.content.startswith("şansıma güveniyorum"):
        await message.channel.send("🪙 yazımı turamı? parayı atıyorum")
        await message.channel.send(yazi_tura())
    else:
        await message.channel.send(message.content)

client.run("token")
