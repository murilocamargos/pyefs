# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: TBD

__all__ = [
    'TriMF',
]

class TriMF:
    """Triangular membership function.

    Parameters
    ----------
    p1 : float
        First parameter to control the triangular shape.

    p2 : float
        Second parameter to control the triangular shape.

    p3 : float
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
    def __init__(self, p1: float, p2: float, p3: float):
        p = sorted([p1, p2, p3])
        self.a_ = p[0]
        self.b_ = p[1]
        self.c_ = p[2]

    def get_params(self):
        """Get the triangular form's parameters.

        Returns
        -------
        params : tuple(float, float, float)
            Ordered triangular three parameters (a,b,c).
        """
        params = (self.a_, self.b_, self.c_)
        return params