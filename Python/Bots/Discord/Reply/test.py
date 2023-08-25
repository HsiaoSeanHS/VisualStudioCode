# import requests

# # Set your custom API endpoint URL here
# custom_api_endpoint = "https://free.churchless.tech/v1/chat/completions"

# def get_bot_response(user_input):
#     payload = {
#         "prompt": f"You: {user_input}\nBot:",
#         "max_tokens": 50,  # Adjust the response length as needed
#     }
#     try:
#         response = requests.post(custom_api_endpoint, json=payload)
#         response_data = response.json()
#         print("Response:", response_data)  # Print the full response for debugging
#         bot_response = response_data.get("text", "").strip()
#     except Exception as e:
#         print("Error:", e)
#         bot_response = "An error occurred while processing the request."
#     return bot_response

# # Main interaction loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Bot: Goodbye!")
#         break
#     bot_response = get_bot_response(user_input)
#     print(f"Bot: {bot_response}")

# Not responding

# from hugchat import hugchat
# from hugchat.login import Login

# email = "hsiaoseanhs@gmail.com"
# passwd = "zAq!2WsE3$"

# # 登入huggingface授权huggingchat
# sign = Login(email, passwd)
# cookies = sign.login()

# # 保存cookies至 usercookies/<email>.json
# sign.saveCookiesToDir("./Discord/Reply/Cookies")

# # 创建一个 ChatBot
# chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# # 创建一个新会话
# id = chatbot.new_conversation()


# while True:
#     chatbot.change_conversation(id)
#     urin = input("You: ")
#     if urin == "exit": break
#     print("Bot: " + chatbot.chat(urin))
#     conversation_list = chatbot.get_conversation_list()
#     print(conversation_list)

# for id in conversation_list: chatbot.delete_conversation(id)

# print("Done.")

# 获取对话列表
# conversation_list = chatbot.get_conversation_list()

# Only one time reply

# import os, time

# from hugchat_api import HuggingChat
# from hugchat_api.core import ListBots
# from hugchat_api.utils import formatHistory, formatConversations

# # EMAIL = os.getenv("hsiaoseanhs@gmail.com")
# # PASSWD = os.getenv("zAq!2WsE3$")
# # COOKIE_STORE_PATH = "./usercookies"

# '''create ThreadPool'''
# HUG = HuggingChat(max_thread=1)


# '''initialize sign in funciton'''
# # sign = HUG.getSign(EMAIL, PASSWD)

# '''sign in or...'''
# # cookies = sign.login(save=True, cookie_dir_path=COOKIE_STORE_PATH)
# # cookies = sign.loadCookiesFromDir()



# '''create bot with MetaAI's model'''
# bot = HUG.getBot(email=email, cookies=cookies, model=ListBots.META_70B_HF)

# '''get all conversations and see one's title'''
# conversations = bot.getConversations()
# conv_id = list(conversations.keys())[0]
# # print(conversations[conv_id])

# '''get all chat histories by conversation_id'''
# histories = bot.getHistoriesByID(conversation_id=conv_id)
# # print(formatHistory(histories))

# '''delete a conversation'''
# bot.removeConversation(conversation_id=conv_id)

# '''create a new conversation'''
# conversation_id = bot.createConversation()

# '''chat'''
# while True:
#     user_input = input("You: ")
#     message = bot.chat(
#         text=user_input,
#         conversation_id=conversation_id,
#         web_search=True,
#         max_tries=2,
#         # callback=(bot.updateTitle, (conversation_id,))
#     )



#     '''wait the full text or...'''
#     while not message.web_search_done:
#         time.sleep(0.1)
#     # print(message.getWebSearchSteps())
#     while not message.isDone():
#         time.sleep(0.1)
#     print("Bot: " + message.getFinalText())

#     '''get the stream text instantly'''
#     # print(message.getWebSearchSteps())
#     # print(message.getText())

PAs = open("D:/PA.txt", "r")
lines = PAs.readlines()
PAs.close()

for line in lines:
    line = line.replace("\n", "")
    if line.find("Email") == 0:
        email = line.split(" ")[1]
        print(email[5:9])
    if line.find("Huggingface") == 0:
        passwd = line.split(" ")[1]
        print(passwd)
        # break

# import sys
# sys.path.insert(0, '../')

# from PA import PW

# Email, Password = PW("HuggingFace")
# print(Email)
# print(Password)