#インストールした discord.py を読み込む
import discord
from discord.ext import commands
import tokun
from ans import ansBox
import subprocess
import ffmpeg
import tokun
from import_random import diceroll
# 自分のBotのアクセストークンに置き換えてください
TOKEN = tokun.TOKUN

# 接続に必要なオブジェクトを生成
client = discord.Client()
print('起動しました')


# 起動時に動作する処理

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    #対応するメッセージに返答
    if message.content in ansBox:
        await message.channel.send(ansBox.get(message.content))
    
    if message.content.startswith("!dice"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)
    


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
