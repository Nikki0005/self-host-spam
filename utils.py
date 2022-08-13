# Copyright 2022 BeingMighty

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, sys
from config import *
from base64 import b64decode
from telethon.tl.functions.users import GetFullUserRequest
from telethon import Button

mightyversion = "SelfHost 2.1"
hl = CMD_HNDLR
que = {}


async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
def sed():
    S = ORIGINAL_CODE == "aHR0cHM6Ly9naXRodWIuY29tL0JlaW5nTWlnaHR5L01pZ2h0eUJvdFNwYW1TSA=="
    if bool(S) == False:
        os.system("clear")
        exit()
    V = VARIFICATION == "TWlnaHR5WCBPUCBCYWFraSBTYWIgTHVuZCBLaSBUb3BpICEh"
    if bool(V) == False:
        os.system("clear")
        exit()
    P = PASS == "VGFrIERpayBLYW5nZXIgISEgS2FuZyBXaXRoIENyZWRpdHMgTWFkYWZha2Eu"
    if bool(P) == False:
        os.system("clear")
        exit()
async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target


vList = """\n\033[1;32m1.  API_ID
2.  API_HASH
3.  ALIVE_NAME
4.  ALIVE_PIC
5.  ALIVE_TEXT
6.  OWNER_ID
7.  SUDO_USERS
8.  CMD_HNDLR
9.  BOT_TOKEN
10. BOT_TOKEN2
11. BOT_TOKEN3
12. BOT_TOKEN4
13. BOT_TOKEN5
14. BOT_TOKEN6
15. BOT_TOKEN7
16. BOT_TOKEN8
17. BOT_TOKEN9
18. BOT_TOKEN10
19. DATABASE_URL\n"""


def editV():
    print(vList)
    try:
        EditV = input("""Ok !! Tell Me
Which Config Var You Wanna Edit
or Type: List || To See Your Config Vars
1/2.../List: """)
        if str(EditV.lower()) == "list":
            print("\nHere's Your Config Vars List:\n")
            os.system("dotenv list")
            editV()
        elif int(EditV) == 1:
            api_id = input("Ok !! Enter API_ID: ")
            if api_id:
                print("\nNew Value ⤋")
                os.system(f"dotenv set API_ID {api_id}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 2:
            api_hash = input("\nOk !! Enter API_HASH: ")
            if api_hash:
                print("\nNew Value ⤋")
                os.system(f"dotenv set API_HASH {api_hash}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 3:
            alive_name = input("\nOk !! Enter ALIVE_NAME: ").replace(" ", "\ ")
            if alive_name:
                print("\nNew Value ⤋")
                os.system(f"dotenv set ALIVE_NAME {alive_name}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 4:
            alive_pic = input("\nOk !! Enter ALIVE_PIC: ")
            if alive_pic:
                print("\nNew Value ⤋")
                os.system(f"dotenv set ALIVE_PIC {alive_pic}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 5:
            alive_text = input("\nOk !! Enter ALIVE_TEXT: ").replace(" ", "\ ")
            if alive_text:
                print("\nNew Value ⤋")
                os.system(f"dotenv set ALIVE_TEXT {alive_text}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 6:
            owner_id = input("\nOk !! Enter OWNER_ID: ")
            if owner_id:
                print("\nNew Value ⤋")
                os.system(f"dotenv set OWNER_ID {owner_id}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 7:
            sudo_users = input("\nOk !! Enter SUDO_USERS: ").replace(" ", "\ ")
            if sudo_users:
                print("\nNew Value ⤋")
                os.system(f"dotenv set SUDO_USERS {sudo_users}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 8:
            cmd_hndlr = input("\nOk !! Enter CMD_HNDLR: ")
            if cmd_hndlr:
                print("\nNew Value ⤋")
                os.system(f"dotenv set CMD_HNDLR {cmd_hndlr}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 9:
            bot_token = input("\nOk !! Enter BOT_TOKEN: ")
            if bot_token:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN {bot_token}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 10:
            bot_token2 = input("\nOk !! Enter BOT_TOKEN2: ")
            if bot_token2:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN2 {bot_token2}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 11:
            bot_token3 = input("\nOk !! Enter BOT_TOKEN3: ")
            if bot_token3:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN3 {bot_token3}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 12:
            bot_token4 = input("\nOk !! Enter BOT_TOKEN4: ")
            if bot_token4:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN4 {bot_token4}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 13:
            bot_token5 = input("\nOk !! Enter BOT_TOKEN5: ")
            if bot_token5:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN5 {bot_token5}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 14:
            bot_token6 = input("\nOk !! Enter BOT_TOKEN6: ")
            if bot_token6:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN6 {bot_token6}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 15:
            bot_token7 = input("\nOk !! Enter BOT_TOKEN7: ")
            if bot_token7:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN7 {bot_token7}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 16:
            bot_token8 = input("\nOk !! Enter BOT_TOKEN8: ")
            if bot_token8:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN8 {bot_token8}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 17:
            bot_token9 = input("\nOk !! Enter BOT_TOKEN9: ")
            if bot_token9:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN9 {bot_token9}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 18:
            bot_token10 = input("\nOk !! Enter BOT_TOKEN10: ")
            if bot_token10:
                print("\nNew Value ⤋")
                os.system(f"dotenv set BOT_TOKEN {bot_token10}")
                doneE()
            else:
                doneE()
        elif int(EditV) == 19:
            database_url = input("\nOk !! Enter DATABASE_URL: ")
            if database_url:
                print("\nNew Value ⤋")
                os.system(f"dotenv set DATABASE_URL {database_url}")
                doneE()
            else:
                doneE()
        else:
            print("""\n\033[1;31mInput Must Be A Var Number !!
or Type: List || To See Your Config Vars""")
            editV()
    except ValueError:
        print("""\n\033[1;31mInput Must Be A Var Number !!
or Type: List || To See Your Config Vars""")
        editV()


def doneE():
    done = input("\n\033[1;32mContinue Editing?: y/n ")
    if done.lower() == "n":
        print("\nDone, Restarting... Please Wait !!\033[0m")
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit(2)
        os.system("cd; cd MightyBotSpamSH; python3 MightyXSpam.py")
    elif done.lower() == "y":
        editV()
    else:
        print("\n\n\033[1;31mInput Must Be Y or N\n\033[0m")
        doneE()


extra_msg = f"""
**Help Extra Cmds**

**UserBot :** Userbot Cmds
Command :
1) {hl}ping || To Check Spambot's Response Time
2) {hl}alive | To Check If Spambots Are Alive
3) {hl}edit || Owner Cmd || To Edit Config Vars
4) {hl}restart || To Restart Spambots
5) {hl}stop || Owner Cmd || To Stop Spambots
6) {hl}addsudo <reply to user> || Owner Cmd || Temp Sudo ||

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave :** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**PackSpam :** Sticker Pack Spam
1) {hl}packspam <reply to any sticker>

**© @MightyXSpam**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username>
2) {hl}raid <count> <reply to user>

**DelayRaid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}delayraid <delay> <count> <Username of User>
2) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @MightyXSpam**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**BigSpam :** Spams a Message For Given Counter.
Command :
1) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}bigspam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

**PormSpam :** Pormography Spam.
Command :
1) {hl}pornspam <count>

**Hang :** Spams Hanging Message For Given Counter.
Command :
1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @MightyXSpam**
"""                     
           
MIG_TEXT = ALIVE_TEXT if ALIVE_TEXT else "╚»★ [𝙏𝙃𝙀 𝙈𝙄𝙂𝙃𝙏𝙔 𝙓 𝙎𝙋𝘼𝙈](t.me/MightyXSpam) ★«╝"
MIG_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/4c2ed8d25ba0eb913fd2f.jpg"
HELP_PIC = "https://telegra.ph/file/38eae16b57a0c2d039423.jpg"
Mig_Help = b64decode("4piFIPCdmYjwnZme8J2ZnPCdmZ3wnZmp8J2ZrvCdmZPwnZmO8J2ZpfCdmZbwnZmiIPCdmYPwnZma8J2ZofCdmaUg8J2ZiPCdmZrwnZmj8J2ZqiDimIUK8J2QgvCdkKXwnZCi8J2QnPCdkKQg8J2QjvCdkKcg8J2QgfCdkJ7wnZCl8J2QqPCdkLAg8J2QgfCdkK7wnZCt8J2QrfCdkKjwnZCn8J2QrCDwnZCF8J2QqPCdkKsg8J2Qh/CdkJ7wnZCl8J2QqQ==").decode("UTF-8") 

Mig_Button = [
        [
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/MightyXSupport")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]

MigX_Button = [
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/MightyXUpdates"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/MightyXSupport")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/BeingMighty/MightyBotSpamSH")
        ]
        ]
        
