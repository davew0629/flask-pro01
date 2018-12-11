from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from config import config

# 原来指定session的存储位置(数据库类型)
from flask_session import Session


# flask扩展中可以先初始化扩展的对象，再去调用init——app方法初始化
db = SQLAlchemy()


# 类似与工厂方法
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config["development"])

    # db = SQLAlchemy(app)

    db.init_app(app)

    # 初始化redis存储对象

    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 开启当前项目CSRF保护,只做服务器验证
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    return app
