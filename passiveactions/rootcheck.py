class rootcheck:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            user = data[1:data.index('!')]
            input = data.split()
            if 'JOIN' in input[1]:
                if 'root' in input[0]:
                    cmd = "PRIVMSG " + input[2][1:] + " :" + user +": Root?!?!?!!??!"
                    cmd += "\r\nKICK " + input[2][1:] + " " + user + " :Root + irc = kick"
                    return cmd
        except:
            return False
       
