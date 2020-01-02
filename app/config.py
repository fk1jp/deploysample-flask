import os

class DBConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pass}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.environ['MYSQL_USER'],
        'pass': os.environ['MYSQL_PASS'],
        'host': os.environ['MYSQL_HOST'],
        'database': os.environ['MYSQL_DATABASE'],
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DBConfig
