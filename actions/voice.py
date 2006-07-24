class voice:

    def __init__(self):
        self = []

    def getAction(self, data):
        input = data.split(' ')
        return 'MODE ' + input[5] + ' +v ' + input[6]
