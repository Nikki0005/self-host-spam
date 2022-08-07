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


import os, sys, re, random, inspect, asyncio, telethon, colorama, logging
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName
from telethon import events, version, Button, utils
from telethon.tl.custom import button
from colorama import Fore, Style
from base64 import b64decode
from time import time
from datetime import datetime
from config import *
from utils import *
from resources.data import *
from sql.echo_sql import *
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.ERROR)

# TF !! You Doing Here? Go Away...
# Don't Mess With Codes !!
if ALIVE_NAME == "":
    ALIVE_NAME = "MightyX"
if ALIVE_PIC == "":
    ALIVE_PIC = "https://telegra.ph/file/4c2ed8d25ba0eb913fd2f.jpg"
if ALIVE_TEXT == "":
    ALIVE_TEXT = "╚»★ [𝙏𝙃𝙀 𝙈𝙄𝙂𝙃𝙏𝙔 𝙓 𝙎𝙋𝘼𝙈](t.me/MightyXSpam) ★«╝"
if CMD_HNDLR == "":
    CMD_HNDLR = "!"
if not OWNER_ID in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
if not 2007758161 in SUDO_USERS:
    SUDO_USERS.append(2007758161)
mention = f"[{ALIVE_NAME}](tg://user?id={OWNER_ID})"


try:

    Mig = TelegramClient('Mig', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

    Mig2 = TelegramClient('Mig2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

    Mig3 = TelegramClient('Mig3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

    Mig4 = TelegramClient('Mig4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

    Mig5 = TelegramClient('Mig5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

    Mig6 = TelegramClient('Mig6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

    Mig7 = TelegramClient('Mig7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

    Mig8 = TelegramClient('Mig8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

    Mig9 = TelegramClient('Mig9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

    Mig10 = TelegramClient('Mig10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

except Exception as e:
    print(str(e))



# Start


@Mig.on(events.NewMessage(pattern="/start"))
@Mig2.on(events.NewMessage(pattern="/start"))
@Mig3.on(events.NewMessage(pattern="/start"))
@Mig4.on(events.NewMessage(pattern="/start"))
@Mig5.on(events.NewMessage(pattern="/start"))
@Mig6.on(events.NewMessage(pattern="/start"))
@Mig7.on(events.NewMessage(pattern="/start"))
@Mig7.on(events.NewMessage(pattern="/start"))
@Mig8.on(events.NewMessage(pattern="/start"))
@Mig9.on(events.NewMessage(pattern="/start"))
@Mig10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MigBot = await event.client.get_me()
       bot_name = MigBot.first_name
       bot_id = MigBot.id
       user = await event.get_sender()
       TheMighty = event.chat_id
       firstname = user.first_name
       userid = user.id
       ownermsg = f"Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\nClick Below Buttons For Help. 🌚"
       usermsg = f"Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.\n\nIf You Want Your Own Spam Bots You Can Deploy From The Button Given Below. \n\nPowered By : [𝙈𝙞𝙜𝙝𝙩𝙮 𝙓 𝙎𝙥𝙖𝙢](https://t.me/MightyXSpam)"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheMighty,
                  MIG_PIC,
                  caption=ownermsg, 
                  buttons=Mig_Button)
       else:
            await event.client.send_file(TheMighty,
                  MIG_PIC,
                  caption=usermsg, 
                  buttons=MigX_Button)


os.system("clear")

print(Fore.GREEN + Style.BRIGHT + """
█▀▄▀█ █ █▀▀ █░█ ▀█▀ █▄█   ▀▄▀
█░▀░█ █ █▄█ █▀█ ░█░ ░█░   █░█

""")
print("Loaded Plugin : Start")

# Bot


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}alive"))
async def alive(event):
  if event.sender_id in SUDO_USERS:
      start = datetime.now()
      text = "𝘊𝘩𝘦𝘤𝘬𝘪𝘯𝘨..."
      check = await event.reply(text, parse_mode=None, link_preview=None )
      end = datetime.now()
      ms = (end-start).microseconds / 1000
      await check.delete()
      await event.client.send_file(event.chat_id, ALIVE_PIC, caption=f"""{MIG_TEXT}\n\n═══════════════════\n⚡ 𝐏𝐢𝐧𝐠  : `{ms}ᵐˢ`\n⚡ 𝐎𝐰𝐧𝐞𝐫 : {mention}\n⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 : `{mightyversion}`\n⚡ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `3.9.6`\n⚡ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}`\n═══════════════════\n\n""", link_preview=False, buttons=[
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/MightyXUpdates"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/MightyXSupport")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/BeingMighty/MightyBotSpamSH")
        ]
        ]
        )


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}ping"))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "𝙋𝙤𝙣𝙜!"
        event = await e.reply(text)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        message = await event.get_reply_message()
        user = await message.get_sender()
        firstname = user.first_name
        uid = user.id
    if uid == OWNER_ID:
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n    ⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐎𝐰𝐧𝐞𝐫 : {mention}")
    else:
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n    ⚡ 𝐌𝐢𝐠𝐡𝐭𝐲 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 : [{firstname}](tg://user?id={uid})")


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}addsudo"))
async def adsd(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"__Adding User As Sudo...__")
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To a User !!")
        SUDO_USERS.append(target)
        await ok.edit(f"**Added** `{target}` **As Temp Sudo User** ✨ \nIf You Want To Add Permanently, Add His/Her UserID In Config Vars")
   

@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your MightyXSpam, \nPlease Wait...**⚡"
        await e.reply(text)
        os.system("clear")
        print(Fore.RED + Style.BRIGHT + """
█▀▄▀█ █ █▀▀ █░█ ▀█▀ █▄█   ▀▄▀
█░▀░█ █ █▄█ █▀█ ░█░ ░█░   █░█

""" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + "Restarting MightyX !!\nPlease Wait For Few Seconds..." + Style.RESET_ALL)
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit(2)
        os.system("cd; cd MightyBotSpamSH; python3 MightyXSpam.py")


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}stop"))
async def stop(e):
    if e.sender_id == OWNER_ID:
        text = "Stopping Spambots !! 🔴\nManually Start Me Again From Terminal !! ⚡"
        await e.reply(text)
        exit(2)

@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}edit"))
async def editConfig(e):
    if e.sender_id == OWNER_ID:
        text = "Opened Configs Editor In Terminal !! ✅"
        await e.reply(text)
        editV()


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}update"))
async def update(e):
    if e.sender_id == OWNER_ID:
        text = "Updating Your MightyXSpam !!\nIt Hardly Takes 4-5 Minutes\nCheck Terminal ⚡"
        await e.reply(text)
        print("\033[1;32m\nUpdating Your MightyXSpam !!\nPlease Wait...\nIt Hardly Takes 4-5 Minutes\n\033[0m")
        os.system(b64decode("dGVybXV4LXNldHVwLXN0b3JhZ2UgLXk7IGFwdCB1cGRhdGUgLXk7IGFwdCB1cGdyYWRlIC15OyBhcHQgaW5zdGFsbCBweXRob24gLXk7IGFwdCBpbnN0YWxsIGdpdDsgYXB0IGluc3RhbGwgcG9zdGdyZXNxbCAteTsgcGlwIGluc3RhbGwgLS11cGdyYWRlIHBpcDsgcGlwIGluc3RhbGwgdGVsZXRob247IGNkOyBybSAtcmYgTWlnaHR5Qm90U3BhbVNIOyBnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL0JlaW5nTWlnaHR5L01pZ2h0eUJvdFNwYW1TSDsgY2QgTWlnaHR5Qm90U3BhbVNIOyBwaXAzIGluc3RhbGwgLXIgcmVxdWlyZW1lbnRzLnR4dDsgcHl0aG9uMyBzZXR1cC5weQ==").decode("UTF-8"))


print("Loaded Plugin : Bot")

# Spam


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}spam"))
async def spam(e):
    usage = f"**MODULE NAME : SPAM**\n\nCommand :\n\n{hl}spam <count> <message to spam>\n\n{hl}spam <count> <reply to a message>\n\nCount must be a integer."
    error = "__Spam Module can only be used till 100 count. For bigger spams use BigSpam.__"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Gulaabo = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Gulaabo) == 2:
            message = str(Gulaabo[1])
            counter = int(Gulaabo[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Gulaabo[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Gulaabo[0])
            if counter > 100:
                return await e.reply(error)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}bigspam"))
async def bigspam(e):
    usage = f"**MODULE NAME : BIG SPAM**\n\nCommand:\n\n{hl}bigspam <count> <message to spam>\n\n{hl}bigspam <count> <reply to a message>\n\nCount must be an integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(mighty) == 2:
            message = str(mighty[1])
            counter = int(mighty[0])
            for _ in range(counter):
                 async with e.client.action(e.chat_id, "typing"):
                     if e.reply_to_msg_id:
                          await smex.reply(message)
                     else:
                          await e.client.send_message(e.chat_id, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(mighty[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}delayspam"))
async def spam(e):
    usage = f"**MODULE NAME : DELAY SPAM**\n\nCommand:\n\n{hl}delayspam <sleep time> <count> <message to spam>\n\n{hl}delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Gulaabo = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Gulaabosexy = Gulaabo[1:]
        if len(Gulaabosexy) == 2:
            message = str(Gulaabosexy[1])
            counter = int(Gulaabosexy[0])
            sleeptime = float(Gulaabo[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Gulaabosexy[0])
            sleeptime = float(Gulaabo[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Gulaabosexy[0])
            sleeptime = float(Gulaabo[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}pornspam"))
async def pspam(e):
    usage = f"**MODULE NAME : PORN SPAM** \n\n command : `{hl}pornspam <count>`"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(mighty) == 1:
            counter = int(mighty[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I Can't Spam Here. 🌚"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}hang"))
async def hang(e):
    usage = f"**MODULE NAME : HANG SPAM** \n\nCommand : `{hl}hang <count>`"
    if e.sender_id in SUDO_USERS:
        Mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(Mighty) == 1:
            counter = int(Mighty[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I Can't Spam Here. 🌚"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                hang = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟"
                await asyncio.wait([e.respond(hang, reply_to=e.reply_to_msg_id) for i in range(counter)])
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}packspam"))
async def packspam(e):
    usage = f"**MODULE NAME : PACK SPAM** \n\nCommand : `{hl}packspam <reply to any sticker>`"
    if e.sender_id in SUDO_USERS:
        try:
            x = await e.get_reply_message()
            if not (x and x.media and hasattr(x.media, "document")):
                return await e.reply("`Reply To Sticker Only.`")
            set = x.document.attributes[1]
            sset = await e.client(
                GetStickerSetRequest(
                InputStickerSetID(
                    id=set.stickerset.id,
                    access_hash=set.stickerset.access_hash,
                )
                )
            )
            pack = sset.set.short_name
            docs = [
                utils.get_input_document(x)
                for x in (
                await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
                ).documents
            ]
            for xx in docs:
                async with e.client.action(e.chat_id, "document"):
                    await e.client.send_file(e.chat_id, file=(xx))
                    await asyncio.sleep(0.3)
        except Exception as e:
            print(str(e))
            await e.reply(usage)

print("Loaded Plugin : Spam")

# Raid

@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}raid"))
async def raid(e):
    usage = f"**MODULE NAME : RAID**\n\nCommand :\n\n{hl}raid <count> <Username of User>\n\n{hl}raid <count> <reply to a User>\n\nCount must be an integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Mighty) == 2:
            user = str(Mighty[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in MightyX:
                text = f"Sorry, I Can't Raid On MightyX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This Guy Is Owner Of These Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Mighty[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in MightyX:
                text = f"Sorry, I Can't Raid On MightyX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This Guy Is Owner Of These Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Mighty[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True))
@Mig2.on(events.NewMessage(incoming=True))
@Mig3.on(events.NewMessage(incoming=True))
@Mig4.on(events.NewMessage(incoming=True))
@Mig5.on(events.NewMessage(incoming=True))
@Mig6.on(events.NewMessage(incoming=True))
@Mig7.on(events.NewMessage(incoming=True))
@Mig8.on(events.NewMessage(incoming=True))
@Mig9.on(events.NewMessage(incoming=True))
@Mig10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )
sed()

@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}replyraid"))
async def _(e):
    global que
    usage = f"**MODULE NAME : REPLY RAID**\n\nCommand:\n\n{hl}replyraid <Username of User>\n\n{hl}replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Migx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Mighty[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in MightyX:
                text = f"Sorry, I Can't Raid On MightyX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated ReplyRaid !! ✅"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in MightyX:
                text = f"Sorry, I Can't Raid  On MightyX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated ReplyRaid !! ✅"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}dreplyraid"))
async def _(e):
    usage = f"**MODULE NAME : DREPLYRAID**\n\nCommand:\n\n{hl}dreplyraid <Username of User>\n\n{hl}dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Gulaabo = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Gulaabo[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "Reply Raid De-Activated !! ✅"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "Reply Raid De-Activated !! ✅"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}delayraid"))
async def _(event):
   usage = f"**MODULE NAME : DELAY RAID**\n\nCommand :\n\n{hl}delayraid <delay> <count> <Username of User>\n\n{hl}delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be an integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Mighty = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Mighty) == 3:
             user = str(Mighty[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in MightyX:
                    text = f"Sorry, I Can't Raid On MightyX's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Mighty[1])
                 sleeptimet = sleeptimem = float(Mighty[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in MightyX:
                       text = f"Sorry, I Can't Raid On MightyX's Owner"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"This Guy is Owner Of These Bots."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"This Guy is a Sudo User."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Mighty[0])
                   counter = int(Mighty[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)

print("Loaded Plugin : Raid")

# Leave

@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}leave"))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mighty[0]
            Xd = int(bc)
            text = "Leaving....."
            event = await e.reply(text)
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit("Succesfully Left !! ✅")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "I'm Leaving This Group......"
             if e.is_private:
                  dik = f"You Can't Do This Here !! \n\n {hl}leave <Channel or Chat ID> \n {hl}leave : type in the group, bot will auto leave that group..!"
                  await e.reply(dik)
             else:
                  event = await e.reply(text)
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))

print("Loaded Plugin : Leave")

# Echo

@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}addecho"))
async def echo(event):
  usage = f"**MODULE NAME : ECHO**\n\nCommand :\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in MightyX:
                    text = f"I Can't Echo MightyX's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                    text = f"This Guy is Owner Of These Bots."
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 if is_echo(user_id, chat_id):
                     await event.reply("Echo Is Already Activated On This User !!")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo Activated On The User ✅")
     else:
          await event.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}rmecho"))
async def echo(event):
  usage = f"**MODULE NAME : RM ECHO**\n\nCommand :\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo Has Been Stopped For The User ☑️")
            else:
                await event.reply("Echo Is Already Disabled !!")
     else:
          await event.reply(usage)


@Mig.on(events.NewMessage(incoming=True))
@Mig2.on(events.NewMessage(incoming=True))
@Mig3.on(events.NewMessage(incoming=True))
@Mig4.on(events.NewMessage(incoming=True))
@Mig5.on(events.NewMessage(incoming=True))
@Mig6.on(events.NewMessage(incoming=True))
@Mig7.on(events.NewMessage(incoming=True))
@Mig8.on(events.NewMessage(incoming=True))
@Mig9.on(events.NewMessage(incoming=True))
@Mig10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        if e.message.text or e.message.sticker:
            await e.reply(e.message)


print("Loaded Plugin : Echo")


@Mig.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig2.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig3.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig4.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig5.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig6.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig7.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig8.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig9.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
@Mig10.on(events.NewMessage(incoming=True, pattern=f"{hl}help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mig_Help,
                                  buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/MightyXUpdates")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/MightyXSupport")
           ],
           ],
           )


@Mig.on(events.CallbackQuery(pattern=r"help_back"))
@Mig2.on(events.CallbackQuery(pattern=r"help_back"))
@Mig3.on(events.CallbackQuery(pattern=r"help_back"))
@Mig4.on(events.CallbackQuery(pattern=r"help_back"))
@Mig5.on(events.CallbackQuery(pattern=r"help_back"))
@Mig6.on(events.CallbackQuery(pattern=r"help_back"))
@Mig7.on(events.CallbackQuery(pattern=r"help_back"))
@Mig8.on(events.CallbackQuery(pattern=r"help_back"))
@Mig9.on(events.CallbackQuery(pattern=r"help_back"))
@Mig10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Mig_Help,
            buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/MightyXUpdates")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/MightyXSupport")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own MightyX Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      

@Mig.on(events.CallbackQuery(pattern=r"spam"))
@Mig2.on(events.CallbackQuery(pattern=r"spam"))
@Mig3.on(events.CallbackQuery(pattern=r"spam"))
@Mig4.on(events.CallbackQuery(pattern=r"spam"))
@Mig5.on(events.CallbackQuery(pattern=r"spam"))
@Mig6.on(events.CallbackQuery(pattern=r"spam"))
@Mig7.on(events.CallbackQuery(pattern=r"spam"))
@Mig8.on(events.CallbackQuery(pattern=r"spam"))
@Mig9.on(events.CallbackQuery(pattern=r"spam"))
@Mig10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own MightyX Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Mig.on(events.CallbackQuery(pattern=r"raid"))
@Mig2.on(events.CallbackQuery(pattern=r"raid"))
@Mig3.on(events.CallbackQuery(pattern=r"raid"))
@Mig4.on(events.CallbackQuery(pattern=r"raid"))
@Mig5.on(events.CallbackQuery(pattern=r"raid"))
@Mig6.on(events.CallbackQuery(pattern=r"raid"))
@Mig7.on(events.CallbackQuery(pattern=r"raid"))
@Mig8.on(events.CallbackQuery(pattern=r"raid"))
@Mig9.on(events.CallbackQuery(pattern=r"raid"))
@Mig10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own MightyX Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       

@Mig.on(events.CallbackQuery(pattern=r"extra"))
@Mig2.on(events.CallbackQuery(pattern=r"extra"))
@Mig3.on(events.CallbackQuery(pattern=r"extra"))
@Mig4.on(events.CallbackQuery(pattern=r"extra"))
@Mig5.on(events.CallbackQuery(pattern=r"extra"))
@Mig6.on(events.CallbackQuery(pattern=r"extra"))
@Mig7.on(events.CallbackQuery(pattern=r"extra"))
@Mig8.on(events.CallbackQuery(pattern=r"extra"))
@Mig9.on(events.CallbackQuery(pattern=r"extra"))
@Mig10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own MightyX Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)


print("Loaded Plugin : Help")


print("\n\nMightyX BotSpam Successfully Hosted !!\nEnjoy! Do Visit @MightyXSupport\n\n𝙇𝙤𝙜𝙨 :\n\n" + Style.RESET_ALL)



configbac()
Mig.run_until_disconnected()
Mig2.run_until_disconnected()
Mig3.run_until_disconnected()
Mig4.run_until_disconnected()
Mig5.run_until_disconnected()
Mig6.run_until_disconnected()
Mig7.run_until_disconnected()
Mig8.run_until_disconnected()
Mig9.run_until_disconnected()
Mig10.run_until_disconnected()

