import random

from collection import messageCollection

async def jinro_bot_reply_ready(client, jobAllocationList:list, jinro_entry_dict:dict):

    jobAllocationList.clear()
    # カスタム絵文字をメッセージに追加
    for emoji in messageCollection.myWerewolfEmojiDict.values():
        await message.add_reaction(emoji)
    botMessage = message

    while message.content != "/end":  # 文字列判定
        message = await client.wait_for("message")

        sum = 0
        for reaction in botMessage.reactions:
            if(reaction.count-1 > 0):
                for i in range(reaction.count-1):
                    sum += 1

        # 参加人数と役職調整の数が妥当かチェック
        if(len(jinro_entry_dict) != sum):
            message.content = ""
            await message.channel.send('参加人数と役職調整の数が合いません')

    await message.channel.send('役職調整終了')

    # 役職調整をもとに役職準備
    for reaction in botMessage.reactions:
        if(reaction.count-1 > 0):
            for i in range(reaction.count-1):
                jobAllocationList.append(reaction.emoji.name)

    # 役職リストをシャッフル
    random.shuffle(jobAllocationList)
    # 役職振分
    for dm_entry_dict in jinro_entry_dict.values():
        job = jobAllocationList.pop()

        jobAllocationDict[dm_entry_dict] = job

        # 送信するメッセージをランダムで決める
        content = messageCollection.myWerewolfPositionDict[job.capitalize()]
        await dm_entry_dict.send(content)
        print(jobAllocationDict)
