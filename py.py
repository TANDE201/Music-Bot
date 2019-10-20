import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("디스코드봇")
    await client.change_presence(status=discord.Status.online, activity=game)

    @client.event
    async def on_message(message):
        if message.content.startswith("!하이"):
            await message.channel.send("하이")
        if message.content.startswith("!디스코드"):
            await message.channel.send("https://discord.gg/4T7k24q")
        if message.content.startswith("!노래 명령어"):
            await message.channel.send("!play,"
                                        "!skip,"
                                         "!stop")
        if message.content.startswith("!사진 명령어"):
            await message.channel.send("!사진 파일이름.jpg(1부터~73까지)")
        if message.content.startswith("!사진"):
            pic = message.content.split(" ")[1]
            await message.channel.send(file=discord.File(pic))
        if message.content.startswith("!경고 명령어"):
            await message.channel.send("!경고 ID")
        if message.content.startswith("!채널메시지 명령어"):
            await message.channel.send("!채널메시지 ID 할말")
        if message.content.startswith("!채널메시지"):
            channel = message.content[7:25]
            msg = message.content[26:]
            await client.get_channel(int(channel)).send(msg)
        if message.content.startswith("!경고"):
            author = message.guild.get_member(int(message.content [4:22]))
            file = openpyxl.load_workbook("경고.xlsx")
            sheet = file.active
            i = 1
            while True:
                if sheet["A" + str(i)].value == str(author.id):
                    sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                    file.save("경고.xlsx")
                    if sheet["B" + str(i)].value == 2:
                        await message.guild.ban(author)
                        await message.channel.send("경고 2회 누적입니다. 서버에서 추방됩니다.")
                    else:
                        await message.channel.send("경고를 1회 받았습니다.")
                    break
                if sheet["A" + str(i)].value ==None:
                    sheet["A" + str(i)].value = str(author.id)
                    sheet["B" + str(i)].value = 1
                    file.save("경고.xlsx")
                    await message.channel.send("경고를 1회 받았습니다.")
                    break
                i += 1
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
