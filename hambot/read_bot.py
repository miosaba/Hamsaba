import discord
from discord.ext import commands
import subprocess
import ffmpeg
import tokun
from voice_generator import creat_WAV


client = commands.Bot(command_prefix='.')
voice_client = None



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def join(ctx):
    #Botをボイスチャンネルに入室。
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        #もし送信者がどこのチャンネルにも入っていないなら
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel #送信者のチャンネル

    await channel.connect() #VoiceChannel.connect()を使用

@client.command()
async def bye(ctx):
    #切断
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    #読み上げ
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print(message.content)
            creat_WAV(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass


client.run(tokun.TOKUN)
