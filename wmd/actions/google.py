__author__ = 'jason@zzq.org'
__version__ = 1.0

import urllib2
import json as simplejson

from wmd.actions import Action

import settings

class GoogleSearch(Action):
    def recv_msg(self, irc, obj_data):
        args = obj_data.params.split(" ")
        channel = args[0]
        if channel == settings.NICKNAME:
            channel = obj_data.get_username()

        if "PRIVMSG" in obj_data.command and ":!google" in args[1].lower():
            search_string = " ".join(args[2:])
            url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&start=%d&rsz=large&q=%s"%(0,search_string.replace(" ","%20"))
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req).read()

            data = simplejson.loads(data)
            result = data['responseData']['results'][0]['url']
            irc.privmsg(channel, result)