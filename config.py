class Config:
    SECRET_KEY = '***'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '***'
    MYSQL_USER = '***'
    MYSQL_PASSWORD = '***'
    MYSQL_DB = '***'
    MYSQL_PORT = ***

config = {
    'development': DevelopmentConfig
}
