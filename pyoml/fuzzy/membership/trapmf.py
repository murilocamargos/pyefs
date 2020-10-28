# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

import numpy as np
from .base import MF, NumericType, ParamsType


class TrapMF(MF):
    """Trapezoidal membership function.

    Parameters
    ----------
    a : NumericType
        First parameter to control the trapzoidal shape.

    b : NumericType
        Second parameter to control the trapzoidal shape.

    c : NumericType
        Third parameter to control the trapzoidal shape.

    d : NumericType
        Fourth parameter to control the trapzoidal shape.

    Attributes
    ----------
    a_ : NumericType
        Trapezoidal shape lower bound.

    b_ : NumericType
        Trapezoidal shape first mid point.

    c_ : NumericType
        Trapezoidal shape second mid point.

    d_ : NumericType
        Trapezoidal shape upper bound.

    Examples
    --------
    >>> from pyoml.fuzzy.membership import TrapMF
    >>> mf = TrapMF(0,1,2,3)
    """
    def __init__(self, a: NumericType, b: NumericType, c: NumericType,
                 d: NumericType, check_order=True):
        super().__init__((a, b, c, d))

        if check_order and not a <= b <= c <= d:
            raise ValueError('The parameters must be specified such that'
                             ' a <= b <= c <= d.')

        self.a_ = a
        self.b_ = b
        self.c_ = c
        self.d_ = d

    def get_params(self) -> ParamsType:
        """Get the trapezoidal form's parameters.

        Returns
        -------
        params : ParamsType
            Ordered trapezoidal four parameters (a,b,c,d).
        """
        params = (self.a_, self.b_, self.c_, self.d_)
        return params

    def get_degree(self, x: NumericType) -> NumericType:
        """Get the membership degree of a float value `x` for
        the trapezoidal MF.

        Parameters
        ----------
        x : NumericType
            Input data for which the membership degree will be
            computed.

        Returns
        -------
        degree : NumericType
            The membership degree for the input `x`. The value
            is in [0, 1].
        """
        mn = np.minimum
        mx = np.maximum
        degree = mx(mn(mn((x - self.a_)/(self.b_ - self.a_),
                          (self.d_ - x)/(self.d_ - self.c_)), 1), 0)
        return degree
