#!/usr/bin/env python

import socket
import sys
from actions.ActionMap import *
from passiveactions.PassiveActionMap import *
from conf.users import *
from wmd import parser

class IRC(object):

    def __init__(self, server=None, nick=None, name=None, port=6667):
        """
        IRC connection library that needs at least server, nick and name
        """
        self.server = server
        self.nick = nick
        self.name = name
        self.port = port

    def locaActions(self):
        """
        Loads the actions internally.
        """
        pass

    def connect(self):
        """
        Connects to the irc server.
        """
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.server, self.port))
        self.log(self.irc.recv(4096))
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER ' + self.name + ' 8 * :Warmachine\r\n')

    def join(self, chan):
        """
        Joins a channel
        """
        self.send('JOIN ' + chan)

    def log(self, string):
        """
        Takes care of log formating.
        """
        print 'log: ' + string

    def send(self, command):
        """
        Sends commands straight to the irc server.
        """
        self.irc.send(command + '\r\n')

    def MainLoop(self):
        """
        Main Event Loop that parses generic commands
        """
        while True:
            data = self.irc.recv(4096)

            if data == '':
                continue

            # Buffering for MOTD.
            if data[-1] != '\n':
                data = data + self.irc.recv(4096)

            for line in data.split('\r\n'):
                obj_data = parser.ircparse(line)
                #pass to action handlers here...
                if (obj_data.prefix == '') and (obj_data.command == '') and (obj_data.params == ''):
                    continue

                print "!" + obj_data.prefix + "~" + obj_data.command + "~" + obj_data.params
                try:
                    for key in passiveactions.keys():
                        pa = passiveactions[key].getAction(obj_data, user)
                        if pa:
                            self.send(pa)

                    if obj_data.params.find(self.nick + ':') > -1 or obj_data.params.find(':!') > -1:
                        curuser = obj_data.getUsername()
                        if curuser not in user:
                            continue
                        for key in actions.keys():
                            if obj_data.params.find(key) > -1:
                                self.send(actions[key].getAction(obj_data))

                except Exception,e:
                    print "Action failed"
                    print e

if __name__ == '__main__':
    import settings
    i = IRC(settings.SERVER, settings.NICKNAME, settings.IDENT)
    i.connect()
    for channel in settings.CHANNELS:
        i.join(channel)
    i.MainLoop()
