from src.models.Model import GetData
from src.utils.filter import getDataFiltered
import src.utils.convertCountry as convertCountry

df_country = GetData('country')


def getAllCountry():
  code = convertCountry.getCode(df_country)
  df_country['country_code'] = code
  df_country_min=df_country.groupby(['country', 'country_code']).size().reset_index(name='counts')

  df_country_min.rename(columns={'counts': 'value','country_code':'id'}, inplace=True)
  return df_country_min[['id', 'value', 'country']]


def getCountryFiltered(key, value):
  
  return getDataFiltered('country',getAllCountry, key, value)
