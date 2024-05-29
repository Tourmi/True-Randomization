from typing import Callable

class RequirementCurve:
    def __init__(self, curve_func : Callable[[int], int]):
        self._curve_func = curve_func
    
    def __call__(self, num : int) -> int:
        return self._curve_func(num)

