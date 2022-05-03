# wbts-bot

Wi-Fi and Bluetooth Tracking System Bot module

## Environment

Requirements that must have the host running the WBTS Bot module:

* Wi-Fi or Ethernet interface.
* Bluetooth interface > v4.0.
* Linux operating system.

## Installation of dependencies

1. `sudo apt-get install bluez`
2. `sudo apt-get install bluetooth`
3. `sudo apt-get install libbluetooth-dev`
4. `sudo apt-get install python-bluez`
5. `sudo apt install pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev`
6. `sudo pip3 install gattlib`
7. `sudo pip3 install pybluez`


## Usage

Modify the file `wbts-bot-config.json`.
```json
{
  "wbts-bot-location": "Home 1",
  "wbts-bot-ip-interface": "wlp1s0",
  "wbts-bot-bluetooth-interface": "hci0",
  "wbts-bot-ip-passive-scan-timer": 10,
  "wbts-bot-le-passive-scan-timer": 10,
  "wbts-bot-bredr-passive-scan-timer": 10,
  "wbts-server-ip": "localhost",
  "wbts-server-http-port": 5000,
  "wbts-server-post-path": "register-devices",
  "wbts-bot-backup-dir": "backups"
}
```
* `wbts-bot-location` refers to the location where the bot is installed.
* `wbts-bot-ip-interface` refers to the IP interface in which the Bot will scan.
* `wbts-bot-bluetooth-interface` refers to the Bluetooth interface in which the Bot will scan.
* `*-scan-timers` refers to the refresh rate of reporting to the WBTS Server.
* `wbts-server-ip` refers to the WBTS Server IP.
* `wbts-server-http-port` refers to the WBTS Server port.
* `wbts-server-post-path` refers to the HTTP endpoint of the WBTS Server (shouldn't be modified).
* `wbts-bot-backup-dir` when the WBTS Server is unavaible, the Bot does backups in this directory.

In order to execute the bot (root privileges needed):

`sudo python3 main.py`


