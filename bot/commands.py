from aiogram.filters import Command
from aiogram import types

from db.models import Users, Message
from db.session import DBSession

from bot.telegram import dp
from agent.core.agent import generate_assistant_response

@dp.message(Command('delete_user'))
async def delete_user(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.full_name

    user = Users(telegram_id=user_id)
    with DBSession() as cur:
        if not user.exists(cur):
            await message.answer("User not found")
            return
        
        user.delete(cur)

    await message.answer(f"User deleted: {name}")

@dp.message(Command('delete_chat'))
async def delete_chat(message: types.Message):
    telegram_id = message.from_user.id

    user = Users(telegram_id=telegram_id)
    with DBSession() as cur:
        db_user = user.get(cur)
        if not db_user:
            await message.answer("User not found")
            return
        
        messages_obj = Message(telegram_id=db_user, content="", role="")
        all_messages = messages_obj.get_all(cur)
        if all_messages:
            messages_obj.delete(cur)
            await message.answer("Chat deleted")
        else:
            await message.answer("No chat found")

@dp.message()
async def content(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    user = Users(telegram_id=user_id)
    with DBSession() as cur:
        if not user.exists(cur):
            user.save(cur)

    response = generate_assistant_response(user_text=text, user_id=user_id)

    await message.answer(response)