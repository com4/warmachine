class join:

    def __init__(self):
        self = []

    def getAction(self, data):
        return 'JOIN ' + data[data.index('join')+5:]
