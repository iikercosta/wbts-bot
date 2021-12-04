import json

CONFIG_FILE = 'wbts-bot-config.json'


class WBTSBotConfig:
    LOCATION: str
    IP_IF: str
    BLUETOOTH_IF: str
    IP_PASSIVE_TIMER: int
    BLE_TIMER: int
    BR_EDR_TIMER: int
    SERVER_IP: str
    SERVER_HTTP_PORT: int
    SERVER_POST_PATH: str

    def __init__(self) -> None:

        try:

            with open(CONFIG_FILE, "r") as fd:

                conf_dict = json.load(fd)
                self.LOCATION = conf_dict["wbts-bot-location"]
                self.IP_IF = conf_dict["wbts-bot-ip-interface"]
                self.BLUETOOTH_IF = conf_dict["wbts-bot-bluetooth-interface"]
                self.IP_PASSIVE_TIMER = conf_dict["wbts-bot-ip-passive-scan-timer"]
                self.BLE_TIMER = conf_dict["wbts-bot-le-passive-scan-timer"]
                self.BR_EDR_TIMER = conf_dict["wbts-bot-bredr-passive-scan-timer"]
                self.SERVER_IP = conf_dict["wbts-server-ip"]
                self.SERVER_HTTP_PORT = conf_dict["wbts-server-http-port"]
                self.SERVER_POST_PATH = conf_dict["wbts-server-post-path"]

        except FileNotFoundError:
            raise FileNotFoundError
