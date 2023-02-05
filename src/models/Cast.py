from src.models.Model import GetData
from src.utils.dataframe import createPivotOf
import pandas as pd

df_genre = GetData('genre')
df_cast = GetData('cast')
df_country = GetData('country')
df_director = GetData('director')
df_rating = GetData('rating')
df_type = GetData('type')

df_cast = GetData('cast')


def getAllCast():
  return df_cast['cast'].value_counts().index


def getCastFiltered(key, value):
  df = pd.DataFrame()
  data = pd.DataFrame()
  match key:
    case 'gendre':
      data = df_genre
      key = 'listed_in'
    case 'country':
      data = df_country
    case 'director':
      data = df_director
    case 'rating':
      data = df_rating
    case 'type':
      data = df_type
    case _:
      return getAllCast()
  df_castGenre = createPivotOf(df, data, key, 'cast')
  castGendre = df_castGenre.loc[df_castGenre[key] == value]
  return castGendre['cast']
