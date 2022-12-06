#%%
import pandas as pd
import numpy as np

amenities = pd.read_json(
    "output/amenity/amenity.json.gz", lines=True, compression="gzip"
)
#%%

#amenities['amenity'].unique()

# list = ['post_box', 'telephone', 'bench', 'toilets', 'bank', 'cafe',
#    'fast_food', 'bbq', 'vending_machine', 'restaurant',
#    'parking_entrance', 'pub', 'fuel', 'bicycle_parking', 'school',
#    'pharmacy', 'recycling', 'waste_disposal', 'waste_basket',
#    'car_wash', 'dentist', 'parking_space', 'doctors', 'parking',
#    'public_building', 'post_office', 'atm', 'childcare', 'bar',
#    'ice_cream', 'bus_station', 'community_centre', 'library',
#    'bicycle_rental', 'drinking_water', 'shelter', 'clinic',
#    'public_bookcase', 'university', 'dojo', 'kindergarten',
#    'ferry_terminal', 'cinema', 'theatre', 'charging_station',
#    'car_rental', 'car_sharing', 'fountain', 'seaplane terminal',
#    'bicycle_repair_station', 'food_court', 'veterinary',
#    'smoking_area', 'post_depot', 'locker', 'bureau_de_change',
#    'clock', 'nightclub', 'animal_boarding', 'motorcycle_parking',
#    'place_of_worship', 'taxi', 'shower', 'arts_centre',
#    'social_facility', 'prep_school', 'college', 'stripclub',
#    'construction', 'boat_rental', 'letter_box', 'social_centre',
#    'fire_station', 'police', 'conference_centre', 'gambling',
#    'marketplace', 'karaoke_box', 'music_school', 'compressed_air',
#    'family_centre', 'townhall', 'sanitary_dump_station', 'studio',
#    'training', 'trolley_bay', 'playground', 'courthouse', 'spa',
#    'loading_dock', 'meditation_centre', 'bistro', 'language_school',
#    'events_venue', 'parcel_locker', 'healthcare', 'binoculars',
#    'vacuum_cleaner', 'waste_basket;recycling', 'hookah_lounge',
#    'trash', 'internet_cafe', 'driving_school', 'disused:restaurant',
#    'water_point', 'casino', 'science', 'ATLAS_clean_room', 'workshop',
#    'safety', 'lobby', 'animal_shelter', 'lounger', 'storage_rental',
#    'vacuum', 'give_box', 'atm;bank', 'EVSE', 'first_aid',
#    'ranger_station', 'dance', 'weighbridge', 'housing co-op',
#    'research_institute', 'monastery', 'nursing_home',
#    'payment_terminal', 'Observation Platform', 'dive_centre',
#    'dressing_room', 'laboratory', 'cooking_school', 'hunting_stand',
#    'money_transfer', 'biergarten', 'mortuary',
#    'waste_transfer_station', 'toy_library', 'animal_training',
#    'lounge', 'hospital', 'bear_box', 'table', 'motorcycle_rental',
#    'leisure', 'prison']

# Remove 'prison', 'money_transfer', 'storage_rental', 'language_school', 

# osm_data = osm_data.replace(['bar', 'biergarten', 'cafe', 'fast_food', 'food_court', 'ice_cream', 'pub', 'restaurant'], 'sustenance')
# osm_data = osm_data.replace(['kick-scooter_rental', 'bicycle_rental', 'bus_station', 'car_rental', 'car_sharing', 'taxi'], 'transportation')
# osm_data = osm_data.replace(['bicycle_parking', 'motorcycle_parking', 'parking', 'parking_entrance', 'parking_space'], 'parking')

# Keep 
#  'cafe', 'fast_food', 'bbq', 'restaurant', 'pub', 'bar', 'ice_cream','food_court','bistro', 'biergarten'
#  'drinking_water' 'fountain'
#  'parking_space', 'parking', 'car_rental', 'car_sharing', 'motorcycle_parking', 'motorcycle_rental',
#  'cinema', 'theatre', 'nightclub', 'arts_centre', 'stripclub', 'boat_rental', 'gambling', 'marketplace', 'karaoke_box','spa', 'hookah_lounge','internet_cafe','casino','dance', 'toy_library',  'leisure'
#   
#  'bus_station', 'bicycle_parking', 'bicycle_rental', 'bicycle_repair_station', 'ferry_terminal',  'seaplane terminal'


# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(amenities["tags"])
unnested_amenities = pd.concat([amenities, tags], axis=1)
print(unnested_amenities)
df = unnested_amenities[unnested_amenities['tourism'].notna()]
print(df)
# https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
#  'cafe', 'fast_food', 'bbq', 'restaurant', 'pub', 'bar', 'ice_cream','food_court','bistro', 'biergarten'
# → Food

#  'parking_space', 'parking', 'car_rental', 'car_sharing', 'motorcycle_parking', 'motorcycle_rental',
# → Car

#  'cinema', 'theatre', 'nightclub', 'arts_centre', 'stripclub', 'boat_rental', 'gambling', 'marketplace', 'karaoke_box','spa', 'hookah_lounge','internet_cafe','casino','dance', 'toy_library',  'leisure' , … other tourist attraction
# -> Attraction

#  'bus_station', 'bicycle_parking', 'bicycle_rental', 'bicycle_repair_station', 'ferry_terminal',  'seaplane terminal'
# -> public transportatin

#%%

food_condition = (
    (amenities["type"] == "cafe")
    | (amenities["type"] == "fast_food")
    | (amenities["type"] == "bbq")
    | (amenities["type"] == "restaurant")
    | (amenities["type"] == "pub")
    | (amenities["type"] == "bar")
    | (amenities["type"] == "ice_cream")
    | (amenities["type"] == "food_court")
    | (amenities["type"] == "bistro")
    | (amenities["type"] == "biergarten")
)

entertainment_condition = (
    (amenities["type"] == "cinema")
    | (amenities["type"] == "cinema")
    | (amenities["type"] == "theatre")
    | (amenities["type"] == "nightclub")
    | (amenities["type"] == "arts_centre")
    | (amenities["type"] == "stripclub")
    | (amenities["type"] == "boat_rental")
    | (amenities["type"] == "gambling")
    | (amenities["type"] == "marketplace")
    | (amenities["type"] == "spa")
    | (amenities["type"] == "hookah_lounge")
    | (amenities["type"] == "internet_cafe")
    | (amenities["type"] == "casino")
    | (amenities["type"] == "dance")
    | (amenities["type"] == "toy_library")
    | (amenities["type"] == "leisure")
)

# public_transportation_condition = (amenities['type'] == 'bus_station') \
#     or (amenities['type'] == 'bicycle_parking') \
#     or (amenities['type'] == 'bicycle_rental') \
#     or (amenities['type'] == 'bicycle_repair_station') \
#     or (amenities['type'] == 'ferry_terminal') \
#     or (amenities['type'] == ) \
#     or (amenities['type'] == ) \
#     or (amenities['type'] == ) \
#     or (amenities['type'] == ) \
#     or (amenities['type'] == ) \

# There's no train station. Maybe suse the stops.csv or station.csv

# For later use.
# attraction_condition =  (amenities['type'] == 'cinema') \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \
# or (amenities['type'] == ) \

conditions = [
    food_condition,
    entertainment_condition,
]
choices = ["food", "entertainment"]
amenities["category"] = np.select(conditions, choices, default=None)

#Keep amenities with category (food and attraction)
amenities = amenities[amenities['category'].notna()]
food_amenities = amenities[amenities['category']=='food']
attraction_amenities = amenities[amenities['category']=='entertainment']

food_amenities.to_csv("cleaned_food_amenities.csv", index=False)
attraction_amenities.to_csv("cleaned_entertainment_amenities.csv", index=False)
# %%
