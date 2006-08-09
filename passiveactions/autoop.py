class autoop:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            if data.command == 'JOIN':
                user = data.getUsername()
                if user in users:
                    print "autoop"

                    if data.params[0] == ':':
                        data.params = data.params[1:]
                    return 'MODE ' + data.params + ' +o ' + user
        except Exception,e:
            return False
