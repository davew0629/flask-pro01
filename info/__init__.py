from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from config import config
import logging
# 原来指定session的存储位置(数据库类型)
from flask_session import Session


# flask扩展中可以先初始化扩展的对象，再去调用init——app方法初始化
db = SQLAlchemy()


def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG) # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)





# 类似与工厂方法
def create_app(config_name):
    setup_log(config_name)

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
