from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db
from info import models
# 通过指定的配置名字创建对应的app
from info.models import User

app = create_app("default_config")
manager = Manager(app)

# 将app与db进行关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


# @app.route('/')
# def index():
#     # session['name'] = 'itcast'
#
#     logging.debug('test for debug 999')
#     logging.warning('test for debug 888')
#     logging.error('test for debug 777')
#     logging.fatal('test for debug 666')
#     current_app.logger.error("test eeror  hghjgjh")
#     return 'index page 666'
#     # return render()
#     # return render_to_response()

@manager.option('-n', '-name', dest="name")
@manager.option('-p', '-password', dest="password")
def createsuperuser(name, password):
    if not all([name, password]):
        print("参数不足")

    user = User()
    user.nick_name = name
    user.mobile = name
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    print("添加成功")

if __name__ == '__main__':
    # print(app.url_map)
    manager.run()

