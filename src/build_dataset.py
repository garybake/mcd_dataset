
import json
import geopandas as gpd

from sources.mcbroken import Mcbroken



def main():
    src = Mcbroken()
    data = src.pull_data()
    gdf = src.as_gdf(data)
    gdf.to_file(r'D:\tmp\mcd.shp')



if __name__ == "__main__":
    main()
