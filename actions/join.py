class join:

    def __init__(self):
        self = []

    def getAction(self, data):
        channel = data.params.split(' ')[3]
        return 'JOIN ' + channel
