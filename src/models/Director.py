from src.models.Model import GetData
from src.utils.dataframe import createPivotOf
import pandas as pd

df_genre = GetData('genre')
df_cast = GetData('cast')
df_rating = GetData('rating')
df_type = GetData('type')
df_country = GetData('country')
df_director = GetData('director')


def getAllDirector():
  return df_director['director'].value_counts().index


def getDirectorFiltered(key, value):
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
    case 'rating':
      data = df_rating
    case 'type':
      data = df_type
    case _:
      return getAllDirector()
  df_director_filtered = createPivotOf(df, data, key, 'director')
  result = df_director_filtered.loc[df_director_filtered[key] == value]
  return result['director']
