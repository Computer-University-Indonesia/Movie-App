from src.models.Model import GetData
import pandas as pd
from src.utils.dataframe import createPivotOf
import src.utils.convertCountry as convertCountry

df_director, df_genre, df_cast, df_country, df_rating, df_type = GetData('all')


def getDataFiltered(model,get_all,key, value):
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
    case 'cast':
      data = df_cast
    case _:
      return get_all()
  df_castGenre = createPivotOf(df, data, key, model)
  result = df_castGenre.loc[df_castGenre[key] == value]
  if(model =='country'):
    code = convertCountry.getCode(result)
    result['id'] = code
    result.rename(columns={0: 'value'}, inplace=True)
  
  return result
