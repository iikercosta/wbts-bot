import time
from multiprocessing import Queue, Process
from socket import AF_PACKET, SOCK_RAW, ntohs, socket
from typing import List

from config import WBTSBotConfig
from model import Device, DeviceType
from utils import get_ethernet_header, macs_to_devices

import bluetooth
from gattlib import DiscoveryService


def passive_ip_scan(if_name: str, time_out: int = 5) -> List[Device]:
    macs: set = set()

    with socket(AF_PACKET, SOCK_RAW, ntohs(3)) as sd:
        sd.bind((if_name, 0))
        start_time = time.time()

        while time.time() < start_time + time_out:
            dest, src, prototype = get_ethernet_header(sd.recv(65535))
            mac = src.hex(':')
            macs.add(mac)

    devs_parsed = macs_to_devices(list(macs), DeviceType.IP)

    return devs_parsed


def passive_le_scan(if_name: str = '', time_out: int = 5) -> List[Device]:

    discover: DiscoveryService = DiscoveryService(if_name)

    discovered_devs = list(set(discover.discover(time_out)))

    return macs_to_devices(discovered_devs, DeviceType.BLUETOOTH_LE)


def passive_br_edr_scan(time_out: int = 5) -> List[Device]:

    discovered_devs = bluetooth.discover_devices(lookup_names=False, duration=time_out)

    return macs_to_devices(discovered_devs, DeviceType.BLUETOOTH_BR_EDR)


def IP_scan_process(queue: Queue, conf: WBTSBotConfig) -> None:
    while True:
        devs: List[Device] = passive_ip_scan(conf.IP_IF, conf.IP_PASSIVE_TIMER)
        if devs:
            queue.put(devs)


def LE_scan_process(queue: Queue, conf: WBTSBotConfig) -> None:
    while True:
        devs: List[Device] = passive_le_scan(conf.BLUETOOTH_IF, conf.BLE_TIMER)
        if devs:
            queue.put(devs)


def BR_EDR_scan_process(queue: Queue, conf: WBTSBotConfig) -> None:
    while True:
        devs: List[Device] = passive_br_edr_scan(conf.BR_EDR_TIMER)
        if devs:
            queue.put(devs)
