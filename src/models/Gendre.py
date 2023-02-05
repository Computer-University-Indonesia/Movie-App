from src.models.Model import GetData 
from src.utils.dataframe import createPivotOf
import pandas as pd

df_genre = GetData('genre')
df_cast = GetData('cast')
df_country = GetData('country')
df_director = GetData('director')
df_rating = GetData('rating')
df_type = GetData('type')

def getAllGendre():
  # get  all gendre from df_genre and sort by most popular gendre and remove duplicates gendre
  return df_genre['listed_in'].value_counts().index
  # gendres = df_genre['listed_in'].value_counts
  

def getGendreFiltered(key, value):
  df = pd.DataFrame()
  data = pd.DataFrame()
  match key:
    case 'cast':
      data = df_cast
    case 'country':
      data = df_country
    case 'director':
      data = df_director
    case 'rating':
      data = df_rating
    case 'type':
      data = df_type
    case _:
      return getAllGendre()
  df_castGenre = createPivotOf(df, data, key, 'listed_in')
  castGendre = df_castGenre.loc[df_castGenre[key]==value]
  return castGendre['listed_in']
