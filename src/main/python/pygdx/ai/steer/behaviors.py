from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.Wander as _Wander
_Wander = _Wander
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as _ReachOrientation
_ReachOrientation = _ReachOrientation
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Wander():
    """com.badlogic.gdx.ai.steer.behaviors.Wander"""
 
    @staticmethod
    def _wrap(java_value: _Wander) -> 'Wander':
        return Wander(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Wander):
        """
        Dynamic initializer for Wander.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Wander__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Wander__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Wander(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Wander(arg0)
        self.__wrapper = val

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setWanderRate(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRate(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderRate(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWanderOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOrientation()"""
        return float._wrap(super(Wander, self).getWanderOrientation())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Wander'._wrap(super(_Wander, self).setLimiter(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setDecelerationRadius(float)"""
        return 'Wander'._wrap(super(_Wander, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def getWanderRate(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRate()"""
        return float._wrap(super(Wander, self).getWanderRate())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getInternalTargetPosition()"""
        return 'math.Vector'._wrap(super(Wander, self).getInternalTargetPosition())

    @overload
    def getWanderOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOffset()"""
        return float._wrap(super(Wander, self).getWanderOffset())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setTarget(self, arg0: 'Location') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Wander'._wrap(super(_Wander, self).setTarget(arg0))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float._wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def setWanderOrientation(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOrientation(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderOrientation(_float.valueOf(arg0)))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Wander'._wrap(super(_Wander, self).setOwner(arg0))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTimeToTarget(float)"""
        return 'Wander'._wrap(super(_Wander, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def getWanderCenter(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderCenter()"""
        return 'math.Vector'._wrap(super(Wander, self).getWanderCenter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float._wrap(super(ReachOrientation, self).getTimeToTarget())

    @overload
    def setWanderRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRadius(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderRadius(_float.valueOf(arg0)))

    @overload
    def isFaceEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Wander.isFaceEnabled()"""
        return bool._wrap(super(Wander, self).isFaceEnabled())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setAlignTolerance(float)"""
        return 'Wander'._wrap(super(_Wander, self).setAlignTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'._wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float._wrap(super(ReachOrientation, self).getAlignTolerance())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getWanderRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRadius()"""
        return float._wrap(super(Wander, self).getWanderRadius())

    @overload
    def setEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setEnabled(boolean)"""
        return 'Wander'._wrap(super(_Wander, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setWanderOffset(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOffset(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderOffset(_float.valueOf(arg0)))

    @overload
    def setFaceEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setFaceEnabled(boolean)"""
        return 'Wander'._wrap(super(_Wander, self).setFaceEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Wander
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.Wander as _Wander
_Wander = _Wander
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as _ReachOrientation
_ReachOrientation = _ReachOrientation
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Wander():
    """com.badlogic.gdx.ai.steer.behaviors.Wander"""
 
    @staticmethod
    def _wrap(java_value: _Wander) -> 'Wander':
        return Wander(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Wander):
        """
        Dynamic initializer for Wander.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Wander__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Wander__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Wander(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Wander(arg0)
        self.__wrapper = val

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setWanderRate(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRate(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderRate(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWanderOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOrientation()"""
        return float._wrap(super(Wander, self).getWanderOrientation())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Wander'._wrap(super(_Wander, self).setLimiter(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setDecelerationRadius(float)"""
        return 'Wander'._wrap(super(_Wander, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def getWanderRate(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRate()"""
        return float._wrap(super(Wander, self).getWanderRate())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getInternalTargetPosition()"""
        return 'math.Vector'._wrap(super(Wander, self).getInternalTargetPosition())

    @overload
    def getWanderOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOffset()"""
        return float._wrap(super(Wander, self).getWanderOffset())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setTarget(self, arg0: 'Location') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Wander'._wrap(super(_Wander, self).setTarget(arg0))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float._wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def setWanderOrientation(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOrientation(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderOrientation(_float.valueOf(arg0)))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Wander'._wrap(super(_Wander, self).setOwner(arg0))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTimeToTarget(float)"""
        return 'Wander'._wrap(super(_Wander, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def getWanderCenter(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderCenter()"""
        return 'math.Vector'._wrap(super(Wander, self).getWanderCenter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float._wrap(super(ReachOrientation, self).getTimeToTarget())

    @overload
    def setWanderRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRadius(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderRadius(_float.valueOf(arg0)))

    @overload
    def isFaceEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Wander.isFaceEnabled()"""
        return bool._wrap(super(Wander, self).isFaceEnabled())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setAlignTolerance(float)"""
        return 'Wander'._wrap(super(_Wander, self).setAlignTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'._wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float._wrap(super(ReachOrientation, self).getAlignTolerance())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getWanderRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRadius()"""
        return float._wrap(super(Wander, self).getWanderRadius())

    @overload
    def setEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setEnabled(boolean)"""
        return 'Wander'._wrap(super(_Wander, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setWanderOffset(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOffset(float)"""
        return 'Wander'._wrap(super(_Wander, self).setWanderOffset(_float.valueOf(arg0)))

    @overload
    def setFaceEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setFaceEnabled(boolean)"""
        return 'Wander'._wrap(super(_Wander, self).setFaceEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Wander 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Flee
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.behaviors.Seek as _Seek
_Seek = _Seek
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.behaviors.Flee as _Flee
_Flee = _Flee
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Flee():
    """com.badlogic.gdx.ai.steer.behaviors.Flee"""
 
    @staticmethod
    def _wrap(java_value: _Flee) -> 'Flee':
        return Flee(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Flee):
        """
        Dynamic initializer for Flee.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Flee__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Flee__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def setEnabled(self, arg0: bool) -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setEnabled(boolean)"""
        return 'Flee'._wrap(super(_Flee, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Flee'._wrap(super(_Flee, self).setOwner(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Seek.getTarget()"""
        return 'utils.Location'._wrap(super(Seek, self).getTarget())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setTarget(self, arg0: 'Location') -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Flee'._wrap(super(_Flee, self).setTarget(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Flee'._wrap(super(_Flee, self).setLimiter(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Flee(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = _Flee(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Flee(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Flee(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Hide
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.Hide as _Hide
_Hide = _Hide
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.behaviors.Arrive as _Arrive
_Arrive = _Arrive
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Hide():
    """com.badlogic.gdx.ai.steer.behaviors.Hide"""
 
    @staticmethod
    def _wrap(java_value: _Hide) -> 'Hide':
        return Hide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Hide):
        """
        Dynamic initializer for Hide.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Hide__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Hide__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setDecelerationRadius(float)"""
        return 'Hide'._wrap(super(_Hide, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def setEnabled(self, arg0: bool) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setEnabled(boolean)"""
        return 'Hide'._wrap(super(_Hide, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def setProximity(self, arg0: 'Proximity') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        return 'Hide'._wrap(super(_Hide, self).setProximity(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Hide'._wrap(super(_Hide, self).setLimiter(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location', arg2: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Hide(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = _Hide(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.behaviors.Hide.getProximity()"""
        return 'steer.Proximity'._wrap(super(Hide, self).getProximity())

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float._wrap(super(Arrive, self).getTimeToTarget())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float._wrap(super(Arrive, self).getArrivalTolerance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Hide(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Hide(arg0)
        self.__wrapper = val

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float._wrap(super(Arrive, self).getDecelerationRadius())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Hide'._wrap(super(_Hide, self).setOwner(arg0))

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setArrivalTolerance(float)"""
        return 'Hide'._wrap(super(_Hide, self).setArrivalTolerance(_float.valueOf(arg0)))

    @overload
    def setTarget(self, arg0: 'Location') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Hide'._wrap(super(_Hide, self).setTarget(arg0))

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Hide.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool._wrap(super(_Hide, self).reportNeighbor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'._wrap(super(Arrive, self).getTarget())

    @overload
    def getDistanceFromBoundary(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Hide.getDistanceFromBoundary()"""
        return float._wrap(super(Hide, self).getDistanceFromBoundary())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Hide(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = _Hide(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setTimeToTarget(float)"""
        return 'Hide'._wrap(super(_Hide, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def setDistanceFromBoundary(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setDistanceFromBoundary(float)"""
        return 'Hide'._wrap(super(_Hide, self).setDistanceFromBoundary(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump$JumpCallback
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.steer.behaviors.Jump as _Jump_JumpCallback
_JumpCallback = _Jump_JumpCallback.JumpCallback
 
class JumpCallback():
    """com.badlogic.gdx.ai.steer.behaviors.Jump.JumpCallback"""
 
    @staticmethod
    def _wrap(java_value: _JumpCallback) -> 'JumpCallback':
        return JumpCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JumpCallback):
        """
        Dynamic initializer for JumpCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JumpCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JumpCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reportAchievability(self, arg0: bool):
        """public abstract void com.badlogic.gdx.ai.steer.behaviors.Jump$JumpCallback.reportAchievability(boolean)"""
        pass

    @abstractmethod
    def takeoff(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.ai.steer.behaviors.Jump$JumpCallback.takeoff(float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.MatchVelocity
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.MatchVelocity as _MatchVelocity
_MatchVelocity = _MatchVelocity
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MatchVelocity():
    """com.badlogic.gdx.ai.steer.behaviors.MatchVelocity"""
 
    @staticmethod
    def _wrap(java_value: _MatchVelocity) -> 'MatchVelocity':
        return MatchVelocity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MatchVelocity):
        """
        Dynamic initializer for MatchVelocity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MatchVelocity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MatchVelocity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _MatchVelocity(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = _MatchVelocity(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTarget()"""
        return 'steer.Steerable'._wrap(super(MatchVelocity, self).getTarget())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _MatchVelocity(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTimeToTarget()"""
        return float._wrap(super(MatchVelocity, self).getTimeToTarget())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'MatchVelocity'._wrap(super(_MatchVelocity, self).setTarget(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'MatchVelocity'._wrap(super(_MatchVelocity, self).setLimiter(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'MatchVelocity'._wrap(super(_MatchVelocity, self).setOwner(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setEnabled(boolean)"""
        return 'MatchVelocity'._wrap(super(_MatchVelocity, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTimeToTarget(self, arg0: float) -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setTimeToTarget(float)"""
        return 'MatchVelocity'._wrap(super(_MatchVelocity, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance as _CollisionAvoidance
_CollisionAvoidance = _CollisionAvoidance
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import com.badlogic.gdx.ai.steer.GroupBehavior as _GroupBehavior
_GroupBehavior = _GroupBehavior
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CollisionAvoidance():
    """com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance"""
 
    @staticmethod
    def _wrap(java_value: _CollisionAvoidance) -> 'CollisionAvoidance':
        return CollisionAvoidance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CollisionAvoidance):
        """
        Dynamic initializer for CollisionAvoidance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CollisionAvoidance__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CollisionAvoidance__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = _CollisionAvoidance(arg0, arg1)
        self.__wrapper = val

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool._wrap(super(_CollisionAvoidance, self).reportNeighbor(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'CollisionAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'CollisionAvoidance'._wrap(super(_CollisionAvoidance, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'CollisionAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'CollisionAvoidance'._wrap(super(_CollisionAvoidance, self).setLimiter(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'CollisionAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.setEnabled(boolean)"""
        return 'CollisionAvoidance'._wrap(super(_CollisionAvoidance, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'._wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(_steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Seek
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.behaviors.Seek as _Seek
_Seek = _Seek
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Seek():
    """com.badlogic.gdx.ai.steer.behaviors.Seek"""
 
    @staticmethod
    def _wrap(java_value: _Seek) -> 'Seek':
        return Seek(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Seek):
        """
        Dynamic initializer for Seek.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Seek__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Seek__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Seek(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = _Seek(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setEnabled(self, arg0: bool) -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setEnabled(boolean)"""
        return 'Seek'._wrap(super(_Seek, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Seek'._wrap(super(_Seek, self).setLimiter(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Seek(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Seek(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Seek.getTarget()"""
        return 'utils.Location'._wrap(super(Seek, self).getTarget())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Seek'._wrap(super(_Seek, self).setOwner(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTarget(self, arg0: 'Location') -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Seek'._wrap(super(_Seek, self).setTarget(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Alignment
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.steer.behaviors.Alignment as _Alignment
_Alignment = _Alignment
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import com.badlogic.gdx.ai.steer.GroupBehavior as _GroupBehavior
_GroupBehavior = _GroupBehavior
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Alignment():
    """com.badlogic.gdx.ai.steer.behaviors.Alignment"""
 
    @staticmethod
    def _wrap(java_value: _Alignment) -> 'Alignment':
        return Alignment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Alignment):
        """
        Dynamic initializer for Alignment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Alignment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Alignment__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = _Alignment(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Alignment':
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment<T> com.badlogic.gdx.ai.steer.behaviors.Alignment.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Alignment'._wrap(super(_Alignment, self).setOwner(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'Alignment':
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment<T> com.badlogic.gdx.ai.steer.behaviors.Alignment.setEnabled(boolean)"""
        return 'Alignment'._wrap(super(_Alignment, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Alignment.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool._wrap(super(_Alignment, self).reportNeighbor(arg0))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Alignment':
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment<T> com.badlogic.gdx.ai.steer.behaviors.Alignment.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Alignment'._wrap(super(_Alignment, self).setLimiter(arg0))

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'._wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(_steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump$GravityComponentHandler
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.behaviors.Jump as _Jump_GravityComponentHandler
_GravityComponentHandler = _Jump_GravityComponentHandler.GravityComponentHandler
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from abc import abstractmethod, ABC
 
class GravityComponentHandler():
    """com.badlogic.gdx.ai.steer.behaviors.Jump.GravityComponentHandler"""
 
    @staticmethod
    def _wrap(java_value: _GravityComponentHandler) -> 'GravityComponentHandler':
        return GravityComponentHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GravityComponentHandler):
        """
        Dynamic initializer for GravityComponentHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GravityComponentHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GravityComponentHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getComponent(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.ai.steer.behaviors.Jump$GravityComponentHandler.getComponent(T)"""
        pass

    @abstractmethod
    def setComponent(self, arg0: 'Vector', arg1: float):
        """public abstract void com.badlogic.gdx.ai.steer.behaviors.Jump$GravityComponentHandler.setComponent(T,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.PrioritySteering
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.behaviors.PrioritySteering as _PrioritySteering
_PrioritySteering = _PrioritySteering
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrioritySteering():
    """com.badlogic.gdx.ai.steer.behaviors.PrioritySteering"""
 
    @staticmethod
    def _wrap(java_value: _PrioritySteering) -> 'PrioritySteering':
        return PrioritySteering(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrioritySteering):
        """
        Dynamic initializer for PrioritySteering.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrioritySteering__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrioritySteering__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _PrioritySteering(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float):
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering(com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = _PrioritySteering(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, arg0: 'SteeringBehavior') -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.add(com.badlogic.gdx.ai.steer.SteeringBehavior<T>)"""
        return 'PrioritySteering'._wrap(super(_PrioritySteering, self).add(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'PrioritySteering'._wrap(super(_PrioritySteering, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setEnabled(self, arg0: bool) -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setEnabled(boolean)"""
        return 'PrioritySteering'._wrap(super(_PrioritySteering, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'PrioritySteering'._wrap(super(_PrioritySteering, self).setLimiter(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSelectedBehaviorIndex(self) -> int:
        """public int com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.getSelectedBehaviorIndex()"""
        return int._wrap(super(PrioritySteering, self).getSelectedBehaviorIndex())

    @overload
    def getEpsilon(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.getEpsilon()"""
        return float._wrap(super(PrioritySteering, self).getEpsilon())

    @overload
    def setEpsilon(self, arg0: float) -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setEpsilon(float)"""
        return 'PrioritySteering'._wrap(super(_PrioritySteering, self).setEpsilon(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Face
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.behaviors.Face as _Face
_Face = _Face
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as _ReachOrientation
_ReachOrientation = _ReachOrientation
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Face():
    """com.badlogic.gdx.ai.steer.behaviors.Face"""
 
    @staticmethod
    def _wrap(java_value: _Face) -> 'Face':
        return Face(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Face):
        """
        Dynamic initializer for Face.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Face__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Face__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Face(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = _Face(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setTimeToTarget(float)"""
        return 'Face'._wrap(super(_Face, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def setEnabled(self, arg0: bool) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setEnabled(boolean)"""
        return 'Face'._wrap(super(_Face, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Face(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Face(arg0)
        self.__wrapper = val

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Face'._wrap(super(_Face, self).setLimiter(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setDecelerationRadius(float)"""
        return 'Face'._wrap(super(_Face, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setTarget(self, arg0: 'Location') -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Face'._wrap(super(_Face, self).setTarget(arg0))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float._wrap(super(ReachOrientation, self).getDecelerationRadius())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float._wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setAlignTolerance(float)"""
        return 'Face'._wrap(super(_Face, self).setAlignTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'._wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float._wrap(super(ReachOrientation, self).getAlignTolerance())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Face'._wrap(super(_Face, self).setOwner(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Separation
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.steer.behaviors.Separation as _Separation
_Separation = _Separation
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import com.badlogic.gdx.ai.steer.GroupBehavior as _GroupBehavior
_GroupBehavior = _GroupBehavior
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Separation():
    """com.badlogic.gdx.ai.steer.behaviors.Separation"""
 
    @staticmethod
    def _wrap(java_value: _Separation) -> 'Separation':
        return Separation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Separation):
        """
        Dynamic initializer for Separation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Separation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Separation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Separation(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = _Separation(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setEnabled(self, arg0: bool) -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setEnabled(boolean)"""
        return 'Separation'._wrap(super(_Separation, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Separation'._wrap(super(_Separation, self).setOwner(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Separation'._wrap(super(_Separation, self).setLimiter(arg0))

    @overload
    def setDecayCoefficient(self, arg0: float) -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setDecayCoefficient(float)"""
        return 'Separation'._wrap(super(_Separation, self).setDecayCoefficient(_float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'._wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(_steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Separation.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool._wrap(super(_Separation, self).reportNeighbor(arg0))

    @overload
    def getDecayCoefficient(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Separation.getDecayCoefficient()"""
        return float._wrap(super(Separation, self).getDecayCoefficient())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.BlendedSteering
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.steer.behaviors.BlendedSteering as _BlendedSteering
_BlendedSteering = _BlendedSteering
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.BlendedSteering as _BlendedSteering_BehaviorAndWeight
_BehaviorAndWeight = _BlendedSteering_BehaviorAndWeight.BehaviorAndWeight
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlendedSteering():
    """com.badlogic.gdx.ai.steer.behaviors.BlendedSteering"""
 
    @staticmethod
    def _wrap(java_value: _BlendedSteering) -> 'BlendedSteering':
        return BlendedSteering(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlendedSteering):
        """
        Dynamic initializer for BlendedSteering.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlendedSteering__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlendedSteering__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def remove(self, arg0: 'BehaviorAndWeight'):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.remove(com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight<T>)"""
        super(_BlendedSteering, self).remove(arg0)

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def remove(self, arg0: 'SteeringBehavior'):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.remove(com.badlogic.gdx.ai.steer.SteeringBehavior<T>)"""
        super(_BlendedSteering, self).remove(arg0)

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'BlendedSteering'._wrap(super(_BlendedSteering, self).setLimiter(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'BehaviorAndWeight') -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.add(com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight<T>)"""
        return 'BlendedSteering'._wrap(super(_BlendedSteering, self).add(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.setEnabled(boolean)"""
        return 'BlendedSteering'._wrap(super(_BlendedSteering, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'BlendedSteering'._wrap(super(_BlendedSteering, self).setOwner(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'SteeringBehavior', arg1: float) -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.add(com.badlogic.gdx.ai.steer.SteeringBehavior<T>,float)"""
        return 'BlendedSteering'._wrap(super(_BlendedSteering, self).add(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _BlendedSteering(arg0)
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'BehaviorAndWeight':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.get(int)"""
        return 'BehaviorAndWeight'._wrap(super(_BlendedSteering, self).get(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Interpose
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.behaviors.Interpose as _Interpose
_Interpose = _Interpose
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import com.badlogic.gdx.ai.steer.behaviors.Arrive as _Arrive
_Arrive = _Arrive
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Interpose():
    """com.badlogic.gdx.ai.steer.behaviors.Interpose"""
 
    @staticmethod
    def _wrap(java_value: _Interpose) -> 'Interpose':
        return Interpose(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Interpose):
        """
        Dynamic initializer for Interpose.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Interpose__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Interpose__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Interpose'._wrap(super(_Interpose, self).setLimiter(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setEnabled(self, arg0: bool) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setEnabled(boolean)"""
        return 'Interpose'._wrap(super(_Interpose, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def getAgentA(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.getAgentA()"""
        return 'steer.Steerable'._wrap(super(Interpose, self).getAgentA())

    @overload
    def getInterpositionRatio(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Interpose.getInterpositionRatio()"""
        return float._wrap(super(Interpose, self).getInterpositionRatio())

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setTimeToTarget(float)"""
        return 'Interpose'._wrap(super(_Interpose, self).setTimeToTarget(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTarget(self, arg0: 'Location') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Interpose'._wrap(super(_Interpose, self).setTarget(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: 'Steerable', arg3: float):
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = _Interpose(arg0, arg1, arg2, _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float._wrap(super(Arrive, self).getTimeToTarget())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float._wrap(super(Arrive, self).getArrivalTolerance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setInterpositionRatio(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setInterpositionRatio(float)"""
        return 'Interpose'._wrap(super(_Interpose, self).setInterpositionRatio(_float.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float._wrap(super(Arrive, self).getDecelerationRadius())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Interpose'._wrap(super(_Interpose, self).setOwner(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setDecelerationRadius(float)"""
        return 'Interpose'._wrap(super(_Interpose, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Interpose(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def setAgentB(self, arg0: 'Steerable') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setAgentB(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Interpose'._wrap(super(_Interpose, self).setAgentB(arg0))

    @overload
    def getAgentB(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.getAgentB()"""
        return 'steer.Steerable'._wrap(super(Interpose, self).getAgentB())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setArrivalTolerance(float)"""
        return 'Interpose'._wrap(super(_Interpose, self).setArrivalTolerance(_float.valueOf(arg0)))

    @overload
    def setAgentA(self, arg0: 'Steerable') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setAgentA(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Interpose'._wrap(super(_Interpose, self).setAgentA(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'._wrap(super(Arrive, self).getTarget())

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Interpose.getInternalTargetPosition()"""
        return 'math.Vector'._wrap(super(Interpose, self).getInternalTargetPosition())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.behaviors.Jump as _Jump_JumpDescriptor
_JumpDescriptor = _Jump_JumpDescriptor.JumpDescriptor
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JumpDescriptor():
    """com.badlogic.gdx.ai.steer.behaviors.Jump.JumpDescriptor"""
 
    @staticmethod
    def _wrap(java_value: _JumpDescriptor) -> 'JumpDescriptor':
        return JumpDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JumpDescriptor):
        """
        Dynamic initializer for JumpDescriptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JumpDescriptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JumpDescriptor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'Vector', arg1: 'Vector'):
        """public void com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor.set(T,T)"""
        super(_JumpDescriptor, self).set(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Vector', arg1: 'Vector'):
        """public com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor(T,T)"""
        val = _JumpDescriptor(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Arrive
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.behaviors.Arrive as _Arrive
_Arrive = _Arrive
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Arrive():
    """com.badlogic.gdx.ai.steer.behaviors.Arrive"""
 
    @staticmethod
    def _wrap(java_value: _Arrive) -> 'Arrive':
        return Arrive(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Arrive):
        """
        Dynamic initializer for Arrive.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Arrive__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Arrive__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = _Arrive(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setTarget(self, arg0: 'Location') -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Arrive'._wrap(super(_Arrive, self).setTarget(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Arrive'._wrap(super(_Arrive, self).setLimiter(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Arrive'._wrap(super(_Arrive, self).setOwner(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setDecelerationRadius(float)"""
        return 'Arrive'._wrap(super(_Arrive, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Arrive(arg0)
        self.__wrapper = val

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setTimeToTarget(float)"""
        return 'Arrive'._wrap(super(_Arrive, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float._wrap(super(Arrive, self).getArrivalTolerance())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'._wrap(super(Arrive, self).getTarget())

    @overload
    def setEnabled(self, arg0: bool) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setEnabled(boolean)"""
        return 'Arrive'._wrap(super(_Arrive, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float._wrap(super(Arrive, self).getTimeToTarget())

    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float._wrap(super(Arrive, self).getDecelerationRadius())

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setArrivalTolerance(float)"""
        return 'Arrive'._wrap(super(_Arrive, self).setArrivalTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.FollowFlowField
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.behaviors.FollowFlowField as _FollowFlowField_FlowField
_FlowField = _FollowFlowField_FlowField.FlowField
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.behaviors.FollowFlowField as _FollowFlowField
_FollowFlowField = _FollowFlowField
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FollowFlowField():
    """com.badlogic.gdx.ai.steer.behaviors.FollowFlowField"""
 
    @staticmethod
    def _wrap(java_value: _FollowFlowField) -> 'FollowFlowField':
        return FollowFlowField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FollowFlowField):
        """
        Dynamic initializer for FollowFlowField.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FollowFlowField__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FollowFlowField__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'FollowFlowField'._wrap(super(_FollowFlowField, self).setLimiter(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setPredictionTime(self, arg0: float) -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setPredictionTime(float)"""
        return 'FollowFlowField'._wrap(super(_FollowFlowField, self).setPredictionTime(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def getFlowField(self) -> 'FlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.getFlowField()"""
        return 'FlowField'._wrap(super(FollowFlowField, self).getFlowField())

    @overload
    def setFlowField(self, arg0: 'FlowField') -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setFlowField(com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T>)"""
        return 'FollowFlowField'._wrap(super(_FollowFlowField, self).setFlowField(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setEnabled(self, arg0: bool) -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setEnabled(boolean)"""
        return 'FollowFlowField'._wrap(super(_FollowFlowField, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'FollowFlowField'._wrap(super(_FollowFlowField, self).setOwner(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'FlowField', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T>,float)"""
        val = _FollowFlowField(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _FollowFlowField(arg0)
        self.__wrapper = val

    @overload
    def getPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.getPredictionTime()"""
        return float._wrap(super(FollowFlowField, self).getPredictionTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'FlowField'):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T>)"""
        val = _FollowFlowField(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.BlendedSteering as _BlendedSteering_BehaviorAndWeight
_BehaviorAndWeight = _BlendedSteering_BehaviorAndWeight.BehaviorAndWeight
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorAndWeight():
    """com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.BehaviorAndWeight"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorAndWeight) -> 'BehaviorAndWeight':
        return BehaviorAndWeight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorAndWeight):
        """
        Dynamic initializer for BehaviorAndWeight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorAndWeight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorAndWeight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBehavior(self) -> 'steer.SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.getBehavior()"""
        return 'steer.SteeringBehavior'._wrap(super(BehaviorAndWeight, self).getBehavior())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setBehavior(self, arg0: 'SteeringBehavior'):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.setBehavior(com.badlogic.gdx.ai.steer.SteeringBehavior<T>)"""
        super(_BehaviorAndWeight, self).setBehavior(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getWeight(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.getWeight()"""
        return float._wrap(super(BehaviorAndWeight, self).getWeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'SteeringBehavior', arg1: float):
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight(com.badlogic.gdx.ai.steer.SteeringBehavior<T>,float)"""
        val = _BehaviorAndWeight(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setWeight(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.setWeight(float)"""
        super(_BehaviorAndWeight, self).setWeight(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Evade
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.steer.behaviors.Evade as _Evade
_Evade = _Evade
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.behaviors.Pursue as _Pursue
_Pursue = _Pursue
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Evade():
    """com.badlogic.gdx.ai.steer.behaviors.Evade"""
 
    @staticmethod
    def _wrap(java_value: _Evade) -> 'Evade':
        return Evade(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Evade):
        """
        Dynamic initializer for Evade.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Evade__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Evade__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Evade'._wrap(super(_Evade, self).setOwner(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.Evade(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = _Evade(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def setMaxPredictionTime(self, arg0: float) -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setMaxPredictionTime(float)"""
        return 'Pursue'._wrap(super(_Pursue, self).setMaxPredictionTime(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Pursue.getMaxPredictionTime()"""
        return float._wrap(super(Pursue, self).getMaxPredictionTime())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Evade(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Evade(arg0, arg1)
        self.__wrapper = val

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Evade'._wrap(super(_Evade, self).setTarget(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Evade'._wrap(super(_Evade, self).setLimiter(arg0))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setEnabled(self, arg0: bool) -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setEnabled(boolean)"""
        return 'Evade'._wrap(super(_Evade, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.getTarget()"""
        return 'steer.Steerable'._wrap(super(Pursue, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Pursue
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.behaviors.Pursue as _Pursue
_Pursue = _Pursue
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pursue():
    """com.badlogic.gdx.ai.steer.behaviors.Pursue"""
 
    @staticmethod
    def _wrap(java_value: _Pursue) -> 'Pursue':
        return Pursue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pursue):
        """
        Dynamic initializer for Pursue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pursue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pursue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setTarget(self, arg0: 'Steerable') -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Pursue'._wrap(super(_Pursue, self).setTarget(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Pursue'._wrap(super(_Pursue, self).setLimiter(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = _Pursue(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getMaxPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Pursue.getMaxPredictionTime()"""
        return float._wrap(super(Pursue, self).getMaxPredictionTime())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setMaxPredictionTime(self, arg0: float) -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setMaxPredictionTime(float)"""
        return 'Pursue'._wrap(super(_Pursue, self).setMaxPredictionTime(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Pursue'._wrap(super(_Pursue, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setEnabled(self, arg0: bool) -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setEnabled(boolean)"""
        return 'Pursue'._wrap(super(_Pursue, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.getTarget()"""
        return 'steer.Steerable'._wrap(super(Pursue, self).getTarget())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _Pursue(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Cohesion
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.steer.behaviors.Cohesion as _Cohesion
_Cohesion = _Cohesion
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import com.badlogic.gdx.ai.steer.GroupBehavior as _GroupBehavior
_GroupBehavior = _GroupBehavior
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Cohesion():
    """com.badlogic.gdx.ai.steer.behaviors.Cohesion"""
 
    @staticmethod
    def _wrap(java_value: _Cohesion) -> 'Cohesion':
        return Cohesion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cohesion):
        """
        Dynamic initializer for Cohesion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cohesion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cohesion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Cohesion':
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion<T> com.badlogic.gdx.ai.steer.behaviors.Cohesion.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Cohesion'._wrap(super(_Cohesion, self).setOwner(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = _Cohesion(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'Cohesion':
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion<T> com.badlogic.gdx.ai.steer.behaviors.Cohesion.setEnabled(boolean)"""
        return 'Cohesion'._wrap(super(_Cohesion, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'._wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(_steer.GroupBehavior, self).setProximity(arg0)

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Cohesion.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool._wrap(super(_Cohesion, self).reportNeighbor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Cohesion':
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion<T> com.badlogic.gdx.ai.steer.behaviors.Cohesion.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Cohesion'._wrap(super(_Cohesion, self).setLimiter(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing as _LookWhereYouAreGoing
_LookWhereYouAreGoing = _LookWhereYouAreGoing
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as _ReachOrientation
_ReachOrientation = _ReachOrientation
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LookWhereYouAreGoing():
    """com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing"""
 
    @staticmethod
    def _wrap(java_value: _LookWhereYouAreGoing) -> 'LookWhereYouAreGoing':
        return LookWhereYouAreGoing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LookWhereYouAreGoing):
        """
        Dynamic initializer for LookWhereYouAreGoing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LookWhereYouAreGoing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LookWhereYouAreGoing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setTarget(self, arg0: 'Location') -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setTarget(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _LookWhereYouAreGoing(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float._wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def setTimeToTarget(self, arg0: float) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setTimeToTarget(float)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setTimeToTarget(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setOwner(arg0))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float._wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'._wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float._wrap(super(ReachOrientation, self).getAlignTolerance())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setDecelerationRadius(float)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setDecelerationRadius(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setEnabled(self, arg0: bool) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setEnabled(boolean)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setLimiter(arg0))

    @overload
    def setAlignTolerance(self, arg0: float) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setAlignTolerance(float)"""
        return 'LookWhereYouAreGoing'._wrap(super(_LookWhereYouAreGoing, self).setAlignTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.ReachOrientation
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as _ReachOrientation
_ReachOrientation = _ReachOrientation
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReachOrientation():
    """com.badlogic.gdx.ai.steer.behaviors.ReachOrientation"""
 
    @staticmethod
    def _wrap(java_value: _ReachOrientation) -> 'ReachOrientation':
        return ReachOrientation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReachOrientation):
        """
        Dynamic initializer for ReachOrientation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReachOrientation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReachOrientation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float._wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setOwner(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setDecelerationRadius(float)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setTimeToTarget(float)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = _ReachOrientation(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTarget(self, arg0: 'Location') -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setTarget(arg0))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setLimiter(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setEnabled(boolean)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setEnabled(_boolean.valueOf(arg0)))

    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float._wrap(super(ReachOrientation, self).getTimeToTarget())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setAlignTolerance(float)"""
        return 'ReachOrientation'._wrap(super(_ReachOrientation, self).setAlignTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'._wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _ReachOrientation(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float._wrap(super(ReachOrientation, self).getAlignTolerance())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.steer.behaviors.FollowFlowField as _FollowFlowField_FlowField
_FlowField = _FollowFlowField_FlowField.FlowField
 
class FlowField():
    """com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.FlowField"""
 
    @staticmethod
    def _wrap(java_value: _FlowField) -> 'FlowField':
        return FlowField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlowField):
        """
        Dynamic initializer for FlowField.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlowField__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlowField__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def lookup(self, arg0: 'Vector'):
        """public abstract T com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField.lookup(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.ai.steer import utils
except ImportError:
    utils = _import_once("pygdx.ai.steer.utils")

import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance as _RaycastObstacleAvoidance
_RaycastObstacleAvoidance = _RaycastObstacleAvoidance
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.utils.RayConfiguration as _RayConfiguration
_RayConfiguration = _RayConfiguration
import com.badlogic.gdx.ai.utils.RaycastCollisionDetector as _RaycastCollisionDetector
_RaycastCollisionDetector = _RaycastCollisionDetector
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RaycastObstacleAvoidance():
    """com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance"""
 
    @staticmethod
    def _wrap(java_value: _RaycastObstacleAvoidance) -> 'RaycastObstacleAvoidance':
        return RaycastObstacleAvoidance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RaycastObstacleAvoidance):
        """
        Dynamic initializer for RaycastObstacleAvoidance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RaycastObstacleAvoidance__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RaycastObstacleAvoidance__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setRayConfiguration(self, arg0: 'RayConfiguration') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setRayConfiguration(com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>)"""
        return 'RaycastObstacleAvoidance'._wrap(super(_RaycastObstacleAvoidance, self).setRayConfiguration(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDistanceFromBoundary(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.getDistanceFromBoundary()"""
        return float._wrap(super(RaycastObstacleAvoidance, self).getDistanceFromBoundary())

    @overload
    def getRayConfiguration(self) -> 'utils.RayConfiguration':
        """public com.badlogic.gdx.ai.steer.utils.RayConfiguration<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.getRayConfiguration()"""
        return 'utils.RayConfiguration'._wrap(super(RaycastObstacleAvoidance, self).getRayConfiguration())

    @overload
    def setDistanceFromBoundary(self, arg0: float) -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setDistanceFromBoundary(float)"""
        return 'RaycastObstacleAvoidance'._wrap(super(_RaycastObstacleAvoidance, self).setDistanceFromBoundary(_float.valueOf(arg0)))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRaycastCollisionDetector(self) -> 'utils.RaycastCollisionDetector':
        """public com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.getRaycastCollisionDetector()"""
        return 'utils.RaycastCollisionDetector'._wrap(super(RaycastObstacleAvoidance, self).getRaycastCollisionDetector())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'RaycastObstacleAvoidance'._wrap(super(_RaycastObstacleAvoidance, self).setOwner(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'RaycastObstacleAvoidance'._wrap(super(_RaycastObstacleAvoidance, self).setLimiter(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'RayConfiguration', arg2: 'RaycastCollisionDetector'):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>,com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T>)"""
        val = _RaycastObstacleAvoidance(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _RaycastObstacleAvoidance(arg0)
        self.__wrapper = val

    @overload
    def setEnabled(self, arg0: bool) -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setEnabled(boolean)"""
        return 'RaycastObstacleAvoidance'._wrap(super(_RaycastObstacleAvoidance, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'RayConfiguration'):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>)"""
        val = _RaycastObstacleAvoidance(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setRaycastCollisionDetector(self, arg0: 'RaycastCollisionDetector') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setRaycastCollisionDetector(com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T>)"""
        return 'RaycastObstacleAvoidance'._wrap(super(_RaycastObstacleAvoidance, self).setRaycastCollisionDetector(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'RayConfiguration', arg2: 'RaycastCollisionDetector', arg3: float):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>,com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T>,float)"""
        val = _RaycastObstacleAvoidance(arg0, arg1, arg2, _float.valueOf(arg3))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.MatchVelocity as _MatchVelocity
_MatchVelocity = _MatchVelocity
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import com.badlogic.gdx.ai.steer.behaviors.Jump as _Jump_JumpDescriptor
_JumpDescriptor = _Jump_JumpDescriptor.JumpDescriptor
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.ai.steer.behaviors.Jump as _Jump
_Jump = _Jump
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Jump():
    """com.badlogic.gdx.ai.steer.behaviors.Jump"""
 
    @staticmethod
    def _wrap(java_value: _Jump) -> 'Jump':
        return Jump(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Jump):
        """
        Dynamic initializer for Jump.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Jump__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Jump__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def calculateRealSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.behaviors.Jump.calculateRealSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_Jump, self).calculateRealSteering(arg0))

    @overload
    def setTakeoffVelocityTolerance(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTakeoffVelocityTolerance(float)"""
        return 'Jump'._wrap(super(_Jump, self).setTakeoffVelocityTolerance(_float.valueOf(arg0)))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTimeToTarget()"""
        return float._wrap(super(MatchVelocity, self).getTimeToTarget())

    @override
    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTarget()"""
        return 'steer.Steerable'._wrap(super(MatchVelocity, self).getTarget())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def getGravity(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Jump.getGravity()"""
        return 'math.Vector'._wrap(super(Jump, self).getGravity())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Jump'._wrap(super(_Jump, self).setTarget(arg0))

    @overload
    def getJumpDescriptor(self) -> 'JumpDescriptor':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T> com.badlogic.gdx.ai.steer.behaviors.Jump.getJumpDescriptor()"""
        return 'JumpDescriptor'._wrap(super(Jump, self).getJumpDescriptor())

    @overload
    def setMaxVerticalVelocity(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setMaxVerticalVelocity(float)"""
        return 'Jump'._wrap(super(_Jump, self).setMaxVerticalVelocity(_float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def getMaxVerticalVelocity(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.getMaxVerticalVelocity()"""
        return float._wrap(super(Jump, self).getMaxVerticalVelocity())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'JumpDescriptor', arg2: 'Vector', arg3: 'GravityComponentHandler', arg4: 'JumpCallback'):
        """public com.badlogic.gdx.ai.steer.behaviors.Jump(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T>,T,com.badlogic.gdx.ai.steer.behaviors.Jump$GravityComponentHandler<T>,com.badlogic.gdx.ai.steer.behaviors.Jump$JumpCallback)"""
        val = _Jump(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def setTakeoffTolerance(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTakeoffTolerance(float)"""
        return 'Jump'._wrap(super(_Jump, self).setTakeoffTolerance(_float.valueOf(arg0)))

    @overload
    def setTakeoffPositionTolerance(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTakeoffPositionTolerance(float)"""
        return 'Jump'._wrap(super(_Jump, self).setTakeoffPositionTolerance(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setGravity(self, arg0: 'Vector') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setGravity(T)"""
        return 'Jump'._wrap(super(_Jump, self).setGravity(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Jump'._wrap(super(_Jump, self).setOwner(arg0))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTimeToTarget(float)"""
        return 'Jump'._wrap(super(_Jump, self).setTimeToTarget(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Jump'._wrap(super(_Jump, self).setLimiter(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def calculateAirborneTimeAndVelocity(self, arg0: 'Vector', arg1: 'JumpDescriptor', arg2: float) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.calculateAirborneTimeAndVelocity(T,com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T>,float)"""
        return float._wrap(super(_Jump, self).calculateAirborneTimeAndVelocity(arg0, arg1, _float.valueOf(arg2)))

    @overload
    def getTakeoffPositionTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.getTakeoffPositionTolerance()"""
        return float._wrap(super(Jump, self).getTakeoffPositionTolerance())

    @overload
    def setJumpDescriptor(self, arg0: 'JumpDescriptor') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setJumpDescriptor(com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T>)"""
        return 'Jump'._wrap(super(_Jump, self).setJumpDescriptor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTakeoffVelocityTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.getTakeoffVelocityTolerance()"""
        return float._wrap(super(Jump, self).getTakeoffVelocityTolerance())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setEnabled(self, arg0: bool) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setEnabled(boolean)"""
        return 'Jump'._wrap(super(_Jump, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.FollowPath
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.ai.steer import utils
except ImportError:
    utils = _import_once("pygdx.ai.steer.utils")

from builtins import type
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import com.badlogic.gdx.ai.steer.behaviors.Arrive as _Arrive
_Arrive = _Arrive
import com.badlogic.gdx.ai.steer.utils.Path as _Path
_Path = _Path
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
import java.lang.Float as _float
import com.badlogic.gdx.ai.steer.behaviors.FollowPath as _FollowPath
_FollowPath = _FollowPath
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.utils.Path as _Path_PathParam
_PathParam = _Path_PathParam.PathParam
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FollowPath():
    """com.badlogic.gdx.ai.steer.behaviors.FollowPath"""
 
    @staticmethod
    def _wrap(java_value: _FollowPath) -> 'FollowPath':
        return FollowPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FollowPath):
        """
        Dynamic initializer for FollowPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FollowPath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FollowPath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'._wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'._wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setLimiter(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPathParam(self) -> 'utils.Path$PathParam':
        """public P com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPathParam()"""
        return 'utils.Path$PathParam'._wrap(super(FollowPath, self).getPathParam())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'._wrap(super(_steer.SteeringBehavior, self).calculateSteering(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setOwner(arg0))

    @overload
    def isArriveEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.FollowPath.isArriveEnabled()"""
        return bool._wrap(super(FollowPath, self).isArriveEnabled())

    @overload
    def setPathOffset(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setPathOffset(float)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setPathOffset(_float.valueOf(arg0)))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float._wrap(super(Arrive, self).getTimeToTarget())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float._wrap(super(Arrive, self).getArrivalTolerance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float._wrap(super(Arrive, self).getDecelerationRadius())

    @overload
    def setTarget(self, arg0: 'Location') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setTarget(arg0))

    @overload
    def setPath(self, arg0: 'Path') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setPath(com.badlogic.gdx.ai.steer.utils.Path<T, P>)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setPath(arg0))

    @overload
    def getPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPredictionTime()"""
        return float._wrap(super(FollowPath, self).getPredictionTime())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setDecelerationRadius(float)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setDecelerationRadius(_float.valueOf(arg0)))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setTimeToTarget(float)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setTimeToTarget(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Path'):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.Path<T, P>)"""
        val = _FollowPath(arg0, arg1)
        self.__wrapper = val

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setArrivalTolerance(float)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setArrivalTolerance(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Path', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.Path<T, P>,float)"""
        val = _FollowPath(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPathOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPathOffset()"""
        return float._wrap(super(FollowPath, self).getPathOffset())

    @overload
    def setPredictionTime(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setPredictionTime(float)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setPredictionTime(_float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getPath(self) -> 'utils.Path':
        """public com.badlogic.gdx.ai.steer.utils.Path<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPath()"""
        return 'utils.Path'._wrap(super(FollowPath, self).getPath())

    @overload
    def setArriveEnabled(self, arg0: bool) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setArriveEnabled(boolean)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setArriveEnabled(_boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Path', arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.Path<T, P>,float,float)"""
        val = _FollowPath(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'._wrap(super(Arrive, self).getTarget())

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.FollowPath.getInternalTargetPosition()"""
        return 'math.Vector'._wrap(super(FollowPath, self).getInternalTargetPosition())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setEnabled(self, arg0: bool) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setEnabled(boolean)"""
        return 'FollowPath'._wrap(super(_FollowPath, self).setEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())