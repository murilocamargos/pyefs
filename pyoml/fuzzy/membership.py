# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT
from typing import Union, Tuple

NumericType = Union[int, float]

__all__ = [
    'TriMF',
    'TrapMF',
]

class MF:
    """General membership function.

    Parameters
    ----------
    params : tuple of ints or floats
        A tuple with all the MF parameters.
    """
    def __init__(self, params: Tuple[NumericType]):
        self._check_num_type(params)
    
    def _check_num_type(self, params: Tuple[NumericType]) -> None:
        """Check if the each param in `params` is numeric [int, float].
        
        Parameters
        ----------
        params : tuple of ints or floats
            A tuple with all the MF parameters.
        """
        for p in params:
            if type(p) not in [int, float]:
                raise TypeError('All parameters must be numeric.')
    
    def get_params(self) -> Tuple[NumericType]:
        """Get the MF parameters."""
        raise NotImplementedError('The `get_params` method must be implemented')
    
    def get_degree(self, x: NumericType) -> NumericType:
        """Get the membership degree of a float value `x` for
        the MF.
        """
        raise NotImplementedError('The `get_degree` method must be implemented')


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
    def __init__(self, a: NumericType, b: NumericType, c: NumericType,\
        d: NumericType, check_order=True):
        super().__init__((a, b, c, d))

        if check_order and not a <= b <= c <= d:
            raise ValueError('The parameters must be specified such that a <= b <= c <= d.')
        
        self.a_ = a
        self.b_ = b
        self.c_ = c
        self.d_ = d
    
    def get_params(self) -> Tuple[NumericType]:
        """Get the trapezoidal form's parameters.

        Returns
        -------
        params : Tuple[NumericType, NumericType, NumericType, NumericType]
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
        degree = max(min(min((x - self.a_)/(self.b_ - self.a_),\
            (self.d_ - x)/(self.d_ - self.c_)), 1), 0)
        return degree


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

    def get_params(self) -> Tuple[NumericType]:
        """Get the triangular form's parameters.

        Returns
        -------
        params : Tuple[NumericType, NumericType, NumericType]
            Ordered triangular three parameters (a,b,c).
        """
        params = (self.a_, self.b_, self.d_)
        return params
