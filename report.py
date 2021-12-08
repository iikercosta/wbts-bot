import json
from multiprocessing import Queue
from typing import List

import requests

from config import WBTSBotConfig
from model import Device


def back_up(backup_n: int, devs_dict: dict) -> None:
    with open(f'backups/{backup_n}backup.json', 'w') as fd:
        json.dump(devs_dict, fd)


def http_reporter(queue: Queue, conf: WBTSBotConfig) -> None:
    back_n: int = 0
    while True:
        devs: List[Device] = queue.get()
        devs_dict = {'location': conf.LOCATION, 'devices': [dev.__dict__ for dev in devs]}
        try:

            requests.post(f'http://{conf.SERVER_IP}:{conf.SERVER_HTTP_PORT}/{conf.SERVER_POST_PATH}', json=devs_dict)

        except OSError:
            back_up(back_n, devs_dict)
            back_n += 1
