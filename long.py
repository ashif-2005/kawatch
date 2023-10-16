import requests

def get_coordinates(address):
    # Replace with your HERE API credentials
    api_key = 'k6AF02uec6xQEzvhF-XB_wdqffYPoVNOjApiS2NK6jY'
    base_url = 'https://geocode.search.hereapi.com/v1/geocode'

    # Prepare the request URL
    params = {
        'q': address,
        'apiKey': api_key
    }

    # Send the HTTP GET request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract the latitude and longitude from the response
    if 'items' in data and len(data['items']) > 0:
        item = data['items'][0]
        position = item['position']
        latitude = position['lat']
        longitude = position['lng']
        return latitude, longitude
    else:
        return None

# Example usage
address = input("Enter the address: ")
coordinates = get_coordinates(address)

if coordinates:
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Invalid address or unable to retrieve coordinates.")
