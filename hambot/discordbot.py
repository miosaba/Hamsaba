#インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/Instructions':#説明書
        await message.channel.send(
        'このbotは特定の単語に反応して発言します\n気が向いたときに更新していますので遊んであげてください\n現在手動で稼働しているので常時反応することができません')
    if message.content == '/DM':#dm送信
        dm=await message.author.create_dm()#メッセージ送信者へDM作成
        await dm.send('これは秘密のメッセージだぞ')#DM送信
    if message.content == '/command':#コマンド表示
        await message.channel.send(
        'Instructions,DM')
    if message.content.startswith('HamterRAW')or 'HamterRAW' in message.content:#文字列の開始が一致
        member_mention="<@312554285009469442>"#これでいける
        await message.channel.send(f'{member_mention}おい呼ばれてるぞ')
    elif message.content =='ハム'or 'ハム'in message.content:
        await message.channel.send('ローストハム')
    elif '太郎' in message.content:
        await message.channel.send('ヘケッ')
    elif message.content =='Ham':
        await message.channel.send('大好きなのは血だまりと金')
    elif message.content =='ビビりハム':
        await message.channel.send('ヘッドフォンぶん投げHamterRAW')
    elif message.content =='嫌い':
        await message.channel.send('Ham好きkillyou')
    elif message.content =='ham':
        await message.channel.send('あほのham')
    if 'はむカービィ'in message.content:
        await message.channel.send('俺はむらびと使い')
    if 'LeGal' in message.content or 'リーガルさん' in message.content:
        await message.channel.send('キャー素敵なのだぁ!!')
    
    #ランダム表示 ok
    random_contents = ["にゃーん","わん！","コケッコッコー",]
    if message.content == "ないて":
        content = random.choice(random_contents)# 送信するメッセージをランダムで決める
        await message.channel.send(content) # メッセージが送られてきたチャンネルに送
#複数人にDMを送る#R.I.P
    randam_dm=[]
    random_content=['はむすき','はむきらい','はむふつう']
    wait_message='hello'
    if message.content == "/randamDM":
        await message.channel.send('何かコメントして /endで終了')
        while wait_message == "/end":#文字列判定
            wait_message = await client.wait_for("message")#ユーザーからのメッセージを待つ
            if wait_message !="/end":
                dms=await message.author.create_dm()#メッセージ送信者へDM作成
                randam_dm.append(dms)#ユーザーを保存
        for dm in randam_dm:
            content = random.choice(random_content)# 送信するメッセージをランダムで決める
            await dm.send(content)#DM送信
        randam_dm.clear()



#Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
