# TraceParser.py --- parsing the .trs file
# Author: Vodka
# Email:vodkazc@gmail.com
# Date: 2016.06.08

import logging


class Trace:
    """Trace Class for .trs file"""

    def __init__(self, path):
        self.path = path
        self.TraceSetObjects = {0x41: 'NT', 0x42: 'NS', 0x43: 'SC', 0x44: 'DS', 0x45: 'TS', 0x46: 'GT',
                                0x47: 'DC', 0x48: 'XO', 0x49: 'XL', 0x4A: 'YL', 0x4B: 'XS', 0x4C: 'YS',
                                0x4D: 'TO', 0x4E: 'LS', 0x5F: 'TB'}
        self.TraceHeader = {}
        self.headerLength = 0
        self.parseTraceHeader()


    def readTraceFileHeader(self, traceFile, byteNum):
        ch = traceFile.read(byteNum)
        self.headerLength += byteNum
        return ch

    def readHeaderDataLength(self, traceFile):
        ch = self.readTraceFileHeader(traceFile, 1)
        dataLength = 0
        if ch & 0x80:
            ch &= 0x7F
            dataLength = self.readTraceFileHeader(traceFile, ch)
        else:
            dataLength = ch

        return dataLength

    def parseTraceHeader(self):
        logging.info('Parsing Trace Header')
        with open(self.path, 'rb') as traceFile:
            while True:
                ch = int(traceFile.read(1))
                self.headerLength += 1

                if ch not in self.TraceSetObjects:
                    logging.error('Unknown Trace Header :' + ch)
                    return False
                if self.TraceSetObjects[ch] in self.parseTraceHeader:
                    logging.error('Duplicate Trace Header :' + ch)
                    return False
                if ch == 0x5F:
                    logging.debug('Parsing Trace File End.')
                    break
                if ch == 0x41:
                    logging.debug('Parsing Trace Header ' + ch)

        return True