from src.models.Model import GetData
from src.utils.filter import getDataFiltered
import src.utils.convertCountry as convertCountry
from src.utils.dataframe import createPivotOf
import pandas as pd
df_country = GetData('country')

def getAllCountry():
  code = convertCountry.getCode(df_country)
  df_country['country_code'] = code
  df_country_min=df_country.groupby(['country', 'country_code']).size().reset_index(name='counts')

  df_country_min.rename(columns={'counts': 'value','country_code':'id'}, inplace=True)
  return df_country_min[['id', 'value', 'country']]


def getCountryFiltered(key, value):
  
  return getDataFiltered('country',getAllCountry, key, value)

def getCountryWithAllAttributes():
  df_countryGenre= pd.DataFrame()
  df_countryGenre = createPivotOf(df_countryGenre, df_country, 'country', 'listed_in')
  country_gendre = df_countryGenre.sort_values(
      by=[0], ascending=False).to_dict(orient='records')


  result = {}
  for item in country_gendre:
    country = item['country']
    listed_in = item['listed_in']
    if country not in result:
      result[country] = {'id': country, 'data': []}
    result[country]['data'].append({'x': listed_in, 'y': item[0]})

  result = list(result.values())
  for r in result:
    r['data'] = sorted(r['data'], key=lambda x: x['y'], reverse=True)
  result = sorted(result, key=lambda x: sum(
      d['y'] for d in x['data']), reverse=True)
  result = result[:10]
  for r in result:
    r['data'] = r['data'][:6]
  return result
