from flask import session

from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand


# from .info import app, db

from info import app, db

manager = Manager(app)

# 将app与db进行关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@info.app.route('/')
def index():
    session['name'] = 'itcast'

    return 'index page 555'


if __name__ == '__main__':

    manager.run()

