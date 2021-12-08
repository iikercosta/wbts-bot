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
            if os.listdir(conf.BACK_UP_DIR):

                for file in os.listdir(conf.BACK_UP_DIR):
                    with open(f'{conf.BACK_UP_DIR}/{file}', 'r') as fd:
                        requests.post(url, json=json.load(fd))

                    print(f'Sent backup{file}')
                    os.remove(f'{conf.BACK_UP_DIR}/{file}')

        except OSError:
            back_up(devs_dict)


