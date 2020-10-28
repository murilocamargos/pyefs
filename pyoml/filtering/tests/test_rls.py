# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

import pytest
import numpy as np
from ..rls import RLS


def test_rls_start():
    # Test RLS start parameters
    rls = RLS(filter_order=5, forgetting_factor=0.999, wscm_factor=1e3)
    params = rls.get_params()
    assert params[:3] == (5, 0.999, 1e3)
    assert (params[3] == 1e3*np.eye(5)).all()
    assert (params[4] == np.zeros((5, 1))).all()


def test_rls_start_with_param_errors():
    # Test RLS start parameters with errors
    with pytest.raises(TypeError) as err:
        _ = RLS(filter_order=5.0, forgetting_factor=0.999, wscm_factor=1e3)
    assert str(err.value) == 'The filter order must be an integer.'

    with pytest.raises(TypeError) as err:
        _ = RLS(filter_order=5, forgetting_factor='0.99', wscm_factor=1e3)
    assert str(err.value) == 'The forgetting factor must be a number.'

    with pytest.raises(TypeError) as err:
        _ = RLS(filter_order=5, forgetting_factor=0.99, wscm_factor='1e3')
    assert str(err.value) == 'The weighted sample covariance matrix factor'\
                             ' must be a number.'

    with pytest.raises(ValueError) as err:
        _ = RLS(filter_order=0, forgetting_factor=0.99, wscm_factor=1e3)
    assert str(err.value) == 'The filter order must be positive.'

    with pytest.raises(ValueError) as err:
        _ = RLS(filter_order=1, forgetting_factor=0, wscm_factor=1e3)
    assert str(err.value) == 'The forgetting error must be in (0,1].'

    with pytest.raises(ValueError) as err:
        _ = RLS(filter_order=1, forgetting_factor=1, wscm_factor=0.9)
    assert str(err.value) == 'The weighted sample covariance matrix factor'\
                             ' must be greater or equal to 1.'


def test_rls_fit_online():
    rls = RLS(filter_order=5, forgetting_factor=0.999, wscm_factor=1e3)

    with pytest.raises(TypeError) as err:
        rls.fit(10, 1)
    assert str(err.value) == 'The input vector must be a column numpy array'\
                             ' with dimensions 5x1.'

    with pytest.raises(ValueError) as err:
        rls.fit(np.array([1, 2, 3]), 1)
    assert str(err.value) == 'The input vector must be a column numpy array'\
                             ' with dimensions 5x1.'

    with pytest.raises(TypeError) as err:
        rls.fit(np.array([1, 2, 3, 4, 5]).reshape((5, 1)), '1')
    assert str(err.value) == 'The output must be numeric.'

    rls.fit(np.array([1, 2, 3, 4, 5]).reshape((5, 1)), 1)
    assert (rls.weights_ != np.zeros((5, 1))).all()
