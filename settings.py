# warmachine
#

# choose the nickname for you bot.
NICKNAME = 'warmachine'

# (optional) Only for servers that have nickserv.
NICKSERV_PASSWORD =''

SERVER = 'irc.freenode.org'
PORT = 6667
IDENT = 'warmachine'

CHANNELS = ('#warmachine-dev',)

ADMINS = ('com4',)

ACTIONS = (
    'wmd.actions.nickserv.IdentWithNickserv',
)

try:
    from local_settings import *
except ImportError:
    pass