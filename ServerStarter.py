import subprocess
import discord
from discord.ext import commands
from dislash import slash_commands, Option, OptionType

summer = commands.Bot(command_prefix = '/') #これがないとスラッシュコマンドを定義できない
slash = slash_commands.SlashClient(summer) #スラッシュコマンド
summer_guilds = [999899466020687882]

@slash.command(
    name = 'start',
    description = 'サーバーを起動します',
    guild_ids = summer_guilds # この引数を省略すれば、このBotを招待したサーバー全てで使えるコマンドになる
)
async def test(inter):
    embed=discord.Embed(title="サーバーを起動しています...", description="これには時間がかかる場合があります", color=0xff0000)
    await inter.reply(embed=embed)
    subprocess.run("起動用.bat", shell=True) #subprocessモジュールでbatを実行させる

summer.run("")
