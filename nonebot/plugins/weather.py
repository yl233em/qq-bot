from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import httpx

weather = on_command("天气")

@weather.handle()
async def handle_weather(bot: Bot, event: Event):
    city = event.get_plaintext().strip()
    if not city:
        await weather.finish("请输入城市名称，例如：/天气 北京")
    url = f"https://wttr.in/{city}?format=3"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code == 200:
            await weather.finish(resp.text)
        else:
            await weather.finish("查询天气失败，请稍后再试。")
