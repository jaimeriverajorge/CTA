import requests
from datetime import datetime

# this script uses the python requests package and the CTA train tracker API
# to send a request a sample request taken from the train tracker API docs:
# https://www.transitchicago.com/developers/ttdocs/#_Toc296199906
# The request gets a maximum of one arrival prediction result from the station with the ID #40360. 
# It also passes the API key for authorization (required).
# request:
# http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=&max=1& mapid=40360&outputType=JSON


#pass in json parsed response
def format(data, north, south):
    trains_n = [] #will contain trains going north
    trains_s = [] #will contain trains going south
    
    #from the returned data, grab the main ETA array:
    eta = data['ctatt']['eta']

    for train in eta:
    
        #get the destination
        dest = train['stpDe']

        # add loop bound trains to trains_s 
        if north in dest:
            trains_n.append(train)
        elif south in dest:
            trains_s.append(train)
    return trains_n, trains_s

def printTrains(trains):
    
    route = trains[0]['stpDe']
    stop = trains[0]['staNm']
    print('\nRoute:', stop, "-", route)
    i = 1
    for train in trains:
        arrivalTime = train['arrT']
        time_obj = datetime.strptime(arrivalTime, "%Y-%m-%dT%H:%M:%S")
        #day = time_obj.strftime("%B %d, %Y")
        time = time_obj.strftime("%I:%M:%S %p")
        #split by date and time
        print("\nArrival", i)
        print(time)
        i+=1


def main(): 
    #CTA API Key
    key = ''
    #station ID - in the original example Southport
    map_id = '40360'
    #amount of trains returned in response
    max_trains = '6'

    # Define the URL with query parameters
    url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    params = {
        'key' : key,
        'mapid': map_id,
        'max': max_trains,
        'outputType': 'JSON'
        
    }

    # Send a GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

    else:
        print(f"Error: {response.status_code}")

    #define north and south variables 
    # in the example we are looking at the Brown line
    # north will be Kimball, south will be the Loop
    north = 'Kimball'
    south = 'Loop'

    #format the response into 2 separate arrays for north and south trains
    trains_north, trains_south = format(data, north, south)

    #get the date just once to print out at the top:
    print("\nToday's date:")
    arrivalTime = trains_north[0]['arrT']
    date = datetime.strptime(arrivalTime, "%Y-%m-%dT%H:%M:%S")
    day = date.strftime("%B %d, %Y")
    print(day)

    printTrains(trains_north)
    printTrains(trains_south)


if __name__ == "__main__":
    main()