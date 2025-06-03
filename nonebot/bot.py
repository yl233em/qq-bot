import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter

nonebot.init()

app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)

nonebot.load_plugins("plugins")
nonebot.load_plugins("nonebot_plugin_nextcloud_stub")

if __name__ == "__main__":
    nonebot.run()
