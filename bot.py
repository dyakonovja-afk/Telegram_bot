import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8435050330:AAHE3A_tgX_bxBjOm_-MDgM1q-gNCdlPJ68"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

texts = {
    1: "🧨 *Разоблачение №1*\n\n"
       "Мотивация не создаёт действие.\n"
       "Она создаёт ощущение, что ты почти начал.\n\n"
       "Пока ты мотивируешься —\n"
       "система продолжает работать без тебя.\n\n"
       "Тебя учили ждать состояния.\n"
       "А не строить среду.",

    2: "🧨 *Разоблачение №2*\n\n"
       "Курсы не делают богатыми.\n"
       "Они продают универсальный путь.\n\n"
       "Универсальный путь удобен продавцу,\n"
       "но бесполезен для конкретного человека.\n\n"
       "Если не получилось — виноват всегда ты.",

    3: "🧨 *Разоблачение №3*\n\n"
       "Занятость — лучший способ не двигаться.\n\n"
       "Когда ты постоянно занят,\n"
       "у тебя нет ресурса задать правильный вопрос.\n\n"
       "Уставший человек не ломает систему.\n"
       "Он в ней выживает."
}

def nav(step):
    kb = types.InlineKeyboardMarkup()
    if step < 3:
        kb.add(types.InlineKeyboardButton("▶️ Следующее", callback_data=f"rev_{step+1}"))
    else:
        kb.add(types.InlineKeyboardButton("💡 Личный разбор", callback_data="personal"))
    kb.add(types.InlineKeyboardButton("📤 Поделиться", switch_inline_query=""))
    return kb

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    kb = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("🧨 Начать", callback_data="rev_1")
    )
    await msg.answer(
        "Это серия коротких разоблачений.\n\n"
        "О деньгах, мышлении и системе,\n"
        "в которой застревает большинство.",
        reply_markup=kb
    )

@dp.callback_query_handler(lambda c: c.data.startswith("rev_"))
async def show(call: types.CallbackQuery):
    step = int(call.data.split("_")[1])
    await call.message.edit_text(
        texts[step],
        reply_markup=nav(step),
        parse_mode="Markdown"
    )

@dp.callback_query_handler(lambda c: c.data == "personal")
async def personal(call: types.CallbackQuery):
    await call.message.edit_text(
        "Хочешь понять, как именно система держит ТЕБЯ.\n\n"
        "Личный разбор — скоро.",
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
