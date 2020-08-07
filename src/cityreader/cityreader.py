import csv
"""
Create a class to hold a city location. Call the class "City". It should have
fields for name, lat and lon (representing latitude and longitude).
"""

class City:
	def __init__(self, name, lat, lon):
		self.name = name
		self.lat = lat
		self.lon = lon
	
	def __repr__(self):
    
    """
    Class city returns city information in specific formatting, for 
    easy to read and understand for anybody reading data.

    Example:
    City: Los Angeles, Latitude: 34.114, Longitude: -118.4068
    """

		return f"<City: {self.name}, Latitude: {self.lat}, Longitude: {self.lon}>"

"""
We have a collection of US cities with population over 750,000 stored in the
file "cities.csv". (CSV stands for "comma-separated values".)

In the body of the `cityreader` function, use Python's built-in "csv" module 
to read this file so that each record is imported into a City instance. Then
return the list with all the City instances from the function.
Google "python 3 csv" for references and use your Google-fu for other examples.

Store the instances in the "cities" list, below.

Note that the first line of the CSV is header that describes the fields--this
should not be loaded into a City object.
"""

cities = []

def cityreader(cities=[]):
  
  """
  Reads in a csv and returns a list cities using the City 
  Class and formating. Returns City as a string, and the Latitude
  and Longitude as Floats.
  """

  with open('cities.csv', newline='') as csvcities:
        read_cities = csv.DictReader(csvcities)
        cities.extend([City(cities['city'], float(cities['lat']), float(cities['lng']))
                       for cities in read_cities])
    
  return cities

cityreader(cities)

"""
Print the list of cities (name, lat, lon), 1 record per line.
"""

for c in cities:
    print(c)

"""
STRETCH GOAL!

Allow the user to input two points, each specified by latitude and longitude.
These points form the corners of a lat/lon square. Pass these latitude and 
longitude values as parameters to the `cityreader_stretch` function, along
with the `cities` list that holds all the City instances from the `cityreader`
function. This function should output all the cities that fall within the 
coordinate square.

Be aware that the user could specify either a lower-left/upper-right pair of
coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
the input data so that it's always one or the other, then search for cities.
In the example below, inputting 32, -120 first and then 45, -100 should not
change the results of what the `cityreader_stretch` function returns.

Example I/O:

Enter lat1,lon1: 45,-100
Enter lat2,lon2: 32,-120
Albuquerque: (35.1055,-106.6476)
Riverside: (33.9382,-117.3949)
San Diego: (32.8312,-117.1225)
Los Angeles: (34.114,-118.4068)
Las Vegas: (36.2288,-115.2603)
Denver: (39.7621,-104.8759)
Phoenix: (33.5722,-112.0891)
Tucson: (32.1558,-110.8777)
Salt Lake City: (40.7774,-111.9301)
"""

"""
WORK NOTES:
Creating Inputs and splitting inputs into seperate lists
to use in cityreader_stretch function
"""
input_one = input('Enter lat1, lon1:')
input_two = input('Enter lat2, long2:')
lat1 = input_one.split(',')[0]
lon1 = input_one.split(',')[1]
lat2 = input_two.split(',')[0]
lon2 = input_two.split(',')[1]

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  
  """
  Function takes in two sets of cordinates and returns a list
  of cities within those cordinates. 

  input_one = first set of cordiates
  input_two = second set of cordinates

  Example:
  'Enter lat1, lon1:' 45, -100
  'Enter lat2, lon2:' 32, -120

  Returns: 
  List of cities within given cordinates.

  Function:
  Converts each input into a float, then compares
  each cordinate to decide which cordinate is higher
  or lower. Once that is decided, using another comparison,
  chooses cities that fall within those parameters. 

  Printing:
  To print list, set a variable to the funcitn, 
  then use a for loop to print each city in list. 
  Will print in formating used in City class. 

  Example:
  test_answers = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
  for i in test_answers:
    print(i)

  """
  
  lat1 = float(lat1)
  lat2 = float(lat2)
  lon1 = float(lon1)
  lon2 = float(lon2)

  if lat1 < lat2:
    lower = float(lat1)
    higher = float(lat2)
  else:
    lower = float(lat2)
    higher = float(lat1)

  if lon1 < lon2:
    low = float(lon1)
    high = float(lon2)
  else:
    low = float(lon2)
    high = float(lon1)

  within = []

  for city in cities:
    if (city.lat > lower and city.lat < higher) and (city.lon > low  and city.lon < high):
      within.append(city)

  return within

test_answers = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
for i in test_answers:
    print(i)
