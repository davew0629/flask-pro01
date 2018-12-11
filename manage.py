from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
# 原来指定session的存储位置(数据库类型)
from flask_session import Session




class Config(object):
    # 项目的配置
    DEBUG = True

    SECRET_KEY = ''
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
    PERMANENT_SESSION_LIFETIME = 86400*2



app = Flask(__name__)
# 加载配置
app.config.from_object(Config)


# 初始化数据库
db = SQLAlchemy(app)

# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启当前项目CSRF保护,只做服务器验证
CSRFProtect(app)
# 设置session保存指定位置
Session(app)


@app.route('/')
def index():
    session['name'] = 'itcast'

    return 'index page'


if __name__ == '__main__':
    app.run(debug=True)