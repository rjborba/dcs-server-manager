#!/usr/bin/env python3
import time
import subprocess
import threading

import datetime

TIME_TO_RESTART = 8 * 60 * 60

dcs_updater_path = 'C:\\Program Files\\Eagle Dynamics\\DCS World Server\\bin\\DCS_updater.exe'
dcs_path = 'C:\\Program Files\\Eagle Dynamics\\DCS World Server\\bin\\DCS.exe'
class Server:
    def __init__(self):
        print('------ FIGHT\'S ON SERVER ------')
        # silent mode not available yet
        # self._start_updater_and_dcs()
        self._start_dcs()

    # def _start_updater_and_dcs(self):
    #     # Updater
    #     try: 
    #         print(datetime.datetime.now(), ': Starting UPDATER')
    #         subprocess.check_call([dcs_updater_path, "update"])
    #         self._start_dcs()
    #     except KeyboardInterrupt:
    #         print(datetime.datetime.now(), ': Script was MANUALLY stopped. Closing Updater.')
    #     except subprocess.CalledProcessError:
    #         print(datetime.datetime.now(), ': UPDATER has exited a non zero code. Check DCS logs for more info. Restarting...')
    #         self._start_updater_and_dcs()

    #     else:
    #         print(datetime.datetime.now(), ': Error during UPDATE trying again...')

    def _start_dcs(self):
         # DCS
        try:
            print(datetime.datetime.now(), ': Starting server')
            subprocess.check_call([dcs_path],
                                timeout=TIME_TO_RESTART)
        except subprocess.TimeoutExpired: 
            print(datetime.datetime.now(), ': DCS has been killed gratefully on timeout... Restarting...')
            time.sleep(5)
            self._start_dcs();
        except KeyboardInterrupt:
            print(datetime.datetime.now(), ': Script was MANUALLY stopped. Closing DCS. Please wait...')
        else:
            print(datetime.datetime.now(), ': DCS has exited before timeout. Check DCS logs for more info. Restarting...')
            self._start_dcs();

server = Server()

