import requests
from bs4 import BeautifulSoup


def weather_data(url):
    """get feels like weather (температура по ощущениям)
    url --  www.gismeteo.com and city
    https://www.gismeteo.ru/weather-sankt-peterburg-4079/
    """
    return _handler_html(url)


def _get_html(url):
    """get html of requested url
    """
    response = requests.get(url, headers={"User-Agent": "Firefox/67.0.4"})

    return response.text


def _handler_html(url):
    """html handler
    """
    soup = BeautifulSoup(_get_html(url), 'lxml')
    divs = soup.find(
                    'div', 
                    {'class': 'content-column column1'}
                ).find(
                    'div', 
                    {'class': 'weathertab-wrap'}
                ).find(
                    'div', 
                    {'class': 'tab-content'}
                )
    
    return _get_data(divs)
    

def _get_data(divs):
    """get time and temperature
    """
    current_time = _get_time(divs)
    current_temp = _get_temp(divs)

    data = [
        [
            current_time.text,
            current_temp.find('span').contents[0].text,
        ]
    ]

    return data


def _get_time(divs):
    """get current time
    """
    return divs.find(
                    'div', 
                    {'class': 'day'}
                )


def _get_temp(divs):
    """get current temp
    """
    return divs.find(
                    'div', 
                    {'class': 'weather'}
                ).find(
                    'div', 
                    {'class': 'weather-feel'}
                )