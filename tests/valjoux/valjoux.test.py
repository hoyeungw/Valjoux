import time

from valjoux import Eta


def test():
    eta = Eta(log=True)
    eta.ini('begin')
    time.sleep(0.4)
    eta.lap('slept')
    time.sleep(1.6)
    eta.end('finale')


test()
