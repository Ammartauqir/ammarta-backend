import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Strava API configuration
STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
STRAVA_REFRESH_TOKEN = os.getenv('STRAVA_REFRESH_TOKEN')

# Cache for Strava data
strava_cache = {
    'data': None,
    'last_updated': None
}

def get_strava_access_token():
    """Get a new access token using the refresh token"""
    response = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': STRAVA_CLIENT_ID,
            'client_secret': STRAVA_CLIENT_SECRET,
            'refresh_token': STRAVA_REFRESH_TOKEN,
            'grant_type': 'refresh_token'
        }
    )
    return response.json()['access_token']

def fetch_strava_activities():
    """Fetch activities from Strava API"""
    access_token = get_strava_access_token()
    
    # Calculate date range (3 months ago)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    
    # Convert to Unix timestamp
    after = int(start_date.timestamp())
    
    response = requests.get(
        'https://www.strava.com/api/v3/athlete/activities',
        headers={'Authorization': f'Bearer {access_token}'},
        params={'after': after, 'per_page': 100}
    )
    
    activities = response.json()
    
    # Process activities to include only relevant data
    processed_activities = []
    for activity in activities:
        processed_activities.append({
            'id': activity['id'],
            'name': activity['name'],
            'type': activity['type'],
            'distance': activity['distance'],  # in meters
            'moving_time': activity['moving_time'],  # in seconds
            'elapsed_time': activity['elapsed_time'],  # in seconds
            'total_elevation_gain': activity['total_elevation_gain'],  # in meters
            'start_date': activity['start_date'],
            'average_speed': activity['average_speed'],  # meters per second
            'max_speed': activity['max_speed'],  # meters per second
            'average_heartrate': activity.get('average_heartrate'),
            'max_heartrate': activity.get('max_heartrate'),
            'elev_high': activity.get('elev_high'),
            'elev_low': activity.get('elev_low'),
            'description': activity.get('description', ''),
            'calories': activity.get('calories')
        })
    
    return processed_activities

def get_cached_activities():
    """Get activities from cache or fetch new data if cache is expired"""
    if (strava_cache['last_updated'] is None or 
        (datetime.now() - strava_cache['last_updated']).total_seconds() > 21600):  # 6 hours
        
        try:
            activities = fetch_strava_activities()
            strava_cache['data'] = activities
            strava_cache['last_updated'] = datetime.now()
        except Exception as e:
            raise e
    
    return strava_cache['data']