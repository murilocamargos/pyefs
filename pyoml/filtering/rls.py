# Authors: Murilo Camargos <murilo.camargosf@gmail.com>
# License: MIT

from typing import Union, Tuple

NumericType = Union[int, float]
ParamsType = Tuple[NumericType, ...]


class RLS:
    def __init__(self, p: int, lbda: NumericType, delta: NumericType):
        self.p_ = p
        self.lbda_ = lbda
        self.delta_ = delta