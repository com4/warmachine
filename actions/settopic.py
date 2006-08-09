class settopic:

    def __init__(self):
        self = []

    def getAction(self, data):
        channel = data.params.split(' ')[3]
        words = data.params.split(' ')[4:]


        say = "" 
        for word in words:
            say += word + " "

        return 'TOPIC ' + channel + ' :' + say
