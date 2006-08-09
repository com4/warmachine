import socket
import sys
from actions.ActionMap import *
from passiveactions.PassiveActionMap import *
from conf.users import *
from wmd import parser
class irc:

    def __init__(self, server=None, nick=None, name=None, port=6667):
        """
        IRC connection library that needs at least server, nick and name
        """
        self.setServer(server)
        self.setNick(nick)
        self.setName(name)
        self.setPort(port)

    def setServer(self, server):
        """
        Sets the servername.
        """
        self.server = server
    def setNick(self, nick):
        """
        Sets the nickname.
        """
        self.nick = nick

    def setName(self, name):
        """
        Sets the name.
        """
        self.name = name

    def setPort(self, port):
        """
        Sets the port number to connect to.
        """
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
                print "!" + obj_data.prefix + "~" + obj_data.command + "~" + obj_data.params
                try:
                    for key in passiveactions.keys():
                        pa = passiveactions[key].getAction(obj_data, user)
                        if pa:
                            self.send(pa)
                except Exception,e:
                    print "Action failed"
                    print e

            # Passive Actions
            try:
                #for key in passiveactions.keys():
                #    pa = passiveactions[key].getAction(data, user)
                #    if pa:
                #        self.send(pa)
            # Direct Actions
                if data.find(self.nick + ':') != -1:
                    curuser = data[1:data.index('!')]
                    if curuser in user:
                        input = data.split()
                        print "$$ " + input
                        for key in actions.keys():
                            if data.find(key) != -1:
                                self.send(actions[key].getAction(data))
                                break
                    else:
                        input = data.split()
                        self.send('PRIVMSG ' + input[2] + ' :' + curuser +
                            ': stop bothering me jerk.')
            except Exception,e:
                print "Action failed"
                print e


if __name__ == '__main__':
    i = irc('irc.inter.net.il', 'warmachine', 'omgident')
    i.connect()
    i.join('#zzq')
    i.MainLoop()
