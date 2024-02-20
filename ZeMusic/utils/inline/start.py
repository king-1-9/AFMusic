from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="『 أضفني إلى مجموعتك 』",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="『 الأوامر 』", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="『 المطور 』", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="『 السورس 』", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』", url=f"https://t.me/IC_19"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="『 أضفني إلى مجموعتك 』",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="『 الأوامر 』", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="『 المطور 』", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="『 السورس 』", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』", url=f"https://t.me/IC_19"),
        ],
    ]
    return buttons
