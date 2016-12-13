
import urllib.parse
import urllib.request
import json



def build_route_url(start_location: str, end_location: list) -> str:
    ''' Takes the input locations and returns the corresponding url'''
    
    base_url = 'http://open.mapquestapi.com/directions/v2/route?'
    API_key = 'Eok7X9zxa7FHGBHmq3HeTBq3IC8qHCkJ'


    parameters = [
        ('key', API_key),
        ('from', start_location)]
       

    for location in end_location:
        parameters.append(('to', location))

    encoded_parameters = urllib.parse.urlencode(parameters)
    return base_url + encoded_parameters
    

def get_json_result(url: str) -> dict:
    ''' Takes in a given url and returns the JavaScript Object as
a dictionary'''

    response = None
    try: 
        routing_response= urllib.request.urlopen(url)
        json_text = routing_response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if routing_response != None:
            routing_response.close()

def build_elev_url(json) -> list:
    ''' Takes in the route JavaScript Object and returns a list of urls corresponding
 to the JavaScript object for elevations'''

    locations = json["route"]["locations"]


    base_url = 'http://open.mapquestapi.com/elevation/v1/profile?'
    API_key = 'Eok7X9zxa7FHGBHmq3HeTBq3IC8qHCkJ'

   
    url_elev_list = []
    for x in locations:
        latlongs = x["latLng"]
        LatLongCollec = str(latlongs['lat']) + ',' + str(latlongs['lng'])
                                           
        built_url = base_url + 'key=' + API_key + '&shapeFormat=raw&unit=f&latLngCollection=' +  LatLongCollec

        url_elev_list.append(built_url)
    return (url_elev_list)
