import socket

from wmd import parser

import settings

class IRC(object):

    def __init__(self, server=None, nick=None, name=None, port=6667):
        """
        IRC connection library that needs at least server, nick and name
        """
        self.server = server
        self.nick = nick
        self.name = name
        self.port = port
        self.actions = dict()

        self.load_actions()

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
        self.rawsend('JOIN ' + chan)

    def log(self, string):
        """
        Takes care of log formating.
        """
        print 'log: ' + string

    def privmsg(self, dest, msg):
        """
        send a privmsg to dest
        """
        self.rawsend('PRIVMSG %s :%s' % (dest, msg))

    def rawsend(self, command):
        """
        Sends commands straight to the irc server.
        """
        self.irc.send(command + '\r\n')

    def load_actions(self):
        """
        Loads the actions internally.
        """
        for action in settings.ACTIONS:
            self.load_action(action)

    def load_action(self, path):
        """
        Loads the provided action
        """
        module_name, class_name = path.rsplit('.', 1)
        module = __import__(module_name, globals(), locals(), [class_name], -1)
        classz = getattr(module, class_name)
        self.actions[class_name] = classz()

    def __call__(self, *args, **kwargs):
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

            # For dynamic loading, we have to add to the actions dictionary after we're through looping. Maybe there
            # are some other cases to use the post_loop_commands
            for line in data.split('\r\n'):
                obj_data = parser.IRCParse(line)
                #pass to action handlers here...
                if (obj_data.prefix == '') and (obj_data.command == '') and (obj_data.params == ''):
                    continue

                print "<- " + obj_data.prefix + "~" + obj_data.command + "~" + obj_data.params

                modules_to_load = []
                for plugin_name in self.actions:
                    retval = self.actions[plugin_name].recv_msg(self, obj_data)
                    if type(retval) == type(dict()):
                        if retval.has_key('load'):
                            modules_to_load.append(retval['load'])
                    elif type(retval) == type('str is str'):
                        self.rawsend(retval)

                for module in modules_to_load:
                    self.load_action(module)
