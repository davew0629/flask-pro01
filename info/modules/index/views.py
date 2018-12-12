

from .. import index_blu




@index_blu.route('/index')
def index():
    # session['name'] = 'itcast'

    # logging.debug('test for debug 999')
    # logging.warning('test for debug 888')
    # logging.error('test for debug 777')
    # logging.fatal('test for debug 666')
    # current_app.logger.error("test eeror  hghjgjh")

    # return render()
    # return render_to_response()
    return 'index page 666'