spyusers = []
spyusers.append('stevetest')

spymaster = ""

class spy:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            user = data.getUsername()
            if user in spyusers:
                if user in data:
                    input = data.split()
                    words = ""
                    for word in data.prefix.split(' ')[1:]:
                        words += ' ' + word
                    return 'PRIVMSG ' + spymaster + ' :' + user + ' in ' + data.prefix.split(' ')[0] + ' said "' + words[2:] + '"'
        except:
            return False
       
