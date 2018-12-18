from flask import render_template, session, current_app, abort, g

from info import constants
from info.models import User, News
from info.utils.common import user_login_data
from . import news_blu


@news_blu.route("/<int:news_id>")
@user_login_data
def news_detail(news_id):

    # 查询用户登陆信息
    # user = query_user_data()
    user = g.user

    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    news_dict_li = []
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    news = None
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)

    if not news:
        abort(404)

    news.clicks += 1

    data = {
        "news": news.to_dict(),
        "user": user.to_dict() if user else None,
        "news_dict_li": news_dict_li
    }
    return render_template("news/detail.html", data=data)