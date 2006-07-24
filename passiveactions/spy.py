spyusers = []
spyusers.append('stevetest')

spymaster = ""

class spy:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            user = data[1:data.index('!')]
            if user in spyusers:
                if user in data:
                    input = data.split()
                    words = ""
                    for word in input[3:]:
                        words += ' ' + word
                    return 'PRIVMSG ' + spymaster + ' :' + user + ' in ' + input[2] + ' said "' + words[2:] + '"'
        except:
            return False
       
