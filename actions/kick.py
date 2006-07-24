class kick:

    def __init__(self):
        self = []

    def getAction(self, data):
        input = data.split(' ')
        return 'KICK ' + input[5] + ' ' + input[6]

