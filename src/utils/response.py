
def success(data):
  return {
    'status_code': 200,
    'message': 'success',
    'data': data
  }
   
def error(message):
    return {
      'status_code': 400,
      'message': message,
      'data': None
    }
