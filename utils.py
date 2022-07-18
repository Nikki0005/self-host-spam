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


from config import *
from base64 import b64decode
from telethon.tl.functions.users import GetFullUserRequest
from telethon import Button

mightyversion = "SelfHost 1.0"
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


extra_msg = f"""
**Help Extra Cmds**

**UserBot :** Userbot Cmds
Command :
1) {hl}ping 
2) {hl}alive
3) {hl}restart
4) {hl}stop || Owner Cmd ||
5) {hl}addsudo <reply to user> || Owner Cmd || Temp Sudo ||

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
1) {hl}raid <count> <username
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
        
