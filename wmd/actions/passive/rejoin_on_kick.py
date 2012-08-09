import time
from wmd.actions import Action

import settings

class RejoinOnKick(Action):
    def recv_msg(self, irc, obj_data):
        if obj_data.command == "KICK":
            (channel, nickname, message) = obj_data.params.strip().split(" ")
            if nickname == settings.NICKNAME:
                time.sleep(10) # TODO: Make this a setting
                irc.join(channel)
                self.log("Rejoined %s" % channel)