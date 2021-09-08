from pyspare.deco import deco_crostab
from texting import LF

from valjoux import strategies


# from pys

def test():
    lapse_result = strategies(
        repeat=int(3.0E+6),
        candidates={
            'alpha': 'st. petersburg',
            'beta': 'bar'
        },
        methods={
            'arch': lambda x: len(x),
            'dev': len
        },
        show_params=True
    )
    print('lapse', LF + deco_crostab(lapse_result.lapse))
    print('result', LF + deco_crostab(lapse_result.result))


test()
