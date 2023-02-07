from flask import Blueprint, request
import src.models.Country as Country 
import src.utils.response as response
CountryApp = Blueprint('CountryApp', __name__)


@CountryApp.route('/countries')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    if key != None and value != None:
      return response.success(Country.getCountryFiltered(key, value).to_dict(orient='records'))
    return response.success(Country.getAllCountry().to_dict(orient='records'))
  except Exception as e:
    return response.error(e.args[0])

@CountryApp.route('/countries/grafik')
def grafik():
  try:
    country = Country.getCountryWithAllAttributes()
    return response.success(country)
  except Exception as e:
    return response.error(e.args[0])