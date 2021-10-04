import soilMoisture as sm
import handleData as hd
import water

def dailyRun():
    reading = sm.takeReading()

    hd.exportData(reading)
    
    if reading < 30:
        sm.sendWaterNotif(reading)
        water.water()

def main():
    dailyRun()

if __name__ == '__main__':
    main()