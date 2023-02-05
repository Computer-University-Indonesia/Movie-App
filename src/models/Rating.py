from src.models.Model import GetData
from src.utils.dataframe import createPivotOf
import pandas as pd

df_genre = GetData('genre')
df_cast = GetData('cast')
df_rating = GetData('rating')
df_type = GetData('type')
df_country = GetData('country')
df_director = GetData('director')



def getAllRating():
  return df_rating['rating'].value_counts().index


def getRatingFiltered(key, value):
  df = pd.DataFrame()
  data = pd.DataFrame()
  match key:
    case 'gendre':
      data = df_genre
      key = 'listed_in'
    case 'cast':
      data = df_cast
    case 'country':
      data = df_country
    case 'director':
      data = df_director
    case 'type':
      data = df_type
    case _:
      return getAllRating()
  df_rating_filtered = createPivotOf(df, data, key, 'rating')
  result = df_rating_filtered.loc[df_rating_filtered[key] == value]
  return result['rating']
