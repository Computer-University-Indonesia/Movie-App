from flask import Blueprint, jsonify
import src.models.Cast as Cast
import src.utils.response as response
CastApp = Blueprint('CastApp', __name__)

@CastApp.route('/casts')
def index():
  try:
    return response.success(Cast.getAllCast().to_list())
  except Exception as e:
    return response.error(e.args[0])
