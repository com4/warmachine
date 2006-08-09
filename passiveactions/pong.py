class pong:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            if data.command == 'PING':
                if data.params[0] == ':':
                    server = data.params[1:]
                else:
                    server = data.params
                print 'Ponged ' +  server
                return 'PONG ' + server
        except:
            return False
