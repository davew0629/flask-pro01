from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask.ext.wtf import CSRFProtect

class Config(object):
    # 项目的配置
    DEBUG = True
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379





app = Flask(__name__)
# 加载配置
app.config.from_object(Config)


# 初始化数据库
db = SQLAlchemy(app)

# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启当前项目CSRF保护,只做服务器验证
CSRFProtect(app)









@app.route('/')
def index():
    return 'index page'

if __name__ == '__main__':
    app.run(debug=True)