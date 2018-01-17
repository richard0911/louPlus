


class BaseConfig(object):
    SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:xz910815@localhost:3306/simpledu?charset=utf8'
    INDEX_PER_PAGE = 15

configs = {
    'development': DevelopmentConfig
}
