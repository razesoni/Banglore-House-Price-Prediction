import json
import os
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = [0] * len(__data_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    with open(os.path.join(data_dir, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open(os.path.join(data_dir, "model.pickle"), "rb") as f:
        global __model
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))