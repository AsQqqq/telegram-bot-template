from aiogram import types
from numpy import delete
from import_bot import ID, ALLUSER, dp

from keyboard import start_keyboard_inline, start_keyboard_simple

async def start_command(message: types.Message):
    await message.delete()
    if not ALLUSER.user_exists(message.from_user.id):
        await ALLUSER.add_user(message.from_user.id)
    if message.from_user.id == ID:
        await message.answer('HELLO ADMIN', reply_markup=start_keyboard_inline)
    else:
        await message.answer('HELLO USER', reply_markup=start_keyboard_inline)

@dp.callback_query_handler(text='start_inline')
async def start_inline(call: types.CallbackQuery):
    await call.message.answer('Вызвана новая клавиатура', 
                        reply_markup=start_keyboard_simple)

def reg_handler(dp):
    dp.register_message_handler(start_command, commands='start')