import geopandas as gpd
import pandas as pd
import folium
from folium import Choropleth

rmap = folium.Map(location=[35.79526126311406, -78.7497823023319], tiles='openstreetmap', zoom_start=5)

rmap.save('map.html')

orgs=pd.read_csv("support.csv")
print(orgs.head())

rmap2=folium.Map(location=[35.79526126311406, -78.7497823023319], tiles='cartodbpositron', zoom_start=8)

for i in range(0, len(orgs)):
  folium.Marker(location=[orgs.iloc[i]['Lat'], orgs.iloc[i]['Long']], popup=orgs.iloc[i]['Place']).add_to(rmap2)

rmap2.save('resourcemap.html')
