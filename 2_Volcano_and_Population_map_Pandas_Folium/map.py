import folium
import pandas
map = folium.Map(location=[38,-99], tiles="stamenterrain", zoom_start=5)
data = pandas.read_csv("Volcanoes.txt")
lats = list(data["LAT"])
longs = list(data["LON"])
elev = list(data["ELEV"])

def color_elevation(elevation):
    if elevation < 1000:
        return "green"
    #elif elevation < 1000 and elevation > 3000:
    elif 1000 <= elevation <3000:
        return "orange"
    else:
        return "red"
    
fg = folium.FeatureGroup("My Map")
    
for lat, long, el in zip(lats,longs,elev):
    fg.add_child(folium.CircleMarker(location=[lat,long],popup=str(el)+"m",fill_color=color_elevation(el),color="grey",fill_opacity=1))
    
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()
,style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 
'orange' if 10000000 >= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fg)
map.save("Map1.html")

