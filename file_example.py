#	acs0-rci.py
#   Brandon Withrow
#   notes:
#       

import time
import serial
import argparse
import sys
from binascii import unhexlify
from binascii import hexlify
from datetime import datetime
import os.path
from os import path


configFile = '.\\RS232_CONFIG_FILES\\CONFIG_FILE\\RS232_ATP_TESTER_CONFIG.txt'
uutFilePath = '.\\RS232_CONFIG_FILES\\UNIT_UNDER_TEST\\'
csFilePath = '.\\RS232_CONFIG_FILES\\COMMAND_SETS\\'
pwrCsFilePath = '.\\RS232_CONFIG_FILES\\COMMAND_SETS\\'
tsleep = .2
maxWaitTime = 12
pwrTimeOut = 3
maxAttempts = 3
reportDir = '.\\RS232_TEST_REPORT\\'
inpTimeout = 2
timeOutError = 'Reply Timeout'
testStartTime = datetime.now()
testReport = ['UUT', 'Serial Number: ', 'Started: ' + testStartTime.strftime("%m-%d-%Y %H.%M.%S")]
stdSetType = 'std'
hexSetType = 'hex'
enStdCmds = 1
enPwrCmds = 1
enInpCmds = 1
allRates = [115200, 38400, 9600]
allRatesMarker = 0
ser = None

def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
        return content_array

def parse_file(path, deliminator):
    input_array = file_read(path)
    leftColData = [0 for x in range(len(input_array))]
    rightColData = [0 for x in range(len(input_array))]
    for i in range(len(input_array)):
        tempArray = input_array[i].split(deliminator)
        leftColData[i] = tempArray[0]
        rightColData[i] = tempArray[1].replace(chr(10), '')
    return (leftColData, rightColData)

def setConfigSettings():
    lCol, rCol = parse_file(configFile, ':')
    global uutFilePath, csFilePath, pwrCsFilePath, tsleep, maxWaitTime, pwrTimeOut, maxAttempts, reportDir, inpTimeout, enStdCmds, enPwrCmds, enInpCmds
    uutFilePath = rCol[0]
    csFilePath =  rCol[1]
    pwrCsFilePath =  rCol[2]
    tsleep = float(rCol[3])
    maxWaitTime = float(rCol[4])
    pwrTimeOut = float(rCol[5])
    maxAttempts = int(rCol[6])
    reportDir = rCol[7]
    inpTimeout = float(rCol[8])
    enStdCmds = int(rCol[9])
    enPwrCmds = int(rCol[10])
    enInpCmds = int(rCol[11])
    return

#ReadIn Config File
setConfigSettings()

testReport[0] = input('Enter UUT Part #: ')
fname = uutFilePath + testReport[0] + '.txt'
if not path.exists(fname):
    input('Error: Test Script was entered incorrectly or does not exist. Consault Engineering if issue persists.')
    sys.exit()
serialNumber = input('Enter UUT Serial #: ')
testReport[1] = 'Serial Number: ' + serialNumber
comPort = input('Enter ComPort (e.g. com7): ')

#Read in UUT Baud Rate, command file, & send/reply input change
try:
    inpSendList, inpReceiveList = parse_file(fname, '~')
    cname = csFilePath + inpReceiveList[0]
except:
    input('Error: Could not locate ' + testReport[0] + '.txt')
    sys.exit()

#Read in UUT RS232 commands
try:
    cmdSendList, cmdReceiveList = parse_file(cname, '~')
    pname = pwrCsFilePath + cmdReceiveList[0]
except:
    input('Error: Could not locate ' + inpReceiveList[0])
    sys.exit()

#Read in UUT Pwr RS232 Commands
try:
    pwrSendList, pwrReceiveList = parse_file(pname, '~')
except:
    input('Error: Could not locate ' + cmdReceiveList[0])
    sys.exit()

while allRatesMarker < 3:

        if inpSendList[0] == 'ALL':
                setBaudRate(comPort, allRates[allRatesMarker])
                testReport.append('Baudrate: ' + str(allRates[allRatesMarker]) + '\n')
                allRatesMarker = allRatesMarker + 1
        else:
                allRatesMarker = 3
                testReport.append('Baudrate: ' + inpSendList[0] + '\n')
                setBaudRate(comPort, int(inpSendList[0]))

        ser.isOpen()
        ser.flushOutput()

        if enStdCmds == 1:
                for i in range(len(cmdSendList))[1:]:
                        if cmdSendList[0] == stdSetType: sendCommand(cmdSendList[i], cmdReceiveList[i])
                        elif cmdSendList[0] ==  hexSetType:  sendHexCommand(cmdSendList[i], cmdReceiveList[i])
                        else: print('Error 0001')
        else: 
                print('Standard Commands are disabled.')
                testReport.append('Standard Commands are disabled.')


        if enPwrCmds == 1:
                time.sleep(pwrTimeOut)
                for i in range(len(pwrSendList)):
                        if cmdSendList[0] == stdSetType: sendCommand(pwrSendList[i], pwrReceiveList[i])
                        elif cmdSendList[0] ==  hexSetType: sendHexCommand(pwrSendList[i], pwrReceiveList[i])
                        else: print('Error 0002')
                        time.sleep(pwrTimeOut)
        else: 
                print('Power Commands are disabled.')
                testReport.append('Power Commands are disabled.')

        if enInpCmds == 1:
                for i in range (len(inpSendList))[1:]:
                        if cmdSendList[0] == stdSetType: sendCommand(inpSendList[i], inpReceiveList[i])
                        elif cmdSendList[0] ==  hexSetType: sendHexCommand(inpSendList[i], inpReceiveList[i])
                        else: print('Error 0003')
                        time.sleep(inpTimeout)
        else: 
                print('Input Commands are disabled.')
                testReport.append('Input Commands are disabled.')

        testEndTime = datetime.now()
        testReport.append('Test Complete: ' + testEndTime.strftime("%m-%d-%Y %H.%M.%S"))
        if inpSendList[0] == 'ALL' and allRatesMarker <= 3:
                if (allRatesMarker-1) == 0: sendBrCommand(':acs0sbmd')
                elif (allRatesMarker-1) == 1: sendBrCommand(':acs0sblo')
                elif (allRatesMarker-1) == 2: sendBrCommand(':acs0sbhi')
        ser.close()
        
#Write test report
trName = reportDir + testReport[0] + '_' + serialNumber + '_' + testStartTime.strftime("%m-%d-%Y_%H.%M.%S") + '.txt'
report = open(trName,'w')

for i in range(len(testReport)):
        report.write(testReport[i] + '\n')
report.close()

        

input('Test Complete\n')
sys.exit()