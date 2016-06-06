#import pico
from ctypes import *
import PicoEnum

picoDll = windll.LoadLibrary("ps5000a.dll")

handle = c_int16(0)
Serial = c_int8()
OpenUnit = picoDll.ps5000aOpenUnit
OpenUnit.argtypes = (POINTER(c_int16), POINTER(c_int8), c_int)
OpenUnit.restype = c_int

status = OpenUnit(handle, None, 0)
'#PicoEnum.DEVICE_RESOLUTION.DR_8BIT'

print(status)
print(handle)

Stop = picoDll.ps5000aStop
status = Stop(handle)

print(status)
