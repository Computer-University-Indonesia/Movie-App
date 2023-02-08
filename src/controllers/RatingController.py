from flask import Blueprint,request
import src.models.Rating as Rating
import src.utils.response as response
RatingApp = Blueprint('RatingApp', __name__)


@RatingApp.route('/ratings')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    ratings = Rating.getAllRating().to_list()
    if (key != None and value != None):
      ratings_filtered = Rating.getRatingFiltered(key, value)
      ratings_renamed = ratings_filtered.rename(columns={0:'count'})
      ratings = ratings_renamed.to_dict(orient='records')
    return response.success(ratings)
  except Exception as e:
    return response.error(e.args[0])


@RatingApp.route('/ratings/grafik')
def grafik():
  try:
    ratings = Rating.getRatingWithAllAttributes()
    return response.success(ratings.to_dict(orient='records'))
  except Exception as e:
    return response.error(e.args[0])