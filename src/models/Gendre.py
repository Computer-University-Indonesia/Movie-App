from src.models.Model import GetData 

df_genre = GetData('genre')
  
def getAllGendre():
  return df_genre['listed_in'].drop_duplicates()
