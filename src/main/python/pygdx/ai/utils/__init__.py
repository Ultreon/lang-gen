from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as _NonBlockingSemaphore
_NonBlockingSemaphore = _NonBlockingSemaphore
from abc import abstractmethod, ABC
 
class NonBlockingSemaphore():
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphore"""
 
    @staticmethod
    def _wrap(java_value: _NonBlockingSemaphore) -> 'NonBlockingSemaphore':
        return NonBlockingSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NonBlockingSemaphore):
        """
        Dynamic initializer for NonBlockingSemaphore.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NonBlockingSemaphore__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NonBlockingSemaphore__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def release(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.release(int)"""
        pass

    @abstractmethod
    def acquire(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.acquire(int)"""
        pass

    @abstractmethod
    def acquire(self, ):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.acquire()"""
        pass

    @abstractmethod
    def release(self, ):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.release()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphore
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as _NonBlockingSemaphore
_NonBlockingSemaphore = _NonBlockingSemaphore
from abc import abstractmethod, ABC
 
class NonBlockingSemaphore():
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphore"""
 
    @staticmethod
    def _wrap(java_value: _NonBlockingSemaphore) -> 'NonBlockingSemaphore':
        return NonBlockingSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NonBlockingSemaphore):
        """
        Dynamic initializer for NonBlockingSemaphore.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NonBlockingSemaphore__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NonBlockingSemaphore__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def release(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.release(int)"""
        pass

    @abstractmethod
    def acquire(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.acquire(int)"""
        pass

    @abstractmethod
    def acquire(self, ):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.acquire()"""
        pass

    @abstractmethod
    def release(self, ):
        """public abstract boolean com.badlogic.gdx.ai.utils.NonBlockingSemaphore.release()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphore 
 
 
# CLASS: com.badlogic.gdx.ai.utils.Collision
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.Collision as _Collision
_Collision = _Collision
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
 
class Collision():
    """com.badlogic.gdx.ai.utils.Collision"""
 
    @staticmethod
    def _wrap(java_value: _Collision) -> 'Collision':
        return Collision(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Collision):
        """
        Dynamic initializer for Collision.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Collision__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Collision__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Vector', arg1: 'Vector'):
        """public com.badlogic.gdx.ai.utils.Collision(T,T)"""
        val = _Collision(arg0, arg1)
        self.__wrapper = val

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
    def set(self, arg0: 'Collision') -> 'Collision':
        """public com.badlogic.gdx.ai.utils.Collision<T> com.badlogic.gdx.ai.utils.Collision.set(com.badlogic.gdx.ai.utils.Collision<T>)"""
        return 'Collision'._wrap(super(_Collision, self).set(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Vector', arg1: 'Vector') -> 'Collision':
        """public com.badlogic.gdx.ai.utils.Collision<T> com.badlogic.gdx.ai.utils.Collision.set(T,T)"""
        return 'Collision'._wrap(super(_Collision, self).set(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphore$Factory
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as _NonBlockingSemaphore_Factory
_Factory = _NonBlockingSemaphore_Factory.Factory
from abc import abstractmethod, ABC
 
class Factory():
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphore.Factory"""
 
    @staticmethod
    def _wrap(java_value: _Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Factory):
        """
        Dynamic initializer for Factory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Factory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Factory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def createSemaphore(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphore$Factory.createSemaphore(java.lang.String,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.Ray
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.Ray as _Ray
_Ray = _Ray
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Ray():
    """com.badlogic.gdx.ai.utils.Ray"""
 
    @staticmethod
    def _wrap(java_value: _Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ray):
        """
        Dynamic initializer for Ray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def set(self, arg0: 'Ray') -> 'Ray':
        """public com.badlogic.gdx.ai.utils.Ray<T> com.badlogic.gdx.ai.utils.Ray.set(com.badlogic.gdx.ai.utils.Ray<T>)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0))

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

    @overload
    def set(self, arg0: 'Vector', arg1: 'Vector') -> 'Ray':
        """public com.badlogic.gdx.ai.utils.Ray<T> com.badlogic.gdx.ai.utils.Ray.set(T,T)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0, arg1))

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

    @overload
    def __init__(self, arg0: 'Vector', arg1: 'Vector'):
        """public com.badlogic.gdx.ai.utils.Ray(T,T)"""
        val = _Ray(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.utils.CircularBuffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.CircularBuffer as _CircularBuffer
_CircularBuffer = _CircularBuffer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CircularBuffer():
    """com.badlogic.gdx.ai.utils.CircularBuffer"""
 
    @staticmethod
    def _wrap(java_value: _CircularBuffer) -> 'CircularBuffer':
        return CircularBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircularBuffer):
        """
        Dynamic initializer for CircularBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircularBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircularBuffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def read(self) -> object:
        """public T com.badlogic.gdx.ai.utils.CircularBuffer.read()"""
        return object._wrap(super(CircularBuffer, self).read())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.CircularBuffer()"""
        val = _CircularBuffer()
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

    @overload
    def store(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.store(T)"""
        return bool._wrap(super(_CircularBuffer, self).store(arg0))

    @overload
    def isResizable(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.isResizable()"""
        return bool._wrap(super(CircularBuffer, self).isResizable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.isEmpty()"""
        return bool._wrap(super(CircularBuffer, self).isEmpty())

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.ai.utils.CircularBuffer(int,boolean)"""
        val = _CircularBuffer(_int.valueOf(arg0), _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.utils.CircularBuffer.clear()"""
        super(CircularBuffer, self).clear()

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.ai.utils.CircularBuffer.ensureCapacity(int)"""
        super(_CircularBuffer, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def isFull(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.isFull()"""
        return bool._wrap(super(CircularBuffer, self).isFull())

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

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.ai.utils.CircularBuffer.size()"""
        return int._wrap(super(CircularBuffer, self).size())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.CircularBuffer(int)"""
        val = _CircularBuffer(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setResizable(self, arg0: bool):
        """public void com.badlogic.gdx.ai.utils.CircularBuffer.setResizable(boolean)"""
        super(_CircularBuffer, self).setResizable(_boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.CircularBuffer()"""
        val = _CircularBuffer()
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.ArithmeticUtils
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
import com.badlogic.gdx.ai.utils.ArithmeticUtils as _ArithmeticUtils
_ArithmeticUtils = _ArithmeticUtils
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArithmeticUtils():
    """com.badlogic.gdx.ai.utils.ArithmeticUtils"""
 
    @staticmethod
    def _wrap(java_value: _ArithmeticUtils) -> 'ArithmeticUtils':
        return ArithmeticUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArithmeticUtils):
        """
        Dynamic initializer for ArithmeticUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArithmeticUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArithmeticUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def gcdPositive(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.gcdPositive(int,int)"""
        return int._wrap(_ArithmeticUtils.gcdPositive(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def lcmPositive(*arg0: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.lcmPositive(int...)"""
        return int._wrap(_ArithmeticUtils.lcmPositive(arg0))

    @staticmethod
    @overload
    def lcmPositive(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.lcmPositive(int,int) throws java.lang.ArithmeticException"""
        return int._wrap(_ArithmeticUtils.lcmPositive(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def gcdPositive(*arg0: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.gcdPositive(int...)"""
        return int._wrap(_ArithmeticUtils.gcdPositive(arg0))

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

    @staticmethod
    @overload
    def wrapAngleAroundZero(arg0: float) -> float:
        """public static float com.badlogic.gdx.ai.utils.ArithmeticUtils.wrapAngleAroundZero(float)"""
        return float._wrap(_ArithmeticUtils.wrapAngleAroundZero(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def mulAndCheck(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.mulAndCheck(int,int) throws java.lang.ArithmeticException"""
        return int._wrap(_ArithmeticUtils.mulAndCheck(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.RaycastCollisionDetector
import com.badlogic.gdx.ai.utils.RaycastCollisionDetector as _RaycastCollisionDetector
_RaycastCollisionDetector = _RaycastCollisionDetector
from abc import abstractmethod, ABC
 
class RaycastCollisionDetector():
    """com.badlogic.gdx.ai.utils.RaycastCollisionDetector"""
 
    @staticmethod
    def _wrap(java_value: _RaycastCollisionDetector) -> 'RaycastCollisionDetector':
        return RaycastCollisionDetector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RaycastCollisionDetector):
        """
        Dynamic initializer for RaycastCollisionDetector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RaycastCollisionDetector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RaycastCollisionDetector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def collides(self, arg0: 'Ray'):
        """public abstract boolean com.badlogic.gdx.ai.utils.RaycastCollisionDetector.collides(com.badlogic.gdx.ai.utils.Ray<T>)"""
        pass

    @abstractmethod
    def findCollision(self, arg0: 'Collision', arg1: 'Ray'):
        """public abstract boolean com.badlogic.gdx.ai.utils.RaycastCollisionDetector.findCollision(com.badlogic.gdx.ai.utils.Collision<T>,com.badlogic.gdx.ai.utils.Ray<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore as _SimpleNonBlockingSemaphore
_SimpleNonBlockingSemaphore = _SimpleNonBlockingSemaphore
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleNonBlockingSemaphore():
    """com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore"""
 
    @staticmethod
    def _wrap(java_value: _SimpleNonBlockingSemaphore) -> 'SimpleNonBlockingSemaphore':
        return SimpleNonBlockingSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleNonBlockingSemaphore):
        """
        Dynamic initializer for SimpleNonBlockingSemaphore.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleNonBlockingSemaphore__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleNonBlockingSemaphore__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def acquire(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.acquire(int)"""
        return bool._wrap(super(_SimpleNonBlockingSemaphore, self).acquire(_int.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore(java.lang.String,int)"""
        val = _SimpleNonBlockingSemaphore(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def acquire(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.acquire()"""
        return bool._wrap(super(SimpleNonBlockingSemaphore, self).acquire())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def release(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.release(int)"""
        return bool._wrap(super(_SimpleNonBlockingSemaphore, self).release(_int.valueOf(arg0)))

    @override
    @overload
    def release(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.release()"""
        return bool._wrap(super(SimpleNonBlockingSemaphore, self).release())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as _NonBlockingSemaphore
_NonBlockingSemaphore = _NonBlockingSemaphore
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore as _SimpleNonBlockingSemaphore_Factory
_Factory = _SimpleNonBlockingSemaphore_Factory.Factory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Factory():
    """com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.Factory"""
 
    @staticmethod
    def _wrap(java_value: _Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Factory):
        """
        Dynamic initializer for Factory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Factory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Factory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def createSemaphore(self, arg0: str, arg1: int) -> 'NonBlockingSemaphore':
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory.createSemaphore(java.lang.String,int)"""
        return 'NonBlockingSemaphore'._wrap(super(_Factory, self).createSemaphore(arg0, _int.valueOf(arg1)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory()"""
        val = _Factory()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory()"""
        val = _Factory()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.ai.utils.Location
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

 
class Location():
    """com.badlogic.gdx.ai.utils.Location"""
 
    @staticmethod
    def _wrap(java_value: _Location) -> 'Location':
        return Location(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Location):
        """
        Dynamic initializer for Location.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Location__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Location__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def vectorToAngle(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.ai.utils.Location.vectorToAngle(T)"""
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
    def newLocation(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.utils.Location.newLocation()"""
        pass

    @abstractmethod
    def getOrientation(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.Location.getOrientation()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository
from builtins import str
import com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository as _NonBlockingSemaphoreRepository
_NonBlockingSemaphoreRepository = _NonBlockingSemaphoreRepository
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as _NonBlockingSemaphore
_NonBlockingSemaphore = _NonBlockingSemaphore
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NonBlockingSemaphoreRepository():
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository"""
 
    @staticmethod
    def _wrap(java_value: _NonBlockingSemaphoreRepository) -> 'NonBlockingSemaphoreRepository':
        return NonBlockingSemaphoreRepository(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NonBlockingSemaphoreRepository):
        """
        Dynamic initializer for NonBlockingSemaphoreRepository.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NonBlockingSemaphoreRepository__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NonBlockingSemaphoreRepository__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def addSemaphore(arg0: str, arg1: int) -> 'NonBlockingSemaphore':
        """public static com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.addSemaphore(java.lang.String,int)"""
        return NonBlockingSemaphore._wrap(_NonBlockingSemaphoreRepository.addSemaphore(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository()"""
        val = _NonBlockingSemaphoreRepository()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def clear():
            """public static void com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.clear()"""
            _NonBlockingSemaphoreRepository.clear()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def removeSemaphore(arg0: str) -> 'NonBlockingSemaphore':
        """public static com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.removeSemaphore(java.lang.String)"""
        return NonBlockingSemaphore._wrap(_NonBlockingSemaphoreRepository.removeSemaphore(arg0))

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

    @staticmethod
    @overload
    def setFactory(arg0: 'Factory'):
        """public static void com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.setFactory(com.badlogic.gdx.ai.utils.NonBlockingSemaphore$Factory)"""
        _NonBlockingSemaphoreRepository.setFactory(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getSemaphore(arg0: str) -> 'NonBlockingSemaphore':
        """public static com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.getSemaphore(java.lang.String)"""
        return NonBlockingSemaphore._wrap(_NonBlockingSemaphoreRepository.getSemaphore(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository()"""
        val = _NonBlockingSemaphoreRepository()
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