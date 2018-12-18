from flask import render_template, session, current_app, abort, g, jsonify, request
from info import constants
from info.models import User, News
from info.utils.common import user_login_data
from info.utils.response_code import RET
from . import news_blu


@news_blu.route("/<int:news_id>")
@user_login_data
def news_detail(news_id):
    print('准备制作news_detail/news_id的返回页面')

    # 定义变量作为是否收藏的标记
    is_collected = False

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

    # 查询新闻数据，通过news_id
    news = None
    try:
        news = News.query.get(news_id)
        print(news)
    except Exception as e:
        current_app.logger.error(e)

    if not news:
        # 返回404页面
        abort(404)

    # 更新新闻的点击次数
    news.clicks += 1

    if user:
        # sqlalchemy会在使用的时候自动加载
        if news in user.collection_news:
            is_collected = True

    data = {
        "news": news.to_dict(),
        "user": user.to_dict() if user else None,
        "news_dict_li": news_dict_li,
        "is_collected": is_collected
    }
    print("准备返回news_detail/news_id页面")
    print(news)
    return render_template("news/detail.html", data=data)


@news_blu.route("/news_collect", methods=['POST'])
@user_login_data
def collect_news():
    print("准备调用collect_news收藏方法")
    user = g.user
    if not user:
        # 用户不是登录状态
        return jsonify(errno=RET.SESSIONERR, errmsg="用户未登陆")

    news_id = request.json.get("news_id")
    action = request.json.get("action")

    if not all([news_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    if action not in ["collect","cancel_collect"]:
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误，事件不在列表")

    try:
        news_id = int(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误，news_id错误")

    try:
        news = News.query.get(news_id)
    except Exception as e:
        return jsonify(errno=RET.DBERR, errmsg="数据库查询news错误")

    if not news:
        return jsonify(errno=RET.NODATA, errmsg="未查询到news数据")

    if action == "cancel_collect":
        #
        if news in user.collection_news:
            user.collection_news.remove(news)
    else:
        if news not in user.collection_news:
            user.collection_news.append(news)

    print("操作成功")
    return jsonify(errno=RET.OK, errmsg="收藏操作成功！")
