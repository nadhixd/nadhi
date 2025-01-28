from ... import *
from datetime import datetime

@app.on_message(cdx("ping"))
@sudo_users_only
async def ping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    m = await eor(message, "**🤖 Ping !**")
    await m.edit(f"**🤖 𝒂𝒓𝒆 𝒉𝒂𝒂 𝒃𝒉𝒂𝒊 𝒌𝒂𝒓𝒐 𝒑𝒊𝒏𝒈 𝒍𝒐 𝒅𝒆𝒌𝒉 𝒍𝒐 !\nLatency:** `{ms}` ms")



__NAME__ = "Ping"
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**
"""
