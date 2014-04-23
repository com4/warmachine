#!/usr/bin/env python
import sqlite3

from wmd.irc import IRC
import settings

if __name__ == '__main__':
    connection = sqlite3.connect(settings.DB_PATH)
    c = connection.cursor()

    # check to see if a table exists
    is_installed = bool(c.execute("SELECT name FROM sqlite_master WHERE "
                                  "type='table' AND name='warmachine_settings'"
                                  ).fetchone()
    )

    if not is_installed:
        c.execute("""CREATE TABLE warmachine_settings (
                        key text,
                        value text,
                        plugin text,
                        primary key (key, plugin)
                        );
        """)
        c.execute("""CREATE TABLE warmachine_plugins (
                        id text,
                        name text,
                        description text,
                        is_active int,
                        primary key (id)
                        );
        """)

    i = IRC(settings.SERVER, settings.NICKNAME, settings.IDENT,
            settings.PASSWORD, settings.PORT,)
    i.connect()
    import time; time.sleep(10)
    for channel in settings.CHANNELS:
        i.join(channel)
    i()
