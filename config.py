class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'erick.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'erick'
    MYSQL_PASSWORD = 'zokater123'
    MYSQL_DB = 'erick$actividades'
    MYSQL_PORT = 3306

config = {
    'development': DevelopmentConfig
}