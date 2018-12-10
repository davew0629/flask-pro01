from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

class Config(object):
    # 项目的配置
    DEBUG = True
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_MODIFICATIONS = False






app = Flask(__name__)
# 加载配置
app.config.from_object(Config)


# 初始化数据库
db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'index page'

if __name__ == '__main__':
    app.run(debug=True)