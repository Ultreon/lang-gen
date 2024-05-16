from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.FullLimiter as __FullLimiter
__FullLimiter = __FullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FullLimiter():
    """com.badlogic.gdx.ai.steer.limiters.FullLimiter"""
 
    @staticmethod
    def __wrap(java_value: __FullLimiter) -> 'FullLimiter':
        return FullLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FullLimiter):
        """
        Dynamic initializer for FullLimiter.
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
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(FullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(FullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxLinearAcceleration(float)"""
        super(__FullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(FullLimiter, self).getMaxLinearAcceleration())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.limiters.FullLimiter(float,float,float,float)"""
        val = __FullLimiter(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxLinearSpeed(float)"""
        super(__FullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxAngularSpeed(float)"""
        super(__FullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

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
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxAngularAcceleration(float)"""
        super(__FullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(FullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__FullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(FullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.FullLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.FullLimiter as __FullLimiter
__FullLimiter = __FullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FullLimiter():
    """com.badlogic.gdx.ai.steer.limiters.FullLimiter"""
 
    @staticmethod
    def __wrap(java_value: __FullLimiter) -> 'FullLimiter':
        return FullLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FullLimiter):
        """
        Dynamic initializer for FullLimiter.
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
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(FullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(FullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxLinearAcceleration(float)"""
        super(__FullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(FullLimiter, self).getMaxLinearAcceleration())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.limiters.FullLimiter(float,float,float,float)"""
        val = __FullLimiter(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxLinearSpeed(float)"""
        super(__FullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxAngularSpeed(float)"""
        super(__FullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

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
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxAngularAcceleration(float)"""
        super(__FullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(FullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__FullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(FullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.FullLimiter 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter as __LinearAccelerationLimiter
__LinearAccelerationLimiter = __LinearAccelerationLimiter
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinearAccelerationLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter"""
 
    @staticmethod
    def __wrap(java_value: __LinearAccelerationLimiter) -> 'LinearAccelerationLimiter':
        return LinearAccelerationLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinearAccelerationLimiter):
        """
        Dynamic initializer for LinearAccelerationLimiter.
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
        """public float com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(LinearAccelerationLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter(float)"""
        val = __LinearAccelerationLimiter(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter.setMaxLinearAcceleration(float)"""
        super(__LinearAccelerationLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(__NullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(__NullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(__NullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.NullLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NullLimiter():
    """com.badlogic.gdx.ai.steer.limiters.NullLimiter"""
 
    @staticmethod
    def __wrap(java_value: __NullLimiter) -> 'NullLimiter':
        return NullLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullLimiter):
        """
        Dynamic initializer for NullLimiter.
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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.limiters.NullLimiter()"""
        val = __NullLimiter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.limiters.NullLimiter()"""
        val = __NullLimiter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

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
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(__NullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(__NullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(__NullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(__NullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.AngularLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.limiters.AngularLimiter as __AngularLimiter
__AngularLimiter = __AngularLimiter
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AngularLimiter():
    """com.badlogic.gdx.ai.steer.limiters.AngularLimiter"""
 
    @staticmethod
    def __wrap(java_value: __AngularLimiter) -> 'AngularLimiter':
        return AngularLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AngularLimiter):
        """
        Dynamic initializer for AngularLimiter.
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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.steer.limiters.AngularLimiter(float,float)"""
        val = __AngularLimiter(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(AngularLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

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
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularLimiter.setMaxAngularSpeed(float)"""
        super(__AngularLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(__NullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(__NullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularLimiter.setMaxAngularAcceleration(float)"""
        super(__AngularLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(AngularLimiter, self).getMaxAngularSpeed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter
from builtins import str
import com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter as __AngularSpeedLimiter
__AngularSpeedLimiter = __AngularSpeedLimiter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AngularSpeedLimiter():
    """com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter"""
 
    @staticmethod
    def __wrap(java_value: __AngularSpeedLimiter) -> 'AngularSpeedLimiter':
        return AngularSpeedLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AngularSpeedLimiter):
        """
        Dynamic initializer for AngularSpeedLimiter.
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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter(float)"""
        val = __AngularSpeedLimiter(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

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
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(AngularSpeedLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(__NullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(__NullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(__NullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

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
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter.setMaxAngularSpeed(float)"""
        super(__AngularSpeedLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearLimiter
from builtins import str
import com.badlogic.gdx.ai.steer.limiters.LinearLimiter as __LinearLimiter
__LinearLimiter = __LinearLimiter
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinearLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearLimiter"""
 
    @staticmethod
    def __wrap(java_value: __LinearLimiter) -> 'LinearLimiter':
        return LinearLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinearLimiter):
        """
        Dynamic initializer for LinearLimiter.
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

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(LinearLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

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
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearLimiter.setMaxLinearAcceleration(float)"""
        super(__LinearLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearLimiter.setMaxLinearSpeed(float)"""
        super(__LinearLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearLimiter(float,float)"""
        val = __LinearLimiter(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(__NullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(__NullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

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
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(LinearLimiter, self).getMaxLinearAcceleration()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter as __AngularAccelerationLimiter
__AngularAccelerationLimiter = __AngularAccelerationLimiter
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AngularAccelerationLimiter():
    """com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter"""
 
    @staticmethod
    def __wrap(java_value: __AngularAccelerationLimiter) -> 'AngularAccelerationLimiter':
        return AngularAccelerationLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AngularAccelerationLimiter):
        """
        Dynamic initializer for AngularAccelerationLimiter.
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

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter.setMaxAngularAcceleration(float)"""
        super(__AngularAccelerationLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(AngularAccelerationLimiter, self).getMaxAngularAcceleration())

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter(float)"""
        val = __AngularAccelerationLimiter(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(__NullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(__NullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(__NullLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as __NullLimiter
__NullLimiter = __NullLimiter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter as __LinearSpeedLimiter
__LinearSpeedLimiter = __LinearSpeedLimiter
from builtins import int
 
class LinearSpeedLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter"""
 
    @staticmethod
    def __wrap(java_value: __LinearSpeedLimiter) -> 'LinearSpeedLimiter':
        return LinearSpeedLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinearSpeedLimiter):
        """
        Dynamic initializer for LinearSpeedLimiter.
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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter(float)"""
        val = __LinearSpeedLimiter(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float.__wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter.setMaxLinearSpeed(float)"""
        super(__LinearSpeedLimiter, self).setMaxLinearSpeed(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(__NullLimiter, self).setZeroLinearSpeedThreshold(__float.valueOf(arg0))

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
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float.__wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(__NullLimiter, self).setMaxLinearAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(__NullLimiter, self).setMaxAngularSpeed(__float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(__NullLimiter, self).setMaxAngularAcceleration(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter.getMaxLinearSpeed()"""
        return float.__wrap(super(LinearSpeedLimiter, self).getMaxLinearSpeed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))