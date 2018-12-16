from flask import render_template, current_app, session

from info import redis_store
from info.models import User
from . import index_blu




@index_blu.route('/')
def index():
    # session['name'] = 'itcast'

    # logging.debug('test for debug 999')
    # logging.warning('test for debug 888')
    # logging.error('test for debug 777')
    # logging.fatal('test for debug 666')
    # current_app.logger.error("test eeror  hghjgjh")

    # return render()
    # return render_to_response()
    # redis_store.set("name", "itcast")  # 在redis中保存一个值 name itcast
    # return 'index page 666'

    # 如果用户已经登录，将当前登录用户的数据传到模板中显示

    user_id = session.get('user_id', None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    data = {
        "user": user.to_dict() if user else None
    }

    return render_template('news/index.html', data=data)


@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')