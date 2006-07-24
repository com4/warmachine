class autoop:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            input = data.split()
            if 'JOIN' in input[1]:
                user = data[1:data.index('!')]
                if user in users:
                    print "autoop"
                    return 'MODE ' + input[2][1:] + ' +o ' + user
        except:
            return False
