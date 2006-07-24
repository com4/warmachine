import os

class pythondoc:

    def __init__(self):
        self = []

    def getAction(self, data):
        try:
            input   = data.split(' ')
            module  = input[5].replace(' ', '')
            try:
                module2 = input[6][0:-2] 
                execstring = "python -c \"from " + module + " import " + module2 + "\nprint " + module2 + ".__doc__\n\" > /tmp/wmpycmd" 
            except:
                module = input[5][0:-2]
                execstring = "python -c \"import " + module + "\nprint " + module + ".__doc__\n\" > /tmp/wmpycmd" 
            os.system(execstring)
            doc = file('/tmp/wmpycmd').read().replace("\n", " ")
        except:
            doc = "I don't know nuthn about that."
        return 'PRIVMSG ' + input[2] + ' :' + doc       
