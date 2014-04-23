__author__ = 'jason@zzq.org'
__version__ = 1.0

import urllib2
import json as simplejson

from wmd.actions import Action

import settings


class GiphySearch(Action):
    def recv_msg(self, irc, obj_data):
        args = obj_data.params.split(" ")
        channel = args[0]
        if channel == settings.NICKNAME:
            channel = obj_data.get_username()

        if "PRIVMSG" in obj_data.command and ":!gif" in args[1].lower():
            search_string = " ".join(args[2:])
            url = "http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC&limit=1" % \
                  (search_string.replace(" ", "%20"), )
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req).read()

            data = simplejson.loads(data)
            try:
                result = data['data'][0]['images']['original']['url']
                irc.privmsg(channel, result)
            except IndexError:
                pass
