import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Включаем логирование, чтобы было видно ошибки
logging.basicConfig(
    level=logging.INFO,
    filename="log.txt",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
# Токен твоего бота (вставь свой!)
BOT_TOKEN = ""

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду /start
@dp.message(Command("start"))
async def start_start(message: types.Message):
    await message.answer("Привет я бот который будет помогать тебе с твоим распорядком дня!")
    await message.answer("Фиксировать прогресс в обучении. (например, тренировок или прочитанных страниц)")
    await message.answer("Все будет просто ты напишешь дату и время и что ты сделал за это время!")
    await message.answer("Я буду это фиксировать запоминать в любой момент ты можешь спросить меня что было в это время или день и я отвечу тебе.")
    await message.answer("Но перед этим всем надо будет ввести команду /save и после сообщенич Начали писать свой прогресс!")
    await message.answer("Ты так же можешь посмотреть все свои записи! прописав команду /myprog")
@dp.message(Command("save"))
async def start_save(message: types.Message):
     await message.answer("Отлично, начали!!!")

@dp.message(Command("myprog"))
async def my_prog(message: types.Message):
    await message.answer("Записи!")
    with open("progress.txt", "r", encoding="utf-8") as t:
        prog=t.read()
        await message.answer(f"Вот твой прогресс! \n {prog}\n")

@dp.message(F.text)
async def progress(message:types.Message):
    message.text
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("progress.txt", "a",encoding="utf-8" ) as p:
        p.write(f"[{now}]{message.text}\n")
    await message.answer("Записал в дневник прогресса!")

# --- Запуск бота ---
async def main():
    """Главная функция запуска."""
    print("Бот запущен и готов к работе!")
    print("Все логи сохраняються в файле, log.txt")
    # Запускаем процесс поллинга новых апдейтов
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем асинхронную функцию main
    asyncio.run(main())