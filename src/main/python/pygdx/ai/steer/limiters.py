from __future__ import annotations
from overload import overload


 
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
import com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter as _LinearAccelerationLimiter
_LinearAccelerationLimiter = _LinearAccelerationLimiter
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinearAccelerationLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter"""
 
    @staticmethod
    def _wrap(java_value: _LinearAccelerationLimiter) -> 'LinearAccelerationLimiter':
        return LinearAccelerationLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinearAccelerationLimiter):
        """
        Dynamic initializer for LinearAccelerationLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinearAccelerationLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinearAccelerationLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularSpeed())

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
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(_NullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter(float)"""
        val = _LinearAccelerationLimiter(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(_NullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(_NullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter.setMaxLinearAcceleration(float)"""
        super(_LinearAccelerationLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(LinearAccelerationLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter
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
import com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter as _LinearAccelerationLimiter
_LinearAccelerationLimiter = _LinearAccelerationLimiter
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinearAccelerationLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter"""
 
    @staticmethod
    def _wrap(java_value: _LinearAccelerationLimiter) -> 'LinearAccelerationLimiter':
        return LinearAccelerationLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinearAccelerationLimiter):
        """
        Dynamic initializer for LinearAccelerationLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinearAccelerationLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinearAccelerationLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularSpeed())

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
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(_NullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter(float)"""
        val = _LinearAccelerationLimiter(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(_NullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(_NullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter.setMaxLinearAcceleration(float)"""
        super(_LinearAccelerationLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(LinearAccelerationLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearAccelerationLimiter 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter as _AngularSpeedLimiter
_AngularSpeedLimiter = _AngularSpeedLimiter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AngularSpeedLimiter():
    """com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter"""
 
    @staticmethod
    def _wrap(java_value: _AngularSpeedLimiter) -> 'AngularSpeedLimiter':
        return AngularSpeedLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AngularSpeedLimiter):
        """
        Dynamic initializer for AngularSpeedLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AngularSpeedLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AngularSpeedLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(AngularSpeedLimiter, self).getMaxAngularSpeed())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter(float)"""
        val = _AngularSpeedLimiter(_float.valueOf(arg0))
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
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(_NullLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(_NullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(_NullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularSpeedLimiter.setMaxAngularSpeed(float)"""
        super(_AngularSpeedLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter as _LinearSpeedLimiter
_LinearSpeedLimiter = _LinearSpeedLimiter
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinearSpeedLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter"""
 
    @staticmethod
    def _wrap(java_value: _LinearSpeedLimiter) -> 'LinearSpeedLimiter':
        return LinearSpeedLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinearSpeedLimiter):
        """
        Dynamic initializer for LinearSpeedLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinearSpeedLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinearSpeedLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularSpeed())

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

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(_NullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(_NullLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(_NullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter(float)"""
        val = _LinearSpeedLimiter(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(LinearSpeedLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearSpeedLimiter.setMaxLinearSpeed(float)"""
        super(_LinearSpeedLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.LinearLimiter
from builtins import str
import com.badlogic.gdx.ai.steer.limiters.LinearLimiter as _LinearLimiter
_LinearLimiter = _LinearLimiter
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
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinearLimiter():
    """com.badlogic.gdx.ai.steer.limiters.LinearLimiter"""
 
    @staticmethod
    def _wrap(java_value: _LinearLimiter) -> 'LinearLimiter':
        return LinearLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinearLimiter):
        """
        Dynamic initializer for LinearLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinearLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinearLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularSpeed())

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
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(LinearLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(_NullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearLimiter.setMaxLinearSpeed(float)"""
        super(_LinearLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

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
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.LinearLimiter.setMaxLinearAcceleration(float)"""
        super(_LinearLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(_NullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.LinearLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(LinearLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.steer.limiters.LinearLimiter(float,float)"""
        val = _LinearLimiter(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.NullLimiter
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
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullLimiter():
    """com.badlogic.gdx.ai.steer.limiters.NullLimiter"""
 
    @staticmethod
    def _wrap(java_value: _NullLimiter) -> 'NullLimiter':
        return NullLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullLimiter):
        """
        Dynamic initializer for NullLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularSpeed())

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
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(_NullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(_NullLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(_NullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularAcceleration(float)"""
        super(_NullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.limiters.NullLimiter()"""
        val = _NullLimiter()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.limiters.NullLimiter()"""
        val = _NullLimiter()
        self.__wrapper = val

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.AngularLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.limiters.AngularLimiter as _AngularLimiter
_AngularLimiter = _AngularLimiter
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AngularLimiter():
    """com.badlogic.gdx.ai.steer.limiters.AngularLimiter"""
 
    @staticmethod
    def _wrap(java_value: _AngularLimiter) -> 'AngularLimiter':
        return AngularLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AngularLimiter):
        """
        Dynamic initializer for AngularLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AngularLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AngularLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularLimiter.setMaxAngularSpeed(float)"""
        super(_AngularLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

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
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.steer.limiters.AngularLimiter(float,float)"""
        val = _AngularLimiter(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(_NullLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(_NullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularLimiter.setMaxAngularAcceleration(float)"""
        super(_AngularLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(AngularLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(AngularLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.FullLimiter
import com.badlogic.gdx.ai.steer.limiters.FullLimiter as _FullLimiter
_FullLimiter = _FullLimiter
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FullLimiter():
    """com.badlogic.gdx.ai.steer.limiters.FullLimiter"""
 
    @staticmethod
    def _wrap(java_value: _FullLimiter) -> 'FullLimiter':
        return FullLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FullLimiter):
        """
        Dynamic initializer for FullLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FullLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FullLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_FullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(FullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxLinearAcceleration(float)"""
        super(_FullLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

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
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxLinearSpeed(float)"""
        super(_FullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(FullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxAngularAcceleration(float)"""
        super(_FullLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

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
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(FullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(FullLimiter, self).getZeroLinearSpeedThreshold())

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
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.limiters.FullLimiter(float,float,float,float)"""
        val = _FullLimiter(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.FullLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(FullLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.FullLimiter.setMaxAngularSpeed(float)"""
        super(_FullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter
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
import com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter as _AngularAccelerationLimiter
_AngularAccelerationLimiter = _AngularAccelerationLimiter
from builtins import bool
import com.badlogic.gdx.ai.steer.limiters.NullLimiter as _NullLimiter
_NullLimiter = _NullLimiter
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AngularAccelerationLimiter():
    """com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter"""
 
    @staticmethod
    def _wrap(java_value: _AngularAccelerationLimiter) -> 'AngularAccelerationLimiter':
        return AngularAccelerationLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AngularAccelerationLimiter):
        """
        Dynamic initializer for AngularAccelerationLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AngularAccelerationLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AngularAccelerationLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getMaxAngularSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxAngularSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxAngularSpeed())

    @override
    @overload
    def getMaxAngularAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter.getMaxAngularAcceleration()"""
        return float._wrap(super(AngularAccelerationLimiter, self).getMaxAngularAcceleration())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter(float)"""
        val = _AngularAccelerationLimiter(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setMaxAngularAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.AngularAccelerationLimiter.setMaxAngularAcceleration(float)"""
        super(_AngularAccelerationLimiter, self).setMaxAngularAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMaxLinearSpeed(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearSpeed()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearSpeed())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getMaxLinearAcceleration(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getMaxLinearAcceleration()"""
        return float._wrap(super(NullLimiter, self).getMaxLinearAcceleration())

    @override
    @overload
    def setMaxAngularSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxAngularSpeed(float)"""
        super(_NullLimiter, self).setMaxAngularSpeed(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setMaxLinearAcceleration(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearAcceleration(float)"""
        super(_NullLimiter, self).setMaxLinearAcceleration(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMaxLinearSpeed(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setMaxLinearSpeed(float)"""
        super(_NullLimiter, self).setMaxLinearSpeed(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setZeroLinearSpeedThreshold(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.limiters.NullLimiter.setZeroLinearSpeedThreshold(float)"""
        super(_NullLimiter, self).setZeroLinearSpeedThreshold(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getZeroLinearSpeedThreshold(self) -> float:
        """public float com.badlogic.gdx.ai.steer.limiters.NullLimiter.getZeroLinearSpeedThreshold()"""
        return float._wrap(super(NullLimiter, self).getZeroLinearSpeedThreshold())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())