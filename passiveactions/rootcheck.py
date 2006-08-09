class rootcheck:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            user = data.getUsername()
            if 'JOIN' in data.command:
                if 'root' in data.prefix:
                    if data.params[0] == ':':
                        data.params = data.params[1:]

                    cmd = "PRIVMSG " + data.params + " :" + user +": Root?!?!?!!??!"
                    cmd += "\r\nKICK " + data.params + " " + user + " :Root + irc = kick"
                    return cmd
        except:
            return False
       
