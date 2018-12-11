from redis import StrictRedis



class Config(object):
    # 项目的配置
    DEBUG = True

    SECRET_KEY = 'afLWSqolE06SiU0a2skKntN3q1LZBWcxVQdN2kv+6W3OazEpu8tnwk0WALKFJDir'
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"
    # 开启session签名
    # SESSION_USE_SIGNER = True
    # 指定session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class DevelopmentConfig(Config):
    # 开发环境配置
    DEBUG = True


class ProductionConfig(Config):
    # 生产环境配置
    DEBUG = False


class TestingConfig(Config):
    # 单元测试环境配置
    DEBUG = True
    TESTING = True

# 定义配置字典
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
