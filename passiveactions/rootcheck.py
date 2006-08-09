class rootcheck:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            user = data.getUsername()
            if 'JOIN' in data.command:
                if 'root' in data.prefix:
                    cmd = "PRIVMSG " + data.prefix + " :" + user +": Root?!?!?!!??!"
                    cmd += "\r\nKICK " + data.prefix + " " + user + " :Root + irc = kick"
                    return cmd
        except:
            return False
       
