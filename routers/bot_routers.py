from aiogram.filters.command import Command
from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from keyboards.bot_keyboards import Keyboards  # pyright:ignore
from create_bot import bot

router = Router(name=__name__)
keyboards = Keyboards()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Вітаємо вас на кафедрі комп'ютерної інженерії та електроніки Кременчуцького національного університету імені Михайла Остроградського.",
        reply_markup=await keyboards.start_keyboard(),
    )


@router.callback_query(F.data == "Освітнє середовище")
async def educational_environment(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.educational_environment_keyboard()
    text = "Освітнє середовище"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "Практична пiдготовка")
async def practical_training(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.practical_training_keyboard()
    text = "Практична пiдготовка"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.start_keyboard()
    text = "Вітаємо вас на кафедрі комп'ютерної інженерії та електроніки Кременчуцького національного університету імені Михайла Остроградського."
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "Мiжнародна дiяльнiсть")
async def international_activity(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.international_activity_keyboard()
    text = "Мiжнародна дiяльнiсть"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "Виховна дiяльнiсть")
async def educational_activity(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.educational_activity_keyboard()
    text = "Виховна дiяльнiсть"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "Наукова дiяльнiсть")
async def scientific_activity(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.scientific_activity_keyboard()
    text = "Наукова дiяльнiсть"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "casual_dual_education")
async def сasul_dual_education(callback_query: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Неформальная освiта",
        url="http://cee.kdu.edu.ua/uk/content/neformalna-osvita",
    )
    builder.button(
        text="Дуальна освiта",
        url="http://cee.kdu.edu.ua/uk/content/dualna-osvita",
    )
    builder.button(
        text="Повернутись до головної cторiнки", callback_data="back_to_main"
    )
    builder.adjust(1)
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    text = "Неформальна i дуальна освiта"
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "master")
async def master(callback_query: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Cпецiальнысть 123 Комп'ютерна інженерія",
        url="http://cee.kdu.edu.ua/uk/content/specialnist-123-kompyuterna-inzheneriya-magistr",
    )
    builder.button(
        text="Cпецiальнiсть 172 Телекомунікації та електротехніка",
        url="http://cee.kdu.edu.ua/uk/content/specialnist-172-telekomunikaciyi-ta-radiotehnika-magistr",
    )
    builder.button(
        text="Повернутись до головної cторiнки", callback_data="back_to_main"
    )
    builder.adjust(1)
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    text = "Другий(магiстерський) рiвень вищої освiти"
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "bakalavriat")
async def bakalavriat(callback_query: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Cпецiальнысть 123 Комп'ютерна інженерія",
        url="http://cee.kdu.edu.ua/uk/content/specialnist-123-kompyuterna-inzheneriya-bakalavr",
    )
    builder.button(
        text="Cпецiальнiсть 171 Електронiка ",
        url="http://cee.kdu.edu.ua/uk/content/specialnist-171-elektronika",
    )
    builder.button(
        text="Повернутись до головної cторiнки", callback_data="back_to_main"
    )
    builder.adjust(1)
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    text = "Перший(бакалаврьский) рiвень вищої освiти"
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "list_education")
async def list_education(callback_query: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Перший(бакалаврьский) рiвень вищої освiти", callback_data="bakalavriat"
    )
    builder.button(
        text="Другий(магiстерський) рiвень вищої освiти", callback_data="master"
    )
    builder.button(
        text="Повернутись до головної cторiнки", callback_data="back_to_main"
    )
    builder.adjust(1)
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    text = "Освiтнi програми"
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "Освiта")
async def education(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.education_keyboard()
    text = "Освiта"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "Вступнику")
async def to_the_entrant(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.to_the_entrant_keyboard()
    text = "Вступнику"
    await bot.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard
    )


@router.callback_query(F.data == "Про кафедру")
async def about_the_department(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    keyboard = await keyboards.about_the_departament_keyboard()
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="Про кафедру",
        reply_markup=keyboard,
    )
