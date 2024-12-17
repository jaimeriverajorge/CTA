# CTA
Building with the CTA's Train Tracker API

get_arrivals.py :
uses the python requests package and the CTA train tracker API to send a request a sample request taken from the train tracker API docs:
https://www.transitchicago.com/developers/ttdocs/#_Toc296199906
The request gets a maximum of one arrival prediction result from the station with the ID #40360 - Southport. 
It also passes the API key for authorization (required).
request:
http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=""&max=1& mapid=40360&outputType=JSON
