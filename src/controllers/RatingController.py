from flask import Blueprint
import src.models.Rating as Rating
import src.utils.response as response
RatingApp = Blueprint('RatingApp', __name__)


@RatingApp.route('/ratings')
def index():
  try:
    return response.success(Rating.getAllRating().to_list())
  except Exception as e:
    return response.error(e.args[0])
