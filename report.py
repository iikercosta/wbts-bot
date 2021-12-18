import json
import os
import time
from multiprocessing import Queue
from typing import List

import requests

from config import WBTSBotConfig
from model import Device


def back_up(devs_dict: dict) -> None:
    with open(f'backups/backup-{int(time.time())}.json', 'w') as fd:
        json.dump(devs_dict, fd)


def http_reporter(queue: Queue, conf: WBTSBotConfig) -> None:
    url: str = f'http://{conf.SERVER_IP}:{conf.SERVER_HTTP_PORT}/{conf.SERVER_POST_PATH}'

    while True:

        devs: List[Device] = queue.get()
        devs_dict = {'location': conf.LOCATION, 'devices': [dev.__dict__ for dev in devs]}

        try:
            requests.post(url, json=devs_dict)

            if len(os.listdir(conf.BACK_UP_DIR)) != 0:
                for f in os.listdir(conf.BACK_UP_DIR):
                    with open(f'{conf.BACK_UP_DIR}/{f}', 'r') as fd:
                        requests.post(url, json=json.load(fd))
                    os.remove(f'{conf.BACK_UP_DIR}/{f}')
        except OSError:
            back_up(devs_dict)
