# warmachine
#

# choose the nickname for you bot.
NICKNAME = 'warmachine'

SERVER = 'irc.freenode.org'
PORT = 6667
IDENT = 'warmachine'

CHANNELS = ('#warmachine-dev',)

ADMINS = ('com4',)

try:
    from local_settings.py import *
except ImportError:
    pass