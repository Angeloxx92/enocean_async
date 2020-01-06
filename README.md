# Python EnOcean Async
A Python library for reading and controlling asynchronously [EnOcean](http://www.enocean.com/) devices.
This library was inspired by [Python EnOcean](https://github.com/kipe/enocean).

I It has been tested on the [SB-300 EnOcean](https://www.enocean.com/en/products/enocean_modules/usb-300-oem/).
This Python module receives messages from an EnOcean interface (e.g. via USB) that runs in an asynchronous Thread and can publish those packets to an asynchronous TCP server.By default it answer to UTETeachInPacket

You may also configure the action done by the EnOcean interface and by the TCP server everytime you recive a RadioPacket. You are not obliged to use the TCP server.

It builds upon `asyncio`

## Define persistant device name for EnOcean interface

If you own an USB EnOcean interface and use it together with some other USB devices you may face the situation that the EnOcean interface gets different device names depending on your plugging and unplugging sequence, such as `/dev/ttyUSB0` or `/dev/ttyUSB1`. 

To solve this you'll need
*  idVendor
*  idProduct
*  serial

of your Enocean USB Serial Communicator. Paste the following lines inside a terminal to find them 
`Remember to take a note of those informations`

```
udevadm info -a -n /dev/ttyUSB0 | grep '{idVendor}' | head -n1
udevadm info -a -n /dev/ttyUSB0 | grep '{idProduct}' | head -n1
udevadm info -a -n /dev/ttyUSB0 | grep '{serial}' | head -n1
```

After that 
```
cd /etc/udev/rules.d/
sudo nano 99-usb-serial.rules
```
Past this line inside the file and **REPLACE** 
*  YOURidVendor
*  YOURidProduct
*  YOURserial

with the ones you've obtained above
```
SUBSYSTEM=="tty", ATTRS{idVendor}=="YOURidVendor", ATTRS{idProduct}=="YOURidProduct", ATTRS{serial}=="YOURserial", SYMLINK+="enocean"
```
after that you're device will be always `/dev/anocean`

***THIS PYTHON MODULE ASSUMES THAT YOU'VE ALREADY DONE THAT***

# Requirements
*  python>=3.7

# Installation

Option 1: Using pip
===================

enocean_async is available on [PyPI](https://pypi.org/project/enocean-async/) and can be
installed using ``pip``:


    # Install system-wide
    $ sudo pip3 install enocean-async

    # ... or user-wide installation
    $ pip3 install --user enocean-async


Option 2: From source
=====================

    $ git clone https://github.com/Angeloxx92/enocean_async.git
    $ cd enocean_async
    $ python3 setup.py install


# Simple Usage
[Examples](https://github.com/Angeloxx92/enocean_async/tree/master/examples)
