#!/usr/bin/python3

import requests
import json
import socket
import time
import pymysql
import datetime

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def setupDB():
    print("Connecting DB")
    try:
        global Base
        Base = automap_base()
        engine = create_engine("mysql+pymysql://root:root@db/info_db")
        Base.prepare(engine, reflect=True)
    except SQLAlchemyError as e:
        raise Exception(e)
    finally:
        return Session(engine)

def insertData(session,data):
    print("Inserting to DB")
    Info_table = Base.classes.info_table
    session.add(Info_table(ip=data['ip'],iptype=data['type'],continent_code=data['continent_code'],continent_name=data['continent_name'],country_code=data['country_code'],country_name=data['country_name'],region_code=data['region_code'],region_name=data['region_name'],city=data['city'],zip=data['zip'],latitude=data['latitude'],longitude=data['longitude'],location=data['location']))
    session.commit()


def getData():
    print("Request data.. @" + str(datetime.datetime.now()))
    r = requests.get(url)
    return r.json()


myIP = socket.gethostbyname(socket.gethostname())
myKey = '422d47fb41a0a40f7d592dd80c4380cc'
url = 'http://api.ipstack.com/' + myIP + '?access_key=' + myKey

def main():
    print("Starting app..")
    session = setupDB()
    while True:
        data = getData()
        insertData(session,data) 
        time.sleep(60)


if __name__ == "__main__":
    main()
