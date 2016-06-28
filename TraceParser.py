# TraceParser.py --- parsing the .trs file
# Author: Vodka
# Email:vodkazc@gmail.com
# Date: 2016.06.08

import logging
import os


class CommonFile(object):
    """Common File Object for IO"""

    def __init__(self, path):
        self.path = path
        self.byteNum = 0
        self.fileHandler = None

    def openFile(self, mode):
        if os.path.exists(self.path):
            self.fileHandler = open(self.path, mode)
            return True
        else:
            logging.info(self.path + 'does not exist.')
            return False

    def closeFile(self):
        if self.fileHandler:
            self.fileHandler.close()
        return True

    def readByte(self, num):
        byte_re = self.fileHandler.read(num)
        self.byteNum += num
        return byte_re

    def readInt(self, num=4):
        byte_re = self.fileHandler.read(num)
        self.byteNum += num
        return int.from_bytes(byte_re, 'little')

    def readFloat(self, num=4):
        byte_re = self.fileHandler.read(num)
        self.byteNum += num
        return float.fromhex(byte_re.hex())

    def readStr(self, num):
        byte_re = self.fileHandler.read(num)
        self.byteNum += num
        return byte_re.decode()

    def writeByte(self, byte_str):
        self.fileHandler.write(byte_str)
        return True

    def writeInt(self, data_in):
        self.fileHandler.write(data_in)


class Trace(object):
    """Trace Class for .trs file"""

    def __init__(self, path):
        self.path = path
        self.traceFile = CommonFile(self.path)
        self.TraceSetObjects = {b'\x41': 'NT', b'\x42': 'NS', b'\x43': 'SC', b'\x44': 'DS', b'\x45': 'TS',
                                b'\x46': 'GT', b'\x47': 'DC', b'\x48': 'XO', b'\x49': 'XL', b'\x4A': 'YL',
                                b'\x4B': 'XS', b'\x4C': 'YS', b'\x4D': 'TO', b'\x4E': 'LS', b'\x5F': 'TB'}
        self.TraceHeader = {}
        self.headerLength = 0
        self.traceNumber = -1
        self.pointCount = -1
        self.sampleCoding = -1
        self.sampleLength = 0
        self.cryptoDataLength = 0
        self.titleSpace = 0
        self.globalTraceTitle = 'trace'
        self.description = None
        self.xAxisOffset = 0
        self.xLabel = ''
        self.yLabel = ''
        self.xAxisScale = 0
        self.yAxisScale = 0
        self.traceOffsetForDisp = 0
        self.logScale = 0
        self.parseTraceHeader()

    def readHeaderDataLength(self):
        data_length = self.traceFile.readInt(1)
        if data_length & 0x80:
            data_length &= 0x7F
            data_length = self.traceFile.readInt(data_length)
        return data_length

    def parseTraceHeader(self):
        logging.info('Parsing Trace Header')
        self.traceFile.openFile('rb')
        while True:
            ch = self.traceFile.readByte(1)

            if ch not in self.TraceSetObjects:
                logging.error('Unknown Trace Header :' + ch.hex())
                raise ValueError('Unknown Trace Header :' + ch.hex())
            if self.TraceSetObjects[ch] in self.TraceHeader:
                logging.error('Duplicate Trace Header :' + ch.hex())
                raise ValueError('Duplication Trace Header')
            if ch == b'\x5F':
                logging.debug('Parsing Trace File End.')
                self.readHeaderDataLength()
                self.headerLength = self.traceFile.byteNum
                logging.debug('Trace Header Length : ' + str(self.headerLength))
                break
            if ch == b'\x41':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 4:
                    logging.error('Wrong trace header : ' + ch.hex())
                    raise ValueError('Wrong Trace Header')
                self.traceNumber = self.traceFile.readInt(data_length)
                logging.debug('Trace Number : ' + str(self.traceNumber))
            if ch == b'\x42':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 4:
                    logging.error('Wrong trace header : ' + ch.hex())
                    raise ValueError('Wrong Trace Header')
                self.pointCount = self.traceFile.readInt(data_length)
                logging.debug('Point Count : ' + str(self.pointCount))
            if ch == b'\x43':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 1:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError('Wrong Trace Header')
                value_tmp = self.traceFile.readInt(1)
                self.sampleCoding = (value_tmp & 0x10)
                self.sampleLength = value_tmp & 0x0F
                logging.debug('Sample Coding : ' + str(self.sampleCoding))
                logging.debug('Sample Length : ' + str(self.sampleLength))
            if ch == b'\x44':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 2:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError('Wrong Trace Header')
                self.cryptoDataLength = self.traceFile.readInt(data_length)
                logging.debug('Crypto Data Length : ' + str(self.cryptoDataLength))
            if ch == b'\x45':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 1:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError('Wrong Trace Header')
                self.titleSpace = self.traceFile.readInt(data_length)
                logging.debug('Title Space : ' + ch.hex())
            if ch == b'\x46':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                self.globalTraceTitle = self.traceFile.readStr(data_length)
                logging.debug('Global Trace Title : ' + self.globalTraceTitle)
            if ch == b'\x47':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                self.description = self.traceFile.readStr(data_length)
                logging.debug('Description : ' + self.description)
            if ch == b'\x48':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 4:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError('Wrong Trace Header : ' + ch.hex())
                self.xAxisOffset = self.traceFile.readInt()
                logging.debug('X-axis Offset : ' + str(self.xAxisOffset))
            if ch == b'\x49':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                self.xLabel = self.traceFile.readStr(data_length)
                logging.debug('X Label : ' + self.xLabel)
            if ch == b'\x4A':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                self.yLabel = self.traceFile.readStr(data_length)
                logging.debug('Y Label : ' + self.yLabel)
            if ch == b'\x4B':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 4:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError
                self.xAxisScale = self.traceFile.readFloat(data_length)
                logging.debug('X-axis Scale : ' + str(self.xAxisScale))
            if ch == b'\x4C':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 4:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError
                self.yAxisScale = self.traceFile.readFloat(data_length)
                logging.debug('Y-axis Scale : ' + str(self.xAxisScale))
            if ch == b'\x4D':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 4:
                    logging.error('Wrong Trace Header : ' + ch.hex())
                    raise ValueError
                self.traceOffsetForDisp = self.traceFile.readInt(data_length)
                logging.debug('Trace Offet For Displying : ' + self.traceOffsetForDisp)
            if ch == b'\x4E':
                logging.debug('Parsing Trace Header ' + ch.hex())
                data_length = self.readHeaderDataLength()
                if data_length != 1:
                    logging.error('Wrong Trace header : ' + ch.hex())
                    raise ValueError
                self.logScale = self.traceFile.readInt(1)
                logging.debug('Log Scale : ' + str(self.logScale))

        self.traceFile.closeFile()
        return True
