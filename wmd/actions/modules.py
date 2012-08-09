from wmd.actions import Action

import settings

class ReloadModule(Action):
    def recv_msg(self, irc, obj_data):
        username = obj_data.get_username()

        if username in settings.ADMINS:
            args = obj_data.params.split(" ")
            if "PRIVMSG" in obj_data.command and "RELOADMODULE" in args[1].upper():
                module = args[2]
                if not module in irc.actions:
                    irc.privmsg(username, "Invalid Module: %s")
                    return
                elif module == self.__class__.__name__:
                    irc.privmsg(username, "Unable to reload self. Try restarting")
                    return
                module_class = irc.actions[module].__module__
                module_path = module_class + '.' + module

                reload(irc.actions[module])

                msg = "Reloaded %s" % (module_path,)
                self.log(msg)
                irc.privmsg(username, msg)

class LoadModule(Action):
    def recv_msg(self, irc, obj_data):
        username = obj_data.get_username()
        if username in settings.ADMINS:
            args = obj_data.params.split(" ")
            if "PRIVMSG" in obj_data.command and ":LOADMODULE" in args[1].upper():
                module_path = args[2]
                if module_path.split(".")[-1] in irc.actions:
                    irc.privmsg(username, "Module %s already loaded" % (module_path,))
                    return
                #irc.load_action(module_path)

                msg = "Loading %s" % (module_path,)
                self.log(msg)
                irc.privmsg(username, msg)
                return {'load': module_path}

class ListModules(Action):
    def recv_msg(self, irc, obj_data):
        username = obj_data.get_username()

        if username in settings.ADMINS:
            args = obj_data.params.split(" ")
            if "PRIVMSG" in obj_data.command and ":LISTMODULES" in args[1].upper():
                for module in irc.actions:
                    msg = module
                    irc.privmsg(username, msg)

class UnloadModule(Action):
    def recv_msg(self, irc, obj_data):
        username = obj_data.get_username()

        if username in settings.ADMINS:
            args = obj_data.params.split(" ")
            if "PRIVMSG" in obj_data.command and ":UNLOADMODULE" in args[1].upper():
                module_name = args[2]
                if not module_name in irc.actions:
                    irc.privmsg(username, "Module %s already unloaded" % (module_name,))
                    return
                    #irc.load_action(module_path)

                msg = "Unloading %s" % (module_name,)
                self.log(msg)
                irc.privmsg(username, msg)
                return {'unload': module_name}