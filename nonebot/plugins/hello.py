from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event

hello = on_command("hello")

@hello.handle()
async def handle_first_receive(bot: Bot, event: Event):
    await hello.finish("你好，我是机器人～")
