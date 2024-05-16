from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.steer.behaviors.Wander as __Wander
__Wander = __Wander
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as __ReachOrientation
__ReachOrientation = __ReachOrientation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import int
 
class Wander():
    """com.badlogic.gdx.ai.steer.behaviors.Wander"""
 
    @staticmethod
    def __wrap(java_value: __Wander) -> 'Wander':
        return Wander(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Wander):
        """
        Dynamic initializer for Wander.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float.__wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setWanderOrientation(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOrientation(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderOrientation(__float.valueOf(arg0)))

    @overload
    def isFaceEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Wander.isFaceEnabled()"""
        return bool.__wrap(super(Wander, self).isFaceEnabled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTarget(self, arg0: 'Location') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Wander'.__wrap(super(__Wander, self).setTarget(arg0))

    @overload
    def getWanderOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOrientation()"""
        return float.__wrap(super(Wander, self).getWanderOrientation())

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float.__wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def getWanderRate(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRate()"""
        return float.__wrap(super(Wander, self).getWanderRate())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getWanderOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOffset()"""
        return float.__wrap(super(Wander, self).getWanderOffset())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'.__wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float.__wrap(super(ReachOrientation, self).getAlignTolerance())

    @overload
    def setEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setEnabled(boolean)"""
        return 'Wander'.__wrap(super(__Wander, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setDecelerationRadius(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setDecelerationRadius(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setFaceEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setFaceEnabled(boolean)"""
        return 'Wander'.__wrap(super(__Wander, self).setFaceEnabled(__boolean.valueOf(arg0)))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTimeToTarget(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setTimeToTarget(__float.valueOf(arg0)))

    @overload
    def getWanderCenter(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderCenter()"""
        return 'math.Vector'.__wrap(super(Wander, self).getWanderCenter())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setAlignTolerance(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setAlignTolerance(__float.valueOf(arg0)))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Wander'.__wrap(super(__Wander, self).setLimiter(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Wander'.__wrap(super(__Wander, self).setOwner(arg0))

    @overload
    def getWanderRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRadius()"""
        return float.__wrap(super(Wander, self).getWanderRadius())

    @overload
    def setWanderRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRadius(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderRadius(__float.valueOf(arg0)))

    @overload
    def setWanderOffset(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOffset(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderOffset(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setWanderRate(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRate(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderRate(__float.valueOf(arg0)))

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getInternalTargetPosition()"""
        return 'math.Vector'.__wrap(super(Wander, self).getInternalTargetPosition())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Wander(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Wander(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Wander
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.steer.behaviors.Wander as __Wander
__Wander = __Wander
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as __ReachOrientation
__ReachOrientation = __ReachOrientation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import int
 
class Wander():
    """com.badlogic.gdx.ai.steer.behaviors.Wander"""
 
    @staticmethod
    def __wrap(java_value: __Wander) -> 'Wander':
        return Wander(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Wander):
        """
        Dynamic initializer for Wander.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float.__wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setWanderOrientation(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOrientation(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderOrientation(__float.valueOf(arg0)))

    @overload
    def isFaceEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Wander.isFaceEnabled()"""
        return bool.__wrap(super(Wander, self).isFaceEnabled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTarget(self, arg0: 'Location') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Wander'.__wrap(super(__Wander, self).setTarget(arg0))

    @overload
    def getWanderOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOrientation()"""
        return float.__wrap(super(Wander, self).getWanderOrientation())

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float.__wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def getWanderRate(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRate()"""
        return float.__wrap(super(Wander, self).getWanderRate())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getWanderOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderOffset()"""
        return float.__wrap(super(Wander, self).getWanderOffset())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'.__wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float.__wrap(super(ReachOrientation, self).getAlignTolerance())

    @overload
    def setEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setEnabled(boolean)"""
        return 'Wander'.__wrap(super(__Wander, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setDecelerationRadius(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setDecelerationRadius(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setFaceEnabled(self, arg0: bool) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setFaceEnabled(boolean)"""
        return 'Wander'.__wrap(super(__Wander, self).setFaceEnabled(__boolean.valueOf(arg0)))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setTimeToTarget(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setTimeToTarget(__float.valueOf(arg0)))

    @overload
    def getWanderCenter(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderCenter()"""
        return 'math.Vector'.__wrap(super(Wander, self).getWanderCenter())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setAlignTolerance(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setAlignTolerance(__float.valueOf(arg0)))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Wander'.__wrap(super(__Wander, self).setLimiter(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Wander'.__wrap(super(__Wander, self).setOwner(arg0))

    @overload
    def getWanderRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Wander.getWanderRadius()"""
        return float.__wrap(super(Wander, self).getWanderRadius())

    @overload
    def setWanderRadius(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRadius(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderRadius(__float.valueOf(arg0)))

    @overload
    def setWanderOffset(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderOffset(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderOffset(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setWanderRate(self, arg0: float) -> 'Wander':
        """public com.badlogic.gdx.ai.steer.behaviors.Wander<T> com.badlogic.gdx.ai.steer.behaviors.Wander.setWanderRate(float)"""
        return 'Wander'.__wrap(super(__Wander, self).setWanderRate(__float.valueOf(arg0)))

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Wander.getInternalTargetPosition()"""
        return 'math.Vector'.__wrap(super(Wander, self).getInternalTargetPosition())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Wander(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Wander(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Wander 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.utils.RaycastCollisionDetector as __RaycastCollisionDetector
__RaycastCollisionDetector = __RaycastCollisionDetector
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
try:
    from pygdx.ai.steer import utils
except ImportError:
    utils = __import_once__("pygdx.ai.steer.utils")

from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance as __RaycastObstacleAvoidance
__RaycastObstacleAvoidance = __RaycastObstacleAvoidance
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.utils.RayConfiguration as __RayConfiguration
__RayConfiguration = __RayConfiguration
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class RaycastObstacleAvoidance():
    """com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance"""
 
    @staticmethod
    def __wrap(java_value: __RaycastObstacleAvoidance) -> 'RaycastObstacleAvoidance':
        return RaycastObstacleAvoidance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RaycastObstacleAvoidance):
        """
        Dynamic initializer for RaycastObstacleAvoidance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setDistanceFromBoundary(self, arg0: float) -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setDistanceFromBoundary(float)"""
        return 'RaycastObstacleAvoidance'.__wrap(super(__RaycastObstacleAvoidance, self).setDistanceFromBoundary(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDistanceFromBoundary(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.getDistanceFromBoundary()"""
        return float.__wrap(super(RaycastObstacleAvoidance, self).getDistanceFromBoundary())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRaycastCollisionDetector(self) -> 'utils.RaycastCollisionDetector':
        """public com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.getRaycastCollisionDetector()"""
        return 'utils.RaycastCollisionDetector'.__wrap(super(RaycastObstacleAvoidance, self).getRaycastCollisionDetector())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def getRayConfiguration(self) -> 'utils.RayConfiguration':
        """public com.badlogic.gdx.ai.steer.utils.RayConfiguration<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.getRayConfiguration()"""
        return 'utils.RayConfiguration'.__wrap(super(RaycastObstacleAvoidance, self).getRayConfiguration())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'RayConfiguration'):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>)"""
        val = __RaycastObstacleAvoidance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'RaycastObstacleAvoidance'.__wrap(super(__RaycastObstacleAvoidance, self).setLimiter(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'RayConfiguration', arg2: 'RaycastCollisionDetector'):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>,com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T>)"""
        val = __RaycastObstacleAvoidance(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setEnabled(boolean)"""
        return 'RaycastObstacleAvoidance'.__wrap(super(__RaycastObstacleAvoidance, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setRaycastCollisionDetector(self, arg0: 'RaycastCollisionDetector') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setRaycastCollisionDetector(com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T>)"""
        return 'RaycastObstacleAvoidance'.__wrap(super(__RaycastObstacleAvoidance, self).setRaycastCollisionDetector(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'RaycastObstacleAvoidance'.__wrap(super(__RaycastObstacleAvoidance, self).setOwner(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __RaycastObstacleAvoidance(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'RayConfiguration', arg2: 'RaycastCollisionDetector', arg3: float):
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>,com.badlogic.gdx.ai.utils.RaycastCollisionDetector<T>,float)"""
        val = __RaycastObstacleAvoidance(arg0, arg1, arg2, __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRayConfiguration(self, arg0: 'RayConfiguration') -> 'RaycastObstacleAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.RaycastObstacleAvoidance.setRayConfiguration(com.badlogic.gdx.ai.steer.utils.RayConfiguration<T>)"""
        return 'RaycastObstacleAvoidance'.__wrap(super(__RaycastObstacleAvoidance, self).setRayConfiguration(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.behaviors.BlendedSteering as __BlendedSteering_BehaviorAndWeight
__BehaviorAndWeight = __BlendedSteering_BehaviorAndWeight.BehaviorAndWeight
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BehaviorAndWeight():
    """com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.BehaviorAndWeight"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorAndWeight) -> 'BehaviorAndWeight':
        return BehaviorAndWeight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorAndWeight):
        """
        Dynamic initializer for BehaviorAndWeight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setBehavior(self, arg0: 'SteeringBehavior'):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.setBehavior(com.badlogic.gdx.ai.steer.SteeringBehavior<T>)"""
        super(__BehaviorAndWeight, self).setBehavior(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'SteeringBehavior', arg1: float):
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight(com.badlogic.gdx.ai.steer.SteeringBehavior<T>,float)"""
        val = __BehaviorAndWeight(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWeight(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.getWeight()"""
        return float.__wrap(super(BehaviorAndWeight, self).getWeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBehavior(self) -> 'steer.SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.getBehavior()"""
        return 'steer.SteeringBehavior'.__wrap(super(BehaviorAndWeight, self).getBehavior())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setWeight(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight.setWeight(float)"""
        super(__BehaviorAndWeight, self).setWeight(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import com.badlogic.gdx.ai.steer.behaviors.Jump as __Jump
__Jump = __Jump
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import com.badlogic.gdx.ai.steer.behaviors.Jump as __Jump_JumpDescriptor
__JumpDescriptor = __Jump_JumpDescriptor.JumpDescriptor
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.ai.steer.behaviors.MatchVelocity as __MatchVelocity
__MatchVelocity = __MatchVelocity
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
from builtins import int
 
class Jump():
    """com.badlogic.gdx.ai.steer.behaviors.Jump"""
 
    @staticmethod
    def __wrap(java_value: __Jump) -> 'Jump':
        return Jump(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Jump):
        """
        Dynamic initializer for Jump.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getGravity(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Jump.getGravity()"""
        return 'math.Vector'.__wrap(super(Jump, self).getGravity())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def calculateRealSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.behaviors.Jump.calculateRealSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__Jump, self).calculateRealSteering(arg0))

    @overload
    def getTakeoffVelocityTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.getTakeoffVelocityTolerance()"""
        return float.__wrap(super(Jump, self).getTakeoffVelocityTolerance())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Jump'.__wrap(super(__Jump, self).setLimiter(arg0))

    @overload
    def getMaxVerticalVelocity(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.getMaxVerticalVelocity()"""
        return float.__wrap(super(Jump, self).getMaxVerticalVelocity())

    @overload
    def setTakeoffPositionTolerance(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTakeoffPositionTolerance(float)"""
        return 'Jump'.__wrap(super(__Jump, self).setTakeoffPositionTolerance(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'JumpDescriptor', arg2: 'Vector', arg3: 'GravityComponentHandler', arg4: 'JumpCallback'):
        """public com.badlogic.gdx.ai.steer.behaviors.Jump(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T>,T,com.badlogic.gdx.ai.steer.behaviors.Jump$GravityComponentHandler<T>,com.badlogic.gdx.ai.steer.behaviors.Jump$JumpCallback)"""
        val = __Jump(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setTakeoffTolerance(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTakeoffTolerance(float)"""
        return 'Jump'.__wrap(super(__Jump, self).setTakeoffTolerance(__float.valueOf(arg0)))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Jump'.__wrap(super(__Jump, self).setOwner(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def calculateAirborneTimeAndVelocity(self, arg0: 'Vector', arg1: 'JumpDescriptor', arg2: float) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.calculateAirborneTimeAndVelocity(T,com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T>,float)"""
        return float.__wrap(super(__Jump, self).calculateAirborneTimeAndVelocity(arg0, arg1, __float.valueOf(arg2)))

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Jump'.__wrap(super(__Jump, self).setTarget(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTimeToTarget()"""
        return float.__wrap(super(MatchVelocity, self).getTimeToTarget())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setGravity(self, arg0: 'Vector') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setGravity(T)"""
        return 'Jump'.__wrap(super(__Jump, self).setGravity(arg0))

    @overload
    def getJumpDescriptor(self) -> 'JumpDescriptor':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T> com.badlogic.gdx.ai.steer.behaviors.Jump.getJumpDescriptor()"""
        return 'JumpDescriptor'.__wrap(super(Jump, self).getJumpDescriptor())

    @overload
    def getTakeoffPositionTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Jump.getTakeoffPositionTolerance()"""
        return float.__wrap(super(Jump, self).getTakeoffPositionTolerance())

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTimeToTarget(float)"""
        return 'Jump'.__wrap(super(__Jump, self).setTimeToTarget(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setJumpDescriptor(self, arg0: 'JumpDescriptor') -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setJumpDescriptor(com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor<T>)"""
        return 'Jump'.__wrap(super(__Jump, self).setJumpDescriptor(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTarget()"""
        return 'steer.Steerable'.__wrap(super(MatchVelocity, self).getTarget())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTakeoffVelocityTolerance(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setTakeoffVelocityTolerance(float)"""
        return 'Jump'.__wrap(super(__Jump, self).setTakeoffVelocityTolerance(__float.valueOf(arg0)))

    @overload
    def setEnabled(self, arg0: bool) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setEnabled(boolean)"""
        return 'Jump'.__wrap(super(__Jump, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def setMaxVerticalVelocity(self, arg0: float) -> 'Jump':
        """public com.badlogic.gdx.ai.steer.behaviors.Jump<T> com.badlogic.gdx.ai.steer.behaviors.Jump.setMaxVerticalVelocity(float)"""
        return 'Jump'.__wrap(super(__Jump, self).setMaxVerticalVelocity(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Flee
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import com.badlogic.gdx.ai.steer.behaviors.Seek as __Seek
__Seek = __Seek
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.behaviors.Flee as __Flee
__Flee = __Flee
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class Flee():
    """com.badlogic.gdx.ai.steer.behaviors.Flee"""
 
    @staticmethod
    def __wrap(java_value: __Flee) -> 'Flee':
        return Flee(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Flee):
        """
        Dynamic initializer for Flee.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Flee(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = __Flee(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setEnabled(self, arg0: bool) -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setEnabled(boolean)"""
        return 'Flee'.__wrap(super(__Flee, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Flee'.__wrap(super(__Flee, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Flee'.__wrap(super(__Flee, self).setLimiter(arg0))

    @overload
    def setTarget(self, arg0: 'Location') -> 'Flee':
        """public com.badlogic.gdx.ai.steer.behaviors.Flee<T> com.badlogic.gdx.ai.steer.behaviors.Flee.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Flee'.__wrap(super(__Flee, self).setTarget(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Flee(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Flee(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Seek.getTarget()"""
        return 'utils.Location'.__wrap(super(Seek, self).getTarget())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Cohesion
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import com.badlogic.gdx.ai.steer.behaviors.Cohesion as __Cohesion
__Cohesion = __Cohesion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.GroupBehavior as __GroupBehavior
__GroupBehavior = __GroupBehavior
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Cohesion():
    """com.badlogic.gdx.ai.steer.behaviors.Cohesion"""
 
    @staticmethod
    def __wrap(java_value: __Cohesion) -> 'Cohesion':
        return Cohesion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cohesion):
        """
        Dynamic initializer for Cohesion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(__steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __Cohesion(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Cohesion.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool.__wrap(super(__Cohesion, self).reportNeighbor(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'Cohesion':
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion<T> com.badlogic.gdx.ai.steer.behaviors.Cohesion.setEnabled(boolean)"""
        return 'Cohesion'.__wrap(super(__Cohesion, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'.__wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Cohesion':
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion<T> com.badlogic.gdx.ai.steer.behaviors.Cohesion.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Cohesion'.__wrap(super(__Cohesion, self).setOwner(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Cohesion':
        """public com.badlogic.gdx.ai.steer.behaviors.Cohesion<T> com.badlogic.gdx.ai.steer.behaviors.Cohesion.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Cohesion'.__wrap(super(__Cohesion, self).setLimiter(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.PrioritySteering
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import com.badlogic.gdx.ai.steer.behaviors.PrioritySteering as __PrioritySteering
__PrioritySteering = __PrioritySteering
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PrioritySteering():
    """com.badlogic.gdx.ai.steer.behaviors.PrioritySteering"""
 
    @staticmethod
    def __wrap(java_value: __PrioritySteering) -> 'PrioritySteering':
        return PrioritySteering(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrioritySteering):
        """
        Dynamic initializer for PrioritySteering.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setEpsilon(self, arg0: float) -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setEpsilon(float)"""
        return 'PrioritySteering'.__wrap(super(__PrioritySteering, self).setEpsilon(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSelectedBehaviorIndex(self) -> int:
        """public int com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.getSelectedBehaviorIndex()"""
        return int.__wrap(super(PrioritySteering, self).getSelectedBehaviorIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, arg0: 'SteeringBehavior') -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.add(com.badlogic.gdx.ai.steer.SteeringBehavior<T>)"""
        return 'PrioritySteering'.__wrap(super(__PrioritySteering, self).add(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float):
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering(com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __PrioritySteering(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setEnabled(self, arg0: bool) -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setEnabled(boolean)"""
        return 'PrioritySteering'.__wrap(super(__PrioritySteering, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __PrioritySteering(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'PrioritySteering'.__wrap(super(__PrioritySteering, self).setLimiter(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'PrioritySteering':
        """public com.badlogic.gdx.ai.steer.behaviors.PrioritySteering<T> com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'PrioritySteering'.__wrap(super(__PrioritySteering, self).setOwner(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getEpsilon(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.PrioritySteering.getEpsilon()"""
        return float.__wrap(super(PrioritySteering, self).getEpsilon())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance as __CollisionAvoidance
__CollisionAvoidance = __CollisionAvoidance
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.GroupBehavior as __GroupBehavior
__GroupBehavior = __GroupBehavior
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CollisionAvoidance():
    """com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance"""
 
    @staticmethod
    def __wrap(java_value: __CollisionAvoidance) -> 'CollisionAvoidance':
        return CollisionAvoidance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollisionAvoidance):
        """
        Dynamic initializer for CollisionAvoidance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(__steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'CollisionAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'CollisionAvoidance'.__wrap(super(__CollisionAvoidance, self).setOwner(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setEnabled(self, arg0: bool) -> 'CollisionAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.setEnabled(boolean)"""
        return 'CollisionAvoidance'.__wrap(super(__CollisionAvoidance, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'.__wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool.__wrap(super(__CollisionAvoidance, self).reportNeighbor(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'CollisionAvoidance':
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance<T> com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'CollisionAvoidance'.__wrap(super(__CollisionAvoidance, self).setLimiter(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.CollisionAvoidance(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __CollisionAvoidance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Face
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as __ReachOrientation
__ReachOrientation = __ReachOrientation
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import com.badlogic.gdx.ai.steer.behaviors.Face as __Face
__Face = __Face
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class Face():
    """com.badlogic.gdx.ai.steer.behaviors.Face"""
 
    @staticmethod
    def __wrap(java_value: __Face) -> 'Face':
        return Face(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Face):
        """
        Dynamic initializer for Face.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setAlignTolerance(self, arg0: float) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setAlignTolerance(float)"""
        return 'Face'.__wrap(super(__Face, self).setAlignTolerance(__float.valueOf(arg0)))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float.__wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Face'.__wrap(super(__Face, self).setLimiter(arg0))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float.__wrap(super(ReachOrientation, self).getDecelerationRadius())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'.__wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float.__wrap(super(ReachOrientation, self).getAlignTolerance())

    @overload
    def setTarget(self, arg0: 'Location') -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Face'.__wrap(super(__Face, self).setTarget(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Face'.__wrap(super(__Face, self).setOwner(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setDecelerationRadius(float)"""
        return 'Face'.__wrap(super(__Face, self).setDecelerationRadius(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setEnabled(self, arg0: bool) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setEnabled(boolean)"""
        return 'Face'.__wrap(super(__Face, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Face(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = __Face(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Face':
        """public com.badlogic.gdx.ai.steer.behaviors.Face<T> com.badlogic.gdx.ai.steer.behaviors.Face.setTimeToTarget(float)"""
        return 'Face'.__wrap(super(__Face, self).setTimeToTarget(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Face(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Face(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as __ReachOrientation
__ReachOrientation = __ReachOrientation
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing as __LookWhereYouAreGoing
__LookWhereYouAreGoing = __LookWhereYouAreGoing
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class LookWhereYouAreGoing():
    """com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing"""
 
    @staticmethod
    def __wrap(java_value: __LookWhereYouAreGoing) -> 'LookWhereYouAreGoing':
        return LookWhereYouAreGoing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LookWhereYouAreGoing):
        """
        Dynamic initializer for LookWhereYouAreGoing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setEnabled(self, arg0: bool) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setEnabled(boolean)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setLimiter(arg0))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float.__wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAlignTolerance(self, arg0: float) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setAlignTolerance(float)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setAlignTolerance(__float.valueOf(arg0)))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float.__wrap(super(ReachOrientation, self).getDecelerationRadius())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'.__wrap(super(ReachOrientation, self).getTarget())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float.__wrap(super(ReachOrientation, self).getAlignTolerance())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setDecelerationRadius(float)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setDecelerationRadius(__float.valueOf(arg0)))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setOwner(arg0))

    @overload
    def setTarget(self, arg0: 'Location') -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setTarget(arg0))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __LookWhereYouAreGoing(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTimeToTarget(self, arg0: float) -> 'LookWhereYouAreGoing':
        """public com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing<T> com.badlogic.gdx.ai.steer.behaviors.LookWhereYouAreGoing.setTimeToTarget(float)"""
        return 'LookWhereYouAreGoing'.__wrap(super(__LookWhereYouAreGoing, self).setTimeToTarget(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Evade
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.Evade as __Evade
__Evade = __Evade
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import com.badlogic.gdx.ai.steer.behaviors.Pursue as __Pursue
__Pursue = __Pursue
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Evade():
    """com.badlogic.gdx.ai.steer.behaviors.Evade"""
 
    @staticmethod
    def __wrap(java_value: __Evade) -> 'Evade':
        return Evade(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Evade):
        """
        Dynamic initializer for Evade.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Evade(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Evade(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Evade'.__wrap(super(__Evade, self).setTarget(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Evade'.__wrap(super(__Evade, self).setLimiter(arg0))

    @override
    @overload
    def getMaxPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Pursue.getMaxPredictionTime()"""
        return float.__wrap(super(Pursue, self).getMaxPredictionTime())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.Evade(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __Evade(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Evade'.__wrap(super(__Evade, self).setOwner(arg0))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.getTarget()"""
        return 'steer.Steerable'.__wrap(super(Pursue, self).getTarget())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setEnabled(self, arg0: bool) -> 'Evade':
        """public com.badlogic.gdx.ai.steer.behaviors.Evade<T> com.badlogic.gdx.ai.steer.behaviors.Evade.setEnabled(boolean)"""
        return 'Evade'.__wrap(super(__Evade, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setMaxPredictionTime(self, arg0: float) -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setMaxPredictionTime(float)"""
        return 'Pursue'.__wrap(super(__Pursue, self).setMaxPredictionTime(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Pursue
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import com.badlogic.gdx.ai.steer.behaviors.Pursue as __Pursue
__Pursue = __Pursue
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Pursue():
    """com.badlogic.gdx.ai.steer.behaviors.Pursue"""
 
    @staticmethod
    def __wrap(java_value: __Pursue) -> 'Pursue':
        return Pursue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pursue):
        """
        Dynamic initializer for Pursue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getMaxPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Pursue.getMaxPredictionTime()"""
        return float.__wrap(super(Pursue, self).getMaxPredictionTime())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setEnabled(self, arg0: bool) -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setEnabled(boolean)"""
        return 'Pursue'.__wrap(super(__Pursue, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Pursue'.__wrap(super(__Pursue, self).setTarget(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Pursue(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Pursue'.__wrap(super(__Pursue, self).setLimiter(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.getTarget()"""
        return 'steer.Steerable'.__wrap(super(Pursue, self).getTarget())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Pursue'.__wrap(super(__Pursue, self).setOwner(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setMaxPredictionTime(self, arg0: float) -> 'Pursue':
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue<T> com.badlogic.gdx.ai.steer.behaviors.Pursue.setMaxPredictionTime(float)"""
        return 'Pursue'.__wrap(super(__Pursue, self).setMaxPredictionTime(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.Pursue(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __Pursue(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Alignment
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.behaviors.Alignment as __Alignment
__Alignment = __Alignment
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.GroupBehavior as __GroupBehavior
__GroupBehavior = __GroupBehavior
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Alignment():
    """com.badlogic.gdx.ai.steer.behaviors.Alignment"""
 
    @staticmethod
    def __wrap(java_value: __Alignment) -> 'Alignment':
        return Alignment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Alignment):
        """
        Dynamic initializer for Alignment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(__steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Alignment':
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment<T> com.badlogic.gdx.ai.steer.behaviors.Alignment.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Alignment'.__wrap(super(__Alignment, self).setLimiter(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __Alignment(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Alignment.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool.__wrap(super(__Alignment, self).reportNeighbor(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Alignment':
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment<T> com.badlogic.gdx.ai.steer.behaviors.Alignment.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Alignment'.__wrap(super(__Alignment, self).setOwner(arg0))

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'.__wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setEnabled(self, arg0: bool) -> 'Alignment':
        """public com.badlogic.gdx.ai.steer.behaviors.Alignment<T> com.badlogic.gdx.ai.steer.behaviors.Alignment.setEnabled(boolean)"""
        return 'Alignment'.__wrap(super(__Alignment, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.BlendedSteering
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.behaviors.BlendedSteering as __BlendedSteering_BehaviorAndWeight
__BehaviorAndWeight = __BlendedSteering_BehaviorAndWeight.BehaviorAndWeight
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.BlendedSteering as __BlendedSteering
__BlendedSteering = __BlendedSteering
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BlendedSteering():
    """com.badlogic.gdx.ai.steer.behaviors.BlendedSteering"""
 
    @staticmethod
    def __wrap(java_value: __BlendedSteering) -> 'BlendedSteering':
        return BlendedSteering(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlendedSteering):
        """
        Dynamic initializer for BlendedSteering.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setEnabled(self, arg0: bool) -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.setEnabled(boolean)"""
        return 'BlendedSteering'.__wrap(super(__BlendedSteering, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'BehaviorAndWeight') -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.add(com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight<T>)"""
        return 'BlendedSteering'.__wrap(super(__BlendedSteering, self).add(arg0))

    @overload
    def remove(self, arg0: 'SteeringBehavior'):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.remove(com.badlogic.gdx.ai.steer.SteeringBehavior<T>)"""
        super(__BlendedSteering, self).remove(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __BlendedSteering(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'BehaviorAndWeight':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.get(int)"""
        return 'BehaviorAndWeight'.__wrap(super(__BlendedSteering, self).get(__int.valueOf(arg0)))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'BlendedSteering'.__wrap(super(__BlendedSteering, self).setLimiter(arg0))

    @overload
    def add(self, arg0: 'SteeringBehavior', arg1: float) -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.add(com.badlogic.gdx.ai.steer.SteeringBehavior<T>,float)"""
        return 'BlendedSteering'.__wrap(super(__BlendedSteering, self).add(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: 'BehaviorAndWeight'):
        """public void com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.remove(com.badlogic.gdx.ai.steer.behaviors.BlendedSteering$BehaviorAndWeight<T>)"""
        super(__BlendedSteering, self).remove(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'BlendedSteering':
        """public com.badlogic.gdx.ai.steer.behaviors.BlendedSteering<T> com.badlogic.gdx.ai.steer.behaviors.BlendedSteering.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'BlendedSteering'.__wrap(super(__BlendedSteering, self).setOwner(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.ai.steer.behaviors.Jump as __Jump_JumpDescriptor
__JumpDescriptor = __Jump_JumpDescriptor.JumpDescriptor
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JumpDescriptor():
    """com.badlogic.gdx.ai.steer.behaviors.Jump.JumpDescriptor"""
 
    @staticmethod
    def __wrap(java_value: __JumpDescriptor) -> 'JumpDescriptor':
        return JumpDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JumpDescriptor):
        """
        Dynamic initializer for JumpDescriptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Vector', arg1: 'Vector'):
        """public com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor(T,T)"""
        val = __JumpDescriptor(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Vector', arg1: 'Vector'):
        """public void com.badlogic.gdx.ai.steer.behaviors.Jump$JumpDescriptor.set(T,T)"""
        super(__JumpDescriptor, self).set(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Hide
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.Arrive as __Arrive
__Arrive = __Arrive
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.steer.behaviors.Hide as __Hide
__Hide = __Hide
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class Hide():
    """com.badlogic.gdx.ai.steer.behaviors.Hide"""
 
    @staticmethod
    def __wrap(java_value: __Hide) -> 'Hide':
        return Hide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Hide):
        """
        Dynamic initializer for Hide.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float.__wrap(super(Arrive, self).getTimeToTarget())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location', arg2: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Hide(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __Hide(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Hide(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = __Hide(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setDistanceFromBoundary(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setDistanceFromBoundary(float)"""
        return 'Hide'.__wrap(super(__Hide, self).setDistanceFromBoundary(__float.valueOf(arg0)))

    @overload
    def setProximity(self, arg0: 'Proximity') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        return 'Hide'.__wrap(super(__Hide, self).setProximity(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setEnabled(self, arg0: bool) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setEnabled(boolean)"""
        return 'Hide'.__wrap(super(__Hide, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'.__wrap(super(Arrive, self).getTarget())

    @overload
    def setTarget(self, arg0: 'Location') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Hide'.__wrap(super(__Hide, self).setTarget(arg0))

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Hide'.__wrap(super(__Hide, self).setOwner(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Hide(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Hide(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float.__wrap(super(Arrive, self).getArrivalTolerance())

    @overload
    def getDistanceFromBoundary(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Hide.getDistanceFromBoundary()"""
        return float.__wrap(super(Hide, self).getDistanceFromBoundary())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setArrivalTolerance(float)"""
        return 'Hide'.__wrap(super(__Hide, self).setArrivalTolerance(__float.valueOf(arg0)))

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Hide.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool.__wrap(super(__Hide, self).reportNeighbor(arg0))

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Hide'.__wrap(super(__Hide, self).setLimiter(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.behaviors.Hide.getProximity()"""
        return 'steer.Proximity'.__wrap(super(Hide, self).getProximity())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setDecelerationRadius(float)"""
        return 'Hide'.__wrap(super(__Hide, self).setDecelerationRadius(__float.valueOf(arg0)))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Hide':
        """public com.badlogic.gdx.ai.steer.behaviors.Hide<T> com.badlogic.gdx.ai.steer.behaviors.Hide.setTimeToTarget(float)"""
        return 'Hide'.__wrap(super(__Hide, self).setTimeToTarget(__float.valueOf(arg0)))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float.__wrap(super(Arrive, self).getDecelerationRadius())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.behaviors.FollowFlowField as __FollowFlowField_FlowField
__FlowField = __FollowFlowField_FlowField.FlowField
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from abc import abstractmethod, ABC
 
class FlowField(ABC):
    """com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.FlowField"""
 
    @staticmethod
    def __wrap(java_value: __FlowField) -> 'FlowField':
        return FlowField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlowField):
        """
        Dynamic initializer for FlowField.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def lookup(self, arg0: 'Vector'):
        """public abstract T com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField.lookup(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump$JumpCallback
import com.badlogic.gdx.ai.steer.behaviors.Jump as __Jump_JumpCallback
__JumpCallback = __Jump_JumpCallback.JumpCallback
from abc import abstractmethod, ABC
 
class JumpCallback(ABC):
    """com.badlogic.gdx.ai.steer.behaviors.Jump.JumpCallback"""
 
    @staticmethod
    def __wrap(java_value: __JumpCallback) -> 'JumpCallback':
        return JumpCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JumpCallback):
        """
        Dynamic initializer for JumpCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.FollowFlowField
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import com.badlogic.gdx.ai.steer.behaviors.FollowFlowField as __FollowFlowField_FlowField
__FlowField = __FollowFlowField_FlowField.FlowField
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.FollowFlowField as __FollowFlowField
__FollowFlowField = __FollowFlowField
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FollowFlowField():
    """com.badlogic.gdx.ai.steer.behaviors.FollowFlowField"""
 
    @staticmethod
    def __wrap(java_value: __FollowFlowField) -> 'FollowFlowField':
        return FollowFlowField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FollowFlowField):
        """
        Dynamic initializer for FollowFlowField.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFlowField(self, arg0: 'FlowField') -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setFlowField(com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T>)"""
        return 'FollowFlowField'.__wrap(super(__FollowFlowField, self).setFlowField(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setEnabled(self, arg0: bool) -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setEnabled(boolean)"""
        return 'FollowFlowField'.__wrap(super(__FollowFlowField, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'FollowFlowField'.__wrap(super(__FollowFlowField, self).setOwner(arg0))

    @overload
    def getFlowField(self) -> 'FlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.getFlowField()"""
        return 'FlowField'.__wrap(super(FollowFlowField, self).getFlowField())

    @overload
    def setPredictionTime(self, arg0: float) -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setPredictionTime(float)"""
        return 'FollowFlowField'.__wrap(super(__FollowFlowField, self).setPredictionTime(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'FollowFlowField':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField<T> com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'FollowFlowField'.__wrap(super(__FollowFlowField, self).setLimiter(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'FlowField', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T>,float)"""
        val = __FollowFlowField(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'FlowField'):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.behaviors.FollowFlowField$FlowField<T>)"""
        val = __FollowFlowField(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowFlowField(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __FollowFlowField(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.FollowFlowField.getPredictionTime()"""
        return float.__wrap(super(FollowFlowField, self).getPredictionTime())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.MatchVelocity
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.behaviors.MatchVelocity as __MatchVelocity
__MatchVelocity = __MatchVelocity
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MatchVelocity():
    """com.badlogic.gdx.ai.steer.behaviors.MatchVelocity"""
 
    @staticmethod
    def __wrap(java_value: __MatchVelocity) -> 'MatchVelocity':
        return MatchVelocity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MatchVelocity):
        """
        Dynamic initializer for MatchVelocity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __MatchVelocity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __MatchVelocity(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTimeToTarget(self, arg0: float) -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setTimeToTarget(float)"""
        return 'MatchVelocity'.__wrap(super(__MatchVelocity, self).setTimeToTarget(__float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __MatchVelocity(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTarget(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTarget()"""
        return 'steer.Steerable'.__wrap(super(MatchVelocity, self).getTarget())

    @overload
    def setTarget(self, arg0: 'Steerable') -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setTarget(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'MatchVelocity'.__wrap(super(__MatchVelocity, self).setTarget(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setEnabled(boolean)"""
        return 'MatchVelocity'.__wrap(super(__MatchVelocity, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'MatchVelocity'.__wrap(super(__MatchVelocity, self).setOwner(arg0))

    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.getTimeToTarget()"""
        return float.__wrap(super(MatchVelocity, self).getTimeToTarget())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'MatchVelocity':
        """public com.badlogic.gdx.ai.steer.behaviors.MatchVelocity<T> com.badlogic.gdx.ai.steer.behaviors.MatchVelocity.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'MatchVelocity'.__wrap(super(__MatchVelocity, self).setLimiter(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.FollowPath
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import java.lang.Boolean as __boolean
try:
    from pygdx.ai.steer import utils
except ImportError:
    utils = __import_once__("pygdx.ai.steer.utils")

from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Class as __Class
__Class = __Class
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.steer.behaviors.Arrive as __Arrive
__Arrive = __Arrive
import com.badlogic.gdx.ai.steer.utils.Path as __Path_PathParam
__PathParam = __Path_PathParam.PathParam
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.FollowPath as __FollowPath
__FollowPath = __FollowPath
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.steer.utils.Path as __Path
__Path = __Path
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import int
 
class FollowPath():
    """com.badlogic.gdx.ai.steer.behaviors.FollowPath"""
 
    @staticmethod
    def __wrap(java_value: __FollowPath) -> 'FollowPath':
        return FollowPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FollowPath):
        """
        Dynamic initializer for FollowPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float.__wrap(super(Arrive, self).getTimeToTarget())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Path'):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.Path<T, P>)"""
        val = __FollowPath(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setArriveEnabled(self, arg0: bool) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setArriveEnabled(boolean)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setArriveEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def getPath(self) -> 'utils.Path':
        """public com.badlogic.gdx.ai.steer.utils.Path<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPath()"""
        return 'utils.Path'.__wrap(super(FollowPath, self).getPath())

    @overload
    def setPathOffset(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setPathOffset(float)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setPathOffset(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'.__wrap(super(Arrive, self).getTarget())

    @overload
    def getPathParam(self) -> 'utils.Path$PathParam':
        """public P com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPathParam()"""
        return 'utils.Path$PathParam'.__wrap(super(FollowPath, self).getPathParam())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Path', arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.Path<T, P>,float,float)"""
        val = __FollowPath(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.FollowPath.getInternalTargetPosition()"""
        return 'math.Vector'.__wrap(super(FollowPath, self).getInternalTargetPosition())

    @overload
    def setEnabled(self, arg0: bool) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setEnabled(boolean)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setDecelerationRadius(float)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setDecelerationRadius(__float.valueOf(arg0)))

    @overload
    def setTimeToTarget(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setTimeToTarget(float)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setTimeToTarget(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float.__wrap(super(Arrive, self).getArrivalTolerance())

    @overload
    def isArriveEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.FollowPath.isArriveEnabled()"""
        return bool.__wrap(super(FollowPath, self).isArriveEnabled())

    @overload
    def setPredictionTime(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setPredictionTime(float)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setPredictionTime(__float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Path', arg2: float):
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.utils.Path<T, P>,float)"""
        val = __FollowPath(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setLimiter(arg0))

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setArrivalTolerance(float)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setArrivalTolerance(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setTarget(self, arg0: 'Location') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setTarget(arg0))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float.__wrap(super(Arrive, self).getDecelerationRadius())

    @overload
    def getPredictionTime(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPredictionTime()"""
        return float.__wrap(super(FollowPath, self).getPredictionTime())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setOwner(arg0))

    @overload
    def setPath(self, arg0: 'Path') -> 'FollowPath':
        """public com.badlogic.gdx.ai.steer.behaviors.FollowPath<T, P> com.badlogic.gdx.ai.steer.behaviors.FollowPath.setPath(com.badlogic.gdx.ai.steer.utils.Path<T, P>)"""
        return 'FollowPath'.__wrap(super(__FollowPath, self).setPath(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPathOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.FollowPath.getPathOffset()"""
        return float.__wrap(super(FollowPath, self).getPathOffset()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Seek
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import com.badlogic.gdx.ai.steer.behaviors.Seek as __Seek
__Seek = __Seek
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class Seek():
    """com.badlogic.gdx.ai.steer.behaviors.Seek"""
 
    @staticmethod
    def __wrap(java_value: __Seek) -> 'Seek':
        return Seek(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Seek):
        """
        Dynamic initializer for Seek.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Seek.getTarget()"""
        return 'utils.Location'.__wrap(super(Seek, self).getTarget())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setTarget(self, arg0: 'Location') -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Seek'.__wrap(super(__Seek, self).setTarget(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setEnabled(self, arg0: bool) -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setEnabled(boolean)"""
        return 'Seek'.__wrap(super(__Seek, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Seek(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Seek(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Seek'.__wrap(super(__Seek, self).setLimiter(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Seek':
        """public com.badlogic.gdx.ai.steer.behaviors.Seek<T> com.badlogic.gdx.ai.steer.behaviors.Seek.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Seek'.__wrap(super(__Seek, self).setOwner(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Seek(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = __Seek(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Arrive
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.behaviors.Arrive as __Arrive
__Arrive = __Arrive
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class Arrive():
    """com.badlogic.gdx.ai.steer.behaviors.Arrive"""
 
    @staticmethod
    def __wrap(java_value: __Arrive) -> 'Arrive':
        return Arrive(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Arrive):
        """
        Dynamic initializer for Arrive.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setArrivalTolerance(float)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setArrivalTolerance(__float.valueOf(arg0)))

    @overload
    def setEnabled(self, arg0: bool) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setEnabled(boolean)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setLimiter(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTarget(self, arg0: 'Location') -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setTarget(arg0))

    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float.__wrap(super(Arrive, self).getTimeToTarget())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = __Arrive(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'.__wrap(super(Arrive, self).getTarget())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setOwner(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Arrive(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setTimeToTarget(float)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setTimeToTarget(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float.__wrap(super(Arrive, self).getArrivalTolerance())

    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float.__wrap(super(Arrive, self).getDecelerationRadius())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Arrive':
        """public com.badlogic.gdx.ai.steer.behaviors.Arrive<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.setDecelerationRadius(float)"""
        return 'Arrive'.__wrap(super(__Arrive, self).setDecelerationRadius(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.ReachOrientation
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.behaviors.ReachOrientation as __ReachOrientation
__ReachOrientation = __ReachOrientation
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class ReachOrientation():
    """com.badlogic.gdx.ai.steer.behaviors.ReachOrientation"""
 
    @staticmethod
    def __wrap(java_value: __ReachOrientation) -> 'ReachOrientation':
        return ReachOrientation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReachOrientation):
        """
        Dynamic initializer for ReachOrientation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setOwner(self, arg0: 'Steerable') -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setOwner(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setTarget(self, arg0: 'Location') -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setTarget(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAlignTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getAlignTolerance()"""
        return float.__wrap(super(ReachOrientation, self).getAlignTolerance())

    @overload
    def setAlignTolerance(self, arg0: float) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setAlignTolerance(float)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setAlignTolerance(__float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTarget()"""
        return 'utils.Location'.__wrap(super(ReachOrientation, self).getTarget())

    @overload
    def setTimeToTarget(self, arg0: float) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setTimeToTarget(float)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setTimeToTarget(__float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setLimiter(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Location'):
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.utils.Location<T>)"""
        val = __ReachOrientation(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __ReachOrientation(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setEnabled(self, arg0: bool) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setEnabled(boolean)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getDecelerationRadius()"""
        return float.__wrap(super(ReachOrientation, self).getDecelerationRadius())

    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.getTimeToTarget()"""
        return float.__wrap(super(ReachOrientation, self).getTimeToTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'ReachOrientation':
        """public com.badlogic.gdx.ai.steer.behaviors.ReachOrientation<T> com.badlogic.gdx.ai.steer.behaviors.ReachOrientation.setDecelerationRadius(float)"""
        return 'ReachOrientation'.__wrap(super(__ReachOrientation, self).setDecelerationRadius(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Separation
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import com.badlogic.gdx.ai.steer.behaviors.Separation as __Separation
__Separation = __Separation
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.GroupBehavior as __GroupBehavior
__GroupBehavior = __GroupBehavior
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Separation():
    """com.badlogic.gdx.ai.steer.behaviors.Separation"""
 
    @staticmethod
    def __wrap(java_value: __Separation) -> 'Separation':
        return Separation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Separation):
        """
        Dynamic initializer for Separation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(__steer.GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.behaviors.Separation(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __Separation(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setEnabled(self, arg0: bool) -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setEnabled(boolean)"""
        return 'Separation'.__wrap(super(__Separation, self).setEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Separation'.__wrap(super(__Separation, self).setLimiter(arg0))

    @overload
    def setDecayCoefficient(self, arg0: float) -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setDecayCoefficient(float)"""
        return 'Separation'.__wrap(super(__Separation, self).setDecayCoefficient(__float.valueOf(arg0)))

    @overload
    def reportNeighbor(self, arg0: 'Steerable') -> bool:
        """public boolean com.badlogic.gdx.ai.steer.behaviors.Separation.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return bool.__wrap(super(__Separation, self).reportNeighbor(arg0))

    @override
    @overload
    def getProximity(self) -> 'steer.Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'steer.Proximity'.__wrap(super(steer.GroupBehavior, self).getProximity())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Separation':
        """public com.badlogic.gdx.ai.steer.behaviors.Separation<T> com.badlogic.gdx.ai.steer.behaviors.Separation.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Separation'.__wrap(super(__Separation, self).setOwner(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDecayCoefficient(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Separation.getDecayCoefficient()"""
        return float.__wrap(super(Separation, self).getDecayCoefficient())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Interpose
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.steer.behaviors.Interpose as __Interpose
__Interpose = __Interpose
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.steer.behaviors.Arrive as __Arrive
__Arrive = __Arrive
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringBehavior as __SteeringBehavior
__SteeringBehavior = __SteeringBehavior
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import int
 
class Interpose():
    """com.badlogic.gdx.ai.steer.behaviors.Interpose"""
 
    @staticmethod
    def __wrap(java_value: __Interpose) -> 'Interpose':
        return Interpose(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Interpose):
        """
        Dynamic initializer for Interpose.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: 'Steerable', arg3: float):
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __Interpose(arg0, arg1, arg2, __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTimeToTarget(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getTimeToTarget()"""
        return float.__wrap(super(Arrive, self).getTimeToTarget())

    @overload
    def setArrivalTolerance(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setArrivalTolerance(float)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setArrivalTolerance(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setOwner(arg0))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(steer.SteeringBehavior, self).isEnabled())

    @overload
    def getInternalTargetPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.behaviors.Interpose.getInternalTargetPosition()"""
        return 'math.Vector'.__wrap(super(Interpose, self).getInternalTargetPosition())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getInterpositionRatio(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Interpose.getInterpositionRatio()"""
        return float.__wrap(super(Interpose, self).getInterpositionRatio())

    @override
    @overload
    def getTarget(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.behaviors.Arrive.getTarget()"""
        return 'utils.Location'.__wrap(super(Arrive, self).getTarget())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setTarget(self, arg0: 'Location') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setTarget(com.badlogic.gdx.ai.utils.Location<T>)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setTarget(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'steer.Steerable'.__wrap(super(steer.SteeringBehavior, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getArrivalTolerance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getArrivalTolerance()"""
        return float.__wrap(super(Arrive, self).getArrivalTolerance())

    @overload
    def setEnabled(self, arg0: bool) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setEnabled(boolean)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def setAgentB(self, arg0: 'Steerable') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setAgentB(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setAgentB(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setLimiter(arg0))

    @overload
    def getAgentA(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.getAgentA()"""
        return 'steer.Steerable'.__wrap(super(Interpose, self).getAgentA())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'steer.SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'steer.SteeringAcceleration'.__wrap(super(__steer.SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getLimiter(self) -> 'steer.Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'steer.Limiter'.__wrap(super(steer.SteeringBehavior, self).getLimiter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAgentB(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.getAgentB()"""
        return 'steer.Steerable'.__wrap(super(Interpose, self).getAgentB())

    @overload
    def setTimeToTarget(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setTimeToTarget(float)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setTimeToTarget(__float.valueOf(arg0)))

    @overload
    def setInterpositionRatio(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setInterpositionRatio(float)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setInterpositionRatio(__float.valueOf(arg0)))

    @override
    @overload
    def getDecelerationRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.behaviors.Arrive.getDecelerationRadius()"""
        return float.__wrap(super(Arrive, self).getDecelerationRadius())

    @overload
    def setDecelerationRadius(self, arg0: float) -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setDecelerationRadius(float)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setDecelerationRadius(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Steerable', arg2: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __Interpose(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setAgentA(self, arg0: 'Steerable') -> 'Interpose':
        """public com.badlogic.gdx.ai.steer.behaviors.Interpose<T> com.badlogic.gdx.ai.steer.behaviors.Interpose.setAgentA(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'Interpose'.__wrap(super(__Interpose, self).setAgentA(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.behaviors.Jump$GravityComponentHandler
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.behaviors.Jump as __Jump_GravityComponentHandler
__GravityComponentHandler = __Jump_GravityComponentHandler.GravityComponentHandler
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from abc import abstractmethod, ABC
 
class GravityComponentHandler(ABC):
    """com.badlogic.gdx.ai.steer.behaviors.Jump.GravityComponentHandler"""
 
    @staticmethod
    def __wrap(java_value: __GravityComponentHandler) -> 'GravityComponentHandler':
        return GravityComponentHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GravityComponentHandler):
        """
        Dynamic initializer for GravityComponentHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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