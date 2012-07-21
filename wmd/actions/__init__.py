class Action(object):
    def log(self, msg):
        print "-> %s: %s" %(self.__class__.__name__, msg)