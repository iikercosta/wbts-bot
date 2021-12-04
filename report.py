from multiprocessing import Queue
from typing import List

import requests

from config import WBTSBotConfig
from model import Device


def http_reporter(queue: Queue, conf: WBTSBotConfig) -> None:
    while True:
        devs: List[Device] = queue.get()
        devs_dict = {'location': conf.LOCATION, 'devices': [dev.__dict__ for dev in devs]}
        try:

            requests.post(f'http://{conf.SERVER_IP}:{conf.SERVER_HTTP_PORT}/{conf.SERVER_POST_PATH}', json=devs_dict)

        except OSError:
            print("Couldn't connect to WBTS server")
