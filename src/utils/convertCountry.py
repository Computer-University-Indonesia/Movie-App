import country_converter as coco

def getCode(df_country):
  df_country['country'] = df_country['country'].replace(
      ['Soviet Union', 'Rusia', 'West Germany', 'East Germany'], ['Russia', 'Russia', 'Germany', 'Germany'])


  standard_names = coco.convert(
    names=df_country['country'].to_list(), to='ISO3')
  return standard_names
  
