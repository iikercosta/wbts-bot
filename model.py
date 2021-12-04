from dataclasses import dataclass
from typing import List


class DeviceType:
    BLUETOOTH_LE: str = 'BLUETOOTH_LE'
    BLUETOOTH_BR_EDR: str = 'BLUETOOTH_BR_EDR'
    IP: str = 'IP'


@dataclass
class Device:
    signature: str
    dev_type: str
    timestamps: List[int]


