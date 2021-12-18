import struct
import time
from socket import htons
from typing import List

from model import Device


def macs_to_devices(devs: list, dev_type: str) -> List[Device]:
    return [Device(mac, dev_type, [int(time.time())]) for mac in devs]


def get_ethernet_header(raw_data: bytes) -> tuple:
    dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

    prototype = htons(prototype)

    return dest, src, prototype
