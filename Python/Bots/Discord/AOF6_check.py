import discord
import requests
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
online = discord.Game("單人伺服器")
offline = discord.Game("多人離線遊戲")
to = "MTEzOTE5MTQwMTY4NzU2MDM1NA "
k = "Gz5L-e "
en = "8zr-xnJT1lY5JK_DYj-3QfJYByHGqRdhfmQOCE"
T = to + k + en
T = T.replace(" ", ".")

def fetch_website_value():
    response = requests.get("https://sr-api.sfirew.com/server/aof6steven159.3utilities.com/")
    if response.status_code == 200:
        return response.json()
    return None

@client.event
async def on_ready():
    print("The service is starting.")
    broken = False
    while True:
        website_data = fetch_website_value()
        if website_data and "online" in website_data:
            online_value = website_data["online"]
            channel = client.get_channel(1139192448342569010)
            if online_value is True:
                if broken is True:
                    await channel.send("伺服器復活了")
                    broken = False
                await client.change_presence(status = discord.Status.online, activity = online)
            else:
                broken = True
                await client.change_presence(status = discord.Status.do_not_disturb, activity = offline)
        await asyncio.sleep(10)

client.run(T)
