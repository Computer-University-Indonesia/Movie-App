from flask import Blueprint
import src.models.Gendre as Gendre
import src.utils.response as response
GenreApp = Blueprint('GenreApp', __name__)


@GenreApp.route('/gendres')
def index():
  try:
    return response.success( Gendre.getAllGendre().to_list())
  except  Exception as e:
    return response.error( e.args[0])
