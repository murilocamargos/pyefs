# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

from .base import NumericType, ParamsType
from .trapmf import TrapMF


class TriMF(TrapMF):
    """Triangular membership function.

    Parameters
    ----------
    a : NumericType
        First parameter to control the triangular shape.

    b : NumericType
        Second parameter to control the triangular shape.

    c : NumericType
        Third parameter to control the triangular shape.

    Attributes
    ----------
    a_ : NumericType
        Triangular shape lower bound.

    b_ : NumericType
        Triangular shape mid point.

    c_ : NumericType
        Triangular shape upper bound.
    
    Examples
    --------
    >>> from pyoml.fuzzy.membership import TriMF
    >>> mf = TriMF(0,1,2)
    """
    def __init__(self, a: NumericType, b: NumericType, c: NumericType):
        super().__init__(a, b, b, c, False)

        if not a <= b <= c:
            raise ValueError('The parameters must be specified such that a <= b <= c.')

    def get_params(self) -> ParamsType:
        """Get the triangular form's parameters.

        Returns
        -------
        params : ParamsType
            Ordered triangular three parameters (a,b,c).
        """
        params = (self.a_, self.b_, self.d_)
        return params
