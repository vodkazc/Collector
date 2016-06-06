"""
File: PicoEnum.py
Author: zc
Date: 2016.6.2
Description: This file include all enums in pico's DLL
"""
from ctypes import *


class CHANNEL:
    CHANNEL_A = 0
    CHANNEL_B = 1
    CHANNEL_C = 2
    CHANNEL_D = 3
    EXTERNAL = 4
    MAX_CHANNELS = EXTERNAL
    TRIGGER_AUX = 5
    MAX_TRIGGER_SOURCES = 6


class THRESHOLD_DIRECTION:
    ABOVE = 0
    BELOW = 1
    RISING = 2
    FALLING = 3
    RISING_OR_FALLING = 4
    ABOVE_LOWER = 5
    BELOW_LOWER = 6
    RISING_LOWER = 7
    FALLING_LOWER = 8

    # Windowing using both thresholds
    INSIDE = ABOVE
    OUTSIDE = BELOW
    ENTER = RISING
    EXIT = FALLING
    ENTER_OR_EXIT = RISING_OR_FALLING
    POSITIVE_RUNT = 9
    NEGATIVE_RUNT = 10
    NONE = RISING


class RATIO_MODE:
    RATIO_MODE_NONE = 0
    RATIO_MODE_AGGREGATE = 1
    RATIO_MODE_DECIMATE = 2
    RATIO_MODE_AVERAGE = 4
    RATIO_MODE_DISTRIBUTION = 8


class DEVICE_RESOLUTION:
    DR_8BIT = 0
    DR_12BIT = 1
    DR_14BIT = 2
    DR_15BIT = 3
    DR_16BIT = 4


class TriggerChannelProperties(Structure):
    _fields_ = [('thresholdUpper', c_int16),
                ('thresholdUpperHysteresis', c_uint16),
                ('thresholdLower', c_int16),
                ('thresholdLowerHysteresis', c_uint16),
                ('channel', c_int),
                ('thresholdMode', c_int)]
