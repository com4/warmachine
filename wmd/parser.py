class ircparse(object):
    #http://www.irchelp.org/irchelp/rfc/rfc.html

    def __init__(self, data):
        self.prefix =''
        self.command = ''
        
        self._rawdata = data

        #print "x" * 80
        #print data
        #print "xo" * 40

        self._process_data(data)

    def _process_data(self, data):
        data = data.strip()
        
        # The presence of a prefix is indicated with a single leading ASCII
        # colon character (':', 0x3b), which must be the first character of
        # the message itself. There must be no gap (whitespace) between the
        # colon and the prefix.
        if data[0] == ':':
            self.prefix = data[1:].split(' ')[0]
        else:
            # If the prefix is missing from the message, it is assumed to have
            # originated from the connection from which it was received.
            #
            # TODO: Get the server name from the parent object.
            pass
