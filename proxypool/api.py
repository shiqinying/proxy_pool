from flask import Flask, g

from proxypool.db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    conn = get_conn()
    return '<h2>Welcome to Proxy Pool System</h2>'+ '<h3>代理总数量：' + str(conn.count()) + '</h3>' + '<h3>满分代理数量：' + str(conn.count_100()) + '</h3>' + '<p><a href="/random">获取随机代理<a/></p>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())

@app.route('/all')
def get_all():
    """
    獲取所有代理
    :return:
    """

    conn = get_conn()
    proxy_list = conn.all()
    proxy_list = '\n'.join(proxy_list)
    return proxy_list


if __name__ == '__main__':
    app.run()
