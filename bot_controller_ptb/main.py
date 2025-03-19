import asyncio
from telegram import Bot

BOT_TOKEN = "7607790356:AAFMtuJtAnwAxmnTDup_LCHSxF9C_JPxFIo"
OWNER_ID = 2134776547
CHAT_ID = 2134776547
USER_ID = 2134776547

bot = Bot(BOT_TOKEN)

async def main():

    response = await bot.set_my_name("Undying")

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
