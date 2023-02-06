from src.utils.dataframe import splitDataFrameList
from src.config.config  import SHAPEFILE

def data_cleaning(df,typeData):
  print('Cleaning data...')
  df = df[1:]
  df = df.dropna(subset=['director', 'cast', 'country', 'date_added', 'rating',
                 'duration', 'show_id'], axis=0, ).reset_index(drop=True)
  # df.drop(['show_id'], axis = 1, inplace = True)
  match typeData:
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
      return  df_country
    case 'all':
      return  split(df)

def split(df):
  df_director = splitDataFrameList(df,'director',', ')
  df_genre = splitDataFrameList(df, 'listed_in', ', ')
  df_cast = splitDataFrameList(df, 'cast', ', ')
  df_country = splitDataFrameList(df, 'country', ', ')
  df_rating = splitDataFrameList(df, 'rating', ', ')
  df_type = splitDataFrameList(df, 'type', ', ')
  return df_director, df_genre, df_cast, df_country, df_rating, df_type
