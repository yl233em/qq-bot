from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent

notify = on_keyword({"服务器宕机了"}, rule=lambda e: isinstance(e, GroupMessageEvent))

@notify.handle()
async def handle_notify(bot: Bot, event: GroupMessageEvent):
    await notify.finish("管理员注意：服务器宕机了！请尽快处理！")
