from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

I am Fastest Gofile Uploader Bot. 
Just send me the media to get stream link from Gofile.io !

Made With 💕 By @Tellybots_4u
    """

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🚦 Bot Status", url="https://t.me/tellybots_4u")],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/tellybots_support")],
    ]
   

    # About Message
    ABOUT = """
**About This Bot** 

A telegram Fastest GoFile Uploader Bot 

Source Code : [Click Here](https://t.me/tellybots_digital)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Tellybots_4u
    """
