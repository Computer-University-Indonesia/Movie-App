from dotenv import dotenv_values
env = dotenv_values(".env")
BASE_URL = env["BASE_URL"] or "http://localhost"
PORT= env['PORT'] or 5000
DEBUG= env['DEBUG'] or True

SHAPEFILE = env['SHAPEFILE'] 
SCRAPING_URL = env['SCRAPING_URL'] 

