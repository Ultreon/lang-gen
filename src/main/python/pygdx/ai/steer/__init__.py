from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.SteerableAdapter as _SteerableAdapter
_SteerableAdapter = _SteerableAdapter
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
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
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

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SteerableAdapter():
    """com.badlogic.gdx.ai.steer.SteerableAdapter"""
 
    @staticmethod
    def _wrap(java_value: _SteerableAdapter) -> 'SteerableAdapter':
        return SteerableAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SteerableAdapter):
        """
        Dynamic initializer for SteerableAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SteerableAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SteerableAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setOrientation(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setOrientation(float)"""
        super(_SteerableAdapter, self).setOrientation(_float.valueOf(arg0))

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxLinearAcceleration()"""
        return float._wrap(super(SteerableAdapter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxAngularSpeed()"""
        return float._wrap(super(SteerableAdapter, self).getMaxAngularSpeed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxLinearSpeed(float)"""
        super(_SteerableAdapter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def newLocation(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.SteerableAdapter.newLocation()"""
        return 'utils.Location'._wrap(super(SteerableAdapter, self).newLocation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isTagged(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteerableAdapter.isTagged()"""
        return bool._wrap(super(SteerableAdapter, self).isTagged())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(SteerableAdapter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxAngularAcceleration(float)"""
        super(_SteerableAdapter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxAngularSpeed(float)"""
        super(_SteerableAdapter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def getOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getOrientation()"""
        return float._wrap(super(SteerableAdapter, self).getOrientation())

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxAngularAcceleration()"""
        return float._wrap(super(SteerableAdapter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxLinearSpeed()"""
        return float._wrap(super(SteerableAdapter, self).getMaxLinearSpeed())

    @override
    @overload
    def getBoundingRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getBoundingRadius()"""
        return float._wrap(super(SteerableAdapter, self).getBoundingRadius())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.SteerableAdapter()"""
        val = _SteerableAdapter()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.SteerableAdapter()"""
        val = _SteerableAdapter()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getAngularVelocity(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getAngularVelocity()"""
        return float._wrap(super(SteerableAdapter, self).getAngularVelocity())

    @overload
    def vectorToAngle(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.vectorToAngle(T)"""
        return float._wrap(super(_SteerableAdapter, self).vectorToAngle(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setTagged(self, arg0: bool):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setTagged(boolean)"""
        super(_SteerableAdapter, self).setTagged(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setZeroLinearSpeedThreshold(float)"""
        super(_SteerableAdapter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.getPosition()"""
        return 'math.Vector'._wrap(super(SteerableAdapter, self).getPosition())

    @override
    @overload
    def getLinearVelocity(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.getLinearVelocity()"""
        return 'math.Vector'._wrap(super(SteerableAdapter, self).getLinearVelocity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def angleToVector(self, arg0: 'Vector', arg1: float) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.angleToVector(T,float)"""
        return 'math.Vector'._wrap(super(_SteerableAdapter, self).angleToVector(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxLinearAcceleration(float)"""
        super(_SteerableAdapter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteerableAdapter
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.SteerableAdapter as _SteerableAdapter
_SteerableAdapter = _SteerableAdapter
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
import java.lang.Boolean as _boolean
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
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

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SteerableAdapter():
    """com.badlogic.gdx.ai.steer.SteerableAdapter"""
 
    @staticmethod
    def _wrap(java_value: _SteerableAdapter) -> 'SteerableAdapter':
        return SteerableAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SteerableAdapter):
        """
        Dynamic initializer for SteerableAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SteerableAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SteerableAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setOrientation(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setOrientation(float)"""
        super(_SteerableAdapter, self).setOrientation(_float.valueOf(arg0))

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxLinearAcceleration()"""
        return float._wrap(super(SteerableAdapter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxAngularSpeed()"""
        return float._wrap(super(SteerableAdapter, self).getMaxAngularSpeed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxLinearSpeed(float)"""
        super(_SteerableAdapter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def newLocation(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.steer.SteerableAdapter.newLocation()"""
        return 'utils.Location'._wrap(super(SteerableAdapter, self).newLocation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isTagged(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteerableAdapter.isTagged()"""
        return bool._wrap(super(SteerableAdapter, self).isTagged())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(SteerableAdapter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxAngularAcceleration(float)"""
        super(_SteerableAdapter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxAngularSpeed(float)"""
        super(_SteerableAdapter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def getOrientation(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getOrientation()"""
        return float._wrap(super(SteerableAdapter, self).getOrientation())

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxAngularAcceleration()"""
        return float._wrap(super(SteerableAdapter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getMaxLinearSpeed()"""
        return float._wrap(super(SteerableAdapter, self).getMaxLinearSpeed())

    @override
    @overload
    def getBoundingRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getBoundingRadius()"""
        return float._wrap(super(SteerableAdapter, self).getBoundingRadius())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.SteerableAdapter()"""
        val = _SteerableAdapter()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.SteerableAdapter()"""
        val = _SteerableAdapter()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getAngularVelocity(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.getAngularVelocity()"""
        return float._wrap(super(SteerableAdapter, self).getAngularVelocity())

    @overload
    def vectorToAngle(self, arg0: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.SteerableAdapter.vectorToAngle(T)"""
        return float._wrap(super(_SteerableAdapter, self).vectorToAngle(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setTagged(self, arg0: bool):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setTagged(boolean)"""
        super(_SteerableAdapter, self).setTagged(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setZeroLinearSpeedThreshold(float)"""
        super(_SteerableAdapter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getPosition(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.getPosition()"""
        return 'math.Vector'._wrap(super(SteerableAdapter, self).getPosition())

    @override
    @overload
    def getLinearVelocity(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.getLinearVelocity()"""
        return 'math.Vector'._wrap(super(SteerableAdapter, self).getLinearVelocity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def angleToVector(self, arg0: 'Vector', arg1: float) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.SteerableAdapter.angleToVector(T,float)"""
        return 'math.Vector'._wrap(super(_SteerableAdapter, self).angleToVector(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.SteerableAdapter.setMaxLinearAcceleration(float)"""
        super(_SteerableAdapter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteerableAdapter 
 
 
# CLASS: com.badlogic.gdx.ai.steer.Proximity
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
from abc import abstractmethod, ABC
 
class Proximity():
    """com.badlogic.gdx.ai.steer.Proximity"""
 
    @staticmethod
    def _wrap(java_value: _Proximity) -> 'Proximity':
        return Proximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Proximity):
        """
        Dynamic initializer for Proximity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Proximity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Proximity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteeringBehavior
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
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SteeringBehavior():
    """com.badlogic.gdx.ai.steer.SteeringBehavior"""
 
    @staticmethod
    def _wrap(java_value: _SteeringBehavior) -> 'SteeringBehavior':
        return SteeringBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SteeringBehavior):
        """
        Dynamic initializer for SteeringBehavior.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SteeringBehavior__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SteeringBehavior__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'SteeringBehavior'._wrap(super(_SteeringBehavior, self).setLimiter(arg0))

    @overload
    def getLimiter(self) -> 'Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'Limiter'._wrap(super(SteeringBehavior, self).getLimiter())

    @overload
    def __init__(self, arg0: 'Steerable'):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        val = _SteeringBehavior(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setEnabled(self, arg0: bool) -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setEnabled(boolean)"""
        return 'SteeringBehavior'._wrap(super(_SteeringBehavior, self).setEnabled(_boolean.valueOf(arg0)))

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
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringBehavior.isEnabled()"""
        return bool._wrap(super(SteeringBehavior, self).isEnabled())

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
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'._wrap(super(_SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getOwner(self) -> 'Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'Steerable'._wrap(super(SteeringBehavior, self).getOwner())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Limiter'):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Limiter)"""
        val = _SteeringBehavior(arg0, arg1)
        self.__wrapper = val

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'SteeringBehavior'._wrap(super(_SteeringBehavior, self).setOwner(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: bool):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,boolean)"""
        val = _SteeringBehavior(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Limiter', arg2: bool):
        """public com.badlogic.gdx.ai.steer.SteeringBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Limiter,boolean)"""
        val = _SteeringBehavior(arg0, arg1, _boolean.valueOf(arg2))
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
 
 
# CLASS: com.badlogic.gdx.ai.steer.GroupBehavior
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
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.SteeringBehavior as _SteeringBehavior
_SteeringBehavior = _SteeringBehavior
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.GroupBehavior as _GroupBehavior
_GroupBehavior = _GroupBehavior
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GroupBehavior():
    """com.badlogic.gdx.ai.steer.GroupBehavior"""
 
    @staticmethod
    def _wrap(java_value: _GroupBehavior) -> 'GroupBehavior':
        return GroupBehavior(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GroupBehavior):
        """
        Dynamic initializer for GroupBehavior.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GroupBehavior__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GroupBehavior__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setLimiter(self, arg0: 'Limiter') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setLimiter(com.badlogic.gdx.ai.steer.Limiter)"""
        return 'SteeringBehavior'._wrap(super(_SteeringBehavior, self).setLimiter(arg0))

    @overload
    def getProximity(self) -> 'Proximity':
        """public com.badlogic.gdx.ai.steer.Proximity<T> com.badlogic.gdx.ai.steer.GroupBehavior.getProximity()"""
        return 'Proximity'._wrap(super(GroupBehavior, self).getProximity())

    @overload
    def setProximity(self, arg0: 'Proximity'):
        """public void com.badlogic.gdx.ai.steer.GroupBehavior.setProximity(com.badlogic.gdx.ai.steer.Proximity<T>)"""
        super(_GroupBehavior, self).setProximity(arg0)

    @override
    @overload
    def getLimiter(self) -> 'Limiter':
        """public com.badlogic.gdx.ai.steer.Limiter com.badlogic.gdx.ai.steer.SteeringBehavior.getLimiter()"""
        return 'Limiter'._wrap(super(SteeringBehavior, self).getLimiter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setEnabled(self, arg0: bool) -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setEnabled(boolean)"""
        return 'SteeringBehavior'._wrap(super(_SteeringBehavior, self).setEnabled(_boolean.valueOf(arg0)))

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
        return bool._wrap(super(SteeringBehavior, self).isEnabled())

    @override
    @overload
    def getOwner(self) -> 'Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.SteeringBehavior.getOwner()"""
        return 'Steerable'._wrap(super(SteeringBehavior, self).getOwner())

    @overload
    def calculateSteering(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringBehavior.calculateSteering(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'._wrap(super(_SteeringBehavior, self).calculateSteering(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Proximity'):
        """public com.badlogic.gdx.ai.steer.GroupBehavior(com.badlogic.gdx.ai.steer.Steerable<T>,com.badlogic.gdx.ai.steer.Proximity<T>)"""
        val = _GroupBehavior(arg0, arg1)
        self.__wrapper = val

    @overload
    def setOwner(self, arg0: 'Steerable') -> 'SteeringBehavior':
        """public com.badlogic.gdx.ai.steer.SteeringBehavior<T> com.badlogic.gdx.ai.steer.SteeringBehavior.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        return 'SteeringBehavior'._wrap(super(_SteeringBehavior, self).setOwner(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.steer.SteeringAcceleration
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
import com.badlogic.gdx.ai.steer.SteeringAcceleration as _SteeringAcceleration
_SteeringAcceleration = _SteeringAcceleration
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
 
class SteeringAcceleration():
    """com.badlogic.gdx.ai.steer.SteeringAcceleration"""
 
    @staticmethod
    def _wrap(java_value: _SteeringAcceleration) -> 'SteeringAcceleration':
        return SteeringAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SteeringAcceleration):
        """
        Dynamic initializer for SteeringAcceleration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SteeringAcceleration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SteeringAcceleration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def calculateMagnitude(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteeringAcceleration.calculateMagnitude()"""
        return float._wrap(super(SteeringAcceleration, self).calculateMagnitude())

    @overload
    def __init__(self, arg0: 'Vector'):
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration(T)"""
        val = _SteeringAcceleration(arg0)
        self.__wrapper = val

    @overload
    def mulAdd(self, arg0: 'SteeringAcceleration', arg1: float) -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.mulAdd(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>,float)"""
        return 'SteeringAcceleration'._wrap(super(_SteeringAcceleration, self).mulAdd(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def calculateSquareMagnitude(self) -> float:
        """public float com.badlogic.gdx.ai.steer.SteeringAcceleration.calculateSquareMagnitude()"""
        return float._wrap(super(SteeringAcceleration, self).calculateSquareMagnitude())

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
    def setZero(self) -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.setZero()"""
        return 'SteeringAcceleration'._wrap(super(SteeringAcceleration, self).setZero())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Vector', arg1: float):
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration(T,float)"""
        val = _SteeringAcceleration(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def add(self, arg0: 'SteeringAcceleration') -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.add(com.badlogic.gdx.ai.steer.SteeringAcceleration<T>)"""
        return 'SteeringAcceleration'._wrap(super(_SteeringAcceleration, self).add(arg0))

    @overload
    def isZero(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.SteeringAcceleration.isZero()"""
        return bool._wrap(super(SteeringAcceleration, self).isZero())

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

    @overload
    def scl(self, arg0: float) -> 'SteeringAcceleration':
        """public com.badlogic.gdx.ai.steer.SteeringAcceleration<T> com.badlogic.gdx.ai.steer.SteeringAcceleration.scl(float)"""
        return 'SteeringAcceleration'._wrap(super(_SteeringAcceleration, self).scl(_float.valueOf(arg0)))

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
 
 
# CLASS: com.badlogic.gdx.ai.steer.Proximity$ProximityCallback
import com.badlogic.gdx.ai.steer.Proximity as _Proximity_ProximityCallback
_ProximityCallback = _Proximity_ProximityCallback.ProximityCallback
from abc import abstractmethod, ABC
 
class ProximityCallback():
    """com.badlogic.gdx.ai.steer.Proximity.ProximityCallback"""
 
    @staticmethod
    def _wrap(java_value: _ProximityCallback) -> 'ProximityCallback':
        return ProximityCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProximityCallback):
        """
        Dynamic initializer for ProximityCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProximityCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProximityCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reportNeighbor(self, arg0: 'Steerable'):
        """public abstract boolean com.badlogic.gdx.ai.steer.Proximity$ProximityCallback.reportNeighbor(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.Limiter
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
 
class Limiter():
    """com.badlogic.gdx.ai.steer.Limiter"""
 
    @staticmethod
    def _wrap(java_value: _Limiter) -> 'Limiter':
        return Limiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Limiter):
        """
        Dynamic initializer for Limiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Limiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Limiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.steer.Steerable
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.ai.steer.Limiter as _Limiter
_Limiter = _Limiter
 
class Steerable():
    """com.badlogic.gdx.ai.steer.Steerable"""
 
    @staticmethod
    def _wrap(java_value: _Steerable) -> 'Steerable':
        return Steerable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Steerable):
        """
        Dynamic initializer for Steerable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Steerable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Steerable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def getPosition(self, ):
        """public abstract T com.badlogic.gdx.ai.utils.Location.getPosition()"""
        pass

    @abstractmethod
    def angleToVector(self, arg0: 'Vector', arg1: float):
        """public abstract T com.badlogic.gdx.ai.utils.Location.angleToVector(T,float)"""
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