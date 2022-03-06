from etl.web_extract_gismeteo import weather_data
from etl.processor_gismeteo import get_processed_data
from etl.db_loader import upload_db
import os


"""get feels like weather (температура по ощущениям)
    url --  www.gismeteo.com and city
    https://www.gismeteo.ru/weather-sankt-peterburg-4079/
    parser retrives the current temperture of feels like temp 
    from servive any time each lunched and stores data to database
    """
url='https://www.gismeteo.ru/weather-sankt-peterburg-4079/'
data=weather_data(url)
cwd_path = os.path.dirname(__file__)
upload_db(cwd_path, data)
