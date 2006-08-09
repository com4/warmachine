class voice:

    def __init__(self):
        self = []

    def getAction(self, data):
        channel = data.params[0:data.params.index(' ')]
        user = data.params.split(' ')[3]
        return 'MODE ' + channel + ' +v ' + user
