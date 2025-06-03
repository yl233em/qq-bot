from nonebot import get_bot, require
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.onebot.v11 import MessageSegment

scheduler.add_job(
    lambda: send_daily_msg(),
    "cron", hour=9, minute=0
)

async def send_daily_msg():
    bot = get_bot()
    if bot:
        # 替换成你的群号
        group_id = 123456789
        await bot.send_group_msg(group_id=group_id, message="早安！新的一天开始啦～")
