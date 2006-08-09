class part:

    def __init__(self):
        self = []

    def getAction(self, data):
        channel = data.params.split(' ')[3]
        return 'PART ' + channel
