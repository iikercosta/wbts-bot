from multiprocessing import Process, Queue

from scanners import IP_scan_process, LE_scan_process, BR_EDR_scan_process
from config import WBTSBotConfig
from report import http_reporter


def main() -> None:

    bot_config: WBTSBotConfig = WBTSBotConfig()
    queue: Queue = Queue()

    http_process = Process(target=http_reporter, args=(queue, bot_config))
    ip_process = Process(target=IP_scan_process, args=(queue, bot_config))
    le_process = Process(target=LE_scan_process, args=(queue, bot_config))
    br_edr_process = Process(target=BR_EDR_scan_process, args=(queue, bot_config))

    ip_process.start()
    le_process.start()
    br_edr_process.start()
    http_process.start()

    ip_process.join()
    le_process.join()
    br_edr_process.join()
    http_process.join()


if __name__ == '__main__':
    main()
