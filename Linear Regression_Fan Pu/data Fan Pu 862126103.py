#!/usr/bin/python
import json
import csv

selects = ['business_id', 'name', 'stars', 'state', 'categories']
business_lst = []
attributes_filter = ['Alcohol', 'BikeParking', 'GoodForKids', 'HasTV' , 'OutdoorSeating', 'RestaurantsReservations', 'WiFi']
parking = 'BusinessParking'
parking_types = ['garage', 'street', 'lot']
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        data = json.loads(line)
        categories = data['categories']
        attributes = data['attributes']
        if categories:
            if 'Restaurants' in categories:
                row = []
                for select in selects:
                    row.append(data.get(select, None))
                attribute_lst = []
                if attributes:
                    for attribute in attributes_filter:
                        attribute_lst.append(attributes.get(attribute, None))
                    parking_attributes = attributes.get(parking, None)
                    if parking_attributes and parking_attributes != 'None':
                        replaced = parking_attributes.replace("\'", "\"").replace('True', '"True"').replace('False', '"False"').replace('None', '"None"')
                        parking_attributes_json = json.loads(replaced)
                        for parking_type in parking_types:
                            attribute_lst.append(parking_attributes_json.get(parking_type, None))
                row.extend(attribute_lst)                            
                business_lst.append(row)                

with open("business.csv", "w", newline="") as f:
    writer = csv.writer(f)
    header = selects + attributes_filter + [s+'_parking' for s in parking_types]
    writer.writerow(header)
    writer.writerows(business_lst)
