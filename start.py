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
from config import *
from utils import *
from telethon import TelegramClient
from telethon.sessions import StringSession


print("\033[1;32m\nPerforming Startup Check... Please Wait !!\n\033[0m")
time.sleep(3)
if API_ID == "":
    raise Exception("\033[1;31mAPI_ID Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if API_HASH == "":
    raise Exception("\033[1;31mAPI_HASH Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN == "":
    raise Exception("\033[1;31mBOT_TOKEN Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN2 == "":
    raise Exception("\033[1;31mBOT_TOKEN2 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN3 == "":
    raise Exception("\033[1;31mBOT_TOKEN3 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN4 == "":
    raise Exception("\033[1;31mBOT_TOKEN4 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN5 == "":
    raise Exception("\033[1;31mBOT_TOKEN5 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN6 == "":
    raise Exception("\033[1;31mBOT_TOKEN6 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN7 == "":
    raise Exception("\033[1;31mBOT_TOKEN7 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN8 == "":
    raise Exception("\033[1;31mBOT_TOKEN8 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN9 == "":
    raise Exception("\033[1;31mBOT_TOKEN9 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if BOT_TOKEN10 == "":
    raise Exception("\033[1;31mBOT_TOKEN10 Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
if DATABASE_URL == "":
    raise Exception("\033[1;31mDatabase URL Var Shouldn't Be Empty !!\nFill It With: python3 setup.py")
print("\033[1;32mPass ✓\n")
time.sleep(1.5)
print("Booting Up... Please Wait !!\033[0m")
try:
    os.system("cd; cd MightyBotSpamSH; python3 MightyXSpam.py")
except Exception as Mighty:
    print(str(Mighty))
