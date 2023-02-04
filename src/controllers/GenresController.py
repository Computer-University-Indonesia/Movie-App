from flask import Blueprint
import src.models.Gendre as Gendre
import src.utils.response as response
GenreApp = Blueprint('GenreApp', __name__)


@GenreApp.route('/gendres')
def index():
  try:
    gendres = Gendre.getAllGendre().to_list()
    return response.success( gendres)
  except  Exception as e:
    return response.error( e.args[0])
