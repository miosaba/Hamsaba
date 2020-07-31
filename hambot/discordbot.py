#インストールした discord.py を読み込む
import discord
import tokun
import random
import ans
# 自分のBotのアクセストークンに置き換えてください
TOKEN = tokun.TOKUN

# 接続に必要なオブジェクトを生成
client = discord.Client()
print('起動しました')
# /randamDM2を入力した人のユーザー情報を格納する /randamDMEndのメッセージによってクリアされる。
randam_dmSecond = []
# 起動時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    wait_message = message
    if message.content == ans.hitWord[0]:  #説明書
        await message.channel.send(ans.ansBox[0])
    if message.content == ans.hitWord[1] :#dm送信
        dm=await message.author.create_dm() #メッセージ送信者へDM作成
        await dm.send(ans.ansBox[1]) #DM送信
    if message.content == ans.hitWord[2]: #コマンド表示
        await message.channel.send(ans.ansBox[2])
    if ans.hitWord[3] in message.content: #メンション
        await message.channel.send(ans.ansBox[3])
    elif ans.hitWord[4] in message.content: #ハム
        await message.channel.send(ans.ansBox[4])
    elif ans.hitWord[5] in message.content: #太郎
        await message.channel.send(ans.ansBox[5])
    elif message.content ==ans.hitWord[6]: #Ham
        await message.channel.send(ans.ansBox[6])
    elif message.content ==ans.hitWord[7]: #ビビり
        await message.channel.send(ans.ansBox[7])
    elif message.content ==ans.hitWord[8]: #嫌い
        await message.channel.send(ans.ansBox[8])
    elif message.content ==ans.hitWord[9]: #ham
        await message.channel.send(ans.ansBox[9])
    if ans.hitWord[10]in message.content: #はむカービィ
        await message.channel.send(ans.ansBox[10])
    if ans.hitWord[11] in message.content: #リーガルさん
        await message.channel.send(ans.ansBox[11])
    if message.content == ans.hitWord[12]: #ランダム表示 ok
        content = random.choice(ans.random_contents)# 送信するメッセージをランダムで決める
        await message.channel.send(content) #メッセージが送られてきたチャンネルに送


    elif message.content == "/randamDM":
        randam_dm = []
        random_content = ['はむすき','はむきらい','はむふつう']
        while wait_message.content != "/end":  # 文字列判定
            await message.channel.send('何かコメントして /endで終了')
            wait_message = await client.wait_for("message")  # ユーザーからのメッセージを待つ
            if wait_message.content != "/end":
                await message.channel.send('受け付けました')
                dms = await wait_message.author.create_dm()  # メッセージ送信者へDM作成
                randam_dm.append(dms)  # ユーザーを保存
                await message.channel.send(wait_message)
        await message.channel.send('受付終了')
        for dm in randam_dm:
            content = random.choice(random_content)  # 送信するメッセージをランダムで決める
            await dm.send(content)  # DM送信
        randam_dm.clear()
    # /randamDM2を入力した人を対象にする方式　/randamDMEndのチャットが来ることで対象者にDMが送信される。
    elif message.content == "/randamDM2":
        dms = await message.author.create_dm()  # メッセージ送信者へDM作成
        randam_dmSecond.append(dms)  # ユーザーを保存
    elif message.content == "/randamDMEnd":
        random_content = ['はむすき', 'はむきらい', 'はむふつう']
        for dm in randam_dmSecond:
            content = random.choice(random_content)  # 送信するメッセージをランダムで決める
            await dm.send(content)  # DM送信
        randam_dmSecond.clear()
        await message.channel.send('終了')
    


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
