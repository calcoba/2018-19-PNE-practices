# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Please enter the name of an user: ")
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
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get some data
login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']
repos_url = "/repos"

print()
print("Name: {}".format(name))
conn.request(METHOD, ENDPOINT + GITHUB_ID + repos_url, None, headers)

r2 = conn.getresponse()

print()
print("Response received: ", end='')
print(r2.status, r2.reason)

text_json = r2.read().decode("utf-8")
conn.close()

repos = json.loads(text_json)
repos_name = []
for i in range(len(repos)):
    repos_name.append(repos[i]['name'])

print("Name of user repos: {}".format(", ".join(repos_name)))

if "2018-19-PNE-repo" in repos_name:
    print("OK")

