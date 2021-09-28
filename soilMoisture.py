import time
import sys
import json
import urllib, httplib

#try importing gpiozero
try:
    from gpiozero import MCP3008
except ImportError:
    print("[ERR] Error with imported libraries. Check that gpiozero is installed.")
    sys.exit()

#try opening calibration json file from local directory
try:
    calJson = open('calibrationValues.json', 'r')
    valDict = json.loads(calJson.readline())
    adc = MCP3008(channel = 4, device = 0)
except:
    print("[ERR] Error opening calibration file. Did you calibrate first?")
    sys.exit()

#converts input from sensor to percentage, if reading is above or below
#minimum or maximum, converts to above or below 100%
def convertToPercentage(reading):
    minimum = valDict['minimum']
    maximum = valDict['maximum']
    
    inverted=(reading-valDict['minimum'])/(valDict['maximum'] - \
        valDict['minimum'])*100
    
    if reading >= minimum and reading <= maximum:
        return(round(abs(inverted-100), 2))
    
    elif reading < minimum:
        return(round(100-abs(inverted-100), 2))
    elif reading > maximum:
        return(round(100+abs(inverted-100), 2))

#takes 10 readings from sensor and returns average as reading
def takeReading():
    avg = 0
    for x in range(0,10):
		avg += adc.value
        
    return float(avg/10)

def sendNotif():
    connection = httplib.HTTPSConnection('api.pushover.net')
    connection.request('POST', '/1/messages.json',
        urllib.urlencode({
            'token' : 'arsrrs2cxmsf6zpnoxf7hffr5zzqb7',
            'user' : 'u69yssmo99dz46cmg6x4de7oqv2uic',
            'message' : 'Soil is dry. Time to water!',
            'device' : 'Jack_iPhone',
            'title' : 'Fern Sensor',
        }), { 'Content-type' : 'application/x-www-form-urlencoded' })
    connection.getresponse()
    

def main():
    newReading = takeReading()
    if newReading < 60:
        sendNotif()
    print(convertToPercentage(newReading))

if __name__ == '__main__':
    main()

