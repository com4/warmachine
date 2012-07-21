from wmd.actions import Action

import settings

class RespondToPing(Action):
    def recv_msg(self, irc, obj_data):
        if obj_data.command == "PING":
            if obj_data.params[0] == ":":
                server = obj_data.params[1:]
            else:
                server = obj_data.params
            msg = "PONG %s" % server
            self.log(msg)
            irc.rawsend(msg)