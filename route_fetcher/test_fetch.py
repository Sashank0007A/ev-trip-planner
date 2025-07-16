# route_fetcher/test_fetch.py

from fetch_route import get_route_distance_time

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjIyNzQ5MGJiMjY4MTQ1YjU4OGNiZDVjNTZkMDFkNTBjIiwiaCI6Im11cm11cjY0In0="

start = "Coimbatore"
end = "Madurai"

distance, duration = get_route_distance_time(start, end, API_KEY)

print(f"Distance: {distance:.2f} km")
print(f"Estimated Time: {duration:.2f} mins")
