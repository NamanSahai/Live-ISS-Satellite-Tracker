from skyfield.api import load
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load TLE data for ISS
stations_url = 'https://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
by_name = {sat.name: sat for sat in satellites}
iss = by_name['ISS (ZARYA)']

# Get current time
ts = load.timescale()
t = ts.now()

# Get ISS location
geocentric = iss.at(t)
subpoint = geocentric.subpoint()
lat = subpoint.latitude.degrees
lon = subpoint.longitude.degrees
alt = subpoint.elevation.km

# Print live data
print(f'Latitude: {lat:.2f}, Longitude: {lon:.2f}, Altitude: {alt:.2f} km')

# Plot on world map
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.COASTLINE)

# Mark ISS
ax.plot(lon, lat, 'ro', markersize=6, transform=ccrs.Geodetic())
plt.title("Current Location of ISS")
plt.savefig("iss_position_map.png")
plt.show()