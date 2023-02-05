from src.models.Model import GetData
# from src.models.Model import GetData
from src.utils.dataframe import createPivotOf
import pandas as pd
import src.utils.convertCountry as convertCountry

df_genre = GetData('genre')
df_cast = GetData('cast')
df_director = GetData('director')
df_rating = GetData('rating')
df_type = GetData('type')

df_cast = GetData('cast')

df_country = GetData('country')


def getAllCountry():
  code = convertCountry.getCode(df_country)
  df_country['country_code'] = code
  df_country_min=df_country.groupby(['country', 'country_code']).size().reset_index(name='counts')

  df_country_min.rename(columns={'counts': 'value','country_code':'id'}, inplace=True)
  return df_country_min[['id', 'value', 'country']]


def getCountryFiltered(key, value):
  df = pd.DataFrame()
  data = pd.DataFrame()
  match key:
    case 'gendre':
      data = df_genre
      key = 'listed_in'
    case 'cast':
      data = df_cast
    case 'director':
      data = df_director
    case 'rating':
      data = df_rating
    case 'type':
      data = df_type
    case _:
      return getAllCountry()
  df_country_filtered = createPivotOf(df, data, key, 'country')
  result = df_country_filtered.loc[df_country_filtered[key] == value]
  code = convertCountry.getCode(result)
  result['id'] = code
  result.rename(columns={0: 'value'}, inplace=True)

  return result
