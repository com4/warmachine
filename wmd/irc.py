import socket

from wmd import parser

import settings
import pprint

class IRC(object):

    def __init__(self, server=None, nick=None, name=None, password=None,
                 port=6667):
        """
        IRC connection library that needs at least server, nick and name
        """
        self.irc = None
        self.server = server
        self.nick = nick
        self.name = name
        self.port = port
        self.password = password

        # the structure
        #   TODO: Refactor
        # self.actions["module_name"][0]: the actual module. saved to reload if needed
        # self.actions["module_name"][1]: dictionary. key = class name, value = class object
        self.actions = dict()

        self.load_actions()

    def connect(self):
        """
        Connects to the irc server.
        """
        self.log("Connecting to %s %s" % (self.server, self.port))
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        using_ssl = False
        if str(self.port).startswith("+"):
            using_ssl = True
            import ssl
            self.log("Connecting via SSL")
            self.irc = ssl.wrap_socket(self.irc,
                                       ca_certs="certs/GeoTrust_Primary_Certification_Authority_-_G2.pem",
                                       ssl_version=ssl.PROTOCOL_TLSv1
                                       )
            self.port = int(self.port[1:])

        self.irc.connect((self.server, self.port))


        self.rawsend('NICK ' + self.nick + '\r\n')
        self.rawsend('USER ' + self.name + ' 8 * :Warmachine\r\n')

        if self.password:
            self.rawsend('PASS %s\r\n' % (self.password))

        self.rawsend('\r\n')

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
        self.log(command)
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

        if self.actions.has_key(module_name):
            module = self.actions[module_name][0]
        else:
            try:
                module = __import__(module_name, globals(), locals(), [class_name], -1)
            except ImportError:
                self.log("Error loading module: %s" %(path,))
                return

        if not self.actions.has_key(module_name):
            self.actions[module_name] = []
            self.actions[module_name].insert(0, module) # Save the module so it can be reloaded later
            self.actions[module_name].insert(1, dict())
        elif class_name in self.actions[module_name][1]:
            self.log("Class already loaded")
            return

        try:
            classz = getattr(module, class_name)
        except AttributeError:
            self.log("Class does not exist in module")
            return

        self.actions[module_name][1][class_name] = classz()

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
                modules_to_unload = []
                for module_name in self.actions:
                    for class_name in self.actions[module_name][1]:
                        retval = self.actions[module_name][1][class_name].recv_msg(self, obj_data)

                        if type(retval) == type(dict()):
                            if retval.has_key('load'):
                                modules_to_load.append(retval['load'])
                            if retval.has_key('unload'):
                                modules_to_unload.append(retval['unload'])
                            elif type(retval) == type('str is str'):
                                self.rawsend(retval)

                            for module in modules_to_load:
                                self.load_action(module)
                            #for module in modules_to_unload:
                            #    if self.actions.has_key(module):
                            #        del(self.actions[module])
