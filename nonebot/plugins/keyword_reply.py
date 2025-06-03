from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Event

keywords = {
    "在吗": "我一直都在！",
    "你好": "你好呀，有什么可以帮你的吗？"
}

reply = on_message()

@reply.handle()
async def handle_keyword(bot: Bot, event: Event):
    msg = event.get_plaintext().strip()
    if msg in keywords:
        await reply.finish(keywords[msg])
