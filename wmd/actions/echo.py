from wmd.actions import Action

import settings

class EchoAction(Action):
    def recv_msg(self, irc, obj_data):
        channel = obj_data.get_username()

        args = obj_data.params.split(" ")
        if "PRIVMSG" in obj_data.command and settings.NICKNAME in args[1]:
            irc.privmsg(channel, " ".join(args[2:]))