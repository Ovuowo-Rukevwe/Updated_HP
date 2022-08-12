import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 1:
        x[loc_index] = 1

    return round(__model.predict([x])[0])


def get_location_names():
    return __locations


def load_saved_artifacts():
    print('loading saved artifacts...starting')
    global __data_columns
    global __locations

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open('./artifacts/predicted_house_price_model', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts...done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(round(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3), 2))
    print(round(get_estimated_price('Vishveshwarya Layout', 2500, 2, 3), 2))
    print(round(get_estimated_price('Whitefield', 5000, 2, 2), 2))
