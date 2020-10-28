# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

from ..rls import RLS


def test_rls_start():
    # Test RLS start parameters
    rls = RLS(filter_order=5, forgetting_factor=0.999, wscm_factor=1e3)
    assert rls.get_params() == (5, 0.999, 1e3)
