class pong:

    def __init__(self):
        self = []

    def getAction(self, data, users):
        try:
            if data.find ( 'PING' ) != -1:
                print 'Ponged ' +  data.split()[1]
                return 'PONG ' + data.split()[1]
        except:
            return False
       
