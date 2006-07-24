class settopic:

    def __init__(self):
        self = []

    def getAction(self, data):
        input = data.split(' ')
        words = ""
        for word in input[6:]:
            words += ' ' + word
        return 'TOPIC ' + input[5] + ' :' + words[1:]
