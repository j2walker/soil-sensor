import matplotlib.pyplot as plt
from datetime import date
import datetime
from PIL import Image
import os

#export data to local sensorData file
def exportData(reading):
    data = open('/home/pi/Personal_Projects/soilMoisture/sensorData.txt', 'a')
    data.write(str(reading) + " " + str(datetime.datetime.now().strftime('%a')) + '.\n')
    data.close()
    
#creates and saves graph from data of past week
def makeGraph():
    dateRange = []
    today = date.today()
    
    endOfWeek = datetime.timedelta(days = 1)
    begOfWeek = datetime.timedelta(days = 8)
    
    a = today - endOfWeek
    b = today - begOfWeek

    dateRange.append(b.strftime('%m/%d/%Y'))
    dateRange.append(a.strftime('%m/%d/%Y'))
    
    x = []
    y = []
    f = open('/home/pi/Personal_Projects/soilMoisture/sensorData.txt', 'r')
    for line in f:
        x.append(line.split()[1])
        y.append(float(line.split()[0]))

    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax1.set_title("%s - %s" % (dateRange[0], dateRange[1]))
    ax1.plot(x,y, c="b", linestyle = (0, (3, 1, 1, 1)))

    ymin, ymax = min(y), max(y)
    plt.ylim(ymin-10, ymax+10)
    plt.ylabel('Soil Moisture (%)')
    plt.xlabel('Day of the Week')
    plt.tight_layout()
    
    #photo handling
    plt.savefig('/home/pi/Personal_Projects/soilMoisture/graphedData.png')
    im = Image.open('/home/pi/Personal_Projects/soilMoisture/graphedData.png')
    rgb_im = im.convert('RGB')
    rgb_im.save('/home/pi/Personal_Projects/soilMoisture/graphedData.jpg')
    os.remove('/home/pi/Personal_Projects/soilMoisture/graphedData.png')