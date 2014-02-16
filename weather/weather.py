import json
import urllib.request
import datetime

LOCATION="kollam"
URL="http://api.openweathermap.org/data/2.5/weather?q="+LOCATION+"&units=metric"

weatherDetails = ["Weather for Kollam."]; 

#print("Staring weather application")
response=urllib.request.urlopen(URL).read().decode('utf-8')
jsonObj = json.loads(response)
#coordinates
coord = jsonObj['coord']
lon = coord['lon']
lat = coord['lat']
#print("Coordinates: "+ str(lon) + " : "+str(lat))
weatherDetails.append("Coordinates: "+ str(lon) + " : "+str(lat)+". ");

#sys details
sysDetails = jsonObj['sys']
sunrise=sysDetails['sunrise']
sunset=sysDetails['sunset']
#print("Sunrise : " + datetime.datetime.fromtimestamp(int(sunrise)).strftime('%H:%M:%S'))
weatherDetails.append("Sunrise is at " + datetime.datetime.fromtimestamp(int(sunrise)).strftime('%H:%M:%S') + ".");
#print("Sunset : " + datetime.datetime.fromtimestamp(int(sunset)).strftime('%H:%M:%S'))
weatherDetails.append("Sunset is at " + datetime.datetime.fromtimestamp(int(sunset)).strftime('%H:%M:%S') + ".");

#weather
weatherStr=jsonObj['weather'][0]
#print(weatherStr['main'] + " : " + weatherStr['description'])
weatherDetails.append("We have "+ weatherStr['description'] + " today");
# other details
mainStr=jsonObj['main']
#print("Temperature : " + str(mainStr['temp']) + " degree Celcius")
weatherDetails.append("Temperature is " + str(mainStr['temp']) + " degree Celcius");
#print("Pressure : " + str(mainStr['pressure']) + " hPa")
weatherDetails.append("Pressure is " + str(mainStr['pressure']) + " hPa");
#print("Humidity : " + str(mainStr['humidity']) + " %")
weatherDetails.append("Humidity is " + str(mainStr['humidity']) + " %)")
#print("Wind Speed : " + str(jsonObj['wind']['speed']))
weatherDetails.append("Wind Speed is " + str(jsonObj['wind']['speed']))

for strVal in weatherDetails:
	subprocess.call("speak",strVal)