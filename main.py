
#Check the MetEireann API for weather forecast info
import requests

import pandas as pd
#Co-ordinates for Dublin City Centre taken from Google Maps
response = requests.get("http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=53.348366;long=-6.254815")
print(response.status_code)
print(response.text)

#Check GitHub

#Testing ability to read in CSV file to a Panda dataframe.
#Dublin Bikes API is not open so I am downloading CSV files
# directly from https://data.gov.ie/dataset/dublinbikes-api
df = pd.read_csv("dublinbikes_20190101_20190401.csv")
print(df.head())


