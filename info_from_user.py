# Module by @DeBotMod
from telethon import events
from userbot import client

info = {'category': 'chat', 'pattern': '.ui', 'description': 'Поиск информации о пользователе. Реплаем на сообщение или аргументом команды'}


CHECK_MARK = ' ✔️ '
CROSS_MARK = ' ❌ '

@client.on(events.NewMessage(pattern=r'^\.ui(?:\s+(@\w+|\d+))$', outgoing=True))
@client.on(events.NewMessage(pattern=r'^\.ui$', outgoing=True))
async def user_info(event: events.NewMessage.Event) -> None:
    if not event.is_reply:
        input_value = event.pattern_match.group(1)
    else:
        reply_message = await event.get_reply_message()
        input_value = str(reply_message.from_id.user_id)
    
    if input_value is None:
        await event.edit('❌ Неверный формат!')

    user = await client.get_entity(int(input_value) if input_value.isdigit() else input_value)

    scam_mark = CHECK_MARK if user.scam else CROSS_MARK
    is_premium = CHECK_MARK if user.premium else CROSS_MARK

    name = f'{user.first_name} {user.last_name}' if user.first_name and user.last_name else user.first_name or user.last_name or CROSS_MARK
    username = user.username or CROSS_MARK
    user_id = f'{user.id}'

    await event.edit(f'👮 <b>SCAM:</b> {scam_mark}\n🌟 <b>Premium:</b> {is_premium}\n🪪 <b>Имя:</b> <code>{name}</code>\n🌐 <b>Юзернейм:</b> {"@" + username if username != CROSS_MARK else username}\n🔢 <b>ID:</b> <code>{user_id}</code>\n⛓️ <b>Ссылка:</b> <a href=tg://openmessage?user_id={user_id}>*тык*</a>', parse_mode='HTML')
