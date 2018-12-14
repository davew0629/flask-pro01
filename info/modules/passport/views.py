from flask import request, abort, current_app, make_response

from info import redis_store, constants
from . import passport_blu

from info.utils.captcha.captcha import captcha


@passport_blu.route('/image_code')
def get_image_code():

    # 1 获取参数 url中？后面的参数
    # 2 判断参数是否有值。没有值返回404
    # 3 生成图片验证码  使用三个参数接收
    # 4 保存图片验证码文字内容到redis
    # 5 返回验证码图片，并设置数据类型，以便浏览器识别其类型

    image_code_id = request.args.get("imageCodeId", None)
    if not image_code_id:
        return abort(403)
    name, text, image = captcha.generate_captcha()
    try:
        redis_store.set("ImageCodeId" + image_code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)
    response = make_response(image)
    response.headers["Content-Type"] = "image/jpg"
    return response

