from src.models.Model import GetData

df_type = GetData('country')


def getAllCountry():
  return df_type['country'].value_counts().index
