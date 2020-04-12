# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.


import os
from pyrogram import ChatPermissions
from userge import userge, Message


@userge.on_cmd("lock", about="""\
__use this to lock group permissions__

**Usage:**

`Allows you to lock some common permission types in the chat.`

[NOTE: Requires proper admin rights in the chat!!!]

**Available types to Lock Permissions:**

`all, msg, media, polls, invite, pin, info, web preview, other [animations, games, stickers, inline bots]`

**Example:**

    `.lock [all | type]`""")
async def lock_perm(message: Message):
    """
    this function can lock chat permissions from tg group
    """
    msg = ""
    media = ""
    other = ""
    webprev = ""
    polls = ""
    info = ""
    invite = ""
    pin = ""
    perm = ""

    lock_type = message.input_str
    chat_id = message.chat.id

    if not lock_type:
        await message.edit(text="**I Can't Lock Nothing! 🤦‍♂️**", del_in=3)
        return

    get_perm = await userge.get_chat(chat_id)

    msg = get_perm.permissions.can_send_messages
    media = get_perm.permissions.can_send_media_messages
    other = get_perm.permissions.can_send_other_messages
    webprev = get_perm.permissions.can_add_web_page_previews
    polls = get_perm.permissions.can_send_polls
    info = get_perm.permissions.can_change_info
    invite = get_perm.permissions.can_invite_users
    pin = get_perm.permissions.can_pin_messages

    if lock_type == "all":
        try:
            await userge.set_chat_permissions(chat_id, ChatPermissions())
            await message.edit(
                text="**🔒 Locked all permission from this Chat!**", del_in=3)

        except:
            await message.edit(
                text=f"**Do I have proper Admin rights for that 🤔**", del_in=3)

        return

    if lock_type == "msg":
        msg = False
        perm = "messages"

    elif lock_type == "media":
        media = False
        perm = "audios, documents, photos, videos, video notes, voice notes"

    elif lock_type == "other":
        other = False
        perm = "animations, games, stickers, inline bots"

    elif lock_type == "webprev":
        webprev = False
        perm = "web page previews"

    elif lock_type == "polls":
        polls = False
        perm = "polls"

    elif lock_type == "info":
        info = False
        perm = "info"

    elif lock_type == "invite":
        invite = False
        perm = "invite"

    elif lock_type == "pin":
        pin = False
        perm = "pin"

    else:
        await message.edit(text=r"**Invalid Lock Type! ¯\_(ツ)_/¯**", del_in=3)
        return

    try:
        await userge.set_chat_permissions(chat_id,
                                          ChatPermissions(can_send_messages=msg,
                                                          can_send_media_messages=media,
                                                          can_send_other_messages=other,
                                                          can_add_web_page_previews=webprev,
                                                          can_send_polls=polls,
                                                          can_change_info=info,
                                                          can_invite_users=invite,
                                                          can_pin_messages=pin, ))

        await message.edit(text=f"**🔒 Locked {perm} for this chat!**", del_in=3)

    except:
        await message.edit(
            text="**Do I have proper Admin rights for that 🤔**", del_in=3)


@userge.on_cmd("unlock", about="""\
__use this to unlock group permissions__

**Usage:**

`Allows you to unlock some common permission types in the chat.`

[NOTE: Requires proper admin rights in the chat!!!]

**Available types to Unlock Permissions:**

`all, msg, media, polls, invite, pin, info, web preview, other [animations, games, stickers, inline bots]`

**Example:**

    `.unlock [all | type]`""")
async def unlock_perm(message: Message):
    """
    this function can unlock chat permissions from tg group
    """
    umsg = ""
    umedia = ""
    uother = ""
    uwebprev = ""
    upolls = ""
    uinfo = ""
    uinvite = ""
    upin = ""
    uperm = ""

    unlock_type = message.input_str
    chat_id = message.chat.id

    if not unlock_type:
        await message.edit(text="**I Can't Unlock Nothing! 🤦‍♂️**", del_in=3)
        return

    get_uperm = await userge.get_chat(chat_id)

    umsg = get_uperm.permissions.can_send_messages
    umedia = get_uperm.permissions.can_send_media_messages
    uother = get_uperm.permissions.can_send_other_messages
    uwebprev = get_uperm.permissions.can_add_web_page_previews
    upolls = get_uperm.permissions.can_send_polls
    uinfo = get_uperm.permissions.can_change_info
    uinvite = get_uperm.permissions.can_invite_users
    upin = get_uperm.permissions.can_pin_messages

    if unlock_type == "all":
        try:
            await userge.set_chat_permissions(chat_id,
                                              ChatPermissions(can_send_messages=True,
                                                              can_send_media_messages=True,
                                                              can_send_other_messages=True,
                                                              can_send_polls=True,
                                                              can_change_info=True,
                                                              can_invite_users=True,
                                                              can_pin_messages=True,
                                                              can_add_web_page_previews=True, ))

            await message.edit(
                text="**🔓 Unlocked all permission from this Chat!**", del_in=3)

        except:
            await message.edit(
                text=f"**Do I have proper Admin rights for that 🤔**", del_in=3)
        return

    if unlock_type == "msg":
        umsg = True
        uperm = "messages"

    elif unlock_type == "media":
        umedia = True
        uperm = "audios, documents, photos, videos, video notes, voice notes"

    elif unlock_type == "other":
        uother = True
        uperm = "animations, games, stickers, inline bots"

    elif unlock_type == "webprev":
        uwebprev = True
        uperm = "web page previews"

    elif unlock_type == "polls":
        upolls = True
        uperm = "polls"

    elif unlock_type == "info":
        uinfo = True
        uperm = "info"

    elif unlock_type == "invite":
        uinvite = True
        uperm = "invite"

    elif unlock_type == "pin":
        upin = True
        uperm = "pin"

    else:
        await message.edit(text=r"**Invalid Unlock Type! ¯\_(ツ)_/¯**", del_in=3)
        return

    try:
        await userge.set_chat_permissions(chat_id,
                                          ChatPermissions(can_send_messages=umsg,
                                                          can_send_media_messages=umedia,
                                                          can_send_other_messages=uother,
                                                          can_add_web_page_previews=uwebprev,
                                                          can_send_polls=upolls,
                                                          can_change_info=uinfo,
                                                          can_invite_users=uinvite,
                                                          can_pin_messages=upin, ))

        await message.edit(text=f"**🔓 Unlocked {uperm} for this chat!**", del_in=3)

    except:
        await message.edit(text=f"**Do I have proper Admin rights for that 🤔**", del_in=3)


@userge.on_cmd("vperm", about="""\
__use this to view group permissions__

**Usage:**

`Allows you to view permission types on/off status in the chat.`""")
async def view_perm(message: Message):
    """
    this function can check chat permissions from tg group
    """

    v_perm = ""
    vmsg = ""
    vmedia = ""
    vother = ""
    vwebprev = ""
    vpolls = ""
    vinfo = ""
    vinvite = ""
    vpin = ""

    await message.edit("`Checking group permissions... Hang on!`")

    v_perm = await userge.get_chat(message.chat.id)

    def convert_to_emoji(val: bool):
        if val is True:
            return "✅"
        else:
            return "❌"

    vmsg = convert_to_emoji(v_perm.permissions.can_send_messages)
    vmedia = convert_to_emoji(v_perm.permissions.can_send_media_messages)
    vother = convert_to_emoji(v_perm.permissions.can_send_other_messages)
    vwebprev = convert_to_emoji(v_perm.permissions.can_add_web_page_previews)
    vpolls = convert_to_emoji(v_perm.permissions.can_send_polls)
    vinfo = convert_to_emoji(v_perm.permissions.can_change_info)
    vinvite = convert_to_emoji(v_perm.permissions.can_invite_users)
    vpin = convert_to_emoji(v_perm.permissions.can_pin_messages)

    if v_perm is not None:
        try:
            permission_view_str = ""

            permission_view_str += f"<b>CHAT PERMISSION INFO:</b>\n\n"
            permission_view_str += f"<b>📩 Send Messages:</b> {vmsg}\n"
            permission_view_str += f"<b>🎭 Send Media:</b> {vmedia}\n"
            permission_view_str += f"<b>🎲 Send Other Messages:</b> {vother}\n"
            permission_view_str += f"<b>🌐 Webpage Preview:</b> {vwebprev}\n"
            permission_view_str += f"<b>🗳 Send Polls:</b> {vpolls}\n"
            permission_view_str += f"<b>ℹ Change Info:</b> {vinfo}\n"
            permission_view_str += f"<b>👥 Invite Users:</b> {vinvite}\n"
            permission_view_str += f"<b>📌 Pin Messages:</b> {vpin}\n"

            if v_perm.photo:
                local_chat_photo = await userge.download_media(
                    message=v_perm.photo.big_file_id
                )

                await userge.send_photo(chat_id=message.chat.id,
                                        photo=local_chat_photo,
                                        caption=permission_view_str,
                                        parse_mode="html")

                os.remove(local_chat_photo)
                await message.delete()

            else:
                await message.edit(permission_view_str)

        except:
            await message.edit(
                text=f"**Something went wrong! do** `.help vperm`", del_in=3)
