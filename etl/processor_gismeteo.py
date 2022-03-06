import pandas as pd
from datetime import date
from etl.web_extract_gismeteo import weather_data


def get_processed_data (data):
    """get processed data retrieved from html
    """
    return _processor (data)


def _processor (data):
    """separate and replace unusual space character from string
    """
    current_date = date.today()
    current_time = data[0][0]
    current_temp = data[0][1].replace(' ','')
    list_obj = {'date': current_date, 'time': current_time, 'temp': current_temp}
    df = pd.DataFrame(list_obj,  index=[0])
    return df