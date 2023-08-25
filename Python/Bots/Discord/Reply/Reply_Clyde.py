import json
import discord
from hugchat import hugchat
from hugchat.login import Login

def AcPw(Service):
    PAs = open("D:/PA.txt", "r")
    lines = PAs.readlines()
    PAs.close()
    for line in lines:
        line = line.replace("\n", "")
        if line.find("Email") == 0: email = line.split(" ")[1]
        if line.find(Service) == 0: passwd = line.split(" ")[1]

    return email, passwd

# intents = discord.Intents.default()
intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents = intents)
to = "MTE0MzQxMDE4NTkxNDgyMjY5Nw "
k = "Gs5BON "
en = "GP_bgGZLlAgzUzx5RzGQOFsl82nNFzmCeEc9EY"
T = to + k + en
T = T.replace(" ", ".")

# target_user_id = 598368596258717718 #1081004946872352958 Clyde
target_channel_id = 1143553654293540864

try:
    cookie_json = open("D:/Cookies/hsiaoseanhs@gmail.com.json")
    chatbot = hugchat.ChatBot(cookies = json.load(cookie_json))
except:
    email, passwd = AcPw("Huggingface")
    sign = Login(email, passwd)
    cookie = sign.login()
    sign.saveCookiesToDir("D:/Cookies")
    chatbot = hugchat.ChatBot(cookies = cookie.get_dict())



async def HugCheat(id, content):
    chatbot.change_conversation(id)
    if content == "exit": 
        # conversation_list = chatbot.get_conversation_list()
        for id in chatbot.get_conversation_list(): chatbot.delete_conversation(id)
        return None
    return chatbot.chat(content)
    

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    try:
        if message.channel.id == target_channel_id:
            # if message.author.id == target_user_id:
            if message.author.id != 1143410185914822697:
                content = message.content
                try: 
                    if first == True: 
                        first = False
                        id = chatbot.new_conversation()
                except: 
                    first = True
                    id = chatbot.new_conversation()
                
                if content == "exit": 
                    await HugCheat(id, "exit")
                    await message.channel.send("||  ||")
                    first = True
                else:
                    reply_to = await message.channel.fetch_message(message.id)
                    await reply_to.reply(await HugCheat(id, content))
                print(id)
    except Exception as e:
        await message.channel.send("I'm broken.")
        print(e)
        try: 
            for id in chatbot.get_conversation_list(): chatbot.delete_conversation(id)
        except: pass

client.run(T)