import time
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(id канала обитания бота)
    client.active_channel = channel
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!русская рулетка':
        a = random.randint(1, 8)
        if a in (2, 4, 6, 8):
            await message.channel.send('Вы выжили')
        else:
            await message.channel.send('Выстрел!')

    if message.content == '!давай сыграем в кости':
        await message.channel.send('хорошо!')
        for i in range(2):
            b = random.randint(1, 6)
            await message.channel.send(f'Выпало число {b}')

    if message.content == '!Рулетка':
        await message.channel.send('У вас 30 секунд для ставок!')
        time.sleep(30)
        n = random.randint(0, 36)
        color = "чёрное" if n % 2 == 0 and n != 0 else "красное"
        await message.channel.send(f'Выпало {n} {color}')

    if message.content == '!правила':
        await message.channel.send("Конечно, вот наши правила: Крупье забирает 3.000$ с каждой ставки\nНе материтесь (по желанию)\nОзнакомьтесь с правилами игр, которые у нас есть:\nРусская рулетка: Участвуют 2 игрока и более, каждый скидывается по определённой сумме и отдаёт их крупье. Кто умрёт, тот и проиграл, а победителю выдаётся сумма денег, которые ставили другие игроки\nКости: Каждый из игроков делает ставку и бросает кости, у кого число больше, тот и забирает поставленную сумму\nРулетка: До запуска рулетки даётся 30 секунд на ставки, где игроки могут выбрать конкретное число, красное, чёрное или zero, в случае выигрыша из банка казино деньги распределяются между победившими\nПриятная игры")

client.run('Токен бота')
