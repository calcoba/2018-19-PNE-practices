# Example of getting information about the weather of
# a location

import http.client
import json
import sys

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"
ARGUMENT = "search/?query="+input("Please enter the name of a capital to get the weather info: ")

# -- For the location we have to use the
# -- Were on earth identifier
# -- London woeid = 44418
# -- Madrid woeid = 766273
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + ARGUMENT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

if not r1.status == 200:
    sys.exit()


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
city_woeid = json.loads(text_json)

# -- Get the data

if city_woeid:
    LOCATION_WOEID = str(city_woeid[0]['woeid'])

    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request(METHOD, ENDPOINT + LOCATION_WOEID + "/", None, headers)

    r2 = conn.getresponse()

    print()
    print("Response received: ", end='')
    print(r2.status, r2.reason)

    text_json = r2.read().decode("utf-8")
    conn.close()

    weather = json.loads(text_json)

    time = weather['time']
    temp0 = weather['consolidated_weather'][0]
    description = temp0['weather_state_name']
    temp = temp0['the_temp']
    place = weather['title']

    print()
    print("Place: {}".format(place))
    print("Time: {}".format(time))
    print("Weather description: {}".format(description))
    print("Current temp: {} degrees".format(temp))

else:
    print("The city you have choose is not available, please try again")

