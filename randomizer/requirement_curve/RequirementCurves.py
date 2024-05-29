from ..Utility import squircle, invert_squircle

from . import ReqCurve
from . import RequirementCurve

_REQUIREMENT_CURVES = {
    ReqCurve.Concave: RequirementCurve(lambda num: round(squircle(num/20, 1.5)*100)),
    ReqCurve.Linear: RequirementCurve(lambda num: round(num*5)),
    ReqCurve.Domed: RequirementCurve(lambda num: round(invert_squircle(num/20, 1.5)*100))
}

def get_curve(index : int) -> RequirementCurve:
    return _REQUIREMENT_CURVES[ReqCurve(index)]