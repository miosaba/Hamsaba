#インストールした discord.py を読み込む
import discord
import random

import tokun
from collection import messageCollection
from cmn import common as dcCommon
from games.jinro import jinroSystem as jinroSys

# 自分のBotのアクセストークンに置き換えてください
TOKUN = tokun.TOKUN
AMAZON_TOKUN = tokun.AMAZON_TOKUN

# 接続に必要なオブジェクトを生成
client = discord.Client()
cmnIns = dcCommon.discordCommon()

jinro_entry_dict = {}
jobAllocationDict = {}

jobAllocationList = []

print('起動しました')

# メッセージ受信時に実行
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合
    if message.author.bot:
        # Botメッセージにリアクション追加
        if message.content == "役職調整":
            jinroSys.jinro_bot_reply_ready()

        return
    message = message

    # メッセージ返信
    if(message.content in messageCollection.myMessageDict):
        messageReply = messageCollection.myMessageDict[message.content]
        if(messageReply):
            await message.channel.send(messageReply)

    # DMメッセージ
    elif message.content == "/randamDM":
        randam_dm = []
        while message.content != "/end":
            await message.channel.send('何かコメントして /endで終了')
            message = await client.wait_for("message")  # ユーザーからのメッセージを待つ
            if message.content != "/end":
                await message.channel.send('受け付けました')
                dms = await message.author.create_dm()  # メッセージ送信者へDM作成
                randam_dm.append(dms)  # ユーザーを保存
        await message.channel.send('受付終了')

        for dm in randam_dm:
            content = random.choice(messageCollection.myRandomDmMessageList)  # 送信するメッセージをランダムで決める
            await dm.send(content)  # DM送信
        randam_dm.clear()
    
    # 人狼ゲーム
    elif message.content == "/人狼":
        jinro_entry_dict.clear()
        
        # 参加者を募る
        await cmnIns.participant_recruiting(jinro_entry_dict, message, client)

        # 役職準備
        await message.channel.send('役職調整')

# Botの起動とDiscordサーバーへの接続
client.run(TOKUN)