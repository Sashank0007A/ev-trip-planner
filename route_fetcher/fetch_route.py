# route_fetcher/fetch_route.py

import openrouteservice
from openrouteservice import convert
import time

def get_route_distance_time(start, end, api_key):
    try:
        client = openrouteservice.Client(key=api_key)

        # Validate and geocode source
        source_result = client.pelias_search(start)
        if not source_result['features']:
            return None, None  # Invalid source

        start_coords = source_result['features'][0]['geometry']['coordinates']
        start_name = source_result['features'][0]['properties']['label']

        # Validate and geocode destination
        dest_result = client.pelias_search(end)
        if not dest_result['features']:
            return None, None  # Invalid dest

        end_coords = dest_result['features'][0]['geometry']['coordinates']
        end_name = dest_result['features'][0]['properties']['label']

        # Now fetch actual route
        route = client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )

        summary = route['features'][0]['properties']['summary']
        distance_km = summary['distance'] / 1000
        duration_min = summary['duration'] / 60

        return distance_km, duration_min

    except Exception as e:
        print("Route fetch error:", str(e)[:100])  # Keep logs short
        return None, None


