from flask import Blueprint, request
import src.models.Gendre as Gendre
import src.utils.response as response
GenreApp = Blueprint('GenreApp', __name__, url_prefix='/gendres')


@GenreApp.get('/')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    gendres = Gendre.getAllGendre()
    if(key != None and value != None) : gendres = Gendre.getGendreFiltered(key, value)
    return response.success(gendres.to_list())
  except  Exception as e:
    return response.error( e.args[0])

@GenreApp.get('/grafik')
def grafik():
  try:
    gendres = Gendre.getGendreWithAllAttributes()
    return response.success(gendres.to_dict(orient='records'))
  except Exception as e:
    return response.error( e.args[0])