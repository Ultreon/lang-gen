from __future__ import annotations
from overload import overload


 
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
import com.badlogic.gdx.ai.steer.GroupBehavior as __GroupBehavior
__GroupBehavior = __GroupBehavior
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GroupBehavior(ABC, __SteeringBehavior, SteeringBehavior):
    """com.badlogic.gdx.ai.steer.GroupBehavior"""
 
    @staticmethod
    def __wrap(java_value: __GroupBehavior) -> 'GroupBehavior':
        return GroupBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GroupBehavior):
        """
        Dynamic initializer for GroupBehavior.
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
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(__GroupBehavior, self).setProximity(arg0)

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.GroupBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __GroupBehavior(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getOwner(self) -> 'Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'Steerable'.__wrap(super(SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'Limiter'.__wrap(super(SteeringBehavior, self).getLimiter())

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

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'.__wrap(super(__SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getProximity(self) -> 'Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'Proximity'.__wrap(super(GroupBehavior, self).getProximity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(SteeringBehavior, self).isEnabled())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setLimiter(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setEnabled(boolean)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.GroupBehavior
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
import com.badlogic.gdx.ai.steer.GroupBehavior as __GroupBehavior
__GroupBehavior = __GroupBehavior
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GroupBehavior(ABC, __SteeringBehavior, SteeringBehavior):
    """com.badlogic.gdx.ai.steer.GroupBehavior"""
 
    @staticmethod
    def __wrap(java_value: __GroupBehavior) -> 'GroupBehavior':
        return GroupBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GroupBehavior):
        """
        Dynamic initializer for GroupBehavior.
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
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(__GroupBehavior, self).setProximity(arg0)

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.GroupBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = __GroupBehavior(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getOwner(self) -> 'Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'Steerable'.__wrap(super(SteeringBehavior, self).getOwner())

    @override
    @overload
    def getLimiter(self) -> 'Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'Limiter'.__wrap(super(SteeringBehavior, self).getLimiter())

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

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'.__wrap(super(__SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getProximity(self) -> 'Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'Proximity'.__wrap(super(GroupBehavior, self).getProximity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(SteeringBehavior, self).isEnabled())

    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setLimiter(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setEnabled(boolean)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.GroupBehavior 
 
 
# CLASS: com.badlogic.gdx.ai.steer.Steerable
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
 
class Steerable(ABC, ai.__Location, utils.Location, __Limiter, Limiter):
    """com.badlogic.gdx.ai.steer.Steerable"""
 
    @staticmethod
    def __wrap(java_value: __Steerable) -> 'Steerable':
        return Steerable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Steerable):
        """
        Dynamic initializer for Steerable.
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
    def getMaxLinearAcceleration(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxLinearAcceleration()"""
        pass

    @abstractmethod
    def setMaxLinearAcceleration(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxLinearAcceleration(float)"""
        pass

    @abstractmethod
    def setMaxAngularAcceleration(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxAngularAcceleration(float)"""
        pass

    @abstractmethod
    def newLocation(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.utils.Location.newLocation()"""
        pass

    @abstractmethod
    def getAngularVelocity(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Steerable.getAngularVelocity()"""
        pass

    @abstractmethod
    def getOrientation(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.Location.getOrientation()"""
        pass

    @abstractmethod
    def isTagged(self, ):
        """public abstract boolean com.badlogic.gdx.ai.steer.Steerable.isTagged()"""
        pass

    @abstractmethod
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setZeroLinearSpeedThreshold(float)"""
        pass

    @abstractmethod
    def setMaxLinearSpeed(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxLinearSpeed(float)"""
        pass

    @abstractmethod
    def vectorToAngle(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.ai.utils.Location.vectorToAngle(T)"""
        pass

    @abstractmethod
    def getMaxAngularSpeed(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxAngularSpeed()"""
        pass

    @abstractmethod
    def setOrientation(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.utils.Location.setOrientation(float)"""
        pass

    @abstractmethod
    def angleToVector(self, arg0: 'Vector', arg1: float):
        """public abstract T com.badlogic.gdx.ai.utils.Location.angleToVector(T,float)"""
        pass

    @abstractmethod
    def getPosition(self, ):
        """public abstract T com.badlogic.gdx.ai.utils.Location.getPosition()"""
        pass

    @abstractmethod
    def getZeroLinearSpeedThreshold(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getZeroLinearSpeedThreshold()"""
        pass

    @abstractmethod
    def getBoundingRadius(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Steerable.getBoundingRadius()"""
        pass

    @abstractmethod
    def setTagged(self, arg0: bool):
        """public abstract void com.badlogic.gdx.ai.steer.Steerable.setTagged(boolean)"""
        pass

    @abstractmethod
    def getMaxAngularAcceleration(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxAngularAcceleration()"""
        pass

    @abstractmethod
    def getLinearVelocity(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.Steerable.getLinearVelocity()"""
        pass

    @abstractmethod
    def getMaxLinearSpeed(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxLinearSpeed()"""
        pass

    @abstractmethod
    def setMaxAngularSpeed(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxAngularSpeed(float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteeringAcceleration
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.SteeringAcceleration as __SteeringAcceleration
__SteeringAcceleration = __SteeringAcceleration
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class SteeringAcceleration():
    """com.badlogic.gdx.ai.steer.SteeringAcceleration"""
 
    @staticmethod
    def __wrap(java_value: __SteeringAcceleration) -> 'SteeringAcceleration':
        return SteeringAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SteeringAcceleration):
        """
        Dynamic initializer for SteeringAcceleration.
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
    def __init__(self, arg0: 'Vector', arg1: float):
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration(T,float)"""
        val = __SteeringAcceleration(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.add(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'.__wrap(super(__SteeringAcceleration, self).add(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Vector'):
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration(T)"""
        val = __SteeringAcceleration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def calculateSquareMagnitude(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteeringAcceleration.calculateSquareMagnitude()"""
        return float.__wrap(super(SteeringAcceleration, self).calculateSquareMagnitude())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringAcceleration.isZero()"""
        return bool.__wrap(super(SteeringAcceleration, self).isZero())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setZero(self) -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.setZero()"""
        return 'SteeringAcceleration'.__wrap(super(SteeringAcceleration, self).setZero())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def scl(self, arg0: float) -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.scl(float)"""
        return 'SteeringAcceleration'.__wrap(super(__SteeringAcceleration, self).scl(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def mulAdd(self, arg0: 'SteeringAcceleration', arg1: float) -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.mulAdd(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>,float)"""
        return 'SteeringAcceleration'.__wrap(super(__SteeringAcceleration, self).mulAdd(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def calculateMagnitude(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteeringAcceleration.calculateMagnitude()"""
        return float.__wrap(super(SteeringAcceleration, self).calculateMagnitude())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.Limiter
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.steer.Limiter as __Limiter
__Limiter = __Limiter
 
class Limiter(ABC):
    """com.badlogic.gdx.ai.steer.Limiter"""
 
    @staticmethod
    def __wrap(java_value: __Limiter) -> 'Limiter':
        return Limiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Limiter):
        """
        Dynamic initializer for Limiter.
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
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setZeroLinearSpeedThreshold(float)"""
        pass

    @abstractmethod
    def setMaxLinearSpeed(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxLinearSpeed(float)"""
        pass

    @abstractmethod
    def getMaxLinearAcceleration(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxLinearAcceleration()"""
        pass

    @abstractmethod
    def getMaxAngularSpeed(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxAngularSpeed()"""
        pass

    @abstractmethod
    def setMaxLinearAcceleration(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxLinearAcceleration(float)"""
        pass

    @abstractmethod
    def setMaxAngularAcceleration(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxAngularAcceleration(float)"""
        pass

    @abstractmethod
    def getZeroLinearSpeedThreshold(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getZeroLinearSpeedThreshold()"""
        pass

    @abstractmethod
    def getMaxAngularAcceleration(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxAngularAcceleration()"""
        pass

    @abstractmethod
    def getMaxLinearSpeed(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.Limiter.getMaxLinearSpeed()"""
        pass

    @abstractmethod
    def setMaxAngularSpeed(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.Limiter.setMaxAngularSpeed(float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SteeringBehavior(ABC):
    """com.badlogic.gdx.ai.steer.SteeringBehavior"""
 
    @staticmethod
    def __wrap(java_value: __SteeringBehavior) -> 'SteeringBehavior':
        return SteeringBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SteeringBehavior):
        """
        Dynamic initializer for SteeringBehavior.
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
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = __SteeringBehavior(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Limiter', arg2: bool):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Limiter,boolean)"""
        val = __SteeringBehavior(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setOwner(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: bool):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,boolean)"""
        val = __SteeringBehavior(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool.__wrap(super(SteeringBehavior, self).isEnabled())

    @overload
    def getLimiter(self) -> 'Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'Limiter'.__wrap(super(SteeringBehavior, self).getLimiter())

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

    @overload
    def getOwner(self) -> 'Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'Steerable'.__wrap(super(SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Limiter'):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Limiter)"""
        val = __SteeringBehavior(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'.__wrap(super(__SteeringBehavior, self).calculateSteering(arg0))

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
    def setLimiter(self, arg0: 'Limiter') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setLimiter(arg0))

    @overload
    def setEnabled(self, arg0: bool) -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setEnabled(boolean)"""
        return 'SteeringBehavior'.__wrap(super(__SteeringBehavior, self).setEnabled(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.Proximity
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
from abc import abstractmethod, ABC
 
class Proximity(ABC):
    """com.badlogic.gdx.ai.steer.Proximity"""
 
    @staticmethod
    def __wrap(java_value: __Proximity) -> 'Proximity':
        return Proximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Proximity):
        """
        Dynamic initializer for Proximity.
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
    def getOwner(self, ):
        """public abstract com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.Proximity.getOwner()"""
        pass

    @abstractmethod
    def findNeighbors(self, arg0: 'ProximityCallback'):
        """public abstract int com.badlogic.gdx.ai.steer.Proximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        pass

    @abstractmethod
    def setOwner(self, arg0: 'Steerable'):
        """public abstract void com.badlogic.gdx.ai.steer.Proximity.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.Proximity$ProximityCallback
import com.badlogic.gdx.ai.steer.Proximity as __Proximity_ProximityCallback
__ProximityCallback = __Proximity_ProximityCallback.ProximityCallback
from abc import abstractmethod, ABC
 
class ProximityCallback(ABC):
    """com.badlogic.gdx.ai.steer.Proximity.ProximityCallback"""
 
    @staticmethod
    def __wrap(java_value: __ProximityCallback) -> 'ProximityCallback':
        return ProximityCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProximityCallback):
        """
        Dynamic initializer for ProximityCallback.
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
    def reportNeighbor(self, arg0: 'Steerable'):
        """public abstract boolean com.badlogic.gdx.ai.steer.Proximity$ProximityCallback.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteerableAdapter
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.steer.SteerableAdapter as __SteerableAdapter
__SteerableAdapter = __SteerableAdapter
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class SteerableAdapter(__Steerable, Steerable):
    """com.badlogic.gdx.ai.steer.SteerableAdapter"""
 
    @staticmethod
    def __wrap(java_value: __SteerableAdapter) -> 'SteerableAdapter':
        return SteerableAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SteerableAdapter):
        """
        Dynamic initializer for SteerableAdapter.
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
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxLinearAcceleration()"""
        return float.__wrap(super(SteerableAdapter, self).getMaxLinearAcceleration())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setZeroLinearSpeedThreshold(float)"""
        super(__SteerableAdapter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxLinearSpeed(float)"""
        super(__SteerableAdapter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def getLinearVelocity(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.getLinearVelocity()"""
        return 'math.Vector'.__wrap(super(SteerableAdapter, self).getLinearVelocity())

    @overload
    def vectorToAngle(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.vectorToAngle(T)"""
        return float.__wrap(super(__SteerableAdapter, self).vectorToAngle(arg0))

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxAngularSpeed()"""
        return float.__wrap(super(SteerableAdapter, self).getMaxAngularSpeed())

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxAngularAcceleration(float)"""
        super(__SteerableAdapter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def newLocation(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.SteerableAdapter.newLocation()"""
        return 'utils.Location'.__wrap(super(SteerableAdapter, self).newLocation())

    @override
    @overload
    def getPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.getPosition()"""
        return 'math.Vector'.__wrap(super(SteerableAdapter, self).getPosition())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getBoundingRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getBoundingRadius()"""
        return float.__wrap(super(SteerableAdapter, self).getBoundingRadius())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getOrientation()"""
        return float.__wrap(super(SteerableAdapter, self).getOrientation())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxAngularSpeed(float)"""
        super(__SteerableAdapter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.SteerableAdapter()"""
        val = __SteerableAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.SteerableAdapter()"""
        val = __SteerableAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def angleToVector(self, arg0: 'Vector', arg1: float) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.angleToVector(T,float)"""
        return 'math.Vector'.__wrap(super(__SteerableAdapter, self).angleToVector(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxLinearAcceleration(float)"""
        super(__SteerableAdapter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(SteerableAdapter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def setOrientation(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setOrientation(float)"""
        super(__SteerableAdapter, self).setOrientation(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxLinearSpeed()"""
        return float.__wrap(super(SteerableAdapter, self).getMaxLinearSpeed())

    @override
    @overload
    def getAngularVelocity(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getAngularVelocity()"""
        return float.__wrap(super(SteerableAdapter, self).getAngularVelocity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setTagged(self, arg0: bool):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setTagged(boolean)"""
        super(__SteerableAdapter, self).setTagged(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxAngularAcceleration()"""
        return float.__wrap(super(SteerableAdapter, self).getMaxAngularAcceleration())

    @override
    @overload
    def isTagged(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteerableAdapter.isTagged()"""
        return bool.__wrap(super(SteerableAdapter, self).isTagged())