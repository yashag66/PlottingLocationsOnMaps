import googlemaps
import geopy.distance
import time
import os
import json

center_point_address = 'Friendship Hospital for Animals  4105 Brandywine St NW Washington, DC 20016'

# These Keywords need to be entered by the end user
keywords_list = ['veterinarian', 'veterinarian near me', 'animal hospital', 'veterinary', 'animal hospital near me',
                 'vet clinics near me', 'animal clinic', 'veterinary clinic', 'pet hospital', 'animal medical center',
                 'vet clinic', 'veterinary clinic near me', 'animal clinic near me', 'veterinary technician',
                 'veterinary hospital', 'pet hospital near me', 'veterinary hospital near me', 'pet doctor',
                 'animal doctor', 'emergency veterinarian', 'veterinary pet insurance', 'veterinary doctor',
                 'pet doctor near me', 'animal doctor near me', 'veterinary physician', 'veterinarian house calls',
                 '24 hour veterinary clinic near me', 'veterinary service', '24 hrs veterinary clinic',
                 'vet clinic services', 'animal clinic services']
keywords_list = ['veterinarian', 'animal hospital', 'veterinary', 'vet clinics', 'animal clinic', 'veterinary clinic', 'pet hospital', 'animal medical center',
                 'vet clinic', 'veterinary technician', 'veterinary hospital', 'pet hospital', 'veterinary hospital', 'pet doctor',
                 'animal doctor', 'emergency veterinarian', 'veterinary pet insurance', 'veterinary doctor',
                 'pet doctor', 'animal doctor', 'veterinary physician', 'veterinarian house calls',
                 '24 hour veterinary clinic', 'veterinary service', '24 hrs veterinary clinic',
                 'vet clinic services', 'animal clinic services','vets','hospital']
# keywords_list = ['mall']
km_range = 100  # Add the range within which results are to be expected

keywords = ','.join(keywords_list)

API_KEY = 'Enter Your API KEY here'   # 'AIkgjhzaSyCg4-RkdvfyoEbbw-GPWE_2ST898bQ--ZZZscGi0Q'

gmaps = googlemaps.Client(key=API_KEY)
loc_coord = {}
count = 0  # to restrict the overcalling of google api using the count flag
check_True = True
DIR = r'C:\Users\yagarwal\Desktop\bevarage_webscrapping\ProgrammingFoundationPython\Maps\files\files.txt'


def file_create(content, DIR=DIR):
    if content:
        with open(DIR, 'w') as f:
            f.write(content)


def get_cord_distance(origin_cord, dest_cord):
    return geopy.distance.distance((origin_cord['lat'], origin_cord['lng']), (dest_cord['lat'], dest_cord['lng'])).km


def get_loc_coords(address):
    global gmaps
    # Response received using the geocode API
    geocode_result = gmaps.geocode(address=address)
    try:
        loc_coord = geocode_result[0]['geometry']['location']
        return loc_coord
    except Exception:
        print("Geocode api returned the result which didnt had lat, long coords", geocode_result)
        exit()


def parse_places_nearby_data(resp_data):
    list_places_nearby = []
    # if len(resp_data['results'])> 1:
    for place_result in resp_data['results']:
        name = place_result['name']
        location = place_result['geometry']['location']
        dist_place = get_cord_distance(loc_coord, location)
        #  Adding only places within the required range to the list
        if dist_place < km_range:
            list_places_nearby.append([name, location, dist_place])
        else:
            print('*******************************')
            print(dist_place)
    return list_places_nearby


def get_nearby_places(loc_coord=loc_coord, keywords=keywords, page_token=None):
    if page_token:
        print('Using Page Token is', page_token)
        time.sleep(5)
        query_result = gmaps.places_nearby(page_token=page_token)
    else:
        # query_result = gmaps.places_nearby(location=(str(loc_coord['lat']), str(loc_coord['lng'])), keyword=keywords,
        #                                    rank_by='distance')
        query_result = gmaps.places_nearby(location=(str(loc_coord['lat']), str(loc_coord['lng'])), radius=50000,
                                           keyword=keywords)

    return query_result


def get_places(loc_coord=loc_coord, keywords=keywords, page_token=None):
    if page_token:
        print('Using Page Token is', page_token)
        time.sleep(5)
        query_result = gmaps.places(page_token=page_token, query=keywords)
    else:
        # query_result = gmaps.places_nearby(location=(str(loc_coord['lat']), str(loc_coord['lng'])), keyword=keywords,
        #                                    rank_by='distance')
        query_result = gmaps.places(location = {'lat':loc_coord['lat'], 'lng': loc_coord['lng']}, radius = 200000,
                                           query=keywords)

    return query_result

# loc_coord = get_loc_coords(center_point_address)
# Comment the below line once the above line is uncommented to get exact coordinates
loc_coord = {'lat': 38.9498552, 'lng': -77.0811148}
fields = 'formatted_address, name, permanently_closed, place_id, plus_code'
page_token = None
places_nearby = []

while check_True:
    query_result = get_places(loc_coord=loc_coord, keywords=keywords, page_token=page_token)
    places_nearby.extend(parse_places_nearby_data(query_result))
    if 'next_page_token' in query_result:
        page_token = query_result['next_page_token']
        print(places_nearby)
        print(page_token)
        print(query_result)
        check_True = True
    else:
        check_True = False
        print("Ending the loop")
        print(query_result)
        file_create(str(places_nearby))

