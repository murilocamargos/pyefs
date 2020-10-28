# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

from ..rls import RLS


def test_rls_start():
    # Test RLS start parameters
    rls = RLS(p=5, lbda=1, delta=1e5)
    assert rls.get_params() == (5, 1, 1e5)
