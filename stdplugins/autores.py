"""Auto-responder for Requests in groups

  © [cHAuHaN](http://t.me/amnd33p)"""

#regex ([a-zA-Z0-9 ]+)( #([r]|[R])equest)($|[\n])

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    if not Config.ENABLE_REQUESTS_RECEIVER:
        return
    pattern = r"([a-zA-Z0-9 ]+)( #([r]|[R])equest)($|[\n])"
    if re.search(pattern, name, flags=re.IGNORECASE):
        if event.chat_id==Config.PRIVATE_GROUP_REQUESTS_RECEIVER:
            message_id = event.message.id
            await event.client.send_message(
                event.chat_id,
                "Your request has been received, It will be fulfilled ASAP.\n`Please don't send a duplicate request within 3 days.`",
                reply_to=message_id
            )
            msg = event.message
            if msg:
                msg_o = await event.client.forward_messages(
                    entity=Config.PRIVATE_GROUP_FOR_REQUESTS_ID,
                    messages=msg,
                    from_peer=event.chat_id,
                    silent=False
                )