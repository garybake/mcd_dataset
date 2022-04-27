
import json
import geopandas as gpd

from sources.mcbroken import Mcbroken



def main():
    src = Mcbroken()
    data = src.pull_data()
    # data = data[0]
    # print(json.dumps(data, indent=4, sort_keys=True))
    # print(src.pull_data())
    clean = src.clean_row(data[0])
    print(clean)
    gdf = gpd.GeoDataFrame.from_features([clean])



if __name__ == "__main__":
    main()
