# Thanks to Sipak bro and Aryan.. 
# animation Idea by @(ItzSipak) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6aa39732748ed7c319943.jpg"
file2 = "https://telegra.ph/file/a6d72504bc09e71484a54.jpg"
file3 = "https://telegra.ph/file/3cdbede1d5d85aa2d50fc.jpg"
file4 = "https://telegra.ph/file/3dae01973943e8b28c931.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "** π³π°ππΊ π²πΎπ±ππ° πΈπ πΎπ½π»πΈπ½π΄**\n\n"
pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
pm_caption += "β About My System β\n\n"
pm_caption += "βΎ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄Κκ±Ιͺα΄Ι΄** β 1.17.5\n"
pm_caption += "βΎ **κ±α΄α΄α΄α΄Κα΄ α΄Κα΄Ι΄Ι΄α΄Κ** β [α΄α΄ΙͺΙ΄](https://t.me/Dark_cobra_support)\n"
pm_caption += "βΎ **ΚΙͺα΄α΄Ι΄κ±α΄**  β [ππ΄π°πΌ π²πΎπ±ππ°](https://github.com/DARK-COBRA)\n"
pm_caption += "βΎ **α΄α΄α΄ΚΚΙͺΙ’Κα΄ ΚΚ** β [π³π°ππΊ-π²πΎπ±ππ°](https://github.com/DARK-COBRA/DARKCOBRA)\n\n"
pm_caption += f"βΎ **α΄Κ α΄α΄sα΄α΄Κ** β [{DEFAULTUSER}](tg://user?id={ghanti})\n"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

