from PicoEnum import *

picoDll = windll.LoadLibrary("ps5000a.dll")

'''
Function: Open the Pico
Py: int OpenUnit(int16* , int8* , int)
C:
PICO_STATUS ps5000aOpenUnit
(
int16_t * handle,
int8_t * serial
PS5000A_DEVICE_RESOLUTION resolution
)
'''
OpenUnit = picoDll.ps5000aOpenUnit
OpenUnit.argtypes = (POINTER(c_int16), POINTER(c_int8), c_int)
OpenUnit.restype = c_int

'''
Function: Set Channel
Py: int SetChannel(int16, int, int16, int, int, float)
C:
PICO_STATUS ps5000aSetChannel
(
int16_t handle,
PS5000A_CHANNEL channel,
int16_t enabled,
PS5000A_COUPLING type,
PS5000A_RANGE range,
float analogueOffset
)
'''
SetChannel = picoDll.ps5000aSetChannel
SetChannel.argtypes = (c_int16, c_int, c_int16, c_int, c_int, c_float)
SetChannel.restypes = c_int

'''
Function: Get Timebase
Py: int GetTimebase(int16, uint32, int32, int32*, int32* , uint32)
C:
PICO_STATUS ps5000aGetTimebase
(
int16_t handle,
uint32_t timebase,
int32_t noSamples,
int32_t * timeIntervalNanoseconds,
int32_t * maxSamples,
uint32_t segmentIndex
)
'''
GetTimebase = picoDll.ps5000aGetTimebase
GetTimebase.argtypes = (c_int16, c_uint32, c_int32, POINTER(c_int32), POINTER(c_int32), c_uint32)
GetTimebase.restypes = c_int

'''
Function: Set Trigger Channel Directions
Py: int SetTriggerChannelDirections
PICO_STATUS ps5000aSetTriggerChannelDirections
(
int16_t handle,
PS5000A_THRESHOLD_DIRECTION channelA,
PS5000A_THRESHOLD_DIRECTION channelB,
PS5000A_THRESHOLD_DIRECTION channelC;
PS5000A_THRESHOLD_DIRECTION channelD;
PS5000A_THRESHOLD_DIRECTION ext,
PS5000A_THRESHOLD_DIRECTION aux
)
'''
SetTriggerChannelDirections = picoDll.ps5000aSetTriggerChannelDirections
SetTriggerChannelDirections.argtypes = (c_int16, c_int, c_int, c_int, c_int, c_int, c_int)
SetTriggerChannelDirections.restypes = c_int

'''
Function: Set Trigger Channel Properties
PICO_STATUS ps5000aSetTriggerChannelProperties
(
int16_t handle,
PS5000A_TRIGGER_CHANNEL_PROPERTIES * channelProperties,
int16_t nChannelProperties,
int16_t auxOutputEnable,
int32_t autoTriggerMilliseconds
)
'''
SetTriggerChannelProperties = picoDll.ps5000aSetTriggerChannelProperties
SetTriggerChannelProperties.argtypes = (c_int16, POINTER(TriggerChannelProperties), c_int16, c_int16, c_int32)
SetTriggerChannelProperties.restypes = c_int

'''
Function: Run Block
PICO_STATUS ps5000aRunBlock
(
int16_t handle,
int32_t noOfPreTriggerSamples,
int32_t noOfPostTriggerSamples,
uint32_t timebase,
int32_t * timeIndisposedMs,
uint32_t segmentIndex,
ps5000aBlockReady lpReady,
void * pParameter
)
'''
RunBlock = picoDll.ps5000aRunBlock
RunBlock.argtypes = (
    c_int16, c_int32, c_int32, c_uint32, POINTER(c_int32), c_uint32, CFUNCTYPE(c_int16, c_int, c_void_p), c_void_p)
RunBlock.restypes = c_int

'''
Function: Set Data Buffer
PICO_STATUS ps5000aSetDataBuffer
(
int16_t handle,
PS5000A_CHANNEL channel,
int16_t * buffer,
int32_t bufferLth,
uint32_t segmentIndex,
PS5000A_RATIO_MODE mode
)
'''
SetDataBuffer = picoDll.ps5000aSetDataBuffer
SetDataBuffer.argtypes = (c_int16, c_int, c_int16, c_int32, c_uint32, c_int)
SetDataBuffer.restypes = c_int

'''
Function: GetValues
PICO_STATUS ps5000aGetValues
(
int16_t handle,
uint32_t startIndex,
uint32_t * noOfSamples,
uint32_t downSampleRatio,
PS5000A_RATIO_MODE downSampleRatioMode,
uint32_t segmentIndex,
int16_t * overflow
)
'''
GetValues = picoDll.ps5000aGetValues
GetValues.argtypes = (c_int16, c_uint32, c_uint32, c_uint32, c_int, c_uint32, c_int16)
GetValues.restypes = c_int

'''
Function: Stop the Pico
PICO_STATUS ps5000aStop
(
int16_t handle
)
'''
Stop = picoDll.ps5000aStop
'#Stop.argtypes = c_int'
'#Stop.restypes = c_int'
