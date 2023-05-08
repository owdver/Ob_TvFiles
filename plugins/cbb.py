#(©)Codexbotz

from pyrogram import __version__

from bot import Bot

from config import OWNER_ID

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()

async def cb_handler(client: Bot, query: CallbackQuery):

    data = query.data

    if data == "about":

        await query.message.edit_text(

            text = f"1. ғɪʀsᴛ ᴊᴏɪɴ ᴛʜᴇ <a href='http://t.me/Ob_Link'><b>ᴄʜᴀɴɴᴇʟ</b></a>\n\n<b>2. ᴛᴀᴘ ᴏɴ ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ ᴀɢᴀɪɴ ᴏʀ ʀᴇʟᴏᴀᴅ ⚡️\n\n3. ᴛᴀᴘ ᴏɴ sᴛᴀʀᴛ ᴀɴᴅ ᴅᴏɴᴇ ✅</b>",

            disable_web_page_preview = True,

            reply_markup = InlineKeyboardMarkup(

                [

                    [

                        InlineKeyboardButton("✅ ᴄʟᴏsᴇ", callback_data = "close")

                    ]

                ]

            )

        )

    elif data == "close":

        await query.message.delete()

        try:

            await query.message.reply_to_message.delete()

        except:

            pass
