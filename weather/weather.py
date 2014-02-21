import json
import urllib.request
import datetime
import subprocess

LOCATION="kollam"
URL="http://api.openweathermap.org/data/2.5/weather?q="+LOCATION+"&units=metric"

def getWeatherDetails():
	weatherDetails = []; 

	response=urllib.request.urlopen(URL).read().decode('utf-8')
	jsonObj = json.loads(response)
	#coordinates
	coord = jsonObj['coord']
	lon = coord['lon']
	lat = coord['lat']
	weatherDetails.append("Coordinates: "+ str(lon) + " : "+str(lat)+". ");

	#sys details
	sysDetails = jsonObj['sys']
	sunrise=sysDetails['sunrise']
	sunset=sysDetails['sunset']

	weatherDetails.append("Sunrise is at " + datetime.datetime.fromtimestamp(int(sunrise)).strftime('%H:%M:%S') + ".");
	weatherDetails.append("Sunset is at " + datetime.datetime.fromtimestamp(int(sunset)).strftime('%H:%M:%S') + ".");

	#weather
	weatherStr=jsonObj['weather'][0]
	weatherDetails.append("We have "+ weatherStr['description'] + " today");
	# other details
	mainStr=jsonObj['main']

	weatherDetails.append("Temperature is " + str(mainStr['temp']) + " degree Celcius");

	weatherDetails.append("Pressure is " + str(mainStr['pressure']) + " hPa");

	weatherDetails.append("Humidity is " + str(mainStr['humidity']) + " %)")

	weatherDetails.append("Wind Speed is " + str(jsonObj['wind']['speed']))

	return weatherDetails

weatherDetails = getWeatherDetails()
for strVal in weatherDetails:
	#subprocess.call(["speak",strVal])
	print(strVal)