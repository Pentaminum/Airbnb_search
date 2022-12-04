#%%
import pandas as pd
from shapely.geometry import Point, Polygon

airbnb = pd.read_csv('airbnb_listings.csv.gz')

def d_to_price(d_price):
    price_list = list(d_price)
    price_list = price_list[1:]
    str_price = ''.join(price_list)
    price = float(str_price.replace(',',''))
    return price

# Data cleaning - only using the data we need
airbnb = airbnb[['name', 'listing_url','neighbourhood', 'latitude', 'longitude', 'price', 'room_type', 'review_scores_rating']] 
airbnb['price'] = airbnb['price'].apply(lambda x: d_to_price(x))
# airbnb = airbnb.sort_values(by=['price']) #min = 0, max = 20000

# Export to a cleaned csv file
airbnb.to_csv("cleaned_airbnb_data.csv", index=False)


# %%
