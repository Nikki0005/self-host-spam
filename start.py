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


import os
from config import *
from utils import *
from telethon import TelegramClient
from telethon.sessions import StringSession

if DATABASE_URL == "":
    raise Exception("Please Fill Database URL In config.py")
if BOT_TOKEN == "":
    raise Exception("Please Fill BOT_TOKEN In config.py")
if BOT_TOKEN2 == "":
    raise Exception("Please Fill BOT_TOKEN2 In config.py")
if BOT_TOKEN3 == "":
    raise Exception("Please Fill BOT_TOKEN3 In config.py")
if BOT_TOKEN4 == "":
    raise Exception("Please Fill BOT_TOKEN4 In config.py")
if BOT_TOKEN5 == "":
    raise Exception("Please Fill BOT_TOKEN5 In config.py")
if BOT_TOKEN6 == "":
    raise Exception("Please Fill BOT_TOKEN6 In config.py")
if BOT_TOKEN7 == "":
    raise Exception("Please Fill BOT_TOKEN7 In config.py")
if BOT_TOKEN8 == "":
    raise Exception("Please Fill BOT_TOKEN8 In config.py")
if BOT_TOKEN9 == "":
    raise Exception("Please Fill BOT_TOKEN9 In config.py")
if BOT_TOKEN10 == "":
    raise Exception("Please Fill BOT_TOKEN10 In config.py")
try:
    os.system("cd && cd MightyBotSpamSH && python3 MightyXSpam.py")
except Exception as Mighty:
    print(str(Mighty))
