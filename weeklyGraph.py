import handleData as hd
import soilMoisture as sm
import os

def weeklyGraph():
   
    hd.makeGraph()
    sm.sendGraphNotification()
    
    #file hanlding for week
    file = open('/home/pi/Personal_Projects/soilMoisture/sensorData.txt', 'w')
    file.close()
    
    os.remove('/home/pi/Personal_Projects/soilMoisture/graphedData.jpg')

def main():
    weeklyGraph()

if __name__ == '__main__':
    main()