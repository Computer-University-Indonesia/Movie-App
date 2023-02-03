from flask import Blueprint
import src.models.Country as Country 
import src.utils.response as response
CountryApp = Blueprint('CountryApp', __name__)


@CountryApp.route('/countries')
def index():
  try:
    return response.success(Country.getAllCountry().to_list())
  except Exception as e:
    return response.error(e.args[0])
