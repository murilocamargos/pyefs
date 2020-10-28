# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT
import numpy as np

from ..base import NumericType, NumParamsType


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

        # Check parameters' types
        if type(filter_order) != int:
            raise TypeError('The filter order must be an integer.')

        if not type(forgetting_factor) in [int, float]:
            raise TypeError('The forgetting factor must be a number.')

        if not type(wscm_factor) in [int, float]:
            raise TypeError('The weighted sample covariance matrix factor'
                            ' must be a number.')

        # Check parameters' values
        if filter_order < 1:
            raise ValueError('The filter order must be positive.')

        if not 0 < forgetting_factor <= 1:
            raise ValueError('The forgetting error must be in (0,1].')

        if wscm_factor < 1:
            raise ValueError('The weighted sample covariance matrix factor'
                             ' must be greater or equal to 1.')

        # Set parameters
        self.filter_order_ = filter_order
        self.forgetting_factor_ = forgetting_factor
        self.wscm_factor_ = wscm_factor
        self.wscm_ = wscm_factor * np.eye(filter_order)
        self.weights_ = np.zeros((filter_order, 1))

    def get_params(self) -> NumParamsType:
        """Get the RLS filter parameters.

        Returns
        -------
        params : NumParamsType
            RLS filter parameters: filter_order, forgetting_factor,
            wscm_factor.
        """
        params = (self.filter_order_, self.forgetting_factor_,
                  self.wscm_factor_, self.wscm_, self.weights_)
        return params

    def fit(self, x: np.ndarray, y: NumericType):
        """Adapt the filters parameters with new input.

        Parameters
        ----------
        x : np.ndarray [filter_order_ x 1]
            The input vector for adapting the RLS parameters.

        y : NumericType
            The output associated with the input `x`.
        """
        error_msg = "The input vector must be a column numpy array"\
                    f" with dimensions {self.filter_order_}x1."

        if type(x) != np.ndarray:
            raise TypeError(error_msg)

        if x.shape != (self.filter_order_, 1):
            raise ValueError(error_msg)

        if not type(y) in [int, float]:
            raise TypeError('The output must be numeric.')

        lbd = self.forgetting_factor_
        lbd_inv = 1/lbd

        alpha = y - np.dot(x.T, self.weights_)
        g = np.dot(np.dot(self.wscm_, x), np.linalg.inv(
            lbd + np.dot(np.dot(x.T, self.wscm_), x)))
        self.wscm_ = lbd_inv*self.wscm_ - np.dot(np.dot(np.dot(
            g, x.T), lbd_inv), self.wscm_)
        self.weights_ += alpha*g
