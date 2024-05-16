from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.concurrent.ConcurrentInitializer as __ConcurrentInitializer
__ConcurrentInitializer = __ConcurrentInitializer
from abc import abstractmethod, ABC
 
class ConcurrentInitializer(ABC):
    """org.apache.commons.lang3.concurrent.ConcurrentInitializer"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentInitializer) -> 'ConcurrentInitializer':
        return ConcurrentInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentInitializer):
        """
        Dynamic initializer for ConcurrentInitializer.
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
    def get(self, ):
        """public abstract T org.apache.commons.lang3.concurrent.ConcurrentInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        pass

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentInitializer
import org.apache.commons.lang3.concurrent.ConcurrentInitializer as __ConcurrentInitializer
__ConcurrentInitializer = __ConcurrentInitializer
from abc import abstractmethod, ABC
 
class ConcurrentInitializer(ABC):
    """org.apache.commons.lang3.concurrent.ConcurrentInitializer"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentInitializer) -> 'ConcurrentInitializer':
        return ConcurrentInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentInitializer):
        """
        Dynamic initializer for ConcurrentInitializer.
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
    def get(self, ):
        """public abstract T org.apache.commons.lang3.concurrent.ConcurrentInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        pass

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentInitializer 
 
 
# CLASS: org.apache.commons.lang3.concurrent.FutureTasks
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.FutureTask as FutureTask
import org.apache.commons.lang3.concurrent.FutureTasks as __FutureTasks
__FutureTasks = __FutureTasks
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
import java.util.concurrent.FutureTask as __FutureTask
__FutureTask = __FutureTask
from builtins import bool
from builtins import int
 
class FutureTasks():
    """org.apache.commons.lang3.concurrent.FutureTasks"""
 
    @staticmethod
    def __wrap(java_value: __FutureTasks) -> 'FutureTasks':
        return FutureTasks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FutureTasks):
        """
        Dynamic initializer for FutureTasks.
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

    @staticmethod
    @overload
    def run(arg0: 'Callable') -> 'FutureTask':
        """public static <V> java.util.concurrent.FutureTask<V> org.apache.commons.lang3.concurrent.FutureTasks.run(java.util.concurrent.Callable<V>)"""
        return FutureTask.__wrap(__FutureTasks.run(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.concurrent.CircuitBreaker
from abc import abstractmethod, ABC
import org.apache.commons.lang3.concurrent.CircuitBreaker as __CircuitBreaker
__CircuitBreaker = __CircuitBreaker
 
class CircuitBreaker(ABC):
    """org.apache.commons.lang3.concurrent.CircuitBreaker"""
 
    @staticmethod
    def __wrap(java_value: __CircuitBreaker) -> 'CircuitBreaker':
        return CircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CircuitBreaker):
        """
        Dynamic initializer for CircuitBreaker.
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
    def incrementAndCheckState(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.incrementAndCheckState(T)"""
        pass

    @abstractmethod
    def isOpen(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.isOpen()"""
        pass

    @abstractmethod
    def checkState(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.checkState()"""
        pass

    @abstractmethod
    def close(self, ):
        """public abstract void org.apache.commons.lang3.concurrent.CircuitBreaker.close()"""
        pass

    @abstractmethod
    def isClosed(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.isClosed()"""
        pass

    @abstractmethod
    def open(self, ):
        """public abstract void org.apache.commons.lang3.concurrent.CircuitBreaker.open()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AtomicInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.concurrent.AtomicInitializer as __AtomicInitializer
__AtomicInitializer = __AtomicInitializer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AtomicInitializer(ABC, __ConcurrentInitializer, ConcurrentInitializer):
    """org.apache.commons.lang3.concurrent.AtomicInitializer"""
 
    @staticmethod
    def __wrap(java_value: __AtomicInitializer) -> 'AtomicInitializer':
        return AtomicInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtomicInitializer):
        """
        Dynamic initializer for AtomicInitializer.
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

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.AtomicInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(AtomicInitializer, self).get())

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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.AtomicInitializer()"""
        val = __AtomicInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.AtomicInitializer()"""
        val = __AtomicInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AtomicSafeInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.lang3.concurrent.AtomicSafeInitializer as __AtomicSafeInitializer
__AtomicSafeInitializer = __AtomicSafeInitializer
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
 
class AtomicSafeInitializer(ABC, __ConcurrentInitializer, ConcurrentInitializer):
    """org.apache.commons.lang3.concurrent.AtomicSafeInitializer"""
 
    @staticmethod
    def __wrap(java_value: __AtomicSafeInitializer) -> 'AtomicSafeInitializer':
        return AtomicSafeInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtomicSafeInitializer):
        """
        Dynamic initializer for AtomicSafeInitializer.
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
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.AtomicSafeInitializer()"""
        val = __AtomicSafeInitializer()
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
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.AtomicSafeInitializer()"""
        val = __AtomicSafeInitializer()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def get(self) -> object:
        """public final T org.apache.commons.lang3.concurrent.AtomicSafeInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(AtomicSafeInitializer, self).get()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.MultiBackgroundInitializer
import org.apache.commons.lang3.concurrent.MultiBackgroundInitializer as __MultiBackgroundInitializer
__MultiBackgroundInitializer = __MultiBackgroundInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future as __Future
__Future = __Future
import java.util.concurrent.ExecutorService as ExecutorService
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
from builtins import object
import org.apache.commons.lang3.concurrent.BackgroundInitializer as __BackgroundInitializer
__BackgroundInitializer = __BackgroundInitializer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MultiBackgroundInitializer(__BackgroundInitializer, BackgroundInitializer):
    """org.apache.commons.lang3.concurrent.MultiBackgroundInitializer"""
 
    @staticmethod
    def __wrap(java_value: __MultiBackgroundInitializer) -> 'MultiBackgroundInitializer':
        return MultiBackgroundInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiBackgroundInitializer):
        """
        Dynamic initializer for MultiBackgroundInitializer.
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
    def __init__(self, arg0: 'ExecutorService'):
        """public org.apache.commons.lang3.concurrent.MultiBackgroundInitializer(java.util.concurrent.ExecutorService)"""
        val = __MultiBackgroundInitializer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setExternalExecutor(self, arg0: 'ExecutorService'):
        """public final synchronized void org.apache.commons.lang3.concurrent.BackgroundInitializer.setExternalExecutor(java.util.concurrent.ExecutorService)"""
        super(__BackgroundInitializer, self).setExternalExecutor(arg0)

    @override
    @overload
    def getFuture(self) -> 'Future':
        """public synchronized java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.BackgroundInitializer.getFuture()"""
        return 'Future'.__wrap(super(BackgroundInitializer, self).getFuture())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.MultiBackgroundInitializer()"""
        val = __MultiBackgroundInitializer()
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

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.MultiBackgroundInitializer()"""
        val = __MultiBackgroundInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.BackgroundInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(BackgroundInitializer, self).get())

    @override
    @overload
    def start(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.start()"""
        return bool.__wrap(super(BackgroundInitializer, self).start())

    @override
    @overload
    def getExternalExecutor(self) -> 'ExecutorService':
        """public final synchronized java.util.concurrent.ExecutorService org.apache.commons.lang3.concurrent.BackgroundInitializer.getExternalExecutor()"""
        return 'ExecutorService'.__wrap(super(BackgroundInitializer, self).getExternalExecutor())

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
    def addInitializer(self, arg0: str, arg1: 'BackgroundInitializer'):
        """public void org.apache.commons.lang3.concurrent.MultiBackgroundInitializer.addInitializer(java.lang.String,org.apache.commons.lang3.concurrent.BackgroundInitializer<?>)"""
        super(__MultiBackgroundInitializer, self).addInitializer(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isStarted(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.isStarted()"""
        return bool.__wrap(super(BackgroundInitializer, self).isStarted()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.Computable
import org.apache.commons.lang3.concurrent.Computable as __Computable
__Computable = __Computable
from abc import abstractmethod, ABC
 
class Computable(ABC):
    """org.apache.commons.lang3.concurrent.Computable"""
 
    @staticmethod
    def __wrap(java_value: __Computable) -> 'Computable':
        return Computable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Computable):
        """
        Dynamic initializer for Computable.
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
    def compute(self, arg0: object):
        """public abstract O org.apache.commons.lang3.concurrent.Computable.compute(I) throws java.lang.InterruptedException"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentUtils
import org.apache.commons.lang3.concurrent.ConcurrentUtils as __ConcurrentUtils
__ConcurrentUtils = __ConcurrentUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.ConcurrentRuntimeException as __ConcurrentRuntimeException
__ConcurrentRuntimeException = __ConcurrentRuntimeException
import java.util.concurrent.Future as __Future
__Future = __Future
import java.util.concurrent.ConcurrentMap as ConcurrentMap
from builtins import object
import org.apache.commons.lang3.concurrent.ConcurrentException as __ConcurrentException
__ConcurrentException = __ConcurrentException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.ExecutionException as ExecutionException
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConcurrentUtils():
    """org.apache.commons.lang3.concurrent.ConcurrentUtils"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentUtils) -> 'ConcurrentUtils':
        return ConcurrentUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentUtils):
        """
        Dynamic initializer for ConcurrentUtils.
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
    def handleCauseUnchecked(arg0: 'ExecutionException'):
        """public static void org.apache.commons.lang3.concurrent.ConcurrentUtils.handleCauseUnchecked(java.util.concurrent.ExecutionException)"""
        __ConcurrentUtils.handleCauseUnchecked(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def handleCause(arg0: 'ExecutionException'):
        """public static void org.apache.commons.lang3.concurrent.ConcurrentUtils.handleCause(java.util.concurrent.ExecutionException) throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        __ConcurrentUtils.handleCause(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def extractCauseUnchecked(arg0: 'ExecutionException') -> 'ConcurrentRuntimeException':
        """public static org.apache.commons.lang3.concurrent.ConcurrentRuntimeException org.apache.commons.lang3.concurrent.ConcurrentUtils.extractCauseUnchecked(java.util.concurrent.ExecutionException)"""
        return ConcurrentRuntimeException.__wrap(__ConcurrentUtils.extractCauseUnchecked(arg0))

    @staticmethod
    @overload
    def initializeUnchecked(arg0: 'ConcurrentInitializer') -> object:
        """public static <T> T org.apache.commons.lang3.concurrent.ConcurrentUtils.initializeUnchecked(org.apache.commons.lang3.concurrent.ConcurrentInitializer<T>)"""
        return object.__wrap(__ConcurrentUtils.initializeUnchecked(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createIfAbsent(arg0: 'ConcurrentMap', arg1: object, arg2: 'ConcurrentInitializer') -> object:
        """public static <K,V> V org.apache.commons.lang3.concurrent.ConcurrentUtils.createIfAbsent(java.util.concurrent.ConcurrentMap<K, V>,K,org.apache.commons.lang3.concurrent.ConcurrentInitializer<V>) throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(__ConcurrentUtils.createIfAbsent(arg0, arg1, arg2))

    @staticmethod
    @overload
    def constantFuture(arg0: object) -> 'Future':
        """public static <T> java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.ConcurrentUtils.constantFuture(T)"""
        return Future.__wrap(__ConcurrentUtils.constantFuture(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def createIfAbsentUnchecked(arg0: 'ConcurrentMap', arg1: object, arg2: 'ConcurrentInitializer') -> object:
        """public static <K,V> V org.apache.commons.lang3.concurrent.ConcurrentUtils.createIfAbsentUnchecked(java.util.concurrent.ConcurrentMap<K, V>,K,org.apache.commons.lang3.concurrent.ConcurrentInitializer<V>)"""
        return object.__wrap(__ConcurrentUtils.createIfAbsentUnchecked(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def putIfAbsent(arg0: 'ConcurrentMap', arg1: object, arg2: object) -> object:
        """public static <K,V> V org.apache.commons.lang3.concurrent.ConcurrentUtils.putIfAbsent(java.util.concurrent.ConcurrentMap<K, V>,K,V)"""
        return object.__wrap(__ConcurrentUtils.putIfAbsent(arg0, arg1, arg2))

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

    @staticmethod
    @overload
    def initialize(arg0: 'ConcurrentInitializer') -> object:
        """public static <T> T org.apache.commons.lang3.concurrent.ConcurrentUtils.initialize(org.apache.commons.lang3.concurrent.ConcurrentInitializer<T>) throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(__ConcurrentUtils.initialize(arg0))

    @staticmethod
    @overload
    def extractCause(arg0: 'ExecutionException') -> 'ConcurrentException':
        """public static org.apache.commons.lang3.concurrent.ConcurrentException org.apache.commons.lang3.concurrent.ConcurrentUtils.extractCause(java.util.concurrent.ExecutionException)"""
        return ConcurrentException.__wrap(__ConcurrentUtils.extractCause(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.LazyInitializer
import org.apache.commons.lang3.concurrent.LazyInitializer as __LazyInitializer
__LazyInitializer = __LazyInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
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
 
class LazyInitializer(ABC, __ConcurrentInitializer, ConcurrentInitializer):
    """org.apache.commons.lang3.concurrent.LazyInitializer"""
 
    @staticmethod
    def __wrap(java_value: __LazyInitializer) -> 'LazyInitializer':
        return LazyInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazyInitializer):
        """
        Dynamic initializer for LazyInitializer.
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
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.LazyInitializer()"""
        val = __LazyInitializer()
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
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.LazyInitializer()"""
        val = __LazyInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.LazyInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(LazyInitializer, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AbstractCircuitBreaker
from builtins import str
from pyquantum_helper import override
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as __AbstractCircuitBreaker
__AbstractCircuitBreaker = __AbstractCircuitBreaker
from builtins import int
 
class AbstractCircuitBreaker(ABC, __CircuitBreaker, CircuitBreaker):
    """org.apache.commons.lang3.concurrent.AbstractCircuitBreaker"""
 
    @staticmethod
    def __wrap(java_value: __AbstractCircuitBreaker) -> 'AbstractCircuitBreaker':
        return AbstractCircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractCircuitBreaker):
        """
        Dynamic initializer for AbstractCircuitBreaker.
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
    def close(self):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.close()"""
        super(AbstractCircuitBreaker, self).close()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.removeChangeListener(java.beans.PropertyChangeListener)"""
        super(__AbstractCircuitBreaker, self).removeChangeListener(arg0)

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
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.AbstractCircuitBreaker()"""
        val = __AbstractCircuitBreaker()
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

    @override
    @overload
    def isClosed(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isClosed()"""
        return bool.__wrap(super(AbstractCircuitBreaker, self).isClosed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isOpen()"""
        return bool.__wrap(super(AbstractCircuitBreaker, self).isOpen())

    @override
    @overload
    def open(self):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.open()"""
        super(AbstractCircuitBreaker, self).open()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def incrementAndCheckState(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.incrementAndCheckState(T)"""
        pass

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.AbstractCircuitBreaker()"""
        val = __AbstractCircuitBreaker()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.addChangeListener(java.beans.PropertyChangeListener)"""
        super(__AbstractCircuitBreaker, self).addChangeListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def checkState(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.checkState()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.lang3.concurrent.MultiBackgroundInitializer as __MultiBackgroundInitializer_MultiBackgroundInitializerResults
__MultiBackgroundInitializerResults = __MultiBackgroundInitializer_MultiBackgroundInitializerResults.MultiBackgroundInitializerResults
from builtins import object
import org.apache.commons.lang3.concurrent.ConcurrentException as __ConcurrentException
__ConcurrentException = __ConcurrentException
import org.apache.commons.lang3.concurrent.BackgroundInitializer as __BackgroundInitializer
__BackgroundInitializer = __BackgroundInitializer
import java.util.Set as Set
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
from builtins import int
 
class MultiBackgroundInitializerResults():
    """org.apache.commons.lang3.concurrent.MultiBackgroundInitializer.MultiBackgroundInitializerResults"""
 
    @staticmethod
    def __wrap(java_value: __MultiBackgroundInitializerResults) -> 'MultiBackgroundInitializerResults':
        return MultiBackgroundInitializerResults(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiBackgroundInitializerResults):
        """
        Dynamic initializer for MultiBackgroundInitializerResults.
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
    def initializerNames(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.initializerNames()"""
        return 'Set'.__wrap(super(MultiBackgroundInitializerResults, self).initializerNames())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getResultObject(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.getResultObject(java.lang.String)"""
        return object.__wrap(super(__MultiBackgroundInitializerResults, self).getResultObject(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getInitializer(self, arg0: str) -> 'BackgroundInitializer':
        """public org.apache.commons.lang3.concurrent.BackgroundInitializer<?> org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.getInitializer(java.lang.String)"""
        return 'BackgroundInitializer'.__wrap(super(__MultiBackgroundInitializerResults, self).getInitializer(arg0))

    @overload
    def isException(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.isException(java.lang.String)"""
        return bool.__wrap(super(__MultiBackgroundInitializerResults, self).isException(arg0))

    @overload
    def isSuccessful(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.isSuccessful()"""
        return bool.__wrap(super(MultiBackgroundInitializerResults, self).isSuccessful())

    @overload
    def getException(self, arg0: str) -> 'ConcurrentException':
        """public org.apache.commons.lang3.concurrent.ConcurrentException org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.getException(java.lang.String)"""
        return 'ConcurrentException'.__wrap(super(__MultiBackgroundInitializerResults, self).getException(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.concurrent.EventCountCircuitBreaker
from builtins import str
from pyquantum_helper import override
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.EventCountCircuitBreaker as __EventCountCircuitBreaker
__EventCountCircuitBreaker = __EventCountCircuitBreaker
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as __AbstractCircuitBreaker
__AbstractCircuitBreaker = __AbstractCircuitBreaker
from builtins import int
 
class EventCountCircuitBreaker(__AbstractCircuitBreaker, AbstractCircuitBreaker):
    """org.apache.commons.lang3.concurrent.EventCountCircuitBreaker"""
 
    @staticmethod
    def __wrap(java_value: __EventCountCircuitBreaker) -> 'EventCountCircuitBreaker':
        return EventCountCircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventCountCircuitBreaker):
        """
        Dynamic initializer for EventCountCircuitBreaker.
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
    def getClosingInterval(self) -> int:
        """public long org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getClosingInterval()"""
        return int.__wrap(super(EventCountCircuitBreaker, self).getClosingInterval())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'TimeUnit', arg3: int):
        """public org.apache.commons.lang3.concurrent.EventCountCircuitBreaker(int,long,java.util.concurrent.TimeUnit,int)"""
        val = __EventCountCircuitBreaker(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public void org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.close()"""
        super(EventCountCircuitBreaker, self).close()

    @override
    @overload
    def checkState(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.checkState()"""
        return bool.__wrap(super(EventCountCircuitBreaker, self).checkState())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getOpeningInterval(self) -> int:
        """public long org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getOpeningInterval()"""
        return int.__wrap(super(EventCountCircuitBreaker, self).getOpeningInterval())

    @override
    @overload
    def isClosed(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isClosed()"""
        return bool.__wrap(super(AbstractCircuitBreaker, self).isClosed())

    @override
    @overload
    def addChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.addChangeListener(java.beans.PropertyChangeListener)"""
        super(__AbstractCircuitBreaker, self).addChangeListener(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'TimeUnit'):
        """public org.apache.commons.lang3.concurrent.EventCountCircuitBreaker(int,long,java.util.concurrent.TimeUnit)"""
        val = __EventCountCircuitBreaker(__int.valueOf(arg0), __long.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isOpen()"""
        return bool.__wrap(super(AbstractCircuitBreaker, self).isOpen())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getClosingThreshold(self) -> int:
        """public int org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getClosingThreshold()"""
        return int.__wrap(super(EventCountCircuitBreaker, self).getClosingThreshold())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def open(self):
        """public void org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.open()"""
        super(EventCountCircuitBreaker, self).open()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'TimeUnit', arg3: int, arg4: int, arg5: 'TimeUnit'):
        """public org.apache.commons.lang3.concurrent.EventCountCircuitBreaker(int,long,java.util.concurrent.TimeUnit,int,long,java.util.concurrent.TimeUnit)"""
        val = __EventCountCircuitBreaker(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4), arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def incrementAndCheckState(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.incrementAndCheckState()"""
        return bool.__wrap(super(EventCountCircuitBreaker, self).incrementAndCheckState())

    @overload
    def getOpeningThreshold(self) -> int:
        """public int org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getOpeningThreshold()"""
        return int.__wrap(super(EventCountCircuitBreaker, self).getOpeningThreshold())

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
    def incrementAndCheckState(self, arg0: 'Integer') -> bool:
        """public boolean org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.incrementAndCheckState(java.lang.Integer)"""
        return bool.__wrap(super(__EventCountCircuitBreaker, self).incrementAndCheckState(arg0))

    @override
    @overload
    def removeChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.removeChangeListener(java.beans.PropertyChangeListener)"""
        super(__AbstractCircuitBreaker, self).removeChangeListener(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as __AbstractCircuitBreaker_State
__State = __AbstractCircuitBreaker_State.State
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class State(ABC, __Enum, Enum):
    """org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.State"""
 
    @staticmethod
    def __wrap(java_value: __State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __State):
        """
        Dynamic initializer for State.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'State':
        """public static org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State.valueOf(java.lang.String)"""
        return State.__wrap(__State.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['State']:
        """public static org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State[] org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State.values()"""
        return List[State].__wrap(__State.values())

    @abstractmethod
    def oppositeState(self, ):
        """public abstract org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State.oppositeState()"""
        pass

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.UncheckedFuture
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Throwable as Throwable
import org.apache.commons.lang3.concurrent.UncheckedFuture as __UncheckedFuture
__UncheckedFuture = __UncheckedFuture
 
class UncheckedFuture(ABC, __Future, Future):
    """org.apache.commons.lang3.concurrent.UncheckedFuture"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedFuture) -> 'UncheckedFuture':
        return UncheckedFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedFuture):
        """
        Dynamic initializer for UncheckedFuture.
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
    def get(self, ):
        """public abstract V org.apache.commons.lang3.concurrent.UncheckedFuture.get()"""
        pass

    @abstractmethod
    def cancel(self, arg0: bool):
        """public abstract boolean java.util.concurrent.Future.cancel(boolean)"""
        pass

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'.__wrap(super(Future, self).exceptionNow())

    @staticmethod
    @overload
    def map(arg0: 'Collection') -> 'Stream':
        """public static <T> java.util.stream.Stream<org.apache.commons.lang3.concurrent.UncheckedFuture<T>> org.apache.commons.lang3.concurrent.UncheckedFuture.map(java.util.Collection<java.util.concurrent.Future<T>>)"""
        return Stream.__wrap(__UncheckedFuture.map(arg0))

    @abstractmethod
    def get(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract V org.apache.commons.lang3.concurrent.UncheckedFuture.get(long,java.util.concurrent.TimeUnit)"""
        pass

    @abstractmethod
    def isCancelled(self, ):
        """public abstract boolean java.util.concurrent.Future.isCancelled()"""
        pass

    @staticmethod
    @overload
    def on(arg0: 'Collection') -> 'Collection':
        """public static <T> java.util.Collection<org.apache.commons.lang3.concurrent.UncheckedFuture<T>> org.apache.commons.lang3.concurrent.UncheckedFuture.on(java.util.Collection<java.util.concurrent.Future<T>>)"""
        return Collection.__wrap(__UncheckedFuture.on(arg0))

    @staticmethod
    @overload
    def on(arg0: 'Future') -> 'UncheckedFuture':
        """public static <T> org.apache.commons.lang3.concurrent.UncheckedFuture<T> org.apache.commons.lang3.concurrent.UncheckedFuture.on(java.util.concurrent.Future<T>)"""
        return UncheckedFuture.__wrap(__UncheckedFuture.on(arg0))

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state())

    @abstractmethod
    def isDone(self, ):
        """public abstract boolean java.util.concurrent.Future.isDone()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import org.apache.commons.lang3.concurrent.ConcurrentException as __ConcurrentException
__ConcurrentException = __ConcurrentException
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConcurrentException(__Exception, Exception):
    """org.apache.commons.lang3.concurrent.ConcurrentException"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentException) -> 'ConcurrentException':
        return ConcurrentException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentException):
        """
        Dynamic initializer for ConcurrentException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentException(java.lang.String,java.lang.Throwable)"""
        val = __ConcurrentException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentException(java.lang.Throwable)"""
        val = __ConcurrentException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.CallableBackgroundInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future as __Future
__Future = __Future
import java.util.concurrent.ExecutorService as ExecutorService
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
from builtins import object
import org.apache.commons.lang3.concurrent.BackgroundInitializer as __BackgroundInitializer
__BackgroundInitializer = __BackgroundInitializer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.concurrent.CallableBackgroundInitializer as __CallableBackgroundInitializer
__CallableBackgroundInitializer = __CallableBackgroundInitializer
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CallableBackgroundInitializer(__BackgroundInitializer, BackgroundInitializer):
    """org.apache.commons.lang3.concurrent.CallableBackgroundInitializer"""
 
    @staticmethod
    def __wrap(java_value: __CallableBackgroundInitializer) -> 'CallableBackgroundInitializer':
        return CallableBackgroundInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CallableBackgroundInitializer):
        """
        Dynamic initializer for CallableBackgroundInitializer.
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
    def setExternalExecutor(self, arg0: 'ExecutorService'):
        """public final synchronized void org.apache.commons.lang3.concurrent.BackgroundInitializer.setExternalExecutor(java.util.concurrent.ExecutorService)"""
        super(__BackgroundInitializer, self).setExternalExecutor(arg0)

    @override
    @overload
    def getFuture(self) -> 'Future':
        """public synchronized java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.BackgroundInitializer.getFuture()"""
        return 'Future'.__wrap(super(BackgroundInitializer, self).getFuture())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Callable'):
        """public org.apache.commons.lang3.concurrent.CallableBackgroundInitializer(java.util.concurrent.Callable<T>)"""
        val = __CallableBackgroundInitializer(arg0)
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

    @overload
    def __init__(self, arg0: 'Callable', arg1: 'ExecutorService'):
        """public org.apache.commons.lang3.concurrent.CallableBackgroundInitializer(java.util.concurrent.Callable<T>,java.util.concurrent.ExecutorService)"""
        val = __CallableBackgroundInitializer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.BackgroundInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(BackgroundInitializer, self).get())

    @override
    @overload
    def start(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.start()"""
        return bool.__wrap(super(BackgroundInitializer, self).start())

    @override
    @overload
    def getExternalExecutor(self) -> 'ExecutorService':
        """public final synchronized java.util.concurrent.ExecutorService org.apache.commons.lang3.concurrent.BackgroundInitializer.getExternalExecutor()"""
        return 'ExecutorService'.__wrap(super(BackgroundInitializer, self).getExternalExecutor())

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

    @override
    @overload
    def isStarted(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.isStarted()"""
        return bool.__wrap(super(BackgroundInitializer, self).isStarted()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.BasicThreadFactory
import java.lang.Thread as Thread
import java.util.concurrent.ThreadFactory as __ThreadFactory
__ThreadFactory = __ThreadFactory
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.BasicThreadFactory as __BasicThreadFactory
__BasicThreadFactory = __BasicThreadFactory
import java.lang.Runnable as Runnable
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import java.lang.Thread as __Thread
__Thread = __Thread
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.Thread as __Thread_UncaughtExceptionHandler
__UncaughtExceptionHandler = __Thread_UncaughtExceptionHandler.UncaughtExceptionHandler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.concurrent.ThreadFactory as ThreadFactory
from builtins import int
 
class BasicThreadFactory(__ThreadFactory, ThreadFactory):
    """org.apache.commons.lang3.concurrent.BasicThreadFactory"""
 
    @staticmethod
    def __wrap(java_value: __BasicThreadFactory) -> 'BasicThreadFactory':
        return BasicThreadFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BasicThreadFactory):
        """
        Dynamic initializer for BasicThreadFactory.
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
    def getWrappedFactory(self) -> 'ThreadFactory':
        """public final java.util.concurrent.ThreadFactory org.apache.commons.lang3.concurrent.BasicThreadFactory.getWrappedFactory()"""
        return 'ThreadFactory'.__wrap(super(BasicThreadFactory, self).getWrappedFactory())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getDaemonFlag(self) -> 'Boolean':
        """public final java.lang.Boolean org.apache.commons.lang3.concurrent.BasicThreadFactory.getDaemonFlag()"""
        return 'Boolean'.__wrap(super(BasicThreadFactory, self).getDaemonFlag())

    @overload
    def getPriority(self) -> 'Integer':
        """public final java.lang.Integer org.apache.commons.lang3.concurrent.BasicThreadFactory.getPriority()"""
        return __transform(super(BasicThreadFactory, self).getPriority()).'Integer'Value()

    @overload
    def getUncaughtExceptionHandler(self) -> 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler':
        """public final java.lang.Thread$UncaughtExceptionHandler org.apache.commons.lang3.concurrent.BasicThreadFactory.getUncaughtExceptionHandler()"""
        return 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler'.__wrap(super(BasicThreadFactory, self).getUncaughtExceptionHandler())

    @overload
    def getThreadCount(self) -> int:
        """public long org.apache.commons.lang3.concurrent.BasicThreadFactory.getThreadCount()"""
        return int.__wrap(super(BasicThreadFactory, self).getThreadCount())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getNamingPattern(self) -> str:
        """public final java.lang.String org.apache.commons.lang3.concurrent.BasicThreadFactory.getNamingPattern()"""
        return str.__wrap(super(BasicThreadFactory, self).getNamingPattern())

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
    def newThread(self, arg0: 'Runnable') -> 'Thread':
        """public java.lang.Thread org.apache.commons.lang3.concurrent.BasicThreadFactory.newThread(java.lang.Runnable)"""
        return 'Thread'.__wrap(super(__BasicThreadFactory, self).newThread(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.concurrent.Memoizer
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import org.apache.commons.lang3.concurrent.Memoizer as __Memoizer
__Memoizer = __Memoizer
from builtins import int
 
class Memoizer(__Computable, Computable):
    """org.apache.commons.lang3.concurrent.Memoizer"""
 
    @staticmethod
    def __wrap(java_value: __Memoizer) -> 'Memoizer':
        return Memoizer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Memoizer):
        """
        Dynamic initializer for Memoizer.
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
    def __init__(self, arg0: 'Computable', arg1: bool):
        """public org.apache.commons.lang3.concurrent.Memoizer(org.apache.commons.lang3.concurrent.Computable<I, O>,boolean)"""
        val = __Memoizer(arg0, __boolean.valueOf(arg1))
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
    def __init__(self, arg0: 'Function', arg1: bool):
        """public org.apache.commons.lang3.concurrent.Memoizer(java.util.function.Function<I, O>,boolean)"""
        val = __Memoizer(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Computable'):
        """public org.apache.commons.lang3.concurrent.Memoizer(org.apache.commons.lang3.concurrent.Computable<I, O>)"""
        val = __Memoizer(arg0)
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

    @overload
    def compute(self, arg0: object) -> object:
        """public O org.apache.commons.lang3.concurrent.Memoizer.compute(I) throws java.lang.InterruptedException"""
        return object.__wrap(super(__Memoizer, self).compute(arg0))

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
    def __init__(self, arg0: 'Function'):
        """public org.apache.commons.lang3.concurrent.Memoizer(java.util.function.Function<I, O>)"""
        val = __Memoizer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.concurrent.TimedSemaphore
import org.apache.commons.lang3.concurrent.TimedSemaphore as __TimedSemaphore
__TimedSemaphore = __TimedSemaphore
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.util.concurrent.TimeUnit as __TimeUnit
__TimeUnit = __TimeUnit
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TimedSemaphore():
    """org.apache.commons.lang3.concurrent.TimedSemaphore"""
 
    @staticmethod
    def __wrap(java_value: __TimedSemaphore) -> 'TimedSemaphore':
        return TimedSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimedSemaphore):
        """
        Dynamic initializer for TimedSemaphore.
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
    def __init__(self, arg0: 'ScheduledExecutorService', arg1: int, arg2: 'TimeUnit', arg3: int):
        """public org.apache.commons.lang3.concurrent.TimedSemaphore(java.util.concurrent.ScheduledExecutorService,long,java.util.concurrent.TimeUnit,int)"""
        val = __TimedSemaphore(arg0, __long.valueOf(arg1), arg2, __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def acquire(self):
        """public synchronized void org.apache.commons.lang3.concurrent.TimedSemaphore.acquire() throws java.lang.InterruptedException"""
        super(TimedSemaphore, self).acquire()

    @overload
    def getAverageCallsPerPeriod(self) -> float:
        """public synchronized double org.apache.commons.lang3.concurrent.TimedSemaphore.getAverageCallsPerPeriod()"""
        return float.__wrap(super(TimedSemaphore, self).getAverageCallsPerPeriod())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getAcquireCount(self) -> int:
        """public synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getAcquireCount()"""
        return int.__wrap(super(TimedSemaphore, self).getAcquireCount())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isShutdown(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.TimedSemaphore.isShutdown()"""
        return bool.__wrap(super(TimedSemaphore, self).isShutdown())

    @overload
    def setLimit(self, arg0: int):
        """public final synchronized void org.apache.commons.lang3.concurrent.TimedSemaphore.setLimit(int)"""
        super(__TimedSemaphore, self).setLimit(__int.valueOf(arg0))

    @overload
    def tryAcquire(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.TimedSemaphore.tryAcquire()"""
        return bool.__wrap(super(TimedSemaphore, self).tryAcquire())

    @overload
    def getUnit(self) -> 'TimeUnit':
        """public java.util.concurrent.TimeUnit org.apache.commons.lang3.concurrent.TimedSemaphore.getUnit()"""
        return 'TimeUnit'.__wrap(super(TimedSemaphore, self).getUnit())

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
    def getAvailablePermits(self) -> int:
        """public synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getAvailablePermits()"""
        return int.__wrap(super(TimedSemaphore, self).getAvailablePermits())

    @overload
    def __init__(self, arg0: int, arg1: 'TimeUnit', arg2: int):
        """public org.apache.commons.lang3.concurrent.TimedSemaphore(long,java.util.concurrent.TimeUnit,int)"""
        val = __TimedSemaphore(__long.valueOf(arg0), arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getLastAcquiresPerPeriod(self) -> int:
        """public synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getLastAcquiresPerPeriod()"""
        return int.__wrap(super(TimedSemaphore, self).getLastAcquiresPerPeriod())

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
    def getLimit(self) -> int:
        """public final synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getLimit()"""
        return int.__wrap(super(TimedSemaphore, self).getLimit())

    @overload
    def shutdown(self):
        """public synchronized void org.apache.commons.lang3.concurrent.TimedSemaphore.shutdown()"""
        super(TimedSemaphore, self).shutdown()

    @overload
    def getPeriod(self) -> int:
        """public long org.apache.commons.lang3.concurrent.TimedSemaphore.getPeriod()"""
        return int.__wrap(super(TimedSemaphore, self).getPeriod())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConstantInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.concurrent.ConstantInitializer as __ConstantInitializer
__ConstantInitializer = __ConstantInitializer
from builtins import int
 
class ConstantInitializer(__ConcurrentInitializer, ConcurrentInitializer):
    """org.apache.commons.lang3.concurrent.ConstantInitializer"""
 
    @staticmethod
    def __wrap(java_value: __ConstantInitializer) -> 'ConstantInitializer':
        return ConstantInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantInitializer):
        """
        Dynamic initializer for ConstantInitializer.
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
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.ConstantInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(ConstantInitializer, self).get())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.concurrent.ConstantInitializer.hashCode()"""
        return int.__wrap(super(ConstantInitializer, self).hashCode())

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.concurrent.ConstantInitializer(T)"""
        val = __ConstantInitializer(arg0)
        self.__dict__ = val.__dict__
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
    def getObject(self) -> object:
        """public final T org.apache.commons.lang3.concurrent.ConstantInitializer.getObject()"""
        return object.__wrap(super(ConstantInitializer, self).getObject())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.concurrent.ConstantInitializer.toString()"""
        return str.__wrap(super(ConstantInitializer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.ConstantInitializer.equals(java.lang.Object)"""
        return bool.__wrap(super(__ConstantInitializer, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AbstractFutureProxy
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import org.apache.commons.lang3.concurrent.AbstractFutureProxy as __AbstractFutureProxy
__AbstractFutureProxy = __AbstractFutureProxy
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractFutureProxy(ABC, __Future, Future):
    """org.apache.commons.lang3.concurrent.AbstractFutureProxy"""
 
    @staticmethod
    def __wrap(java_value: __AbstractFutureProxy) -> 'AbstractFutureProxy':
        return AbstractFutureProxy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractFutureProxy):
        """
        Dynamic initializer for AbstractFutureProxy.
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
    def get(self) -> object:
        """public V org.apache.commons.lang3.concurrent.AbstractFutureProxy.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(AbstractFutureProxy, self).get())

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
    def getFuture(self) -> 'Future':
        """public java.util.concurrent.Future<V> org.apache.commons.lang3.concurrent.AbstractFutureProxy.getFuture()"""
        return 'Future'.__wrap(super(AbstractFutureProxy, self).getFuture())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractFutureProxy.isDone()"""
        return bool.__wrap(super(AbstractFutureProxy, self).isDone())

    @overload
    def get(self, arg0: int, arg1: 'TimeUnit') -> object:
        """public V org.apache.commons.lang3.concurrent.AbstractFutureProxy.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__AbstractFutureProxy, self).get(__long.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractFutureProxy.isCancelled()"""
        return bool.__wrap(super(AbstractFutureProxy, self).isCancelled())

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
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'.__wrap(super(Future, self).exceptionNow())

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
    def cancel(self, arg0: bool) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractFutureProxy.cancel(boolean)"""
        return bool.__wrap(super(__AbstractFutureProxy, self).cancel(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Future'):
        """public org.apache.commons.lang3.concurrent.AbstractFutureProxy(java.util.concurrent.Future<V>)"""
        val = __AbstractFutureProxy(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker
from builtins import str
from pyquantum_helper import override
import java.lang.Long as Long
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker as __ThresholdCircuitBreaker
__ThresholdCircuitBreaker = __ThresholdCircuitBreaker
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as __AbstractCircuitBreaker
__AbstractCircuitBreaker = __AbstractCircuitBreaker
from builtins import int
 
class ThresholdCircuitBreaker(__AbstractCircuitBreaker, AbstractCircuitBreaker):
    """org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker"""
 
    @staticmethod
    def __wrap(java_value: __ThresholdCircuitBreaker) -> 'ThresholdCircuitBreaker':
        return ThresholdCircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThresholdCircuitBreaker):
        """
        Dynamic initializer for ThresholdCircuitBreaker.
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
    def checkState(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.checkState()"""
        return bool.__wrap(super(ThresholdCircuitBreaker, self).checkState())

    @overload
    def getThreshold(self) -> int:
        """public long org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.getThreshold()"""
        return int.__wrap(super(ThresholdCircuitBreaker, self).getThreshold())

    @override
    @overload
    def close(self):
        """public void org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.close()"""
        super(ThresholdCircuitBreaker, self).close()

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

    @overload
    def incrementAndCheckState(self, arg0: 'Long') -> bool:
        """public boolean org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.incrementAndCheckState(java.lang.Long)"""
        return bool.__wrap(super(__ThresholdCircuitBreaker, self).incrementAndCheckState(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isClosed(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isClosed()"""
        return bool.__wrap(super(AbstractCircuitBreaker, self).isClosed())

    @override
    @overload
    def addChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.addChangeListener(java.beans.PropertyChangeListener)"""
        super(__AbstractCircuitBreaker, self).addChangeListener(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def removeChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.removeChangeListener(java.beans.PropertyChangeListener)"""
        super(__AbstractCircuitBreaker, self).removeChangeListener(arg0)

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isOpen()"""
        return bool.__wrap(super(AbstractCircuitBreaker, self).isOpen())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker(long)"""
        val = __ThresholdCircuitBreaker(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def open(self):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.open()"""
        super(AbstractCircuitBreaker, self).open()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentRuntimeException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.ConcurrentRuntimeException as __ConcurrentRuntimeException
__ConcurrentRuntimeException = __ConcurrentRuntimeException
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConcurrentRuntimeException(__RuntimeException, RuntimeException):
    """org.apache.commons.lang3.concurrent.ConcurrentRuntimeException"""
 
    @staticmethod
    def __wrap(java_value: __ConcurrentRuntimeException) -> 'ConcurrentRuntimeException':
        return ConcurrentRuntimeException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConcurrentRuntimeException):
        """
        Dynamic initializer for ConcurrentRuntimeException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentRuntimeException(java.lang.String,java.lang.Throwable)"""
        val = __ConcurrentRuntimeException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentRuntimeException(java.lang.Throwable)"""
        val = __ConcurrentRuntimeException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.UncheckedExecutionException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import org.apache.commons.lang3.concurrent.UncheckedExecutionException as __UncheckedExecutionException
__UncheckedExecutionException = __UncheckedExecutionException
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UncheckedExecutionException(lang3.__UncheckedException, exception.UncheckedException):
    """org.apache.commons.lang3.concurrent.UncheckedExecutionException"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedExecutionException) -> 'UncheckedExecutionException':
        return UncheckedExecutionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedExecutionException):
        """
        Dynamic initializer for UncheckedExecutionException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.UncheckedExecutionException(java.lang.Throwable)"""
        val = __UncheckedExecutionException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.UncheckedTimeoutException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import org.apache.commons.lang3.concurrent.UncheckedTimeoutException as __UncheckedTimeoutException
__UncheckedTimeoutException = __UncheckedTimeoutException
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UncheckedTimeoutException(lang3.__UncheckedException, exception.UncheckedException):
    """org.apache.commons.lang3.concurrent.UncheckedTimeoutException"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedTimeoutException) -> 'UncheckedTimeoutException':
        return UncheckedTimeoutException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedTimeoutException):
        """
        Dynamic initializer for UncheckedTimeoutException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.UncheckedTimeoutException(java.lang.Throwable)"""
        val = __UncheckedTimeoutException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.concurrent.BasicThreadFactory as __BasicThreadFactory
__BasicThreadFactory = __BasicThreadFactory
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.concurrent.BasicThreadFactory as __BasicThreadFactory_Builder
__Builder = __BasicThreadFactory_Builder.Builder
import java.lang.Integer as __int
from builtins import bool
import java.util.concurrent.ThreadFactory as ThreadFactory
from builtins import int
 
class Builder(lang3.__Builder, builder.Builder):
    """org.apache.commons.lang3.concurrent.BasicThreadFactory.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def reset(self):
        """public void org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.reset()"""
        super(Builder, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def priority(self, arg0: int) -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.priority(int)"""
        return 'Builder'.__wrap(super(__Builder, self).priority(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def daemon(self, arg0: bool) -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.daemon(boolean)"""
        return 'Builder'.__wrap(super(__Builder, self).daemon(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def wrappedFactory(self, arg0: 'ThreadFactory') -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.wrappedFactory(java.util.concurrent.ThreadFactory)"""
        return 'Builder'.__wrap(super(__Builder, self).wrappedFactory(arg0))

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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def uncaughtExceptionHandler(self, arg0: 'UncaughtExceptionHandler') -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.uncaughtExceptionHandler(java.lang.Thread$UncaughtExceptionHandler)"""
        return 'Builder'.__wrap(super(__Builder, self).uncaughtExceptionHandler(arg0))

    @override
    @overload
    def build(self) -> 'BasicThreadFactory':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.build()"""
        return 'BasicThreadFactory'.__wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def namingPattern(self, arg0: str) -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.namingPattern(java.lang.String)"""
        return 'Builder'.__wrap(super(__Builder, self).namingPattern(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.CircuitBreakingException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.concurrent.CircuitBreakingException as __CircuitBreakingException
__CircuitBreakingException = __CircuitBreakingException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CircuitBreakingException(__RuntimeException, RuntimeException):
    """org.apache.commons.lang3.concurrent.CircuitBreakingException"""
 
    @staticmethod
    def __wrap(java_value: __CircuitBreakingException) -> 'CircuitBreakingException':
        return CircuitBreakingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CircuitBreakingException):
        """
        Dynamic initializer for CircuitBreakingException.
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
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException(java.lang.Throwable)"""
        val = __CircuitBreakingException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException()"""
        val = __CircuitBreakingException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException()"""
        val = __CircuitBreakingException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException(java.lang.String)"""
        val = __CircuitBreakingException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException(java.lang.String,java.lang.Throwable)"""
        val = __CircuitBreakingException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.BackgroundInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future as __Future
__Future = __Future
import java.util.concurrent.ExecutorService as ExecutorService
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
from builtins import object
import org.apache.commons.lang3.concurrent.BackgroundInitializer as __BackgroundInitializer
__BackgroundInitializer = __BackgroundInitializer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BackgroundInitializer(ABC, __ConcurrentInitializer, ConcurrentInitializer):
    """org.apache.commons.lang3.concurrent.BackgroundInitializer"""
 
    @staticmethod
    def __wrap(java_value: __BackgroundInitializer) -> 'BackgroundInitializer':
        return BackgroundInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BackgroundInitializer):
        """
        Dynamic initializer for BackgroundInitializer.
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
    def getFuture(self) -> 'Future':
        """public synchronized java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.BackgroundInitializer.getFuture()"""
        return 'Future'.__wrap(super(BackgroundInitializer, self).getFuture())

    @overload
    def getExternalExecutor(self) -> 'ExecutorService':
        """public final synchronized java.util.concurrent.ExecutorService org.apache.commons.lang3.concurrent.BackgroundInitializer.getExternalExecutor()"""
        return 'ExecutorService'.__wrap(super(BackgroundInitializer, self).getExternalExecutor())

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

    @overload
    def isStarted(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.isStarted()"""
        return bool.__wrap(super(BackgroundInitializer, self).isStarted())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.BackgroundInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object.__wrap(super(BackgroundInitializer, self).get())

    @overload
    def setExternalExecutor(self, arg0: 'ExecutorService'):
        """public final synchronized void org.apache.commons.lang3.concurrent.BackgroundInitializer.setExternalExecutor(java.util.concurrent.ExecutorService)"""
        super(__BackgroundInitializer, self).setExternalExecutor(arg0)

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
    def start(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.start()"""
        return bool.__wrap(super(BackgroundInitializer, self).start())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))