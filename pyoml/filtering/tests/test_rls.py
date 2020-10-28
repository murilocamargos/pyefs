# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

import numpy as np
from ..rls import RLS


def test_rls_start():
    # Test RLS start parameters
    rls = RLS(filter_order=5, forgetting_factor=0.999, wscm_factor=1e3)
    params = rls.get_params()
    assert params[:3] == (5, 0.999, 1e3)
    assert (params[3] == 1e3*np.eye(5)).all()
    assert (params[4] == np.zeros((5,1))).all()
