from wmd.actions import Action

import settings

class ReloadModule(Action):
    def recv_msg(self, irc, obj_data):
        username = obj_data.get_username()

        if username in settings.ADMINS:
            args = obj_data.params.split(" ")
            if "PRIVMSG" in obj_data.command and "RELOADMODULE" in args[1].upper():

                module_name, class_name = args[2].rsplit('.', 1)


                if not module_name in irc.actions:
                    irc.privmsg(username, "Invalid Module: %s" % module_name)
                    return
                elif not class_name in irc.actions[module_name][1]:
                    irc.privmsg(self, username, "Invalid Plugin" % class_name)
                elif class_name == self.__class__.__name__:
                    irc.privmsg(username, "Unable to reload self. Try restarting")
                    return

                reload(irc.actions[module_name][0])
                try:
                    classz = getattr(irc.actions[module_name][0], class_name)
                except AttributeError:
                    self.log("Class does not exist in module")
                    return

                irc.actions[module_name][1][class_name] = classz()

                msg = "Reloaded %s.%s" % (module_name, class_name)
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