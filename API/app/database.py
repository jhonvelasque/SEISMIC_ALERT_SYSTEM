from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from telegram import Bot
import pymysql

DB_HOST = 'database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com'
DB_USER = 'luis'
DB_PASSWORD = '1234'
DB_NAME = 'alertasSismicas'


def conectar_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conectar_db)

Base = declarative_base()