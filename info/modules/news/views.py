from flask import render_template, session, current_app

from info.models import User
from . import news_blu


@news_blu.route("/<int:news_id>")
def news_detail(news_id):
    user_id = session.get("user_id", None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)


    data = {
        "user": user.to_dict() if user else None
    }
    return render_template("news/detail.html", data=data)