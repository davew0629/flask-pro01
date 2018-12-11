from flask import session, current_app
import logging
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from info import create_app, db

# 通过指定的配置名字创建对应的app
app = create_app("development")
manager = Manager(app)

# 将app与db进行关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    # session['name'] = 'itcast'

    logging.debug('test for debug 999')
    logging.warning('test for debug 888')
    logging.error('test for debug 777')
    logging.fatal('test for debug 666')
    current_app.logger.error("test eeror  hghjgjh")
    return 'index page 666'


if __name__ == '__main__':

    manager.run()

