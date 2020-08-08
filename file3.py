#exercise:map of metropolitan cities
import folium
import pandas
data=pandas.read_csv("metropolitan1cities.csv")
lon=list(data["lon"])
lat=list(data["lat"])
color=list(data["color"])
cityname=list(data["cityname"])
map=folium.Map(location=(12.58,77.34),zoom_start=3)
fg=folium.FeatureGroup(name="bangloremap")
for ll,lt,city,color in zip(lon,lat,cityname,color):
  fg.add_child(folium.Marker(location=(ll,lt),popup=city,icon=folium.Icon(color=(color))))
map.add_child(fg)
map.save('bmap2.html')


