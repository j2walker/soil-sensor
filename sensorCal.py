import sys
import time
import json
try:
	from gpiozero import MCP3008
except ImportError:
	print("[ERR] Error with imported libraries. \
	Check that gpiozero is installed.")

#confirm desire to calibrate before starting
def confirmation():

	while True:
		confirmation = raw_input("Begin calibration? (y/n): ")
		if confirmation == "n":
			sys.exit()
		elif  confirmation == "y":

			print("[INFO] Beginning calibration...")
			time.sleep(1.2)
			break
		elif confirmation != "y" or "n":
			print("\nPlease answer with (y/n): \n")
	

#calibration method for soil sensor
def calibrate():
	#channel from MCP chip, device from which SPI CE you're using (0 or 1)
	adc = MCP3008(channel = 4, device = 0)
	
	avgMax = dryCalibration(adc)
	time.sleep(1.3)
	avgMin = wetCalibration(adc)
	
	return avgMax, avgMin
	
#calibration to get minimum dry value	
def dryCalibration(adc):
	avgmax = 0
	breaker = 0
		
	print("\n[INFO] DRY calibration...")
	time.sleep(1.2)
	print("\nMake sure sensor is COMPLETELY dry\n")
	time.sleep(1.8)
	while breaker == 0:
		calConf = raw_input("Ready to calibrate DRY? (y/n) ")
		if calConf == "y":
			breaker = 1
		elif calConf == "n":
			print("\nPlease try again later")
			sys.exit()
		elif calConf != "n" or "y":
			print("\nPlease answer with (y/n): \n")
			
	print("\nCalibrating in...")
	for x in range(5,0,-1):
		print(x)
		time.sleep(1)
		
	for x in range(0,10):
		avgmax += adc.value
	avgmax = float(avgmax/10)
	
	print("\n[INFO] DRY calibration complete...\n")
	return avgmax

# calibration to get max wet value
def wetCalibration(adc):
	avgmin = 0
	print("\n[INFO] WET calibration...")
	time.sleep(1.2)
	print("\nMake sure sensor is COMPLETELY submerged in water to white line \n")
	while True:
		calConf = raw_input("Ready to calibrate WET? (y/n) ")
		if calConf == "y":
			break
		elif calConf == "n":
			print("\nPlease try again later")
			sys.exit()
		elif calConf != "n" or "y":
			print("\nPlease answer with (y/n): \n")
	print("Calibrating in...")
	for x in range(5,0,-1):
		print(x)
		time.sleep(1)
		
	for x in range(0,10):
		avgmin += adc.value
	avgmin = float(avgmin/10)
	
	print("\n[INFO] DRY calibration complete...\n")
	return avgmin

def main():
	confirmation()
	maxValue, minValue = calibrate()
	print("[INFO] Calibration complete")
	values = {'maximum' : maxValue, 'minimum' : minValue}
	

	newCalFile = open('calibrationValues.json', 'w')
	json.dump(values, newCalFile)

if __name__ == '__main__':
	main()
	
