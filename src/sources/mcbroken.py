
import requests

from .datasource import DataSource


class Mcbroken(DataSource):

    url = 'https://mcbroken2.nyc3.digitaloceanspaces.com/markers.json'

    def pull_data(self):
        # r = requests.get(self.url)
        # if r.status_code != 200:
        #     r.raise_for_status()
        #
        # features = r.json()['features']
        features = [{'geometry': {'coordinates': ['-74.010086', '40.709438', 0.0], 'type': 'Point'}, 'properties': {'is_broken': False, 'is_active': True, 'dot': 'inactive', 'state': 'NY', 'city': 'New York', 'street': '160 Broadway', 'country': 'USA', 'last_checked': 'Checked 418766 minutes ago'}, 'type': 'Feature'}, {'geometry': {'coordinates': ['-74.010736', '40.716366', 0.0], 'type': 'Point'}, 'properties': {'is_broken': True, 'is_active': True, 'dot': 'inactive', 'state': 'NY', 'city': 'New York', 'street': '167 Chambers St (303 Greenwich St)', 'country': 'USA', 'last_checked': 'Checked 418766 minutes ago'}, 'type': 'Feature'}, {'geometry': {'coordinates': ['-74.001052', '40.718587', 0.0], 'type': 'Point'}, 'properties': {'is_broken': False, 'is_active': True, 'dot': 'inactive', 'state': 'NY', 'city': 'New York', 'street': '262 Canal St', 'country': 'USA', 'last_checked': 'Checked 418766 minutes ago'}, 'type': 'Feature'}, {'geometry': {'coordinates': ['-73.989226', '40.712839', 0.0], 'type': 'Point'}, 'properties': {'is_broken': True, 'is_active': True, 'dot': 'inactive', 'state': 'NY', 'city': 'New York', 'street': '213 Madison Street', 'country': 'USA', 'last_checked': 'Checked 687985 minutes ago'}, 'type': 'Feature'}]

        return features[:4]

    def clean_row(self, row):

        geometry = row['geometry']
        coords = geometry['coordinates']
        geometry['coordinates'] = [float(f) for f in coords]

        r = {
            'geometry': geometry
        }
        properties = row['properties']
        for prop in properties:
            r[prop] = properties[prop]
        return r
