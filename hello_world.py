import discord

f = open('discord-bot-token.txt', 'r')
TOKEN = f.read()
f.close()
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('起動確認')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/hello」と発言したら「hello,world」が返る処理
    if message.content == 'hello':
        await message.channel.send('hello,world')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)