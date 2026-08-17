import requests
import pandas as pd
import time

# Step 1: Replace with your actual Google API Key
API_KEY = "AIzaSyBofTxTN2X4d6sSyeaorDIHTGdrxU7kRUI"

# Step 2: Define Search Parameters
location = "39.0997,-94.5786"  # Kansas City center (latitude, longitude)
radius = 20000  # Search radius in meters (20 km)
place_type = "bakery"

# Step 3: Base URL for Google Places API
base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Step 4: Function to Fetch Bakery Data
def fetch_bakery_data():
    bakery_list = []
    next_page_token = None

    while True:  # Loop starts here
        # Build API Request
        params = {
            "location": location,
            "radius": radius,
            "type": place_type,
            "key": API_KEY
        }
        if next_page_token:
            params["pagetoken"] = next_page_token  # Fetch next page

        response = requests.get(base_url, params=params)

        # Step 5: Check if API Request is Successful
        if response.status_code != 200:
            print("❌ Error: API request failed! Status code:", response.status_code)
            print("Response:", response.text)
            return []  # Use return instead of break (fixes the error)

        # Step 6: Convert API response to JSON format
        data = response.json()

        # Step 7: Extract Bakery Details
        for place in data.get("results", []):
            bakery_list.append({
                "Name": place.get("name"),
                "Address": place.get("vicinity"),
                "Rating": place.get("rating"),
                "Number_of_Reviews": place.get("user_ratings_total"),
                "Latitude": place["geometry"]["location"]["lat"],
                "Longitude": place["geometry"]["location"]["lng"]
            })

        # Step 8: Check if There's More Data (Pagination)
        next_page_token = data.get("next_page_token")
        if not next_page_token:
            break  # Correct usage inside the loop

        # Google requires a short delay before using next page token
        time.sleep(2)

    return bakery_list

# Step 9: Run the Function and Save Data
bakery_data = fetch_bakery_data()

# Step 10: Convert Data to CSV
df = pd.DataFrame(bakery_data)
df.to_csv("kc_bakeries_google.csv", index=False)

print("Google Maps bakery data saved to kc_bakeries_google.csv")
