import geopandas as gpd
import pandas as pd
import folium
from folium import Choropleth
import matplotlib.pyplot as plt


counties=gpd.read_file('/Users/namrata/Downloads/NCDOT_County_Boundaries/NCDOT_County_Boundaries.shp')
# print(counties.head())

ctys=counties[["CountyName", "geometry"]].set_index("CountyName") #set dataframe index as county name
# print(ctys.head())

percent = pd.read_csv('/Users/namrata/Downloads/asian_pop.csv')
apercent=percent[["CountyName", "% Asian"]].set_index("CountyName") # filters dataset to reflect county and Asian percentage
print(type(percent['% Asian'][0]))
# print(apercent.head())

for_plotting = counties.merge(apercent, left_on = 'CountyName', right_on='CountyName') #merges counties and Asian population data
print(for_plotting.head())

county_asia_map=folium.Map(location=[35.79024437,-78.65030817], tiles='cartodbpositron', zoom_start=12)
Choropleth(
 geo_data=for_plotting,
 name='Choropleth',
 data=for_plotting,
 columns=['CountyName','% Asian'],
 key_on="feature.id",
 fill_color="YlGn",
 fill_opacity=0.7,
 line_opacity=.1,
 legend_name='Asian Population By NC County'
).add_to(county_asia_map)

folium.LayerControl().add_to(county_asia_map)
county_asia_map.save('asian_popmap.html')

# matplotlib
fig, ax = plt.subplots(1, figsize=(10,6))
for_plotting.plot(column='% Asian', cmap='Blues', linewidth=1, ax=ax, edgecolor='0.9', legend = True)
ax.axis('off')

plt.savefig("asianpop.png")
