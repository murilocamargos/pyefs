# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT
from typing import Union


__all__ = [
    'TriMF',
]

class TriMF:
    """Triangular membership function.

    Parameters
    ----------
    a : float
        First parameter to control the triangular shape.

    b : float
        Second parameter to control the triangular shape.

    c : float
        Third parameter to control the triangular shape.

    Attributes
    ----------
    a_ : float
        Triangular shape lower bound.

    b_ : float
        Triangular shape mid point.

    c_ : float
        Triangular shape upper bound.
    
    Examples
    --------
    >>> from pyoml.fuzzy.membership import TriMF
    >>> mf = TriMF(0,1,2)
    """
    def __init__(self, a: Union[int, float], b: Union[int, float],\
        c: Union[int, float]):

        self._check_num_type((a, b, c))

        if not a <= b <= c:
            raise ValueError('The parameters must be specified such that a <= b <= c.')
        
        self.a_ = a
        self.b_ = b
        self.c_ = c

    def _check_num_type(self, params: tuple) -> None:
        """Check if the each param in `params` is numeric [int, float].
        
        Parameters
        ----------
        params : tuple of ints or floats
            A tuple with all the MF parameters.
        """
        for p in params:
            if type(p) not in [int, float]:
                raise TypeError('All parameters must be numeric.')

    def get_params(self):
        """Get the triangular form's parameters.

        Returns
        -------
        params : tuple(float, float, float)
            Ordered triangular three parameters (a,b,c).
        """
        params = (self.a_, self.b_, self.c_)
        return params
    
    def get_degree(self, x: float):
        """Get the membership degree of a float value `x` for
        the triangular MF.

        Parameters
        ----------
        x : float
            Input data for which the membership degree will be
            computed.
        
        Returns
        -------
        degree : float 
            The membership degree for the input `x`. The value
            is in [0, 1].
        """
        degree = max(min((x - self.a_)/(self.b_ - self.a_),\
            (self.c_ - x)/(self.c_ - self.b_)), 0)
        return degree