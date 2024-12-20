import requests
import json 

# this script uses the python requests package and the CTA train tracker API
# to send a request a sample request taken from the train tracker API docs:
# https://www.transitchicago.com/developers/ttdocs/#_Toc296199906
# The request gets a maximum of one arrival prediction result from the station with the ID #40360. 
# It also passes the API key for authorization (required).
# request:
# http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=&max=1& mapid=40360&outputType=JSON

key = ""

# Define the URL with query parameters
url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
params = {
    'key' : key,
    'mapid': '40360',
    'max': '5',
    'outputType': 'JSON'
    
}

# Send a GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the JSON data
    #print("This is the parsed response from requests package")
   # print(data)

else:
    print(f"Error: {response.status_code}")

#pass in json parsed response
def format(data):

    #from the returned data, grab the main ETA dictionary:
    eta = data['ctatt']['eta']

    #grab first train
    train1 = eta[0]

    #print the key value pairs with a new line in between
    #for key in train1:
     #   print(key, (train1[key]))

    for train in eta:

    
        #get stop name
        stop = train['staNm']

        #get the destination
        direction = train['stpDe']
        
        #get the arrival time of the next train
        arrivalTime = train['arrT']

        #split by date and time
        date, time = arrivalTime.split('T')

        print("Station:")
        print(stop)
        print(direction)

        print("Arrival:")
        print("Date:", date)
        
        print("Time:", time)

format(data)

#  return {
#        'statusCode': 200,
#        'body':'Hello from Lambda!'
#    }