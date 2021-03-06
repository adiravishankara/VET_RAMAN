#!/usr/bin/env python
################################################################################
#                               demo-simple.py                                 #
################################################################################
#                                                                              #
#  DESCRIPTION:  Simplest possible Python demo.                                #
#                                                                              #
#  ENVIRONMENT:  (if using Miniconda3)                                         #
#                $ rm -f environment.yml                                       #
#                $ ln -s environments/conda-linux.yml  (or macos, etc)         #
#                $ conda env create -n wasatch3                                #
#                $ conda activate wasatch3                                     #
#  INVOCATION:                                                                 #
#                $ python demo-simple.py                                       #
#                                                                              #
################################################################################
import sys

from wasatch.WasatchBus    import WasatchBus
from wasatch.WasatchDevice import WasatchDevice
from wasatch.MockUSBDevice import MockUSBDevice as MUD

bus = WasatchBus()
if not bus.device :
    print("no spectrometers found")
    sys.exit(1)

device_id = bus.device_ids[0]
print("found %s" % device_id)

device = WasatchDevice(device_id)
device = MUD(device_id)
if not device.connect():
    print("connection failed")
    sys.exit(1)

print("connected to %s %s with %d pixels from (%.2f, %.2f)" % (
    device.settings.eeprom.model,
    device.settings.eeprom.serial_number,
    device.settings.pixels(),
    device.settings.wavelengths[0],
    device.settings.wavelengths[-1]))

print("setting integration time")
device.hardware.set_integration_time_ms(10)
# or: device.change_setting("integration_time_ms", 10)

print("reading spectrum")
spectrum = device.hardware.get_line().spectrum
# or: spectrum = device.acquire_data().spectrum

for pixel in range(device.settings.pixels()):
    print("%8.2f %8.2f" % (device.settings.wavelengths[pixel], spectrum[pixel]))

print("done")
