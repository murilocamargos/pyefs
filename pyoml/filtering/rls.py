# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

from typing import Union, Tuple

NumericType = Union[int, float]
ParamsType = Tuple[NumericType, ...]


class RLS:
    """Recursive Least Squares adaptive filter.

    Parameters
    ----------
    filter_order : int
        The number of most recent samples that will be used as regressors.
        It must be positive, i.e., greater than 0.

    forgetting_factor : NumericType (default: 1)
        A forgetting factor that gives exponentially less weight to older
        error samples. It must within (0,1].
        When equal to 1, no sample gets "forgotten".

    wscm_factor : NumericType (default: 1e5)
        Weighted sample covariance matrix initial value.

    Attributes
    ----------
    filter_order_ : int
        Filter's order.

    forgetting_factor_ : NumericType
        Filter's forgetting factor.

    wscm_factor_ : NumericType
        Filter's Weighted sample covariance matrix factor.

    Examples
    --------
    >>> from pyoml.filtering import RLS
    >>> rls = RLS(4, 0.99)
    """
    def __init__(self, filter_order: int, forgetting_factor: NumericType = 1,
                 wscm_factor: NumericType = 1e5):
        self.filter_order_ = filter_order
        self.forgetting_factor_ = forgetting_factor
        self.wscm_factor_ = wscm_factor

    def get_params(self) -> ParamsType:
        """Get the RLS filter parameters.

        Returns
        -------
        params : ParamsType
            RLS filter parameters: filter_order, forgetting_factor,
            wscm_factor.
        """
        params = (self.filter_order_, self.forgetting_factor_,
                  self.wscm_factor_)
        return params
