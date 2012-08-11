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

DB_PATH = "warmachine.db"

ACTIONS = (
    'wmd.actions.passive.nickserv.IdentWithNickserv',
    'wmd.actions.passive.pong.RespondToPing',
    'wmd.actions.passive.topic_archive.TopicArchive',
    'wmd.actions.passive.rejoin_on_kick.RejoinOnKick',
    'wmd.actions.modules.ReloadModule',
    'wmd.actions.modules.LoadModule',
    'wmd.actions.modules.ListModules',
    'wmd.actions.modules.UnloadModule',
    'wmd.actions.google.GoogleSearch',
)

try:
    from local_settings import *
except ImportError:
    pass