from src.models.Model import GetData

df_type = GetData('director')


def getAllDirector():
  return df_type['director'].drop_duplicates()
