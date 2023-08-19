import discord
import asyncio
import aiohttp
import keep_alive

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents = intents)
online = discord.Game("Server is online.")
offline = discord.Game("Server is offline.")
outline = discord.Game("Bot is broken or checking website is not responding.")
to = "111 "             # Need to change
k = "222 "              # Need to change
en = "333"              # Need to change
T = to + k + en
T = T.replace(" ", ".")
Server_IP = "server.ip" # Need to change


async def fetch_website_value():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://api.mcstatus.io/v2/status/java/" + Server_IP)
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
    broken = False # Variables with condition cannot be Global variable
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
                        await channel.send(Server_IP + "復活了")
                        broken = False
                    await client.change_presence(status = discord.Status.online, activity = online)
                else:
                    broken = True
                    await client.change_presence(status = discord.Status.do_not_disturb, activity = offline)
        except: 
            broken = True
            await client.change_presence(status = discord.Status.idle, activity = outline)
            fail_times += 1
            print("失敗了", end = ""), print(fail_times, end = ""), print("次")
            # if fail_times > 10:
            #     print("嘗試次數已超過10次")
            #     break
            await asyncio.sleep(60)
            continue
        await asyncio.sleep(10)

keep_alive.keep_alive()
client.run(T)
