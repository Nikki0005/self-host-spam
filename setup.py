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


import os, colorama, time
from colorama import Fore, Style

if os.path.exists(".env"):
    os.system("rm -rf .env; touch .env")

def setup():
    print(Fore.GREEN + Style.BRIGHT + """
█▀▄▀█ █ █▀▀ █░█ ▀█▀ █▄█   ▀▄▀
█░▀░█ █ █▄█ █▀█ ░█░ ░█░   █░█

\n⊰||⊹ MightyX Configs Setup ⊹||⊱\n\n""")
    time.sleep(2)
    api_id = input("Enter API_ID: ")
    if api_id:
        print("⤋")
        os.system(f"dotenv set API_ID {api_id}")
    api_hash = input("\nEnter API_HASH: ")
    if api_hash:
        print("⤋")
        os.system(f"dotenv set API_HASH {api_hash}")
    alive_name = input("\nEnter ALIVE_NAME: ")
    if alive_name:
        print("⤋")
        os.system(f"dotenv set ALIVE_NAME {alive_name}")
    alive_pic = input("\nEnter ALIVE_PIC: ")
    if alive_pic:
        print("⤋")
        os.system(f"dotenv set ALIVE_PIC {alive_pic}")
    alive_text = input("\nEnter ALIVE_TEXT: ")
    if alive_text:
        print("⤋")
        os.system(f"dotenv set ALIVE_TEXT {alive_text}")
    owner_id = input("\nEnter OWNER_ID: ")
    if owner_id:
        print("⤋")
        os.system(f"dotenv set OWNER_ID {owner_id}")
    sudo_users = input("\nEnter SUDO_USERS: ")
    if sudo_users:
        print("⤋")
        os.system(f"dotenv set SUDO_USERS {sudo_users}")
    cmd_hndlr = input("\nEnter CMD_HNDLR: ")
    if cmd_hndlr:
        print("⤋")
        os.system(f"dotenv set CMD_HNDLR {cmd_hndlr}")
    bot_token = input("\nEnter BOT_TOKEN: ")
    if bot_token:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN {bot_token}")
    bot_token2 = input("\nEnter BOT_TOKEN2: ")
    if bot_token2:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN2 {bot_token2}")
    bot_token3 = input("\nEnter BOT_TOKEN3: ")
    if bot_token3:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN3 {bot_token3}")
    bot_token4 = input("\nEnter BOT_TOKEN4: ")
    if bot_token4:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN4 {bot_token4}")
    bot_token5 = input("\nEnter BOT_TOKEN5: ")
    if bot_token5:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN5 {bot_token5}")
    bot_token6 = input("\nEnter BOT_TOKEN6: ")
    if bot_token6:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN6 {bot_token6}")
    bot_token7 = input("\nEnter BOT_TOKEN7: ")
    if bot_token7:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN7 {bot_token7}")
    bot_token8 = input("\nEnter BOT_TOKEN8: ")
    if bot_token8:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN8 {bot_token8}")
    bot_token9 = input("\nEnter BOT_TOKEN9: ")
    if bot_token9:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN9 {bot_token9}")
    bot_token10 = input("\nEnter BOT_TOKEN10: ")
    if bot_token10:
        print("⤋")
        os.system(f"dotenv set BOT_TOKEN {bot_token10}")
    database_url = input("\nEnter DATABASE_URL: ")
    if database_url:
        print("⤋")
        os.system(f"dotenv set DATABASE_URL {database_url}")
    recheck()
    

def recheck():
    Recheck = input(Fore.GREEN + Style.BRIGHT + "\nFilled ALL Vars Correctly?: y/n ")
    if Recheck.lower() == "n":
        os.system("clear")
        print("Ok !! Fill Your Vars Again")
        setup()
    elif Recheck.lower() == "y":
        os.system("clear")
        ready()
    else:
        print(Fore.RED + Style.BRIGHT + "\nInput Must Be Y or N" + Style.RESET_ALL)
        recheck()


def ready():
    print(Fore.GREEN + Style.BRIGHT + """
█▀▄▀█ █ █▀▀ █░█ ▀█▀ █▄█   ▀▄▀
█░▀░█ █ █▄█ █▀█ ░█░ ░█░   █░█

""")
    Ready = input("Wanna Start MightyX Now?: y/n ")
    if Ready.lower() == "y":
        os.system("clear; cd; cd MightyBotSpamSH; python3 start.py")
    elif Ready.lower() == "n":
        print("\nNevermind !! You Can Start It Later With :\n\ncd; cd MightyBotSpamSH; python3 start.py\n")
        exit()
    else:
        os.system("clear")
        print(Fore.RED + Style.BRIGHT + "\nInput Must Be Y or N" + Style.RESET_ALL)
        ready()

os.system("clear")
setup()
