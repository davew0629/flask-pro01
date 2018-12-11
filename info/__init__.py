from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect

from config import Config

# 原来指定session的存储位置(数据库类型)
from flask_session import Session

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

db.init_app(app)

# 初始化redis存储对象

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启当前项目CSRF保护,只做服务器验证
CSRFProtect(app)
# 设置session保存指定位置
Session(app)
