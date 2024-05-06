import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, html
from aiogram.filters.command import Command
from token import TOKEN
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
import wikipedia
from aiogram.utils.media_group import MediaGroupBuilder
from random import randint
# from add import add_table
# from read import GetUser
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    fullname = message.from_user.full_name
    tg_id = message.from_user.id
    username = message.from_user.username
    urls = message.from_user.url
    await message.answer(text=f"Assalomu alaykum\n<a href = '{urls}'>{fullname}</a>")

@dp.message(F.text=="Misol")
async def get_misol(message: Message):
    await message.answer("Nechta misol ishlamoqchisiz")


@dp.message(F.text)
async def get_photo(message: Message):
    text = message.text
    a = len(text.split())

    if a == 1:
        javoblar = ''
        misollar = ""
        for i in range(int(text)):
            a = randint(50, 60)
            b = randint(50, 60)
            misollar += f"{a} + {b} = ? \n"
            javoblar += f"{a + b} "
        with open('azizbek.txt', 'w') as f:
            f.write(f"{javoblar}")
        await message.answer(f"Siz soragan misol\n {misollar}")
    else:
        with open('azizbek.txt', 'r') as name:
            d = name.read()
        soni = d.split()
        user_j = text.split()
        print("Random T_j: ", soni)
        print("user: ", user_j)
        cnt = 0
        for i in range(len(soni)):
            if user_j[i] == soni[i]:
                cnt += 1
        await message.answer(f"Sizning misollaringiz tekshirilmoqda...\n {cnt}")





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Bot foalyatini tugatdi")
