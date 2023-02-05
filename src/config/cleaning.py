from src.utils.dataframe import splitDataFrameList
from src.config.config  import SHAPEFILE

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
      return  df_country

# def split(df):
  # df_director = splitDataFrameList(df,'director',', ')
  # df_genre = splitDataFrameList(df, 'listed_in', ', ')
  # df_cast = splitDataFrameList(df, 'cast', ', ')
  # df_country = splitDataFrameList(df, 'country', ', ')
  # df_rating = splitDataFrameList(df, 'rating', ', ')
  # df_type = splitDataFrameList(df, 'type', ', ')
  # return 