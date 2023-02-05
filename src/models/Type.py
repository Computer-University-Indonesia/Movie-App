from src.models.Model import GetData
from src.utils.dataframe import createPivotOf
import pandas as pd

df_genre = GetData('genre')
df_cast = GetData('cast')
df_rating = GetData('rating')
df_country = GetData('country')
df_director = GetData('director')
df_type = GetData('type')


def getAllType():
  return df_type['type'].value_counts().index


def getTypeFiltered(key, value):
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
    case 'rating':
      data = df_rating
    case _:
      return getAllType()
  df_director_filtered = createPivotOf(df, data, key, 'type')
  result = df_director_filtered.loc[df_director_filtered[key] == value]
  return result['type']
