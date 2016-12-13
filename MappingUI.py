
import lab3input
import lab3urlandjson
import lab3class

def main():

    while True:
            list_of_address = lab3input.get_address()
            list_of_outputs = lab3input.output_spec()

            start_location = list_of_address[0]

            end_location = []
            end_location.extend(list_of_address[1:])
            
            try:
                url = lab3urlandjson.build_route_url(start_location, end_location)
            except:
                print('')
                print('MAPQUEST ERROR')
            try:
                jason = lab3urlandjson.get_json_result(url)
                output_to_class(list_of_outputs, jason)
            except:
                print('NO ROUTE FOUND')
    

def output_to_class(outputs: list, json):
    ''' Takes in the specified output and the JavaScript Object and prints out
    data stored inside the JavaScript Object'''
    print('')
    for output in outputs:
        if output == 'STEPS':
            
            directions = lab3class.STEPS(json)
            directions.output()
            print('\n')

        if output == 'LATLONG':

            latlng = lab3class.LATLONG(json)
            latlng.output()

        if output == 'TOTALDISTANCE':
            distance = lab3class.TOTALDISTANCE(json)
            distance.output()

        if output == 'TOTALTIME':
            time = lab3class.TOTALTIME(json)
            time.output()
            
        if output == 'ELEVATION':
            print('ELEVATIONS')
            list_url = lab3urlandjson.build_elev_url(json)
            for url in list_url:
               elev_json = lab3urlandjson.get_json_result(url)
               elevation = lab3class.ELEVATION(elev_json)
               elevation.output()
            print('')
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')                       
            
if __name__ == '__main__':
    main()

    


    
        
