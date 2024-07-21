import requests
import json

api_key = 'dabe58733d866f8c661fe595b0e1478fe4de6bf9439782f2c5b47607098bbed5'
endpoint = 'https://external.transitapp.com/v3/public/stop_departures'
params = {
    'global_stop_id': 'DCTATX:4074',
    'remove_cancelled': True,
    'should_update_realtime': True
}
headers = {
    'apiKey': api_key
}

print("Sending API request for stop departures with parameters:", params)


try:
    
    response = requests.get(endpoint, params=params, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    # Check if the response is not empty
    if response.text:
        data = response.json()
    else:
        print("Empty response received")
        data = {}

    # Further processing only if data is not empty
    if data:
        # Extract departure data
        departures = []
        for departure in data.get('departures', []):  # Adjust based on actual API response structure
            departures.append({
                'route_id': departure['route_id'],
                'departure_time': departure['departure_time'],
                'is_real_time': departure['is_real_time']
            })

        

        # Convert to DataFrame and save to CSV if departures are not empty
        if departures:
            df = pd.DataFrame(departures)
            df.to_csv('stop_departures.csv', index=False)
            print("Data saved to 'stop_departures.csv'")
        
    else:
        print("No data to process, check API response and error messages.")

except requests.exceptions.RequestException as e:
    # Handle exceptions that occur during the API request
    print("An error occurred during the API request:", e)

except Exception as e:
    # Handle other possible exceptions
    print("A general error occurred:", e)
