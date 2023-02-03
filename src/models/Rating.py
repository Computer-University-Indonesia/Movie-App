from src.models.Model import GetData

df_type = GetData('rating')


def getAllRating():
  return df_type['rating'].drop_duplicates()
