import requests

# Set up HERE API credentials
API_KEY = "k6AF02uec6xQEzvhF-XB_wdqffYPoVNOjApiS2NK6jY"

# Define the latitude and longitude
latitude =11.13728
longitude =77.329787

# Construct the request URL
url = f"https://revgeocode.search.hereapi.com/v1/revgeocode?at={latitude},{longitude}&apiKey={API_KEY}"

# Send the HTTP GET request
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract the address from the response
address = data["items"][0]["address"]["label"]

# Print the address
print("Address:", address)
