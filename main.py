import phonenumbers
import opencage
import folium
from phonenumbers import geocoder

phone_number = input("Enter the phone number in international format (e.g., +1234567890): ")

try:
    parsed_number = phonenumbers.parse(phone_number)
    location = geocoder.description_for_number(parsed_number, "en")
    print("Location:", location)
    from phonenumbers import carrier
    service_pro = phonenumbers.parse(phone_number)
    print(carrier.name_for_number(service_pro,"en"))
    from opencage.geocoder import OpenCageGeocode
    key = '64b826e3185947139ac08d27332793fa'
    geocoder = OpenCageGeocode(key)
    query = str(location)
    result = geocoder.geocode(query)
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    print(lat,lng)
    myMap = folium.Map(location=[lat,lng] , zoom_start=9)
    folium.Marker([lat , lng],popup=location).add_to(myMap)
    myMap.save('location.html')
except phonenumbers.NumberParseException as e:
    print("Error:", e)