# インストールした discord.py を読み込む
import discord
import re
import os

def convert_url(url):
    """ URLをvxtwitter.comに変換する """
    return re.sub(r'https?://(www\.)?(twitter\.com|x\.com)', r'https://vxtwitter.com', url)

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # URLを検出して変換する
    urls = re.findall(r'https?://[www\.]?twitter\.com/\S+|https?://[www\.]?x\.com/\S+', message.content)
    if urls:
        converted_urls = [convert_url(url) for url in urls]
        reply_text = '\n'.join(converted_urls)
        await message.channel.send(reply_text)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)