
import json
import lab3urlandjson
import urllib



class STEPS:
    def __init__(self, json):
        self.json = json

    def output(self):
        ''' accesses the JavaScript object and prints out the narratives which are the directions'''
        print('DIRECTIONS')
        legs = self.json['route']['legs']
        for x in legs:
            maneuvers = x['maneuvers']
            for steps in maneuvers:
                print(steps['narrative'])

              

class TOTALTIME:
    def __init__(self, json):
        self.json = json

    def output(self):
        ''' accesses the JavaScript Object and returns the time rounded to the nearest minute'''
        x = self.json['route']['time']
        x = round(x/60)
        print('TOTAL TIME: {} minutes'.format(x))
        print('')




class LATLONG:
    def __init__(self, json):
        self.json = json

    def output(self):
        ''' accesses the JavaScript Object and returns the latitudes and longitudes formatted into
    the correct NSEW orientation'''
        locations = self.json["route"]["locations"]

        for x in locations:
            latlong = x["latLng"]
            

            if latlong['lat'] < 0:
                lat = round(latlong['lat'], 2) * -1
                latitude = str(lat) + 'S'
            elif latlong['lat'] > 0:
                lat= round(latlong['lat'], 2)
                latitude = str(lat) + 'N'

            if latlong['lng'] < 0:
                long = round(latlong['lng'], 2) * -1
                longitude = str(long) + 'W'
            elif latlong['lng'] > 0:
                long = round(latlong['lng'], 2)
                longitude = str(long) + 'E'

            print(latitude, longitude)
        print('')




class TOTALDISTANCE:
    ''' accesses the JavaScript Object and returns the distance rounded to the nearest mile'''
    def __init__(self, json):
        self.json = json

    def output(self):
        x = self.json['route']['distance']

        print('TOTAL DISTANCE: {} miles'.format(round(x)))
        print('')


class ELEVATION:
    ''' accesses the JavaScript Object and the height of elevation rounded to the nearest foot'''
    def __init__(self, json):
        self.json = json
    def output(self):
        elevation = self.json['elevationProfile']
        for x in elevation:
            print(round(x['height']))
       


        
