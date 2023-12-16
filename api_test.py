import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Connects to the open-notify API and prints the response
try:
    #Gets the names of the people currently on the ISS
    response = requests.get("http://api.open-notify.org/astros.json")
    print('====================')
    print("Response: ", response.status_code)
    
    print('====================')

    data = response.json()
    jprint(data)

    #Prints the number of people currently on the ISS, there names and the craft they are on
    print('====================')
    print('Currently on ISS: ', data['number'])

    print('Names of people on ISS: ')
    
    for person in data['people']:
        print(person['name'], 'is on the', person['craft'])

#If the connection fails, print the error
except Exception as e:
    print('====================')
    print("The server couldn't fulfill the request: ", e)
    
print('====================')

try:
    #Gets the current location of the ISS
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print('====================')
    print("Response: ", response.status_code)
    print('====================')

    data = response.json()
    jprint(data)

    #Prints the current location of the ISS
    print('====================')
    print('Current location of ISS: ')
    print('Latitude: ', data['iss_position']['latitude'])
    print('Longitude: ', data['iss_position']['longitude'])
    
#If the connection fails, print the error
except Exception as e:
    print('====================')
    print("The server couldn't fulfill the request: ", e)
