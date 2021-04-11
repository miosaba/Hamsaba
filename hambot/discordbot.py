#インストールした discord.py を読み込む
import discord
import random

import tokun
import messageCollection
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
    wait_message = message
    messageChannel = message.channel

    # メッセージ返信
    messageReply=messageCollection.myMessageDict[wait_message.content]
    if(messageReply):
        await messageChannel.send(messageReply)

    # DMメッセージ
    elif message.content == "/randamDM":
        randam_dm = []
        while wait_message.content != "/end":  # 文字列判定
            await messageChannel.send('何かコメントして /endで終了')
            wait_message = await client.wait_for("message")  # ユーザーからのメッセージを待つ
            if wait_message.content != "/end":
                await messageChannel.send('受け付けました')
                dms = await wait_message.author.create_dm()  # メッセージ送信者へDM作成
                randam_dm.append(dms)  # ユーザーを保存
        await messageChannel.send('受付終了')

        for dm in randam_dm:
            content = random.choice(messageCollection.myRandomDmMessageList)  # 送信するメッセージをランダムで決める
            await dm.send(content)  # DM送信
        randam_dm.clear()
        
     #サイコロ
    if message.content.startswith("!dice"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        mention = f'{message.author.mention} {dice[cnt]} ' #メンションとダイス結果を格納
        await message.channel.send(mention)
        del dice[cnt]
        del mention
        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)