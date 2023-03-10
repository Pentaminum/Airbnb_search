#%%
import pandas as pd

stop = pd.read_csv("Stops.csv")
station = pd.read_csv("Stations.csv")

del stop['x'], stop['y']
del station['x'], station['y']


stop = stop[['stop_name','Longitude','Latitude']]
station = station[['Exch_Name','Longitude','Latitude']]

stop.rename(columns={'stop_name': 'name'}, inplace=True)
station.rename(columns={'Exch_Name': 'name'}, inplace=True)
combined = pd.concat([stop, station], axis=0)

#combined.to_cvs("cleaned_public_transporation.csv")
print(combined)
combined.to_csv("cleaned_public_transportation.csv")
# station.to_csv('cleaned_stations.csv')
# %%
