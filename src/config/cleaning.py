from src.utils.dataframe import splitDataFrameList
from src.config.config  import SHAPEFILE
import geopandas as gpd
import country_converter as coco
import pandas as pd

def data_cleaning(df,type):
  df = df[1:]
  df.dropna(subset=['director', 'cast', 'country', 'date_added', 'rating', 'duration'], axis=0, inplace=True)
  df.drop(['show_id'], axis = 1, inplace = True)
  df.reset_index(drop=True, inplace=True)
  # df_director, df_genre, df_cast, df_country, df_rating, df_type = split(df)
  match type :
    case 'director':
      return splitDataFrameList(df,'director',', ')
    case 'genre':
      return splitDataFrameList(df, 'listed_in', ', ')
    case 'cast':
      return splitDataFrameList(df, 'cast', ', ')
    case 'rating':
      return splitDataFrameList(df, 'rating', ', ')
    case 'type':
      return splitDataFrameList(df, 'type', ', ')
    case 'country':
      df_country = splitDataFrameList(df, 'country', ', ')
      df_country['country'] = df_country['country'].replace(['United States'], 'United States of America')
      geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
      # Rename columns.
      geo_df.columns = ['country', 'country_code', 'geometry']
      # Next, we need to ensure that our data matches with the country codes. 
      iso3_codes = geo_df['country'].to_list()
      # Convert to iso3_codes
      iso2_codes_list = coco.convert(names=iso3_codes, to='ISO2', not_found='NULL')
      # Add the list with iso2 codes to the dataframe
      geo_df['iso2_code'] = iso2_codes_list
      # There are some countries for which the converter could not find a country code. 
      # We will drop these countries.
      geo_df = geo_df.drop(geo_df.loc[geo_df['iso2_code'] == 'NULL'].index)
      df_country = pd.merge(left=df_country, right=geo_df, how='left', left_on='country', right_on='country')
      return  df_country

# def split(df):
  # df_director = splitDataFrameList(df,'director',', ')
  # df_genre = splitDataFrameList(df, 'listed_in', ', ')
  # df_cast = splitDataFrameList(df, 'cast', ', ')
  # df_country = splitDataFrameList(df, 'country', ', ')
  # df_rating = splitDataFrameList(df, 'rating', ', ')
  # df_type = splitDataFrameList(df, 'type', ', ')
  # return 