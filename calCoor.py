from math import sin, cos, atan2, radians, sqrt, ceil
              
print("Latitude & Longitude Distance Calculator")
lat1 = int(input("Input Latitude 1 : "))
lat2 = int(input("Input Latitude 2 : "))
lon1 = int(input("Input Longitude 1 : "))
lon2 = int(input("Input Longitude 2 : "))

R = 6371
lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
dlat = lat2 - lat1
dlon = lon2 - lon1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = R * c

print("------------------------")
print(f"Distance = {ceil(d)} km")
print("------------------------")