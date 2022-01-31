
#Check the MetEireann API for weather forecast info
import requests
#Co-ordinates for Dublin City Centre taken from Google Maps
response = requests.get("http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=53.348366;long=-6.254815")
print(response.status_code)
print(response.text)

