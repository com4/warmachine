NICKNAME = 'warmachine'

SERVER = 'irc.freenode.org'
PORT = 6667
IDENT = 'warmachine'

CHANNELS = ('#antitech-dev',)

try:
    from local_settings.py import *
except ImportError:
    pass