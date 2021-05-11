
import discord

class discordCommon():

    # await instans.participant_recruiting(dict:Dict, message, client)
    async def participant_recruiting(self, dictionary, message, client):
        await message.channel.send('何かコメントして /endで終了')
        while message.content != "/end":  # 文字列判定
            message = await client.wait_for("message")  # ユーザーからのメッセージを待つ
            if message.content == "/参加数":
                    await message.channel.send('現在'+ str(len(dictionary)) + '名参加中')
            else:
                dms = await message.author.create_dm()  # メッセージ送信者へDM作成
                check_dict = dict(dictionary)
                # 重複チェックしユーザーを保存 
                if len(dictionary) != 0:
                    for dm in check_dict.values():
                        if(dm.id != dms.id):
                            dictionary[dms.id] = dms  
                else:
                    dictionary[dms.id] = dms
        await message.channel.send('受付終了')