from src.models.Model import GetData

df_type = GetData('type')


def getAllType():
  return df_type['type'].drop_duplicates()
