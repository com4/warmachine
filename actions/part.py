class part:

    def __init__(self):
        self = []

    def getAction(self, data):
        return 'PART ' + data[data.index('part')+5:]
