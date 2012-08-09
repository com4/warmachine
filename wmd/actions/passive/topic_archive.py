from wmd.actions import Action

import settings

class TopicArchive(Action):
    def recv_msg(self, irc, obj_data):
        if obj_data.command == "TOPIC":
            (channel, topic) = obj_data.params.strip().split(" ", 1)
            topic = topic[1:]

            f = open("topic_archive.log", "a+")
            f.write("%s %s %s" % (channel, obj_data.prefix, topic))
            f.close()