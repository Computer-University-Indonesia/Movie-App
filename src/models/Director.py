from src.models.Model import GetData

df_type = GetData('director')


def getAllDirector():
  return df_type['director'].value_counts().index
