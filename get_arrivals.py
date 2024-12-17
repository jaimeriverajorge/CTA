import requests
# this script uses the python requests package and the CTA train tracker API
# to send a request a sample request taken from the train tracker API docs:
# https://www.transitchicago.com/developers/ttdocs/#_Toc296199906
# The request gets a maximum of one arrival prediction result from the station with the ID #40360. 
# It also passes the API key for authorization (required).
# request:
# http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=&max=1& mapid=40360&outputType=JSON

key = "971b7cc22ddf4804902cc49d2c8b6063"

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
    # Print or process the JSON data
    print(data)
else:
    print(f"Error: {response.status_code}")
