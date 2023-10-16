import phonenumbers
from mynumber import number
from phonenumbers import geocoder
import folium

sanNumber=phonenumbers.parse(number)

yourlocation=geocoder.description_for_number(sanNumber,"en")

print(yourlocation)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode("ea817b35bf9a486b91c5be4cba6358ad")

query=str(yourlocation)

results=geocoder.geocode(query)

print(results)

lat=11.0238
lng=76.9452
print(lat,lng)

mymap= folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat, lng],popup=yourlocation).add_to((mymap))
mymap.save('myLocation.html')


