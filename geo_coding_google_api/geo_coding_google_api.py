# This program asks the user for searching a location and then, after using
# the Google API, returns some information about the searched location. However, 
# if you don't have the Google API, you will be directed to use the directory
# provided by Dr. Chuck.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here and un-comment the line:
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignoring the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter the locations please:\n")
    if len(address) < 1: break
    
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # Here, we encode the searched location and add it to the service url.
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving ", url, "\n")

    # Through openning the url, Google API generates the json code including
    # the information. The json is received as unicode.
    uh = urllib.request.urlopen(url, context=ctx)
    #The unicode jason is decoded as json.
    data = uh.read().decode()
    print(data)
    try:
        js = json.loads(data)
        print(js, '\n')
    except:
        js = None
        print("except activated\n")

    if js is None or "status" not in js or js['status'] != "OK":
        print("Failure")
        continue
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('lat: ', lat, ' and lng: ', lng, '\n')

    location = js['results'][0]['formatted_address']
    print('location: ', location)

print('\nThanks for reviewing')

# Thanks for reviewing
