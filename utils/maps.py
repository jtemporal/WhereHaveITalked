import pandas as pd
from ipyleaflet import Map, Marker, basemaps


def load_data():
    """Loads dataset from places.csv using pandas

    Returns:
        df: A Pandas.DataFrame containing all stored data
    """
    return pd.read_csv('places.csv')


def save_data(dataset):
    """Saves new data points to dataset in places.csv using pandas

    Args:
        dataset: required, Pandas.DataFrame with locations
    """
    dataset.to_csv('places.csv', index=False)


def creates_standard_map():
    """Creates a standard map with OpenStreetMap

    Returns:
        map: A ipyleaflet.Map
    """
    center = (13.133932434766733, 16.103938729508073)
    return Map(basemap=basemaps.OpenStreetMap.Mapnik, center=center, zoom=2)


def adds_markers(my_map, dataset):
    """Adds Markers to map from each place in dataset

    Args:
        my_map: required, ipyleaflet.Map standard map to add markers
        dataset: required, Pandas.DataFrame with locations

    Return:
        my_map: A ipyleaflet.Map with marker layers
    """

    for _, place in dataset.iterrows():
        marker = Marker(
            location=[place['latitude'], place['longitude']],
            title=place['name']
        )
        my_map.add_layer(marker)

    return my_map


def create_map():
    """Adds markers and creates HTML file for the map

    Return:
        created: bool, True if map was successfully saved, False otherwise
    """
    try:
        df = load_data()
        my_map = creates_standard_map()
        marked_map = adds_markers(my_map, df)
        marked_map.save('templates/index.html')
    except:
        return False
    return True


def create_new_place(place_data):
    """Adds new lines to the dataset and then saves the data

    Args:
        place_data: dict, A dictionary containing a new place data

    Return:
        created: bool, True if map was successfully saved, False otherwise
    """
    df = load_data()
    result = df.append(place_data, ignore_index=True)
    result = result.drop_duplicates(keep=False)
    save_data(result)
