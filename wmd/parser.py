class IRCParse(object):
    #http://www.irchelp.org/irchelp/rfc/rfc.html

    def __init__(self, data):
        self.prefix =''
        self.command = ''
        self.params = ''
        
        self._rawdata = data

        if data != '':
            self._process_data(data)

    def get_username(self):
        # Usernames are from 0 to the !... extract it out of we can.
        if self.prefix.find('!') > -1:
            return self.prefix[0:self.prefix.index('!')]
        else:
            return False

    def get_channel(self):
        return self.get_username()

    def _process_data(self, data):
        data = data.strip()
        
        # The presence of a prefix is indicated with a single leading ASCII
        # colon character (':', 0x3b), which must be the first character of
        # the message itself. There must be no gap (whitespace) between the
        # colon and the prefix.
        if data[0] == ':':
            self.prefix = data[1:].split(' ')[0]
            start_at = 1
        else:
            # If the prefix is missing from the message, it is assumed to have
            # originated from the connection from which it was received.
            #
            # TODO: Get the server name from the parent object.
            start_at = 0

        # Command comes 2nd (Or first if the prefix is missing) 
        if len(data.split(' ')) > start_at:
            self.command = data.split(' ')[start_at]

        # Finally we reconstruct the parameters. We'll let the plugins figure out
        # what they mean since they could potentially be very different.
        if len(data.split(' ')) > (start_at + 1):
            for param in data.split(' ')[(start_at+1):]:
                self.params += param + " "
            self.params.strip()