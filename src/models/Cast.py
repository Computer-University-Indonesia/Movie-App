from src.models.Model import GetData

df_cast = GetData('cast')


def getAllCast():
  return df_cast['cast'].value_counts().index
