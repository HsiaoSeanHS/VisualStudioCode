import discord
import asyncio
import aiohttp
import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
online = discord.Game("單人伺服器")
offline = discord.Game("多人離線遊戲")
outline = discord.Game("無修正的Bug")
to = "MTEzOTE5MTQwMTY4NzU2MDM1NA "
k = "Gz5L-e "
en = "8zr-xnJT1lY5JK_DYj-3QfJYByHGqRdhfmQOCE"
T = to + k + en
T = T.replace(" ", ".")
Server_IP = "aof6steven159.3utilities.com"


async def fetch_website_value():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://sr-api.sfirew.com/server/" + Server_IP + "/")
        if response.status == 200:
            website_data = await response.json()
            await session.close()
            return website_data
        else: 
            await session.close()
            return None

@client.event
async def on_ready():
    print("The service is starting.")
    broken = False #Variables with condition cannot be Global variable
    fail_times = 0
    while True:
        try:
            website_data = await fetch_website_value()
            if website_data and "online" in website_data:
                fail_times = 0
                online_value = website_data["online"]
                if online_value is True:
                    if broken is True:
                        channel =  await client.get_channel(1139192448342569010)
                        await channel.send("伺服器復活了")
                        broken = False
                    await client.change_presence(status = discord.Status.online, activity = online)
                else:
                    broken = True
                    await client.change_presence(status = discord.Status.do_not_disturb, activity = offline)
        except: 
            broken = True
            await client.change_presence(status = discord.Status.idle, activity = outline)
            fail_times += 1
            # print("失敗了", end = ""), print(fail_times, end = ""), print("次")
            print("失敗了" + fail_times + "次")
            if fail_times > 10:
                print("嘗試次數已超過10次")
                break
            await asyncio.sleep(1)
            continue
        await asyncio.sleep(10)

keep_alive.keep_alive()
client.run(T)
