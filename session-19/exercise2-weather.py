# Example of getting information about the weather of
# a location

import http.client
import json


def connect(method, endpoints, headers):
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(method, endpoints, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    if not r1.status == 200:
        return

    text_json = r1.read().decode("utf-8")
    conn.close()

    try:
        city_data = json.loads(text_json)
        city_woeid = city_data[0]['woeid']
        return city_woeid

    except IndexError:
        return "Please choose another city or watch the spell"


# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"
headers = {'User-Agent': 'http-client'}
METHOD = "GET"
activity = True


while activity:
    ARGUMENT = "search/?query="+input("Please enter the name of a capital to get the weather info: ")
    COMPLETE_ENDPOINT = ENDPOINT + ARGUMENT

    city_woeid = connect(METHOD, COMPLETE_ENDPOINT, headers)
    if type(city_woeid) is int:
        activity = False
    else:
        print(city_woeid)

# -- Get the data

if city_woeid:
    LOCATION_WOEID = str(city_woeid)

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
