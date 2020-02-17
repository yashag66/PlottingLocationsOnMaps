# List of icons
# http://kml4earth.appspot.com/icons.html

import pygmaps


# lat_long_list = [(30.3358376, 77.8701919), (30.307977, 78.048457), (30.3216419, 78.0413095), (30.3427904, 77.886958), (30.378598, 77.825396), (30.3548185, 77.8460573), (30.3345816, 78.0537813), (30.387299, 78.090614), (30.3272198, 78.0355272), (30.3840597, 77.9311923), (30.4158, 77.9663), (30.340426, 77.952092), (30.3984348, 78.0747887), (30.3431313, 77.9555512), (30.273471, 77.9997158)]

lat_long_dict = {(30.3358376, 77.8701919): 1, (30.307977, 78.048457): 2, (30.3216419, 78.0413095): 1, (30.3427904, 77.886958): 2, (30.378598, 77.825396): 1, (30.3548185, 77.8460573): 2, (30.3345816, 78.0537813): 1, (30.387299, 78.090614): 2, (30.3272198, 78.0355272): 1, (30.3840597, 77.9311923): 2, (30.4158, 77.9663): 1, (30.340426, 77.952092): 2, (30.3984348, 78.0747887): 1, (30.3431313, 77.9555512): 2, (30.273471, 77.9997158): 1}
icon_dict = {1:'http://maps.google.com/mapfiles/kml/pal2/icon40.png', 2:'http://maps.google.com/mapfiles/kml/pal3/icon33.png'}

mymap3 = pygmaps.pygmaps(30.3164945, 78.03219179999999, 15)
# ls = []
count = 0
for key, value in lat_long_dict.items():

    # add a point into a map
    # 1st argument is latitude
    # 2nd argument is longitude
    # 3rd argument is icon to be used
    # 4th argument is colour of the point showed in thed map
    # using HTML colour code e.g.
    # red "# FF0000", Blue "# 0000FF", Green "# 00FF00"
    print(icon_dict[value])
    mymap3.addpoint(key[0], key[1], icon_dict[value], "#FF0000")

mymap3.draw('pygmap3.html')

