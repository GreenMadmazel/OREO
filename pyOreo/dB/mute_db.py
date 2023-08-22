# Oreo - UserBot

from .. import udB


def get_muted():
    return udB.get_key("MUTE") or {}


def mute(chat, id):
    ok = get_muted()
    if ok.get(chat):
        if id not in ok[chat]:
            ok[chat].append(id)
    else:
        ok.update({chat: [id]})
    return udB.set_key("MUTE", ok)


def unmute(chat, id):
    ok = get_muted()
    if ok.get(chat) and id in ok[chat]:
        ok[chat].remove(id)
    return udB.set_key("MUTE", ok)


def is_muted(chat, id):
    ok = get_muted()
    return bool(ok.get(chat) and id in ok[chat])
