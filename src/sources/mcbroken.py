import numpy as np
import requests
import geopandas as gpd

from .datasource import DataSource


class Mcbroken(DataSource):
    url = 'https://mcbroken2.nyc3.digitaloceanspaces.com/markers.json'

    def pull_data(self):
        r = requests.get(self.url)
        if r.status_code != 200:
            r.raise_for_status()

        features = r.json()['features']
        return features

    def clean_row(self, row):
        coords = row['geometry']['coordinates']
        row['geometry']['coordinates'] = np.array(
            [float(coords[0]), float(coords[1])])
        return row

    def as_gdf(self, features):
        """Convert dataframe to geodataframe"""
        gdf = gpd.GeoDataFrame.from_features(
            [self.clean_row(r) for r in features])
        return gdf
