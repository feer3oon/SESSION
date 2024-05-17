from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""• ¦ اهلا بـك عزيـزي  {msg.from_user.mention}
• ¦ فـي بـوت اسـتـخـراج الـجـلـسـات
• ¦ يمكنك استخراج الجلسات الـتالية
• ¦ بايروجرام للحسابات & بايروجرام للبوتات
• ¦ بـايـروجـرام مـيوزك احـدث إصـدار 
• ¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

• ¦ بواسطـة : [𓏺𝗠𝗥 . 𝗫](tg://user?id=6308685423) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=" ••• اضغط لبدا استخراج كود •••", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𓏺ꪔᖇ . ꪎ ‌ 𝚂𝙾𝚄𝚁𝙲𝙴 ♟️", url="https://t.me/VETHON"),
                    InlineKeyboardButton("DEV 𓏺𝗠𝗥 . 𝗫 ‌", user_id=6308685423)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
