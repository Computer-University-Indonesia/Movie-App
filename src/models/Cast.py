from src.models.Model import GetData

df_cast = GetData('cast')


def getAllCast():
  return df_cast['cast'].drop_duplicates()
