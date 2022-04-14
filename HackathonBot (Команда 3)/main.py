from calendar import c
from aiogram import Bot,Dispatcher,types,executor
import Variables

bot = Bot(token = Variables.Strings.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Здравствуйте, я Worky-bot! Я создан для поиска работы для молодых специалистов.\
    \n Список команд:\n/findjob - Подбор подходящих вакансий\n<i>*Поиск основан на сайте superjob.ru</i>")

@dp.message_handler(commands="findjob")
async def Work(message: types.Message):
    await message.answer(text='Введите через запятую без пробелов свои данные.\n <b>1.</b> Ваш возраст.\n <b>2.</b> Ваш пол - Мужчина или Женщина (цифра от 1 до 2).\
    \n <b>3.</b> Ваш опыт работы - без опыта, от 1 года, от 3 лет, от 6 лет (цифра от 1 до 4).')
    @dp.message_handler()
    async def Job(message: types.Message):
        m = message.text.split(sep=',')
        gender = {'1':2, '2':3}
        await message.answer(Variables.Data.by_id(0, int(m[0]),gender.get(m[1]),int(m[2])), reply_markup=Variables.Keys.keyboard)

@dp.callback_query_handler(text='end')
async def next(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer('Спасибо за использование этого бота!')
    await callback_query.message.delete_reply_markup()

executor.start_polling(dp)

