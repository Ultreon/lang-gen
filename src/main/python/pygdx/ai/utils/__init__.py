from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore as __SimpleNonBlockingSemaphore_Factory
__Factory = __SimpleNonBlockingSemaphore_Factory.Factory
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as __NonBlockingSemaphore
__NonBlockingSemaphore = __NonBlockingSemaphore
from builtins import int
 
class Factory():
    """com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.Factory"""
 
    @staticmethod
    def __wrap(java_value: __Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Factory):
        """
        Dynamic initializer for Factory.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createSemaphore(self, arg0: str, arg1: int) -> 'NonBlockingSemaphore':
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory.createSemaphore(java.lang.String,int)"""
        return 'NonBlockingSemaphore'.__wrap(super(__Factory, self).createSemaphore(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore as __SimpleNonBlockingSemaphore_Factory
__Factory = __SimpleNonBlockingSemaphore_Factory.Factory
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as __NonBlockingSemaphore
__NonBlockingSemaphore = __NonBlockingSemaphore
from builtins import int
 
class Factory():
    """com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.Factory"""
 
    @staticmethod
    def __wrap(java_value: __Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Factory):
        """
        Dynamic initializer for Factory.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createSemaphore(self, arg0: str, arg1: int) -> 'NonBlockingSemaphore':
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory.createSemaphore(java.lang.String,int)"""
        return 'NonBlockingSemaphore'.__wrap(super(__Factory, self).createSemaphore(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore$Factory 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphore$Factory
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as __NonBlockingSemaphore_Factory
__Factory = __NonBlockingSemaphore_Factory.Factory
from abc import abstractmethod, ABC
 
class Factory(ABC):
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphore.Factory"""
 
    @staticmethod
    def __wrap(java_value: __Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Factory):
        """
        Dynamic initializer for Factory.
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
    def createSemaphore(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphore$Factory.createSemaphore(java.lang.String,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.Location
from pyquantum_helper import import_once as __import_once__
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
 
class Location(ABC):
    """com.badlogic.gdx.ai.utils.Location"""
 
    @staticmethod
    def __wrap(java_value: __Location) -> 'Location':
        return Location(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Location):
        """
        Dynamic initializer for Location.
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
    def vectorToAngle(self, arg0: 'Vector'):
        """public abstract float com.badlogic.gdx.ai.utils.Location.vectorToAngle(T)"""
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
    def newLocation(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.utils.Location.newLocation()"""
        pass

    @abstractmethod
    def getOrientation(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.Location.getOrientation()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.ArithmeticUtils
from builtins import str
import com.badlogic.gdx.ai.utils.ArithmeticUtils as __ArithmeticUtils
__ArithmeticUtils = __ArithmeticUtils
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
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
 
class ArithmeticUtils():
    """com.badlogic.gdx.ai.utils.ArithmeticUtils"""
 
    @staticmethod
    def __wrap(java_value: __ArithmeticUtils) -> 'ArithmeticUtils':
        return ArithmeticUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArithmeticUtils):
        """
        Dynamic initializer for ArithmeticUtils.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def gcdPositive(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.gcdPositive(int,int)"""
        return int.__wrap(__ArithmeticUtils.gcdPositive(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def lcmPositive(*arg0: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.lcmPositive(int...)"""
        return int.__wrap(__ArithmeticUtils.lcmPositive(arg0))

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

    @staticmethod
    @overload
    def wrapAngleAroundZero(arg0: float) -> float:
        """public static float com.badlogic.gdx.ai.utils.ArithmeticUtils.wrapAngleAroundZero(float)"""
        return float.__wrap(__ArithmeticUtils.wrapAngleAroundZero(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def gcdPositive(*arg0: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.gcdPositive(int...)"""
        return int.__wrap(__ArithmeticUtils.gcdPositive(arg0))

    @staticmethod
    @overload
    def lcmPositive(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.lcmPositive(int,int) throws java.lang.ArithmeticException"""
        return int.__wrap(__ArithmeticUtils.lcmPositive(__int.valueOf(arg0), __int.valueOf(arg1)))

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

    @staticmethod
    @overload
    def mulAndCheck(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.ai.utils.ArithmeticUtils.mulAndCheck(int,int) throws java.lang.ArithmeticException"""
        return int.__wrap(__ArithmeticUtils.mulAndCheck(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository as __NonBlockingSemaphoreRepository
__NonBlockingSemaphoreRepository = __NonBlockingSemaphoreRepository
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as __NonBlockingSemaphore
__NonBlockingSemaphore = __NonBlockingSemaphore
from builtins import int
 
class NonBlockingSemaphoreRepository():
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository"""
 
    @staticmethod
    def __wrap(java_value: __NonBlockingSemaphoreRepository) -> 'NonBlockingSemaphoreRepository':
        return NonBlockingSemaphoreRepository(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NonBlockingSemaphoreRepository):
        """
        Dynamic initializer for NonBlockingSemaphoreRepository.
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
 
        @staticmethod
        @overload
        def clear():
            """public static void com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.clear()"""
            __NonBlockingSemaphoreRepository.clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def removeSemaphore(arg0: str) -> 'NonBlockingSemaphore':
        """public static com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.removeSemaphore(java.lang.String)"""
        return NonBlockingSemaphore.__wrap(__NonBlockingSemaphoreRepository.removeSemaphore(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def addSemaphore(arg0: str, arg1: int) -> 'NonBlockingSemaphore':
        """public static com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.addSemaphore(java.lang.String,int)"""
        return NonBlockingSemaphore.__wrap(__NonBlockingSemaphoreRepository.addSemaphore(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository()"""
        val = __NonBlockingSemaphoreRepository()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository()"""
        val = __NonBlockingSemaphoreRepository()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def setFactory(arg0: 'Factory'):
        """public static void com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.setFactory(com.badlogic.gdx.ai.utils.NonBlockingSemaphore$Factory)"""
        __NonBlockingSemaphoreRepository.setFactory(arg0)

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

    @staticmethod
    @overload
    def getSemaphore(arg0: str) -> 'NonBlockingSemaphore':
        """public static com.badlogic.gdx.ai.utils.NonBlockingSemaphore com.badlogic.gdx.ai.utils.NonBlockingSemaphoreRepository.getSemaphore(java.lang.String)"""
        return NonBlockingSemaphore.__wrap(__NonBlockingSemaphoreRepository.getSemaphore(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.NonBlockingSemaphore
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.utils.NonBlockingSemaphore as __NonBlockingSemaphore
__NonBlockingSemaphore = __NonBlockingSemaphore
 
class NonBlockingSemaphore(ABC):
    """com.badlogic.gdx.ai.utils.NonBlockingSemaphore"""
 
    @staticmethod
    def __wrap(java_value: __NonBlockingSemaphore) -> 'NonBlockingSemaphore':
        return NonBlockingSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NonBlockingSemaphore):
        """
        Dynamic initializer for NonBlockingSemaphore.
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore as __SimpleNonBlockingSemaphore
__SimpleNonBlockingSemaphore = __SimpleNonBlockingSemaphore
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleNonBlockingSemaphore():
    """com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore"""
 
    @staticmethod
    def __wrap(java_value: __SimpleNonBlockingSemaphore) -> 'SimpleNonBlockingSemaphore':
        return SimpleNonBlockingSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleNonBlockingSemaphore):
        """
        Dynamic initializer for SimpleNonBlockingSemaphore.
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
    def acquire(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.acquire(int)"""
        return bool.__wrap(super(__SimpleNonBlockingSemaphore, self).acquire(__int.valueOf(arg0)))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def release(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.release()"""
        return bool.__wrap(super(SimpleNonBlockingSemaphore, self).release())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore(java.lang.String,int)"""
        val = __SimpleNonBlockingSemaphore(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def release(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.release(int)"""
        return bool.__wrap(super(__SimpleNonBlockingSemaphore, self).release(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def acquire(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.SimpleNonBlockingSemaphore.acquire()"""
        return bool.__wrap(super(SimpleNonBlockingSemaphore, self).acquire())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.RaycastCollisionDetector
import com.badlogic.gdx.ai.utils.RaycastCollisionDetector as __RaycastCollisionDetector
__RaycastCollisionDetector = __RaycastCollisionDetector
from abc import abstractmethod, ABC
 
class RaycastCollisionDetector(ABC):
    """com.badlogic.gdx.ai.utils.RaycastCollisionDetector"""
 
    @staticmethod
    def __wrap(java_value: __RaycastCollisionDetector) -> 'RaycastCollisionDetector':
        return RaycastCollisionDetector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RaycastCollisionDetector):
        """
        Dynamic initializer for RaycastCollisionDetector.
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
    def collides(self, arg0: 'Ray'):
        """public abstract boolean com.badlogic.gdx.ai.utils.RaycastCollisionDetector.collides(com.badlogic.gdx.ai.utils.Ray<T>)"""
        pass

    @abstractmethod
    def findCollision(self, arg0: 'Collision', arg1: 'Ray'):
        """public abstract boolean com.badlogic.gdx.ai.utils.RaycastCollisionDetector.findCollision(com.badlogic.gdx.ai.utils.Collision<T>,com.badlogic.gdx.ai.utils.Ray<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.Collision
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.utils.Collision as __Collision
__Collision = __Collision
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Collision():
    """com.badlogic.gdx.ai.utils.Collision"""
 
    @staticmethod
    def __wrap(java_value: __Collision) -> 'Collision':
        return Collision(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Collision):
        """
        Dynamic initializer for Collision.
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
    def set(self, arg0: 'Vector', arg1: 'Vector') -> 'Collision':
        """public com.badlogic.gdx.ai.utils.Collision<T> com.badlogic.gdx.ai.utils.Collision.set(T,T)"""
        return 'Collision'.__wrap(super(__Collision, self).set(arg0, arg1))

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
    def __init__(self, arg0: 'Vector', arg1: 'Vector'):
        """public com.badlogic.gdx.ai.utils.Collision(T,T)"""
        val = __Collision(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def set(self, arg0: 'Collision') -> 'Collision':
        """public com.badlogic.gdx.ai.utils.Collision<T> com.badlogic.gdx.ai.utils.Collision.set(com.badlogic.gdx.ai.utils.Collision<T>)"""
        return 'Collision'.__wrap(super(__Collision, self).set(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.Ray
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
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
import com.badlogic.gdx.ai.utils.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class Ray():
    """com.badlogic.gdx.ai.utils.Ray"""
 
    @staticmethod
    def __wrap(java_value: __Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ray):
        """
        Dynamic initializer for Ray.
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
        """public com.badlogic.gdx.ai.utils.Ray(T,T)"""
        val = __Ray(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Vector', arg1: 'Vector') -> 'Ray':
        """public com.badlogic.gdx.ai.utils.Ray<T> com.badlogic.gdx.ai.utils.Ray.set(T,T)"""
        return 'Ray'.__wrap(super(__Ray, self).set(arg0, arg1))

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
    def set(self, arg0: 'Ray') -> 'Ray':
        """public com.badlogic.gdx.ai.utils.Ray<T> com.badlogic.gdx.ai.utils.Ray.set(com.badlogic.gdx.ai.utils.Ray<T>)"""
        return 'Ray'.__wrap(super(__Ray, self).set(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.CircularBuffer
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.utils.CircularBuffer as __CircularBuffer
__CircularBuffer = __CircularBuffer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CircularBuffer():
    """com.badlogic.gdx.ai.utils.CircularBuffer"""
 
    @staticmethod
    def __wrap(java_value: __CircularBuffer) -> 'CircularBuffer':
        return CircularBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CircularBuffer):
        """
        Dynamic initializer for CircularBuffer.
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
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.isEmpty()"""
        return bool.__wrap(super(CircularBuffer, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def read(self) -> object:
        """public T com.badlogic.gdx.ai.utils.CircularBuffer.read()"""
        return object.__wrap(super(CircularBuffer, self).read())

    @overload
    def isResizable(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.isResizable()"""
        return bool.__wrap(super(CircularBuffer, self).isResizable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.ai.utils.CircularBuffer(int,boolean)"""
        val = __CircularBuffer(__int.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.ai.utils.CircularBuffer.size()"""
        return int.__wrap(super(CircularBuffer, self).size())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.CircularBuffer()"""
        val = __CircularBuffer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def store(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.store(T)"""
        return bool.__wrap(super(__CircularBuffer, self).store(arg0))

    @overload
    def isFull(self) -> bool:
        """public boolean com.badlogic.gdx.ai.utils.CircularBuffer.isFull()"""
        return bool.__wrap(super(CircularBuffer, self).isFull())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.CircularBuffer()"""
        val = __CircularBuffer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.utils.CircularBuffer.clear()"""
        super(CircularBuffer, self).clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.ai.utils.CircularBuffer.ensureCapacity(int)"""
        super(__CircularBuffer, self).ensureCapacity(__int.valueOf(arg0))

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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.CircularBuffer(int)"""
        val = __CircularBuffer(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setResizable(self, arg0: bool):
        """public void com.badlogic.gdx.ai.utils.CircularBuffer.setResizable(boolean)"""
        super(__CircularBuffer, self).setResizable(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))