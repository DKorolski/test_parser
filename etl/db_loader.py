import sqlite3
import os
import datetime
from etl.processor_gismeteo import get_processed_data


def upload_db(path, data):
    """create database (sql lite), define db schema and 
    process data manipulation (dml)
    """
    connection = sqlite3.connect(path+'/gismeteo_data.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                observation_date TEXT,
                observation_time TEXT,
                feels_like_temp INTEGER,
                process_sk INTEGER,
                created_dttm FLOAT
                )''')
    process_sk = os.getpid()
    created_dttm = datetime.datetime.now().timestamp()
    values_df=get_processed_data(data)
    connection.commit()
    cursor.execute(
            """
                insert into weather(
                    observation_date,
                    observation_time,
                    feels_like_temp,
                    process_sk,
                    created_dttm
                ) values (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                )""", (
                    values_df['date'][0],
                    values_df['time'][0],
                    values_df['temp'][0],
                    process_sk,
                    created_dttm
                )
        )       
    connection.commit()
    connection.close()
    print("end processing row")

