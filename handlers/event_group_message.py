from aiogram import Router, F
from aiogram.enums.content_type import ContentType
from aiogram.enums.chat_type import ChatType
from aiogram.types import Message
from aiogram.filters import Command
from settings import TG_ADMIN_GROUP_ID, RCON_IP, RCON_PORT, RCON_PWD, ADMIN_ID
from rcon.source import Client


router = Router(name=__name__)
router.message.filter(
    F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}),
)


@router.message(F.content_type.in_({ContentType.NEW_CHAT_MEMBERS}))
@router.message(F.content_type.in_({ContentType.GROUP_CHAT_CREATED, ContentType.SUPERGROUP_CHAT_CREATED}))
async def group_created_handler(message: Message) -> None:
    await message.answer(
        '<b>✅ Спасибо за добавление бота в группу.</b>\n'
        '\n'
        'Имейте ввиду, что бот не сможет взаимодействовать с сообщениями, '
        'если у него не будет соответствующих прав. Для использования бота, '
        'выдайте ему права администратора группы.\n'
    )


@router.message(Command(commands='wladd'))
async def wladd(message: Message) -> None:
    if str(message.chat.id) != TG_ADMIN_GROUP_ID:
        return
    
    arguments = message.text.split(' ')[1:]
    
    if not arguments:
        return await message.answer(
            'Укажите ник человека: `/wladd player`'
        )

    with Client(RCON_IP, int(RCON_PORT), passwd=RCON_PWD) as client:
        response = client.run('whitelist', 'add', arguments[0])

    await message.answer(response)


@router.message(Command(commands='wldel'))
async def wldel(message: Message) -> None:
    if str(message.chat.id) != TG_ADMIN_GROUP_ID:
        return
    
    arguments = message.text.split(' ')[1:]
    
    if not arguments:
        return await message.answer(
            'Укажите ник человека: `/wldel player`'
        )

    with Client(RCON_IP, int(RCON_PORT), passwd=RCON_PWD) as client:
        response = client.run('whitelist', 'remove', arguments[0])

    await message.answer(response)


@router.message(Command(commands='wllist'))
async def wllist(message: Message) -> None:
    if str(message.chat.id) != TG_ADMIN_GROUP_ID:
        return
    
    with Client(RCON_IP, int(RCON_PORT), passwd=RCON_PWD) as client:
        response = client.run('whitelist', 'list')

    await message.answer(response)


@router.message(Command(commands='exec'))
async def exec_mc(message: Message) -> None:
    if str(message.from_user.id) != ADMIN_ID:
        return
    
    arguments = message.text.split(' ')[1:]

    with Client(RCON_IP, int(RCON_PORT), passwd=RCON_PWD) as client:
        response = client.run(*arguments)

    await message.answer(response)
