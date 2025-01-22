# Create a list of 10 countries with earthquakes in the last 24 hours from the following website 
# https://www.volcanodiscovery.com/earthquakes/today.html
earthquakes = ['Indonesia', 'Japan', 'Philippines', 'Chile', 'Alaska', 'Papua New Guinea', 'Mexico', 'New Zealand', 'Tonga', 'Taiwan']
# Create another list with the magnitude of earthquakes, the number of earthquakes should be the same as the country name in the list created above 
magnitude = [5.1, 4.8, 4.5, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6]
# Print the list of countries and their corresponding magnitude of earthquakes
print(earthquakes, magnitude)

# create a dictionary with the country as the key and the magnitude as the value
earthquake_dict = dict(zip(earthquakes, magnitude))
# Print the dictionary after sorting by magnitude
print(earthquake_dict)

# Print the country with the highest magnitude of earthquake
print(max(earthquake_dict, key=earthquake_dict.get))