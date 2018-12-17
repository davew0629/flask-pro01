# 新闻详情模块的蓝图
from flask import Blueprint


news_blu = Blueprint("news", __name__, url_prefix="/new")

from . import views

