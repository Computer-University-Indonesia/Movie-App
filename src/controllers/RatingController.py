from flask import Blueprint,request
import src.models.Rating as Rating
import src.utils.response as response
RatingApp = Blueprint('RatingApp', __name__)


@RatingApp.route('/ratings')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    ratings = Rating.getAllRating()
    if (key != None and value != None):
      ratings = Rating.getRatingFiltered(key, value)
    return response.success(ratings.to_list())
  except Exception as e:
    return response.error(e.args[0])


@RatingApp.route('/ratings/grafik')
def grafik():
  try:
    ratings = Rating.getRatingWithAllAttributes()
    return response.success(ratings.to_dict(orient='records'))
  except Exception as e:
    return response.error(e.args[0])