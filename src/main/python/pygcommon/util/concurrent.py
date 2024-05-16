from __future__ import annotations
from overload import overload


 
import com.google.common.util.concurrent.Service as __Service
__Service = __Service
import java.util.concurrent.TimeUnit as TimeUnit
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
 
class Service(ABC):
    """com.google.common.util.concurrent.Service"""
 
    @staticmethod
    def __wrap(java_value: __Service) -> 'Service':
        return Service(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Service):
        """
        Dynamic initializer for Service.
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
    def failureCause(self, ):
        """public abstract java.lang.Throwable com.google.common.util.concurrent.Service.failureCause()"""
        pass

    @abstractmethod
    def stopAsync(self, ):
        """public abstract com.google.common.util.concurrent.Service com.google.common.util.concurrent.Service.stopAsync()"""
        pass

    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.Service.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__Service, self).awaitRunning(timeout)

    @abstractmethod
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.Service.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def state(self, ):
        """public abstract com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.Service.state()"""
        pass

    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.Service.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__Service, self).awaitTerminated(timeout)

    @abstractmethod
    def awaitTerminated(self, ):
        """public abstract void com.google.common.util.concurrent.Service.awaitTerminated()"""
        pass

    @abstractmethod
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.Service.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def awaitRunning(self, ):
        """public abstract void com.google.common.util.concurrent.Service.awaitRunning()"""
        pass

    @abstractmethod
    def startAsync(self, ):
        """public abstract com.google.common.util.concurrent.Service com.google.common.util.concurrent.Service.startAsync()"""
        pass

    @abstractmethod
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public abstract void com.google.common.util.concurrent.Service.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        pass

    @abstractmethod
    def isRunning(self, ):
        """public abstract boolean com.google.common.util.concurrent.Service.isRunning()"""
        pass

 
 
 
# CLASS: com.google.common.util.concurrent.Service
import com.google.common.util.concurrent.Service as __Service
__Service = __Service
import java.util.concurrent.TimeUnit as TimeUnit
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
 
class Service(ABC):
    """com.google.common.util.concurrent.Service"""
 
    @staticmethod
    def __wrap(java_value: __Service) -> 'Service':
        return Service(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Service):
        """
        Dynamic initializer for Service.
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
    def failureCause(self, ):
        """public abstract java.lang.Throwable com.google.common.util.concurrent.Service.failureCause()"""
        pass

    @abstractmethod
    def stopAsync(self, ):
        """public abstract com.google.common.util.concurrent.Service com.google.common.util.concurrent.Service.stopAsync()"""
        pass

    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.Service.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__Service, self).awaitRunning(timeout)

    @abstractmethod
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.Service.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def state(self, ):
        """public abstract com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.Service.state()"""
        pass

    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.Service.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__Service, self).awaitTerminated(timeout)

    @abstractmethod
    def awaitTerminated(self, ):
        """public abstract void com.google.common.util.concurrent.Service.awaitTerminated()"""
        pass

    @abstractmethod
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.Service.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def awaitRunning(self, ):
        """public abstract void com.google.common.util.concurrent.Service.awaitRunning()"""
        pass

    @abstractmethod
    def startAsync(self, ):
        """public abstract com.google.common.util.concurrent.Service com.google.common.util.concurrent.Service.startAsync()"""
        pass

    @abstractmethod
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public abstract void com.google.common.util.concurrent.Service.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        pass

    @abstractmethod
    def isRunning(self, ):
        """public abstract boolean com.google.common.util.concurrent.Service.isRunning()"""
        pass

 
 
 
# CLASS: com.google.common.util.concurrent.Service 
 
 
# CLASS: com.google.common.util.concurrent.UncaughtExceptionHandlers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.Thread as __Thread_UncaughtExceptionHandler
__UncaughtExceptionHandler = __Thread_UncaughtExceptionHandler.UncaughtExceptionHandler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.util.concurrent.UncaughtExceptionHandlers as __UncaughtExceptionHandlers
__UncaughtExceptionHandlers = __UncaughtExceptionHandlers
from builtins import int
 
class UncaughtExceptionHandlers():
    """com.google.common.util.concurrent.UncaughtExceptionHandlers"""
 
    @staticmethod
    def __wrap(java_value: __UncaughtExceptionHandlers) -> 'UncaughtExceptionHandlers':
        return UncaughtExceptionHandlers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncaughtExceptionHandlers):
        """
        Dynamic initializer for UncaughtExceptionHandlers.
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

    @staticmethod
    @overload
    def systemExit() -> 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler':
        """public static java.lang.Thread$UncaughtExceptionHandler com.google.common.util.concurrent.UncaughtExceptionHandlers.systemExit()"""
        return UncaughtExceptionHandler.Thread$UncaughtExceptionHandler.__wrap(__UncaughtExceptionHandlers.systemExit())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.Atomics
from builtins import str
import java.util.concurrent.atomic.AtomicReferenceArray as __AtomicReferenceArray
__AtomicReferenceArray = __AtomicReferenceArray
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.concurrent.atomic.AtomicReferenceArray as AtomicReferenceArray
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.util.concurrent.Atomics as __Atomics
__Atomics = __Atomics
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.atomic.AtomicReference as AtomicReference
import java.util.concurrent.atomic.AtomicReference as __AtomicReference
__AtomicReference = __AtomicReference
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Atomics():
    """com.google.common.util.concurrent.Atomics"""
 
    @staticmethod
    def __wrap(java_value: __Atomics) -> 'Atomics':
        return Atomics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Atomics):
        """
        Dynamic initializer for Atomics.
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
    def newReference(initialValue: object) -> 'AtomicReference':
        """public static <V> java.util.concurrent.atomic.AtomicReference<V> com.google.common.util.concurrent.Atomics.newReference(V)"""
        return AtomicReference.__wrap(__Atomics.newReference(initialValue))

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

    @staticmethod
    @overload
    def newReference() -> 'AtomicReference':
        """public static <V> java.util.concurrent.atomic.AtomicReference<V> com.google.common.util.concurrent.Atomics.newReference()"""
        return AtomicReference.__wrap(__Atomics.newReference())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def newReferenceArray(array: 'Object') -> 'AtomicReferenceArray':
        """public static <E> java.util.concurrent.atomic.AtomicReferenceArray<E> com.google.common.util.concurrent.Atomics.newReferenceArray(E[])"""
        return AtomicReferenceArray.__wrap(__Atomics.newReferenceArray(array))

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

    @staticmethod
    @overload
    def newReferenceArray(length: int) -> 'AtomicReferenceArray':
        """public static <E> java.util.concurrent.atomic.AtomicReferenceArray<E> com.google.common.util.concurrent.Atomics.newReferenceArray(int)"""
        return AtomicReferenceArray.__wrap(__Atomics.newReferenceArray(__int.valueOf(length)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ListenableFutureTask
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import java.util.concurrent.Future.State as State
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.concurrent.Executor as Executor
from builtins import object
import com.google.common.util.concurrent.ListenableFutureTask as __ListenableFutureTask
__ListenableFutureTask = __ListenableFutureTask
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
import java.util.concurrent.FutureTask as __FutureTask
__FutureTask = __FutureTask
from builtins import bool
from builtins import int
 
class ListenableFutureTask():
    """com.google.common.util.concurrent.ListenableFutureTask"""
 
    @staticmethod
    def __wrap(java_value: __ListenableFutureTask) -> 'ListenableFutureTask':
        return ListenableFutureTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListenableFutureTask):
        """
        Dynamic initializer for ListenableFutureTask.
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
    def get(self) -> object:
        """public V java.util.concurrent.FutureTask.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(FutureTask, self).get())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public java.util.concurrent.Future$State java.util.concurrent.FutureTask.state()"""
        return 'State.Future$State'.__wrap(super(FutureTask, self).state())

    @override
    @overload
    def addListener(self, listener: 'Runnable', exec: 'Executor'):
        """public void com.google.common.util.concurrent.ListenableFutureTask.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__ListenableFutureTask, self).addListener(listener, exec)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.concurrent.FutureTask.toString()"""
        return str.__wrap(super(FutureTask, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ListenableFutureTask.get(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ListenableFutureTask, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean java.util.concurrent.FutureTask.isCancelled()"""
        return bool.__wrap(super(FutureTask, self).isCancelled())

    @override
    @overload
    def run(self):
        """public void java.util.concurrent.FutureTask.run()"""
        super(FutureTask, self).run()

    @staticmethod
    @overload
    def create(runnable: 'Runnable', result: object) -> 'ListenableFutureTask':
        """public static <V> com.google.common.util.concurrent.ListenableFutureTask<V> com.google.common.util.concurrent.ListenableFutureTask.create(java.lang.Runnable,V)"""
        return ListenableFutureTask.__wrap(__ListenableFutureTask.create(runnable, result))

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
    def isDone(self) -> bool:
        """public boolean java.util.concurrent.FutureTask.isDone()"""
        return bool.__wrap(super(FutureTask, self).isDone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(callable: 'Callable') -> 'ListenableFutureTask':
        """public static <V> com.google.common.util.concurrent.ListenableFutureTask<V> com.google.common.util.concurrent.ListenableFutureTask.create(java.util.concurrent.Callable<V>)"""
        return ListenableFutureTask.__wrap(__ListenableFutureTask.create(callable))

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public java.lang.Throwable java.util.concurrent.FutureTask.exceptionNow()"""
        return 'Throwable'.__wrap(super(FutureTask, self).exceptionNow())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def cancel(self, arg0: bool) -> bool:
        """public boolean java.util.concurrent.FutureTask.cancel(boolean)"""
        return bool.__wrap(super(__FutureTask, self).cancel(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resultNow(self) -> object:
        """public V java.util.concurrent.FutureTask.resultNow()"""
        return object.__wrap(super(FutureTask, self).resultNow())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.AtomicLongMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.function.LongUnaryOperator as LongUnaryOperator
import java.util.function.LongBinaryOperator as LongBinaryOperator
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.AtomicLongMap as __AtomicLongMap
__AtomicLongMap = __AtomicLongMap
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AtomicLongMap():
    """com.google.common.util.concurrent.AtomicLongMap"""
 
    @staticmethod
    def __wrap(java_value: __AtomicLongMap) -> 'AtomicLongMap':
        return AtomicLongMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtomicLongMap):
        """
        Dynamic initializer for AtomicLongMap.
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
    def clear(self):
        """public void com.google.common.util.concurrent.AtomicLongMap.clear()"""
        super(AtomicLongMap, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAndUpdate(self, key: object, updaterFunction: 'LongUnaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndUpdate(K,java.util.function.LongUnaryOperator)"""
        return int.__wrap(super(__AtomicLongMap, self).getAndUpdate(key, updaterFunction))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAndDecrement(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndDecrement(K)"""
        return int.__wrap(super(__AtomicLongMap, self).getAndDecrement(key))

    @overload
    def accumulateAndGet(self, key: object, x: int, accumulatorFunction: 'LongBinaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.accumulateAndGet(K,long,java.util.function.LongBinaryOperator)"""
        return int.__wrap(super(__AtomicLongMap, self).accumulateAndGet(key, __long.valueOf(x), accumulatorFunction))

    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.lang.Long> com.google.common.util.concurrent.AtomicLongMap.asMap()"""
        return 'Map'.__wrap(super(AtomicLongMap, self).asMap())

    @overload
    def remove(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.remove(K)"""
        return int.__wrap(super(__AtomicLongMap, self).remove(key))

    @overload
    def put(self, key: object, newValue: int) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.put(K,long)"""
        return int.__wrap(super(__AtomicLongMap, self).put(key, __long.valueOf(newValue)))

    @overload
    def getAndAdd(self, key: object, delta: int) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndAdd(K,long)"""
        return int.__wrap(super(__AtomicLongMap, self).getAndAdd(key, __long.valueOf(delta)))

    @overload
    def getAndAccumulate(self, key: object, x: int, accumulatorFunction: 'LongBinaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndAccumulate(K,long,java.util.function.LongBinaryOperator)"""
        return int.__wrap(super(__AtomicLongMap, self).getAndAccumulate(key, __long.valueOf(x), accumulatorFunction))

    @overload
    def size(self) -> int:
        """public int com.google.common.util.concurrent.AtomicLongMap.size()"""
        return int.__wrap(super(AtomicLongMap, self).size())

    @overload
    def addAndGet(self, key: object, delta: int) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.addAndGet(K,long)"""
        return int.__wrap(super(__AtomicLongMap, self).addAndGet(key, __long.valueOf(delta)))

    @overload
    def removeAllZeros(self):
        """public void com.google.common.util.concurrent.AtomicLongMap.removeAllZeros()"""
        super(AtomicLongMap, self).removeAllZeros()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def decrementAndGet(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.decrementAndGet(K)"""
        return int.__wrap(super(__AtomicLongMap, self).decrementAndGet(key))

    @staticmethod
    @overload
    def create() -> 'AtomicLongMap':
        """public static <K> com.google.common.util.concurrent.AtomicLongMap<K> com.google.common.util.concurrent.AtomicLongMap.create()"""
        return AtomicLongMap.__wrap(__AtomicLongMap.create())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def create(m: 'Map') -> 'AtomicLongMap':
        """public static <K> com.google.common.util.concurrent.AtomicLongMap<K> com.google.common.util.concurrent.AtomicLongMap.create(java.util.Map<? extends K, ? extends java.lang.Long>)"""
        return AtomicLongMap.__wrap(__AtomicLongMap.create(m))

    @overload
    def sum(self) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.sum()"""
        return int.__wrap(super(AtomicLongMap, self).sum())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def get(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.get(K)"""
        return int.__wrap(super(__AtomicLongMap, self).get(key))

    @overload
    def updateAndGet(self, key: object, updaterFunction: 'LongUnaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.updateAndGet(K,java.util.function.LongUnaryOperator)"""
        return int.__wrap(super(__AtomicLongMap, self).updateAndGet(key, updaterFunction))

    @overload
    def incrementAndGet(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.incrementAndGet(K)"""
        return int.__wrap(super(__AtomicLongMap, self).incrementAndGet(key))

    @overload
    def containsKey(self, key: object) -> bool:
        """public boolean com.google.common.util.concurrent.AtomicLongMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AtomicLongMap, self).containsKey(key))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.util.concurrent.AtomicLongMap.isEmpty()"""
        return bool.__wrap(super(AtomicLongMap, self).isEmpty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AtomicLongMap.toString()"""
        return str.__wrap(super(AtomicLongMap, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.util.concurrent.AtomicLongMap.putAll(java.util.Map<? extends K, ? extends java.lang.Long>)"""
        super(__AtomicLongMap, self).putAll(m)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def removeIfZero(self, key: object) -> bool:
        """public boolean com.google.common.util.concurrent.AtomicLongMap.removeIfZero(K)"""
        return bool.__wrap(super(__AtomicLongMap, self).removeIfZero(key))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAndIncrement(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndIncrement(K)"""
        return int.__wrap(super(__AtomicLongMap, self).getAndIncrement(key)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner5$ClosingFunction5
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner5_ClosingFunction5
__ClosingFunction5 = __ClosingFuture_Combiner5_ClosingFunction5.Combiner5.ClosingFunction5
from abc import abstractmethod, ABC
 
class ClosingFunction5(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner5.ClosingFunction5"""
 
    @staticmethod
    def __wrap(java_value: __ClosingFunction5) -> 'ClosingFunction5':
        return ClosingFunction5(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingFunction5):
        """
        Dynamic initializer for ClosingFunction5.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object, value5: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner5$ClosingFunction5.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4,V5) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingListenableFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ForwardingListenableFuture as __ForwardingListenableFuture
__ForwardingListenableFuture = __ForwardingListenableFuture
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import com.google.common.util.concurrent.ForwardingFuture as __ForwardingFuture
__ForwardingFuture = __ForwardingFuture
from builtins import int
 
class ForwardingListenableFuture(ABC):
    """com.google.common.util.concurrent.ForwardingListenableFuture"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingListenableFuture) -> 'ForwardingListenableFuture':
        return ForwardingListenableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingListenableFuture):
        """
        Dynamic initializer for ForwardingListenableFuture.
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
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ForwardingFuture, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool.__wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(ForwardingFuture, self).get())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool.__wrap(super(__ForwardingFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

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
    def addListener(self, listener: 'Runnable', exec: 'Executor'):
        """public void com.google.common.util.concurrent.ForwardingListenableFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__ForwardingListenableFuture, self).addListener(listener, exec)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

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
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool.__wrap(super(ForwardingFuture, self).isDone())

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
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state()) 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$Policies
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_Policy
__Policy = __CycleDetectingLockFactory_Policy.Policy
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_Policies
__Policies = __CycleDetectingLockFactory_Policies.Policies
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Policies(ABC):
    """com.google.common.util.concurrent.CycleDetectingLockFactory.Policies"""
 
    @staticmethod
    def __wrap(java_value: __Policies) -> 'Policies':
        return Policies(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Policies):
        """
        Dynamic initializer for Policies.
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
    def values() -> List['Policies']:
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory$Policies[] com.google.common.util.concurrent.CycleDetectingLockFactory$Policies.values()"""
        return List[Policies].__wrap(__Policies.values())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

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

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Policies':
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory$Policies com.google.common.util.concurrent.CycleDetectingLockFactory$Policies.valueOf(java.lang.String)"""
        return Policies.__wrap(__Policies.valueOf(name))

    @abstractmethod
    def handlePotentialDeadlock(self, exception: 'PotentialDeadlockException'):
        """public abstract void com.google.common.util.concurrent.CycleDetectingLockFactory$Policy.handlePotentialDeadlock(com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture
__ClosingFuture = __ClosingFuture
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner
__Combiner = __ClosingFuture_Combiner.Combiner
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner2
__Combiner2 = __ClosingFuture_Combiner2.Combiner2
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Combiner2():
    """com.google.common.util.concurrent.ClosingFuture.Combiner2"""
 
    @staticmethod
    def __wrap(java_value: __Combiner2) -> 'Combiner2':
        return Combiner2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Combiner2):
        """
        Dynamic initializer for Combiner2.
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
    def call(self, function: 'ClosingFunction2', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner2.call(com.google.common.util.concurrent.ClosingFuture$Combiner2$ClosingFunction2<V1, V2, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner2, self).call(function, executor))

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
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).call(combiningCallable, executor))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def callAsync(self, function: 'AsyncClosingFunction2', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner2.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner2$AsyncClosingFunction2<V1, V2, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner2, self).callAsync(function, executor))

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).callAsync(combiningCallable, executor))

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ValueAndCloser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_ValueAndCloser
__ValueAndCloser = __ClosingFuture_ValueAndCloser.ValueAndCloser
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
 
class ValueAndCloser():
    """com.google.common.util.concurrent.ClosingFuture.ValueAndCloser"""
 
    @staticmethod
    def __wrap(java_value: __ValueAndCloser) -> 'ValueAndCloser':
        return ValueAndCloser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueAndCloser):
        """
        Dynamic initializer for ValueAndCloser.
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
    def closeAsync(self):
        """public void com.google.common.util.concurrent.ClosingFuture$ValueAndCloser.closeAsync()"""
        super(ValueAndCloser, self).closeAsync()

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
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ClosingFuture$ValueAndCloser.get() throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(ValueAndCloser, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingExecutorService
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.ForwardingExecutorService as __ForwardingExecutorService
__ForwardingExecutorService = __ForwardingExecutorService
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Runnable as Runnable
import java.util.Collection as Collection
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
from builtins import object
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ForwardingExecutorService(ABC):
    """com.google.common.util.concurrent.ForwardingExecutorService"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingExecutorService) -> 'ForwardingExecutorService':
        return ForwardingExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingExecutorService):
        """
        Dynamic initializer for ForwardingExecutorService.
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
    def submit(self, task: 'Runnable') -> 'Future':
        """public java.util.concurrent.Future<?> com.google.common.util.concurrent.ForwardingExecutorService.submit(java.lang.Runnable)"""
        return 'Future'.__wrap(super(__ForwardingExecutorService, self).submit(task))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isShutdown()"""
        return bool.__wrap(super(ForwardingExecutorService, self).isShutdown())

    @override
    @overload
    def execute(self, command: 'Runnable'):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.execute(java.lang.Runnable)"""
        super(__ForwardingExecutorService, self).execute(command)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def submit(self, task: 'Runnable', result: object) -> 'Future':
        """public <T> java.util.concurrent.Future<T> com.google.common.util.concurrent.ForwardingExecutorService.submit(java.lang.Runnable,T)"""
        return 'Future'.__wrap(super(__ForwardingExecutorService, self).submit(task, result))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> com.google.common.util.concurrent.ForwardingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(ForwardingExecutorService, self).shutdownNow())

    @override
    @overload
    def shutdown(self):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.shutdown()"""
        super(ForwardingExecutorService, self).shutdown()

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ForwardingExecutorService, self).invokeAny(tasks, __long.valueOf(timeout), unit))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isTerminated()"""
        return bool.__wrap(super(ForwardingExecutorService, self).isTerminated())

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
    def awaitTermination(self, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ForwardingExecutorService, self).awaitTermination(__long.valueOf(timeout), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def invokeAll(self, tasks: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ForwardingExecutorService, self).invokeAll(tasks))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def invokeAny(self, tasks: 'Collection') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingExecutorService, self).invokeAny(tasks))

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ForwardingExecutorService, self).invokeAll(tasks, __long.valueOf(timeout), unit))

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def submit(self, task: 'Callable') -> 'Future':
        """public <T> java.util.concurrent.Future<T> com.google.common.util.concurrent.ForwardingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'Future'.__wrap(super(__ForwardingExecutorService, self).submit(task))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.Striped
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.Striped as __Striped
__Striped = __Striped
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class Striped(ABC):
    """com.google.common.util.concurrent.Striped"""
 
    @staticmethod
    def __wrap(java_value: __Striped) -> 'Striped':
        return Striped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Striped):
        """
        Dynamic initializer for Striped.
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

    @staticmethod
    @overload
    def readWriteLock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.ReadWriteLock> com.google.common.util.concurrent.Striped.readWriteLock(int)"""
        return Striped.__wrap(__Striped.readWriteLock(__int.valueOf(stripes)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def lazyWeakReadWriteLock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.ReadWriteLock> com.google.common.util.concurrent.Striped.lazyWeakReadWriteLock(int)"""
        return Striped.__wrap(__Striped.lazyWeakReadWriteLock(__int.valueOf(stripes)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def bulkGet(self, keys: 'Iterable') -> 'Iterable':
        """public java.lang.Iterable<L> com.google.common.util.concurrent.Striped.bulkGet(java.lang.Iterable<?>)"""
        return 'Iterable'.__wrap(super(__Striped, self).bulkGet(keys))

    @abstractmethod
    def getAt(self, index: int):
        """public abstract L com.google.common.util.concurrent.Striped.getAt(int)"""
        pass

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

    @abstractmethod
    def size(self, ):
        """public abstract int com.google.common.util.concurrent.Striped.size()"""
        pass

    @staticmethod
    @overload
    def semaphore(stripes: int, permits: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.Semaphore> com.google.common.util.concurrent.Striped.semaphore(int,int)"""
        return Striped.__wrap(__Striped.semaphore(__int.valueOf(stripes), __int.valueOf(permits)))

    @abstractmethod
    def get(self, key: object):
        """public abstract L com.google.common.util.concurrent.Striped.get(java.lang.Object)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def lazyWeakSemaphore(stripes: int, permits: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.Semaphore> com.google.common.util.concurrent.Striped.lazyWeakSemaphore(int,int)"""
        return Striped.__wrap(__Striped.lazyWeakSemaphore(__int.valueOf(stripes), __int.valueOf(permits)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def lock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.Lock> com.google.common.util.concurrent.Striped.lock(int)"""
        return Striped.__wrap(__Striped.lock(__int.valueOf(stripes)))

    @staticmethod
    @overload
    def lazyWeakLock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.Lock> com.google.common.util.concurrent.Striped.lazyWeakLock(int)"""
        return Striped.__wrap(__Striped.lazyWeakLock(__int.valueOf(stripes)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractService
import com.google.common.util.concurrent.AbstractService as __AbstractService
__AbstractService = __AbstractService
from builtins import str
from pyquantum_helper import override
import com.google.common.util.concurrent.Service as __Service
__Service = __Service
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.Service as __Service_State
__State = __Service_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractService(ABC):
    """com.google.common.util.concurrent.AbstractService"""
 
    @staticmethod
    def __wrap(java_value: __AbstractService) -> 'AbstractService':
        return AbstractService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractService):
        """
        Dynamic initializer for AbstractService.
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
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractService, self).awaitRunning(timeout)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractService, self).awaitTerminated(__long.valueOf(timeout), unit)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractService.failureCause()"""
        return 'Throwable'.__wrap(super(AbstractService, self).failureCause())

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractService.isRunning()"""
        return bool.__wrap(super(AbstractService, self).isRunning())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def awaitRunning(self):
        """public final void com.google.common.util.concurrent.AbstractService.awaitRunning()"""
        super(AbstractService, self).awaitRunning()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractService.stopAsync()"""
        return 'Service'.__wrap(super(AbstractService, self).stopAsync())

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractService, self).awaitTerminated(timeout)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractService.startAsync()"""
        return 'Service'.__wrap(super(AbstractService, self).startAsync())

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(__AbstractService, self).addListener(listener, executor)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractService.state()"""
        return 'State'.__wrap(super(AbstractService, self).state())

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractService.awaitTerminated()"""
        super(AbstractService, self).awaitTerminated()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractService.toString()"""
        return str.__wrap(super(AbstractService, self).toString())

    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractService, self).awaitRunning(__long.valueOf(timeout), unit)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.TimeLimiter
import java.lang.Object as __object
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Object as __Object
__Object = __Object
import java.time.Duration as Duration
import com.google.common.util.concurrent.TimeLimiter as __TimeLimiter
__TimeLimiter = __TimeLimiter
import java.util.concurrent.Callable as Callable
from abc import abstractmethod, ABC
from builtins import object
 
class TimeLimiter(ABC):
    """com.google.common.util.concurrent.TimeLimiter"""
 
    @staticmethod
    def __wrap(java_value: __TimeLimiter) -> 'TimeLimiter':
        return TimeLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeLimiter):
        """
        Dynamic initializer for TimeLimiter.
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
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def callWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def runWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        pass

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,java.time.Duration)"""
        return object.__wrap(super(__TimeLimiter, self).newProxy(target, interfaceType, timeout))

    @overload
    def callWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__TimeLimiter, self).callWithTimeout(callable, timeout))

    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__TimeLimiter, self).runUninterruptiblyWithTimeout(runnable, timeout)

    @overload
    def runWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(__TimeLimiter, self).runWithTimeout(runnable, timeout)

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__TimeLimiter, self).callUninterruptiblyWithTimeout(callable, timeout))

    @abstractmethod
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def newProxy(self, target: object, interfaceType: 'Class', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,long,java.util.concurrent.TimeUnit)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingListenableFuture$SimpleForwardingListenableFuture
import java.lang.Boolean as __boolean
from builtins import type
import java.util.concurrent.Future as __Future
__Future = __Future
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Class as __Class
__Class = __Class
import com.google.common.util.concurrent.ForwardingListenableFuture as __ForwardingListenableFuture
__ForwardingListenableFuture = __ForwardingListenableFuture
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import com.google.common.util.concurrent.ForwardingListenableFuture as __ForwardingListenableFuture_SimpleForwardingListenableFuture
__SimpleForwardingListenableFuture = __ForwardingListenableFuture_SimpleForwardingListenableFuture.SimpleForwardingListenableFuture
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import com.google.common.util.concurrent.ForwardingFuture as __ForwardingFuture
__ForwardingFuture = __ForwardingFuture
from builtins import int
 
class SimpleForwardingListenableFuture(ABC):
    """com.google.common.util.concurrent.ForwardingListenableFuture.SimpleForwardingListenableFuture"""
 
    @staticmethod
    def __wrap(java_value: __SimpleForwardingListenableFuture) -> 'SimpleForwardingListenableFuture':
        return SimpleForwardingListenableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleForwardingListenableFuture):
        """
        Dynamic initializer for SimpleForwardingListenableFuture.
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
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ForwardingFuture, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool.__wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(ForwardingFuture, self).get())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool.__wrap(super(__ForwardingFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

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
    def addListener(self, listener: 'Runnable', exec: 'Executor'):
        """public void com.google.common.util.concurrent.ForwardingListenableFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__ForwardingListenableFuture, self).addListener(listener, exec)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

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
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool.__wrap(super(ForwardingFuture, self).isDone())

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
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state()) 
 
 
# CLASS: com.google.common.util.concurrent.Runnables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Runnable as __Runnable
__Runnable = __Runnable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.Runnables as __Runnables
__Runnables = __Runnables
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Runnables():
    """com.google.common.util.concurrent.Runnables"""
 
    @staticmethod
    def __wrap(java_value: __Runnables) -> 'Runnables':
        return Runnables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Runnables):
        """
        Dynamic initializer for Runnables.
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

    @staticmethod
    @overload
    def doNothing() -> 'Runnable':
        """public static java.lang.Runnable com.google.common.util.concurrent.Runnables.doNothing()"""
        return Runnable.__wrap(__Runnables.doNothing()) 
 
 
# CLASS: com.google.common.util.concurrent.ThreadFactoryBuilder
import java.util.concurrent.ThreadFactory as __ThreadFactory
__ThreadFactory = __ThreadFactory
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ThreadFactoryBuilder as __ThreadFactoryBuilder
__ThreadFactoryBuilder = __ThreadFactoryBuilder
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.concurrent.ThreadFactory as ThreadFactory
from builtins import int
 
class ThreadFactoryBuilder():
    """com.google.common.util.concurrent.ThreadFactoryBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ThreadFactoryBuilder) -> 'ThreadFactoryBuilder':
        return ThreadFactoryBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadFactoryBuilder):
        """
        Dynamic initializer for ThreadFactoryBuilder.
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

    @overload
    def build(self) -> 'ThreadFactory':
        """public java.util.concurrent.ThreadFactory com.google.common.util.concurrent.ThreadFactoryBuilder.build()"""
        return 'ThreadFactory'.__wrap(super(ThreadFactoryBuilder, self).build())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.ThreadFactoryBuilder()"""
        val = __ThreadFactoryBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setDaemon(self, daemon: bool) -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setDaemon(boolean)"""
        return 'ThreadFactoryBuilder'.__wrap(super(__ThreadFactoryBuilder, self).setDaemon(__boolean.valueOf(daemon)))

    @overload
    def setUncaughtExceptionHandler(self, uncaughtExceptionHandler: 'UncaughtExceptionHandler') -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setUncaughtExceptionHandler(java.lang.Thread$UncaughtExceptionHandler)"""
        return 'ThreadFactoryBuilder'.__wrap(super(__ThreadFactoryBuilder, self).setUncaughtExceptionHandler(uncaughtExceptionHandler))

    @overload
    def setNameFormat(self, nameFormat: str) -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setNameFormat(java.lang.String)"""
        return 'ThreadFactoryBuilder'.__wrap(super(__ThreadFactoryBuilder, self).setNameFormat(nameFormat))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.ThreadFactoryBuilder()"""
        val = __ThreadFactoryBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setThreadFactory(self, backingThreadFactory: 'ThreadFactory') -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setThreadFactory(java.util.concurrent.ThreadFactory)"""
        return 'ThreadFactoryBuilder'.__wrap(super(__ThreadFactoryBuilder, self).setThreadFactory(backingThreadFactory))

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
    def setPriority(self, priority: int) -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setPriority(int)"""
        return 'ThreadFactoryBuilder'.__wrap(super(__ThreadFactoryBuilder, self).setPriority(__int.valueOf(priority))) 
 
 
# CLASS: com.google.common.util.concurrent.ServiceManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.collect.ImmutableSetMultimap as __ImmutableSetMultimap
__ImmutableSetMultimap = __ImmutableSetMultimap
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.ServiceManager as __ServiceManager
__ServiceManager = __ServiceManager
import com.google.common.collect.ImmutableMap as __ImmutableMap
__ImmutableMap = __ImmutableMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ServiceManager():
    """com.google.common.util.concurrent.ServiceManager"""
 
    @staticmethod
    def __wrap(java_value: __ServiceManager) -> 'ServiceManager':
        return ServiceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServiceManager):
        """
        Dynamic initializer for ServiceManager.
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
    def servicesByState(self) -> 'pygcollect.ImmutableSetMultimap':
        """public com.google.common.collect.ImmutableSetMultimap<com.google.common.util.concurrent.Service$State, com.google.common.util.concurrent.Service> com.google.common.util.concurrent.ServiceManager.servicesByState()"""
        return 'pygcollect.ImmutableSetMultimap'.__wrap(super(ServiceManager, self).servicesByState())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def startupDurations(self) -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<com.google.common.util.concurrent.Service, java.time.Duration> com.google.common.util.concurrent.ServiceManager.startupDurations()"""
        return 'pygcollect.ImmutableMap'.__wrap(super(ServiceManager, self).startupDurations())

    @overload
    def startAsync(self) -> 'ServiceManager':
        """public com.google.common.util.concurrent.ServiceManager com.google.common.util.concurrent.ServiceManager.startAsync()"""
        return 'ServiceManager'.__wrap(super(ServiceManager, self).startAsync())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def awaitStopped(self, timeout: int, unit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitStopped(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__ServiceManager, self).awaitStopped(__long.valueOf(timeout), unit)

    @overload
    def awaitStopped(self, timeout: 'Duration'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitStopped(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__ServiceManager, self).awaitStopped(timeout)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def stopAsync(self) -> 'ServiceManager':
        """public com.google.common.util.concurrent.ServiceManager com.google.common.util.concurrent.ServiceManager.stopAsync()"""
        return 'ServiceManager'.__wrap(super(ServiceManager, self).stopAsync())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def awaitHealthy(self):
        """public void com.google.common.util.concurrent.ServiceManager.awaitHealthy()"""
        super(ServiceManager, self).awaitHealthy()

    @overload
    def awaitHealthy(self, timeout: 'Duration'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitHealthy(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__ServiceManager, self).awaitHealthy(timeout)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, services: 'Iterable'):
        """public com.google.common.util.concurrent.ServiceManager(java.lang.Iterable<? extends com.google.common.util.concurrent.Service>)"""
        val = __ServiceManager(services)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def startupTimes(self) -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<com.google.common.util.concurrent.Service, java.lang.Long> com.google.common.util.concurrent.ServiceManager.startupTimes()"""
        return 'pygcollect.ImmutableMap'.__wrap(super(ServiceManager, self).startupTimes())

    @overload
    def awaitStopped(self):
        """public void com.google.common.util.concurrent.ServiceManager.awaitStopped()"""
        super(ServiceManager, self).awaitStopped()

    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public void com.google.common.util.concurrent.ServiceManager.addListener(com.google.common.util.concurrent.ServiceManager$Listener,java.util.concurrent.Executor)"""
        super(__ServiceManager, self).addListener(listener, executor)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.ServiceManager.toString()"""
        return str.__wrap(super(ServiceManager, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isHealthy(self) -> bool:
        """public boolean com.google.common.util.concurrent.ServiceManager.isHealthy()"""
        return bool.__wrap(super(ServiceManager, self).isHealthy())

    @overload
    def awaitHealthy(self, timeout: int, unit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitHealthy(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__ServiceManager, self).awaitHealthy(__long.valueOf(timeout), unit) 
 
 
# CLASS: com.google.common.util.concurrent.UncheckedExecutionException
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
import com.google.common.util.concurrent.UncheckedExecutionException as __UncheckedExecutionException
__UncheckedExecutionException = __UncheckedExecutionException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UncheckedExecutionException():
    """com.google.common.util.concurrent.UncheckedExecutionException"""
 
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

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedExecutionException(java.lang.String,java.lang.Throwable)"""
        val = __UncheckedExecutionException(message, cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedExecutionException(java.lang.Throwable)"""
        val = __UncheckedExecutionException(cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Peeker
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
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Peeker
__Peeker = __ClosingFuture_Peeker.Peeker
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Peeker():
    """com.google.common.util.concurrent.ClosingFuture.Peeker"""
 
    @staticmethod
    def __wrap(java_value: __Peeker) -> 'Peeker':
        return Peeker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Peeker):
        """
        Dynamic initializer for Peeker.
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
    def getDone(self, closingFuture: 'ClosingFuture') -> object:
        """public final <D> D com.google.common.util.concurrent.ClosingFuture$Peeker.getDone(com.google.common.util.concurrent.ClosingFuture<D>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__Peeker, self).getDone(closingFuture))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ClosingCallable
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_ClosingCallable
__ClosingCallable = __ClosingFuture_ClosingCallable.ClosingCallable
 
class ClosingCallable(ABC):
    """com.google.common.util.concurrent.ClosingFuture.ClosingCallable"""
 
    @staticmethod
    def __wrap(java_value: __ClosingCallable) -> 'ClosingCallable':
        return ClosingCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingCallable):
        """
        Dynamic initializer for ClosingCallable.
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
    def call(self, closer: 'DeferredCloser'):
        """public abstract V com.google.common.util.concurrent.ClosingFuture$ClosingCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingBlockingQueue
import java.util.function.Predicate as Predicate
import com.google.common.collect.ForwardingCollection as __ForwardingCollection
__ForwardingCollection = __ForwardingCollection
import com.google.common.util.concurrent.ForwardingBlockingQueue as __ForwardingBlockingQueue
__ForwardingBlockingQueue = __ForwardingBlockingQueue
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.google.common.collect.ForwardingQueue as __ForwardingQueue
__ForwardingQueue = __ForwardingQueue
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ForwardingBlockingQueue(ABC):
    """com.google.common.util.concurrent.ForwardingBlockingQueue"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingBlockingQueue) -> 'ForwardingBlockingQueue':
        return ForwardingBlockingQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingBlockingQueue):
        """
        Dynamic initializer for ForwardingBlockingQueue.
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
    def contains(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).contains(object))

    @overload
    def retainAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).retainAll(collection))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def offer(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingQueue.offer(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ForwardingBlockingQueue, self).offer(e, __long.valueOf(timeout), unit))

    @overload
    def removeAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).removeAll(collection))

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingCollection.size()"""
        return int.__wrap(super(pygcollect.ForwardingCollection, self).size())

    @override
    @overload
    def peek(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.peek()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).peek())

    @overload
    def containsAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).containsAll(collection))

    @overload
    def addAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).addAll(collection))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def poll(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.poll()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).poll())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def put(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingQueue.put(E) throws java.lang.InterruptedException"""
        super(__ForwardingBlockingQueue, self).put(e)

    @override
    @overload
    def remainingCapacity(self) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingQueue.remainingCapacity()"""
        return int.__wrap(super(ForwardingBlockingQueue, self).remainingCapacity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.isEmpty()"""
        return bool.__wrap(super(pygcollect.ForwardingCollection, self).isEmpty())

    @overload
    def drainTo(self, c: 'Collection', maxElements: int) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingQueue.drainTo(java.util.Collection<? super E>,int)"""
        return int.__wrap(super(__ForwardingBlockingQueue, self).drainTo(c, __int.valueOf(maxElements)))

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
    def remove(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.remove()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).remove())

    @overload
    def remove(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).remove(object))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingCollection.clear()"""
        super(pygcollect.ForwardingCollection, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.common.collect.ForwardingCollection.toArray()"""
        return List[object].__wrap(super(pygcollect.ForwardingCollection, self).toArray())

    @override
    @overload
    def element(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.element()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).element())

    @overload
    def add(self, element: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.add(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).add(element))

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingCollection.iterator()"""
        return 'Iterator'.__wrap(super(pygcollect.ForwardingCollection, self).iterator())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @override
    @overload
    def take(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingQueue.take() throws java.lang.InterruptedException"""
        return object.__wrap(super(ForwardingBlockingQueue, self).take())

    @overload
    def drainTo(self, c: 'Collection') -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingQueue.drainTo(java.util.Collection<? super E>)"""
        return int.__wrap(super(__ForwardingBlockingQueue, self).drainTo(c))

    @overload
    def toArray(self, array: 'Object') -> List[object]:
        """public <T> T[] com.google.common.collect.ForwardingCollection.toArray(T[])"""
        return List[object].__wrap(super(__pygcollect.ForwardingCollection, self).toArray(array))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @overload
    def offer(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingQueue.offer(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingQueue, self).offer(o))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def poll(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingQueue.poll(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object.__wrap(super(__ForwardingBlockingQueue, self).poll(__long.valueOf(timeout), unit)) 
 
 
# CLASS: com.google.common.util.concurrent.Callables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.AsyncCallable as __AsyncCallable
__AsyncCallable = __AsyncCallable
import com.google.common.util.concurrent.Callables as __Callables
__Callables = __Callables
import java.util.concurrent.Callable as __Callable
__Callable = __Callable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Callables():
    """com.google.common.util.concurrent.Callables"""
 
    @staticmethod
    def __wrap(java_value: __Callables) -> 'Callables':
        return Callables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Callables):
        """
        Dynamic initializer for Callables.
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
    def asAsyncCallable(callable: 'Callable', listeningExecutorService: 'ListeningExecutorService') -> 'AsyncCallable':
        """public static <T> com.google.common.util.concurrent.AsyncCallable<T> com.google.common.util.concurrent.Callables.asAsyncCallable(java.util.concurrent.Callable<T>,com.google.common.util.concurrent.ListeningExecutorService)"""
        return AsyncCallable.__wrap(__Callables.asAsyncCallable(callable, listeningExecutorService))

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
    def returning(value: object) -> 'Callable':
        """public static <T> java.util.concurrent.Callable<T> com.google.common.util.concurrent.Callables.returning(T)"""
        return Callable.__wrap(__Callables.returning(value))

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
 
 
# CLASS: com.google.common.util.concurrent.ForwardingFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import com.google.common.util.concurrent.ForwardingFuture as __ForwardingFuture
__ForwardingFuture = __ForwardingFuture
from builtins import int
 
class ForwardingFuture(ABC):
    """com.google.common.util.concurrent.ForwardingFuture"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingFuture) -> 'ForwardingFuture':
        return ForwardingFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingFuture):
        """
        Dynamic initializer for ForwardingFuture.
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
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ForwardingFuture, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool.__wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(ForwardingFuture, self).get())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool.__wrap(super(__ForwardingFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

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
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

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
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool.__wrap(super(ForwardingFuture, self).isDone())

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
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state()) 
 
 
# CLASS: com.google.common.util.concurrent.ListeningExecutorService
from pyquantum_helper import override
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.util.Collection as Collection
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
from abc import abstractmethod, ABC
from builtins import object
import java.util.List as __List
__List = __List
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.ListeningExecutorService as __ListeningExecutorService
__ListeningExecutorService = __ListeningExecutorService
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Executor as __Executor
__Executor = __Executor
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.util.List as List
 
class ListeningExecutorService(ABC):
    """com.google.common.util.concurrent.ListeningExecutorService"""
 
    @staticmethod
    def __wrap(java_value: __ListeningExecutorService) -> 'ListeningExecutorService':
        return ListeningExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListeningExecutorService):
        """
        Dynamic initializer for ListeningExecutorService.
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
    def isShutdown(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isShutdown()"""
        pass

    @abstractmethod
    def submit(self, task: 'Runnable'):
        """public abstract com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable)"""
        pass

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ListeningExecutorService, self).invokeAll(tasks, timeout))

    @abstractmethod
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract boolean java.util.concurrent.ExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @abstractmethod
    def shutdownNow(self, ):
        """public abstract java.util.List<java.lang.Runnable> java.util.concurrent.ExecutorService.shutdownNow()"""
        pass

    @abstractmethod
    def submit(self, task: 'Runnable', result: object):
        """public abstract <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable,T)"""
        pass

    @abstractmethod
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit'):
        """public abstract <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @abstractmethod
    def invokeAny(self, arg0: 'Collection'):
        """public abstract <T> T java.util.concurrent.ExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def submit(self, task: 'Callable'):
        """public abstract <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ListeningExecutorService.submit(java.util.concurrent.Callable<T>)"""
        pass

    @abstractmethod
    def invokeAll(self, tasks: 'Collection'):
        """public abstract <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        pass

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @abstractmethod
    def execute(self, arg0: 'Runnable'):
        """public abstract void java.util.concurrent.Executor.execute(java.lang.Runnable)"""
        pass

    @overload
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ListeningExecutorService, self).awaitTermination(timeout))

    @abstractmethod
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit'):
        """public abstract <T> T java.util.concurrent.ExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        pass

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ListeningExecutorService, self).invokeAny(tasks, timeout))

    @abstractmethod
    def shutdown(self, ):
        """public abstract void java.util.concurrent.ExecutorService.shutdown()"""
        pass

    @abstractmethod
    def isTerminated(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isTerminated()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.FluentFuture
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import java.lang.Boolean as __boolean
from builtins import type
import java.util.concurrent.Future as __Future
__Future = __Future
import com.google.common.util.concurrent.FluentFuture as __FluentFuture
__FluentFuture = __FluentFuture
import com.google.common.util.concurrent.AbstractFuture as __AbstractFuture
__AbstractFuture = __AbstractFuture
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.Long as __long
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import int
 
class FluentFuture(ABC):
    """com.google.common.util.concurrent.FluentFuture"""
 
    @staticmethod
    def __wrap(java_value: __FluentFuture) -> 'FluentFuture':
        return FluentFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FluentFuture):
        """
        Dynamic initializer for FluentFuture.
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
    def transform(self, function: 'Function', executor: 'Executor') -> 'FluentFuture':
        """public final <T> com.google.common.util.concurrent.FluentFuture<T> com.google.common.util.concurrent.FluentFuture.transform(com.google.common.base.Function<? super V, T>,java.util.concurrent.Executor)"""
        return 'FluentFuture'.__wrap(super(__FluentFuture, self).transform(function, executor))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isCancelled()"""
        return bool.__wrap(super(AbstractFuture, self).isCancelled())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def from(future: 'ListenableFuture') -> 'FluentFuture':
        """public static <V> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.from(com.google.common.util.concurrent.ListenableFuture<V>)"""
        return FluentFuture.__wrap(__FluentFuture.from(future))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public void com.google.common.util.concurrent.AbstractFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__AbstractFuture, self).addListener(listener, executor)

    @staticmethod
    @overload
    def from(future: 'FluentFuture') -> 'FluentFuture':
        """public static <V> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.from(com.google.common.util.concurrent.FluentFuture<V>)"""
        return FluentFuture.__wrap(__FluentFuture.from(future))

    @overload
    def addCallback(self, callback: 'FutureCallback', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.FluentFuture.addCallback(com.google.common.util.concurrent.FutureCallback<? super V>,java.util.concurrent.Executor)"""
        super(__FluentFuture, self).addCallback(callback, executor)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.cancel(boolean)"""
        return bool.__wrap(super(__AbstractFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isDone()"""
        return bool.__wrap(super(AbstractFuture, self).isDone())

    @overload
    def withTimeout(self, timeout: int, unit: 'TimeUnit', scheduledExecutor: 'ScheduledExecutorService') -> 'FluentFuture':
        """public final com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.withTimeout(long,java.util.concurrent.TimeUnit,java.util.concurrent.ScheduledExecutorService)"""
        return 'FluentFuture'.__wrap(super(__FluentFuture, self).withTimeout(__long.valueOf(timeout), unit, scheduledExecutor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @overload
    def withTimeout(self, timeout: 'Duration', scheduledExecutor: 'ScheduledExecutorService') -> 'FluentFuture':
        """public final com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.withTimeout(java.time.Duration,java.util.concurrent.ScheduledExecutorService)"""
        return 'FluentFuture'.__wrap(super(__FluentFuture, self).withTimeout(timeout, scheduledExecutor))

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state())

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__AbstractFuture, self).get(__long.valueOf(timeout), unit))

    @overload
    def transformAsync(self, function: 'AsyncFunction', executor: 'Executor') -> 'FluentFuture':
        """public final <T> com.google.common.util.concurrent.FluentFuture<T> com.google.common.util.concurrent.FluentFuture.transformAsync(com.google.common.util.concurrent.AsyncFunction<? super V, T>,java.util.concurrent.Executor)"""
        return 'FluentFuture'.__wrap(super(__FluentFuture, self).transformAsync(function, executor))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractFuture.toString()"""
        return str.__wrap(super(AbstractFuture, self).toString())

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(AbstractFuture, self).get())

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
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'.__wrap(super(Future, self).exceptionNow())

    @overload
    def catchingAsync(self, exceptionType: 'Class', fallback: 'AsyncFunction', executor: 'Executor') -> 'FluentFuture':
        """public final <X extends java.lang.Throwable> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.catchingAsync(java.lang.Class<X>,com.google.common.util.concurrent.AsyncFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'FluentFuture'.__wrap(super(__FluentFuture, self).catchingAsync(exceptionType, fallback, executor))

    @overload
    def catching(self, exceptionType: 'Class', fallback: 'Function', executor: 'Executor') -> 'FluentFuture':
        """public final <X extends java.lang.Throwable> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.catching(java.lang.Class<X>,com.google.common.base.Function<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'FluentFuture'.__wrap(super(__FluentFuture, self).catching(exceptionType, fallback, executor))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler$Schedule
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.Duration as Duration
import com.google.common.util.concurrent.AbstractScheduledService as __AbstractScheduledService_CustomScheduler_Schedule
__Schedule = __AbstractScheduledService_CustomScheduler_Schedule.CustomScheduler.Schedule
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Schedule():
    """com.google.common.util.concurrent.AbstractScheduledService.CustomScheduler.Schedule"""
 
    @staticmethod
    def __wrap(java_value: __Schedule) -> 'Schedule':
        return Schedule(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Schedule):
        """
        Dynamic initializer for Schedule.
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
    def __init__(self, delay: int, unit: 'TimeUnit'):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler$Schedule(long,java.util.concurrent.TimeUnit)"""
        val = __Schedule(__long.valueOf(delay), unit)
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

    @overload
    def __init__(self, delay: 'Duration'):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler$Schedule(java.time.Duration)"""
        val = __Schedule(delay)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering
import java.util.concurrent.locks.ReentrantLock as ReentrantLock
from builtins import str
import java.lang.Boolean as __boolean
import java.util.concurrent.locks.ReentrantReadWriteLock as ReentrantReadWriteLock
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.locks.ReentrantLock as __ReentrantLock
__ReentrantLock = __ReentrantLock
import java.util.concurrent.locks.ReentrantReadWriteLock as __ReentrantReadWriteLock
__ReentrantReadWriteLock = __ReentrantReadWriteLock
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_WithExplicitOrdering
__WithExplicitOrdering = __CycleDetectingLockFactory_WithExplicitOrdering.WithExplicitOrdering
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory
__CycleDetectingLockFactory = __CycleDetectingLockFactory
import java.lang.Enum as Enum
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
 
class WithExplicitOrdering():
    """com.google.common.util.concurrent.CycleDetectingLockFactory.WithExplicitOrdering"""
 
    @staticmethod
    def __wrap(java_value: __WithExplicitOrdering) -> 'WithExplicitOrdering':
        return WithExplicitOrdering(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WithExplicitOrdering):
        """
        Dynamic initializer for WithExplicitOrdering.
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
    def newInstanceWithExplicitOrdering(enumClass: 'Class', policy: 'Policy') -> 'WithExplicitOrdering':
        """public static <E extends java.lang.Enum<E>> com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering<E> com.google.common.util.concurrent.CycleDetectingLockFactory.newInstanceWithExplicitOrdering(java.lang.Class<E>,com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return WithExplicitOrdering.__wrap(__CycleDetectingLockFactory.newInstanceWithExplicitOrdering(enumClass, policy))

    @overload
    def newReentrantLock(self, lockName: str, fair: bool) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String,boolean)"""
        return 'ReentrantLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantLock(lockName, __boolean.valueOf(fair)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newReentrantLock(self, rank: 'Enum') -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantLock(E)"""
        return 'ReentrantLock'.__wrap(super(__WithExplicitOrdering, self).newReentrantLock(rank))

    @overload
    def newReentrantReadWriteLock(self, lockName: str) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String)"""
        return 'ReentrantReadWriteLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newReentrantLock(self, lockName: str) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String)"""
        return 'ReentrantLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantLock(lockName))

    @overload
    def newReentrantReadWriteLock(self, rank: 'Enum', fair: bool) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantReadWriteLock(E,boolean)"""
        return 'ReentrantReadWriteLock'.__wrap(super(__WithExplicitOrdering, self).newReentrantReadWriteLock(rank, __boolean.valueOf(fair)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def newReentrantLock(self, rank: 'Enum', fair: bool) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantLock(E,boolean)"""
        return 'ReentrantLock'.__wrap(super(__WithExplicitOrdering, self).newReentrantLock(rank, __boolean.valueOf(fair)))

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
    def newInstance(policy: 'Policy') -> 'CycleDetectingLockFactory':
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory com.google.common.util.concurrent.CycleDetectingLockFactory.newInstance(com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return CycleDetectingLockFactory.__wrap(__CycleDetectingLockFactory.newInstance(policy))

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
    def newReentrantReadWriteLock(self, lockName: str, fair: bool) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String,boolean)"""
        return 'ReentrantReadWriteLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName, __boolean.valueOf(fair)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def newReentrantReadWriteLock(self, rank: 'Enum') -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantReadWriteLock(E)"""
        return 'ReentrantReadWriteLock'.__wrap(super(__WithExplicitOrdering, self).newReentrantReadWriteLock(rank)) 
 
 
# CLASS: com.google.common.util.concurrent.ListenableScheduledFuture
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import com.google.common.util.concurrent.ListenableScheduledFuture as __ListenableScheduledFuture
__ListenableScheduledFuture = __ListenableScheduledFuture
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Delayed as __Delayed
__Delayed = __Delayed
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
 
class ListenableScheduledFuture(ABC):
    """com.google.common.util.concurrent.ListenableScheduledFuture"""
 
    @staticmethod
    def __wrap(java_value: __ListenableScheduledFuture) -> 'ListenableScheduledFuture':
        return ListenableScheduledFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListenableScheduledFuture):
        """
        Dynamic initializer for ListenableScheduledFuture.
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
    def get(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract V java.util.concurrent.Future.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public abstract void com.google.common.util.concurrent.ListenableFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
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

    @abstractmethod
    def isCancelled(self, ):
        """public abstract boolean java.util.concurrent.Future.isCancelled()"""
        pass

    @abstractmethod
    def get(self, ):
        """public abstract V java.util.concurrent.Future.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def getDelay(self, arg0: 'TimeUnit'):
        """public abstract long java.util.concurrent.Delayed.getDelay(java.util.concurrent.TimeUnit)"""
        pass

    @abstractmethod
    def compareTo(self, arg0: object):
        """public abstract int java.lang.Comparable.compareTo(T)"""
        pass

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
 
 
# CLASS: com.google.common.util.concurrent.FutureCallback
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.FutureCallback as __FutureCallback
__FutureCallback = __FutureCallback
 
class FutureCallback(ABC):
    """com.google.common.util.concurrent.FutureCallback"""
 
    @staticmethod
    def __wrap(java_value: __FutureCallback) -> 'FutureCallback':
        return FutureCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FutureCallback):
        """
        Dynamic initializer for FutureCallback.
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
    def onFailure(self, t: 'Throwable'):
        """public abstract void com.google.common.util.concurrent.FutureCallback.onFailure(java.lang.Throwable)"""
        pass

    @abstractmethod
    def onSuccess(self, result: object):
        """public abstract void com.google.common.util.concurrent.FutureCallback.onSuccess(V)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ExecutionError
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
import java.lang.Error as Error
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.ExecutionError as __ExecutionError
__ExecutionError = __ExecutionError
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExecutionError():
    """com.google.common.util.concurrent.ExecutionError"""
 
    @staticmethod
    def __wrap(java_value: __ExecutionError) -> 'ExecutionError':
        return ExecutionError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExecutionError):
        """
        Dynamic initializer for ExecutionError.
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
    def __init__(self, message: str, cause: 'Error'):
        """public com.google.common.util.concurrent.ExecutionError(java.lang.String,java.lang.Error)"""
        val = __ExecutionError(message, cause)
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

    @overload
    def __init__(self, cause: 'Error'):
        """public com.google.common.util.concurrent.ExecutionError(java.lang.Error)"""
        val = __ExecutionError(cause)
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
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService$Scheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.AbstractScheduledService as __AbstractScheduledService_Scheduler
__Scheduler = __AbstractScheduledService_Scheduler.Scheduler
import java.time.Duration as Duration
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Scheduler(ABC):
    """com.google.common.util.concurrent.AbstractScheduledService.Scheduler"""
 
    @staticmethod
    def __wrap(java_value: __Scheduler) -> 'Scheduler':
        return Scheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scheduler):
        """
        Dynamic initializer for Scheduler.
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
    def newFixedDelaySchedule(initialDelay: 'Duration', delay: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler.__wrap(__Scheduler.newFixedDelaySchedule(initialDelay, delay))

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

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: int, period: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler.__wrap(__Scheduler.newFixedRateSchedule(__long.valueOf(initialDelay), __long.valueOf(period), unit))

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: 'Duration', period: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler.__wrap(__Scheduler.newFixedRateSchedule(initialDelay, period))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: int, delay: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler.__wrap(__Scheduler.newFixedDelaySchedule(__long.valueOf(initialDelay), __long.valueOf(delay), unit))

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
 
 
# CLASS: com.google.common.util.concurrent.Monitor$Guard
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.Monitor as __Monitor_Guard
__Guard = __Monitor_Guard.Guard
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
from builtins import int
 
class Guard(ABC):
    """com.google.common.util.concurrent.Monitor.Guard"""
 
    @staticmethod
    def __wrap(java_value: __Guard) -> 'Guard':
        return Guard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Guard):
        """
        Dynamic initializer for Guard.
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

    @abstractmethod
    def isSatisfied(self, ):
        """public abstract boolean com.google.common.util.concurrent.Monitor$Guard.isSatisfied()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.SettableFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.concurrent.Executor as Executor
from builtins import object
import com.google.common.util.concurrent.AbstractFuture as __AbstractFuture
__AbstractFuture = __AbstractFuture
import com.google.common.util.concurrent.SettableFuture as __SettableFuture
__SettableFuture = __SettableFuture
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import com.google.common.util.concurrent.AbstractFuture as __AbstractFuture_TrustedFuture
__TrustedFuture = __AbstractFuture_TrustedFuture.TrustedFuture
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SettableFuture():
    """com.google.common.util.concurrent.SettableFuture"""
 
    @staticmethod
    def __wrap(java_value: __SettableFuture) -> 'SettableFuture':
        return SettableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SettableFuture):
        """
        Dynamic initializer for SettableFuture.
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
    def isCancelled(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractFuture$TrustedFuture.isCancelled()"""
        return bool.__wrap(super(TrustedFuture, self).isCancelled())

    @override
    @overload
    def isDone(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractFuture$TrustedFuture.isDone()"""
        return bool.__wrap(super(TrustedFuture, self).isDone())

    @override
    @overload
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractFuture$TrustedFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__TrustedFuture, self).addListener(listener, executor)

    @overload
    def set(self, value: object) -> bool:
        """public boolean com.google.common.util.concurrent.SettableFuture.set(V)"""
        return bool.__wrap(super(__SettableFuture, self).set(value))

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public final V com.google.common.util.concurrent.AbstractFuture$TrustedFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__TrustedFuture, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractFuture.toString()"""
        return str.__wrap(super(AbstractFuture, self).toString())

    @staticmethod
    @overload
    def create() -> 'SettableFuture':
        """public static <V> com.google.common.util.concurrent.SettableFuture<V> com.google.common.util.concurrent.SettableFuture.create()"""
        return SettableFuture.__wrap(__SettableFuture.create())

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
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'.__wrap(super(Future, self).exceptionNow())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractFuture$TrustedFuture.cancel(boolean)"""
        return bool.__wrap(super(__TrustedFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

    @overload
    def setException(self, throwable: 'Throwable') -> bool:
        """public boolean com.google.common.util.concurrent.SettableFuture.setException(java.lang.Throwable)"""
        return bool.__wrap(super(__SettableFuture, self).setException(throwable))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def get(self) -> object:
        """public final V com.google.common.util.concurrent.AbstractFuture$TrustedFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(TrustedFuture, self).get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setFuture(self, future: 'ListenableFuture') -> bool:
        """public boolean com.google.common.util.concurrent.SettableFuture.setFuture(com.google.common.util.concurrent.ListenableFuture<? extends V>)"""
        return bool.__wrap(super(__SettableFuture, self).setFuture(future))

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
 
 
# CLASS: com.google.common.util.concurrent.AbstractFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.concurrent.Executor as Executor
from builtins import object
import com.google.common.util.concurrent.AbstractFuture as __AbstractFuture
__AbstractFuture = __AbstractFuture
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractFuture(ABC):
    """com.google.common.util.concurrent.AbstractFuture"""
 
    @staticmethod
    def __wrap(java_value: __AbstractFuture) -> 'AbstractFuture':
        return AbstractFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractFuture):
        """
        Dynamic initializer for AbstractFuture.
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
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isCancelled()"""
        return bool.__wrap(super(AbstractFuture, self).isCancelled())

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
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__AbstractFuture, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractFuture.toString()"""
        return str.__wrap(super(AbstractFuture, self).toString())

    @override
    @overload
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public void com.google.common.util.concurrent.AbstractFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__AbstractFuture, self).addListener(listener, executor)

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(AbstractFuture, self).get())

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
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'.__wrap(super(Future, self).exceptionNow())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.cancel(boolean)"""
        return bool.__wrap(super(__AbstractFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isDone()"""
        return bool.__wrap(super(AbstractFuture, self).isDone())

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
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner3$AsyncClosingFunction3
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner3_AsyncClosingFunction3
__AsyncClosingFunction3 = __ClosingFuture_Combiner3_AsyncClosingFunction3.Combiner3.AsyncClosingFunction3
from abc import abstractmethod, ABC
 
class AsyncClosingFunction3(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner3.AsyncClosingFunction3"""
 
    @staticmethod
    def __wrap(java_value: __AsyncClosingFunction3) -> 'AsyncClosingFunction3':
        return AsyncClosingFunction3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncClosingFunction3):
        """
        Dynamic initializer for AsyncClosingFunction3.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner3$AsyncClosingFunction3.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.MoreExecutors
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
import java.util.concurrent.ScheduledExecutorService as __ScheduledExecutorService
__ScheduledExecutorService = __ScheduledExecutorService
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
import java.util.concurrent.ScheduledThreadPoolExecutor as ScheduledThreadPoolExecutor
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.Executor as __Executor
__Executor = __Executor
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
from builtins import bool
import java.util.concurrent.ThreadFactory as __ThreadFactory
__ThreadFactory = __ThreadFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.MoreExecutors as __MoreExecutors
__MoreExecutors = __MoreExecutors
import java.lang.Long as __long
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ListeningExecutorService as __ListeningExecutorService
__ListeningExecutorService = __ListeningExecutorService
import java.util.concurrent.ThreadPoolExecutor as ThreadPoolExecutor
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.ListeningScheduledExecutorService as __ListeningScheduledExecutorService
__ListeningScheduledExecutorService = __ListeningScheduledExecutorService
import java.lang.Integer as __int
import java.util.concurrent.ThreadFactory as ThreadFactory
from builtins import int
 
class MoreExecutors():
    """com.google.common.util.concurrent.MoreExecutors"""
 
    @staticmethod
    def __wrap(java_value: __MoreExecutors) -> 'MoreExecutors':
        return MoreExecutors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MoreExecutors):
        """
        Dynamic initializer for MoreExecutors.
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
    def getExitingScheduledExecutorService(executor: 'ScheduledThreadPoolExecutor', terminationTimeout: 'Duration') -> 'ScheduledExecutorService':
        """public static java.util.concurrent.ScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor,java.time.Duration)"""
        return ScheduledExecutorService.__wrap(__MoreExecutors.getExitingScheduledExecutorService(executor, terminationTimeout))

    @staticmethod
    @overload
    def getExitingExecutorService(executor: 'ThreadPoolExecutor', terminationTimeout: 'Duration') -> 'ExecutorService':
        """public static java.util.concurrent.ExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingExecutorService(java.util.concurrent.ThreadPoolExecutor,java.time.Duration)"""
        return ExecutorService.__wrap(__MoreExecutors.getExitingExecutorService(executor, terminationTimeout))

    @staticmethod
    @overload
    def getExitingScheduledExecutorService(executor: 'ScheduledThreadPoolExecutor', terminationTimeout: int, timeUnit: 'TimeUnit') -> 'ScheduledExecutorService':
        """public static java.util.concurrent.ScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor,long,java.util.concurrent.TimeUnit)"""
        return ScheduledExecutorService.__wrap(__MoreExecutors.getExitingScheduledExecutorService(executor, __long.valueOf(terminationTimeout), timeUnit))

    @staticmethod
    @overload
    def newDirectExecutorService() -> 'ListeningExecutorService':
        """public static com.google.common.util.concurrent.ListeningExecutorService com.google.common.util.concurrent.MoreExecutors.newDirectExecutorService()"""
        return ListeningExecutorService.__wrap(__MoreExecutors.newDirectExecutorService())

    @staticmethod
    @overload
    def getExitingScheduledExecutorService(executor: 'ScheduledThreadPoolExecutor') -> 'ScheduledExecutorService':
        """public static java.util.concurrent.ScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor)"""
        return ScheduledExecutorService.__wrap(__MoreExecutors.getExitingScheduledExecutorService(executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def shutdownAndAwaitTermination(service: 'ExecutorService', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.MoreExecutors.shutdownAndAwaitTermination(java.util.concurrent.ExecutorService,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__MoreExecutors.shutdownAndAwaitTermination(service, __long.valueOf(timeout), unit))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def listeningDecorator(delegate: 'ExecutorService') -> 'ListeningExecutorService':
        """public static com.google.common.util.concurrent.ListeningExecutorService com.google.common.util.concurrent.MoreExecutors.listeningDecorator(java.util.concurrent.ExecutorService)"""
        return ListeningExecutorService.__wrap(__MoreExecutors.listeningDecorator(delegate))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def platformThreadFactory() -> 'ThreadFactory':
        """public static java.util.concurrent.ThreadFactory com.google.common.util.concurrent.MoreExecutors.platformThreadFactory()"""
        return ThreadFactory.__wrap(__MoreExecutors.platformThreadFactory())

    @staticmethod
    @overload
    def newSequentialExecutor(delegate: 'Executor') -> 'Executor':
        """public static java.util.concurrent.Executor com.google.common.util.concurrent.MoreExecutors.newSequentialExecutor(java.util.concurrent.Executor)"""
        return Executor.__wrap(__MoreExecutors.newSequentialExecutor(delegate))

    @staticmethod
    @overload
    def addDelayedShutdownHook(service: 'ExecutorService', terminationTimeout: 'Duration'):
        """public static void com.google.common.util.concurrent.MoreExecutors.addDelayedShutdownHook(java.util.concurrent.ExecutorService,java.time.Duration)"""
        __MoreExecutors.addDelayedShutdownHook(service, terminationTimeout)

    @staticmethod
    @overload
    def getExitingExecutorService(executor: 'ThreadPoolExecutor', terminationTimeout: int, timeUnit: 'TimeUnit') -> 'ExecutorService':
        """public static java.util.concurrent.ExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingExecutorService(java.util.concurrent.ThreadPoolExecutor,long,java.util.concurrent.TimeUnit)"""
        return ExecutorService.__wrap(__MoreExecutors.getExitingExecutorService(executor, __long.valueOf(terminationTimeout), timeUnit))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def directExecutor() -> 'Executor':
        """public static java.util.concurrent.Executor com.google.common.util.concurrent.MoreExecutors.directExecutor()"""
        return Executor.__wrap(__MoreExecutors.directExecutor())

    @staticmethod
    @overload
    def shutdownAndAwaitTermination(service: 'ExecutorService', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.MoreExecutors.shutdownAndAwaitTermination(java.util.concurrent.ExecutorService,java.time.Duration)"""
        return bool.__wrap(__MoreExecutors.shutdownAndAwaitTermination(service, timeout))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def listeningDecorator(delegate: 'ScheduledExecutorService') -> 'ListeningScheduledExecutorService':
        """public static com.google.common.util.concurrent.ListeningScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.listeningDecorator(java.util.concurrent.ScheduledExecutorService)"""
        return ListeningScheduledExecutorService.__wrap(__MoreExecutors.listeningDecorator(delegate))

    @staticmethod
    @overload
    def addDelayedShutdownHook(service: 'ExecutorService', terminationTimeout: int, timeUnit: 'TimeUnit'):
        """public static void com.google.common.util.concurrent.MoreExecutors.addDelayedShutdownHook(java.util.concurrent.ExecutorService,long,java.util.concurrent.TimeUnit)"""
        __MoreExecutors.addDelayedShutdownHook(service, __long.valueOf(terminationTimeout), timeUnit)

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
    def getExitingExecutorService(executor: 'ThreadPoolExecutor') -> 'ExecutorService':
        """public static java.util.concurrent.ExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingExecutorService(java.util.concurrent.ThreadPoolExecutor)"""
        return ExecutorService.__wrap(__MoreExecutors.getExitingExecutorService(executor))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.util.concurrent.Monitor
import java.lang.Thread as Thread
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.Monitor as __Monitor_Guard
__Guard = __Monitor_Guard.Guard
import java.time.Duration as Duration
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.Monitor as __Monitor
__Monitor = __Monitor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Monitor():
    """com.google.common.util.concurrent.Monitor"""
 
    @staticmethod
    def __wrap(java_value: __Monitor) -> 'Monitor':
        return Monitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Monitor):
        """
        Dynamic initializer for Monitor.
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
    def enterWhen(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.enterWhen(com.google.common.util.concurrent.Monitor$Guard) throws java.lang.InterruptedException"""
        super(__Monitor, self).enterWhen(guard)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def enterInterruptibly(self, time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterInterruptibly(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterInterruptibly(__long.valueOf(time), unit))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def enterWhenUninterruptibly(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhenUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(super(__Monitor, self).enterWhenUninterruptibly(guard, __long.valueOf(time), unit))

    @overload
    def enterIf(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIf(com.google.common.util.concurrent.Monitor$Guard)"""
        return bool.__wrap(super(__Monitor, self).enterIf(guard))

    @overload
    def enterWhenUninterruptibly(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhenUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration)"""
        return bool.__wrap(super(__Monitor, self).enterWhenUninterruptibly(guard, time))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def waitFor(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitFor(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).waitFor(guard, __long.valueOf(time), unit))

    @overload
    def enter(self, time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enter(long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(super(__Monitor, self).enter(__long.valueOf(time), unit))

    @overload
    def newGuard(self, isSatisfied: 'BooleanSupplier') -> 'Guard':
        """public com.google.common.util.concurrent.Monitor$Guard com.google.common.util.concurrent.Monitor.newGuard(java.util.function.BooleanSupplier)"""
        return 'Guard'.__wrap(super(__Monitor, self).newGuard(isSatisfied))

    @overload
    def enterIf(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIf(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(super(__Monitor, self).enterIf(guard, __long.valueOf(time), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def leave(self):
        """public void com.google.common.util.concurrent.Monitor.leave()"""
        super(Monitor, self).leave()

    @overload
    def enterInterruptibly(self):
        """public void com.google.common.util.concurrent.Monitor.enterInterruptibly() throws java.lang.InterruptedException"""
        super(Monitor, self).enterInterruptibly()

    @overload
    def enterWhen(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhen(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterWhen(guard, __long.valueOf(time), unit))

    @overload
    def enterIfInterruptibly(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIfInterruptibly(com.google.common.util.concurrent.Monitor$Guard) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterIfInterruptibly(guard))

    @overload
    def enterWhen(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhen(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterWhen(guard, time))

    @overload
    def enterIfInterruptibly(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIfInterruptibly(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterIfInterruptibly(guard, __long.valueOf(time), unit))

    @overload
    def enterWhenUninterruptibly(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.enterWhenUninterruptibly(com.google.common.util.concurrent.Monitor$Guard)"""
        super(__Monitor, self).enterWhenUninterruptibly(guard)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def waitForUninterruptibly(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.waitForUninterruptibly(com.google.common.util.concurrent.Monitor$Guard)"""
        super(__Monitor, self).waitForUninterruptibly(guard)

    @overload
    def waitFor(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.waitFor(com.google.common.util.concurrent.Monitor$Guard) throws java.lang.InterruptedException"""
        super(__Monitor, self).waitFor(guard)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getQueueLength(self) -> int:
        """public int com.google.common.util.concurrent.Monitor.getQueueLength()"""
        return int.__wrap(super(Monitor, self).getQueueLength())

    @overload
    def hasQueuedThread(self, thread: 'Thread') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.hasQueuedThread(java.lang.Thread)"""
        return bool.__wrap(super(__Monitor, self).hasQueuedThread(thread))

    @overload
    def enterIf(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIf(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration)"""
        return bool.__wrap(super(__Monitor, self).enterIf(guard, time))

    @overload
    def isOccupiedByCurrentThread(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.isOccupiedByCurrentThread()"""
        return bool.__wrap(super(Monitor, self).isOccupiedByCurrentThread())

    @overload
    def enter(self):
        """public void com.google.common.util.concurrent.Monitor.enter()"""
        super(Monitor, self).enter()

    @overload
    def hasWaiters(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.hasWaiters(com.google.common.util.concurrent.Monitor$Guard)"""
        return bool.__wrap(super(__Monitor, self).hasWaiters(guard))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isFair(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.isFair()"""
        return bool.__wrap(super(Monitor, self).isFair())

    @overload
    def tryEnterIf(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.tryEnterIf(com.google.common.util.concurrent.Monitor$Guard)"""
        return bool.__wrap(super(__Monitor, self).tryEnterIf(guard))

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.Monitor()"""
        val = __Monitor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.Monitor()"""
        val = __Monitor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def waitForUninterruptibly(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitForUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration)"""
        return bool.__wrap(super(__Monitor, self).waitForUninterruptibly(guard, time))

    @overload
    def enterIfInterruptibly(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIfInterruptibly(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterIfInterruptibly(guard, time))

    @overload
    def __init__(self, fair: bool):
        """public com.google.common.util.concurrent.Monitor(boolean)"""
        val = __Monitor(__boolean.valueOf(fair))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def waitForUninterruptibly(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitForUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(super(__Monitor, self).waitForUninterruptibly(guard, __long.valueOf(time), unit))

    @overload
    def enterInterruptibly(self, time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterInterruptibly(java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).enterInterruptibly(time))

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
    def isOccupied(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.isOccupied()"""
        return bool.__wrap(super(Monitor, self).isOccupied())

    @overload
    def tryEnter(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.tryEnter()"""
        return bool.__wrap(super(Monitor, self).tryEnter())

    @overload
    def waitFor(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitFor(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__Monitor, self).waitFor(guard, time))

    @overload
    def getWaitQueueLength(self, guard: 'Guard') -> int:
        """public int com.google.common.util.concurrent.Monitor.getWaitQueueLength(com.google.common.util.concurrent.Monitor$Guard)"""
        return int.__wrap(super(__Monitor, self).getWaitQueueLength(guard))

    @overload
    def getOccupiedDepth(self) -> int:
        """public int com.google.common.util.concurrent.Monitor.getOccupiedDepth()"""
        return int.__wrap(super(Monitor, self).getOccupiedDepth())

    @overload
    def hasQueuedThreads(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.hasQueuedThreads()"""
        return bool.__wrap(super(Monitor, self).hasQueuedThreads())

    @overload
    def enter(self, time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enter(java.time.Duration)"""
        return bool.__wrap(super(__Monitor, self).enter(time)) 
 
 
# CLASS: com.google.common.util.concurrent.Uninterruptibles
import java.lang.Thread as Thread
import java.util.concurrent.locks.Condition as Condition
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.concurrent.Semaphore as Semaphore
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
import java.time.Duration as Duration
import com.google.common.util.concurrent.Uninterruptibles as __Uninterruptibles
__Uninterruptibles = __Uninterruptibles
from builtins import object
import java.util.concurrent.locks.Lock as Lock
import java.util.concurrent.BlockingQueue as BlockingQueue
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.CountDownLatch as CountDownLatch
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Uninterruptibles():
    """com.google.common.util.concurrent.Uninterruptibles"""
 
    @staticmethod
    def __wrap(java_value: __Uninterruptibles) -> 'Uninterruptibles':
        return Uninterruptibles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Uninterruptibles):
        """
        Dynamic initializer for Uninterruptibles.
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
    def joinUninterruptibly(toJoin: 'Thread', timeout: int, unit: 'TimeUnit'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.joinUninterruptibly(java.lang.Thread,long,java.util.concurrent.TimeUnit)"""
        __Uninterruptibles.joinUninterruptibly(toJoin, __long.valueOf(timeout), unit)

    @staticmethod
    @overload
    def getUninterruptibly(future: 'Future', timeout: int, unit: 'TimeUnit') -> object:
        """public static <V> V com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly(java.util.concurrent.Future<V>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(__Uninterruptibles.getUninterruptibly(future, __long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def awaitTerminationUninterruptibly(executor: 'ExecutorService'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly(java.util.concurrent.ExecutorService)"""
        __Uninterruptibles.awaitTerminationUninterruptibly(executor)

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,java.time.Duration)"""
        return bool.__wrap(__Uninterruptibles.tryAcquireUninterruptibly(semaphore, timeout))

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
    def sleepUninterruptibly(sleepFor: 'Duration'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.sleepUninterruptibly(java.time.Duration)"""
        __Uninterruptibles.sleepUninterruptibly(sleepFor)

    @staticmethod
    @overload
    def takeUninterruptibly(queue: 'BlockingQueue') -> object:
        """public static <E> E com.google.common.util.concurrent.Uninterruptibles.takeUninterruptibly(java.util.concurrent.BlockingQueue<E>)"""
        return object.__wrap(__Uninterruptibles.takeUninterruptibly(queue))

    @staticmethod
    @overload
    def awaitTerminationUninterruptibly(executor: 'ExecutorService', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly(java.util.concurrent.ExecutorService,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__Uninterruptibles.awaitTerminationUninterruptibly(executor, __long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def awaitUninterruptibly(latch: 'CountDownLatch'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.CountDownLatch)"""
        __Uninterruptibles.awaitUninterruptibly(latch)

    @staticmethod
    @overload
    def tryLockUninterruptibly(lock: 'Lock', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryLockUninterruptibly(java.util.concurrent.locks.Lock,java.time.Duration)"""
        return bool.__wrap(__Uninterruptibles.tryLockUninterruptibly(lock, timeout))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def putUninterruptibly(queue: 'BlockingQueue', element: object):
        """public static <E> void com.google.common.util.concurrent.Uninterruptibles.putUninterruptibly(java.util.concurrent.BlockingQueue<E>,E)"""
        __Uninterruptibles.putUninterruptibly(queue, element)

    @staticmethod
    @overload
    def getUninterruptibly(future: 'Future', timeout: 'Duration') -> object:
        """public static <V> V com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly(java.util.concurrent.Future<V>,java.time.Duration) throws java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(__Uninterruptibles.getUninterruptibly(future, timeout))

    @staticmethod
    @overload
    def awaitUninterruptibly(condition: 'Condition', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.locks.Condition,java.time.Duration)"""
        return bool.__wrap(__Uninterruptibles.awaitUninterruptibly(condition, timeout))

    @staticmethod
    @overload
    def joinUninterruptibly(toJoin: 'Thread', timeout: 'Duration'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.joinUninterruptibly(java.lang.Thread,java.time.Duration)"""
        __Uninterruptibles.joinUninterruptibly(toJoin, timeout)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__Uninterruptibles.tryAcquireUninterruptibly(semaphore, __long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', permits: int, timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,int,java.time.Duration)"""
        return bool.__wrap(__Uninterruptibles.tryAcquireUninterruptibly(semaphore, __int.valueOf(permits), timeout))

    @staticmethod
    @overload
    def awaitUninterruptibly(latch: 'CountDownLatch', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.CountDownLatch,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__Uninterruptibles.awaitUninterruptibly(latch, __long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def awaitTerminationUninterruptibly(executor: 'ExecutorService', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly(java.util.concurrent.ExecutorService,java.time.Duration)"""
        return bool.__wrap(__Uninterruptibles.awaitTerminationUninterruptibly(executor, timeout))

    @staticmethod
    @overload
    def getUninterruptibly(future: 'Future') -> object:
        """public static <V> V com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly(java.util.concurrent.Future<V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(__Uninterruptibles.getUninterruptibly(future))

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', permits: int, timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,int,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__Uninterruptibles.tryAcquireUninterruptibly(semaphore, __int.valueOf(permits), __long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def tryLockUninterruptibly(lock: 'Lock', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryLockUninterruptibly(java.util.concurrent.locks.Lock,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__Uninterruptibles.tryLockUninterruptibly(lock, __long.valueOf(timeout), unit))

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
    def joinUninterruptibly(toJoin: 'Thread'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.joinUninterruptibly(java.lang.Thread)"""
        __Uninterruptibles.joinUninterruptibly(toJoin)

    @staticmethod
    @overload
    def awaitUninterruptibly(latch: 'CountDownLatch', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.CountDownLatch,java.time.Duration)"""
        return bool.__wrap(__Uninterruptibles.awaitUninterruptibly(latch, timeout))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def awaitUninterruptibly(condition: 'Condition', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.locks.Condition,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(__Uninterruptibles.awaitUninterruptibly(condition, __long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def sleepUninterruptibly(sleepFor: int, unit: 'TimeUnit'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.sleepUninterruptibly(long,java.util.concurrent.TimeUnit)"""
        __Uninterruptibles.sleepUninterruptibly(__long.valueOf(sleepFor), unit) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_AsyncClosingFunction
__AsyncClosingFunction = __ClosingFuture_AsyncClosingFunction.AsyncClosingFunction
from abc import abstractmethod, ABC
 
class AsyncClosingFunction(ABC):
    """com.google.common.util.concurrent.ClosingFuture.AsyncClosingFunction"""
 
    @staticmethod
    def __wrap(java_value: __AsyncClosingFunction) -> 'AsyncClosingFunction':
        return AsyncClosingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncClosingFunction):
        """
        Dynamic initializer for AsyncClosingFunction.
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
    def apply(self, closer: 'DeferredCloser', input: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,T) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingBlockingDeque
import java.util.function.Predicate as Predicate
import com.google.common.collect.ForwardingCollection as __ForwardingCollection
__ForwardingCollection = __ForwardingCollection
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Deque as __Deque
__Deque = __Deque
import java.util.Collection as Collection
import com.google.common.collect.ForwardingDeque as __ForwardingDeque
__ForwardingDeque = __ForwardingDeque
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.google.common.util.concurrent.ForwardingBlockingDeque as __ForwardingBlockingDeque
__ForwardingBlockingDeque = __ForwardingBlockingDeque
import com.google.common.collect.ForwardingQueue as __ForwardingQueue
__ForwardingQueue = __ForwardingQueue
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Deque as Deque
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ForwardingBlockingDeque(ABC):
    """com.google.common.util.concurrent.ForwardingBlockingDeque"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingBlockingDeque) -> 'ForwardingBlockingDeque':
        return ForwardingBlockingDeque(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingBlockingDeque):
        """
        Dynamic initializer for ForwardingBlockingDeque.
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
    def contains(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).contains(object))

    @overload
    def removeAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).removeAll(collection))

    @override
    @overload
    def take(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.take() throws java.lang.InterruptedException"""
        return object.__wrap(super(ForwardingBlockingDeque, self).take())

    @override
    @overload
    def pollFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.pollFirst()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).pollFirst())

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingCollection.size()"""
        return int.__wrap(super(pygcollect.ForwardingCollection, self).size())

    @overload
    def pollLast(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.pollLast(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object.__wrap(super(__ForwardingBlockingDeque, self).pollLast(__long.valueOf(timeout), unit))

    @override
    @overload
    def peek(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.peek()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).peek())

    @override
    @overload
    def remainingCapacity(self) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingDeque.remainingCapacity()"""
        return int.__wrap(super(ForwardingBlockingDeque, self).remainingCapacity())

    @overload
    def containsAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).containsAll(collection))

    @overload
    def offerLast(self, e: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.offerLast(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingDeque, self).offerLast(e))

    @overload
    def addAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).addAll(collection))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def poll(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.poll()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).poll())

    @override
    @overload
    def peekFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.peekFirst()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).peekFirst())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def offerLast(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingDeque.offerLast(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ForwardingBlockingDeque, self).offerLast(e, __long.valueOf(timeout), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.isEmpty()"""
        return bool.__wrap(super(pygcollect.ForwardingCollection, self).isEmpty())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def poll(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.poll(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object.__wrap(super(__ForwardingBlockingDeque, self).poll(__long.valueOf(timeout), unit))

    @override
    @overload
    def getFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.getFirst()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).getFirst())

    @override
    @overload
    def push(self, e: object):
        """public void com.google.common.collect.ForwardingDeque.push(E)"""
        super(__pygcollect.ForwardingDeque, self).push(e)

    @overload
    def offerFirst(self, e: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.offerFirst(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingDeque, self).offerFirst(e))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def takeFirst(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.takeFirst() throws java.lang.InterruptedException"""
        return object.__wrap(super(ForwardingBlockingDeque, self).takeFirst())

    @override
    @overload
    def addLast(self, e: object):
        """public void com.google.common.collect.ForwardingDeque.addLast(E)"""
        super(__pygcollect.ForwardingDeque, self).addLast(e)

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingCollection.clear()"""
        super(pygcollect.ForwardingCollection, self).clear()

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.common.collect.ForwardingCollection.toArray()"""
        return List[object].__wrap(super(pygcollect.ForwardingCollection, self).toArray())

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingDeque.descendingIterator()"""
        return 'Iterator'.__wrap(super(pygcollect.ForwardingDeque, self).descendingIterator())

    @override
    @overload
    def addFirst(self, e: object):
        """public void com.google.common.collect.ForwardingDeque.addFirst(E)"""
        super(__pygcollect.ForwardingDeque, self).addFirst(e)

    @overload
    def add(self, element: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.add(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).add(element))

    @override
    @overload
    def put(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingDeque.put(E) throws java.lang.InterruptedException"""
        super(__ForwardingBlockingDeque, self).put(e)

    @override
    @overload
    def pop(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.pop()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).pop())

    @overload
    def pollFirst(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.pollFirst(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object.__wrap(super(__ForwardingBlockingDeque, self).pollFirst(__long.valueOf(timeout), unit))

    @override
    @overload
    def removeLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.removeLast()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).removeLast())

    @override
    @overload
    def takeLast(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.takeLast() throws java.lang.InterruptedException"""
        return object.__wrap(super(ForwardingBlockingDeque, self).takeLast())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def reversed(self) -> 'Deque':
        """public default java.util.Deque<E> java.util.Deque.reversed()"""
        return 'Deque'.__wrap(super(Deque, self).reversed())

    @override
    @overload
    def pollLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.pollLast()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).pollLast())

    @overload
    def drainTo(self, c: 'Collection') -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingDeque.drainTo(java.util.Collection<? super E>)"""
        return int.__wrap(super(__ForwardingBlockingDeque, self).drainTo(c))

    @overload
    def offer(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingQueue.offer(E)"""
        return bool.__wrap(super(__pygcollect.ForwardingQueue, self).offer(o))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def removeFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.removeFirst()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).removeFirst())

    @override
    @overload
    def peekLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.peekLast()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).peekLast())

    @overload
    def offer(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingDeque.offer(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ForwardingBlockingDeque, self).offer(e, __long.valueOf(timeout), unit))

    @overload
    def retainAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).retainAll(collection))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.getLast()"""
        return object.__wrap(super(pygcollect.ForwardingDeque, self).getLast())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.remove()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).remove())

    @overload
    def remove(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingCollection, self).remove(object))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'.__wrap(super(Collection, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def putLast(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingDeque.putLast(E) throws java.lang.InterruptedException"""
        super(__ForwardingBlockingDeque, self).putLast(e)

    @overload
    def offerFirst(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingDeque.offerFirst(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ForwardingBlockingDeque, self).offerFirst(e, __long.valueOf(timeout), unit))

    @overload
    def removeFirstOccurrence(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.removeFirstOccurrence(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingDeque, self).removeFirstOccurrence(o))

    @overload
    def removeLastOccurrence(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.removeLastOccurrence(java.lang.Object)"""
        return bool.__wrap(super(__pygcollect.ForwardingDeque, self).removeLastOccurrence(o))

    @override
    @overload
    def element(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.element()"""
        return object.__wrap(super(pygcollect.ForwardingQueue, self).element())

    @override
    @overload
    def putFirst(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingDeque.putFirst(E) throws java.lang.InterruptedException"""
        super(__ForwardingBlockingDeque, self).putFirst(e)

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingCollection.iterator()"""
        return 'Iterator'.__wrap(super(pygcollect.ForwardingCollection, self).iterator())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def drainTo(self, c: 'Collection', maxElements: int) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingDeque.drainTo(java.util.Collection<? super E>,int)"""
        return int.__wrap(super(__ForwardingBlockingDeque, self).drainTo(c, __int.valueOf(maxElements)))

    @overload
    def toArray(self, array: 'Object') -> List[object]:
        """public <T> T[] com.google.common.collect.ForwardingCollection.toArray(T[])"""
        return List[object].__wrap(super(__pygcollect.ForwardingCollection, self).toArray(array)) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService
from builtins import str
from pyquantum_helper import override
import com.google.common.util.concurrent.Service as __Service
__Service = __Service
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.AbstractScheduledService as __AbstractScheduledService
__AbstractScheduledService = __AbstractScheduledService
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.Service as __Service_State
__State = __Service_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractScheduledService(ABC):
    """com.google.common.util.concurrent.AbstractScheduledService"""
 
    @staticmethod
    def __wrap(java_value: __AbstractScheduledService) -> 'AbstractScheduledService':
        return AbstractScheduledService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractScheduledService):
        """
        Dynamic initializer for AbstractScheduledService.
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
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractScheduledService, self).awaitTerminated(__long.valueOf(timeout), unit)

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractScheduledService.isRunning()"""
        return bool.__wrap(super(AbstractScheduledService, self).isRunning())

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractScheduledService.startAsync()"""
        return 'Service'.__wrap(super(AbstractScheduledService, self).startAsync())

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractScheduledService.stopAsync()"""
        return 'Service'.__wrap(super(AbstractScheduledService, self).stopAsync())

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractScheduledService.failureCause()"""
        return 'Throwable'.__wrap(super(AbstractScheduledService, self).failureCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractScheduledService, self).awaitRunning(timeout)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractScheduledService.toString()"""
        return str.__wrap(super(AbstractScheduledService, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractScheduledService, self).awaitTerminated(timeout)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def awaitRunning(self):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitRunning()"""
        super(AbstractScheduledService, self).awaitRunning()

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
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractScheduledService, self).awaitRunning(__long.valueOf(timeout), unit)

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitTerminated()"""
        super(AbstractScheduledService, self).awaitTerminated()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractScheduledService.state()"""
        return 'State'.__wrap(super(AbstractScheduledService, self).state())

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(__AbstractScheduledService, self).addListener(listener, executor)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.AtomicDoubleArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.util.concurrent.AtomicDoubleArray as __AtomicDoubleArray
__AtomicDoubleArray = __AtomicDoubleArray
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.DoubleBinaryOperator as DoubleBinaryOperator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
import java.util.function.DoubleUnaryOperator as DoubleUnaryOperator
 
class AtomicDoubleArray():
    """com.google.common.util.concurrent.AtomicDoubleArray"""
 
    @staticmethod
    def __wrap(java_value: __AtomicDoubleArray) -> 'AtomicDoubleArray':
        return AtomicDoubleArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtomicDoubleArray):
        """
        Dynamic initializer for AtomicDoubleArray.
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
    def compareAndSet(self, i: int, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDoubleArray.compareAndSet(int,double,double)"""
        return bool.__wrap(super(__AtomicDoubleArray, self).compareAndSet(__int.valueOf(i), __double.valueOf(expect), __double.valueOf(update)))

    @overload
    def getAndSet(self, i: int, newValue: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndSet(int,double)"""
        return float.__wrap(super(__AtomicDoubleArray, self).getAndSet(__int.valueOf(i), __double.valueOf(newValue)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AtomicDoubleArray.toString()"""
        return str.__wrap(super(AtomicDoubleArray, self).toString())

    @overload
    def accumulateAndGet(self, i: int, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.accumulateAndGet(int,double,java.util.function.DoubleBinaryOperator)"""
        return float.__wrap(super(__AtomicDoubleArray, self).accumulateAndGet(__int.valueOf(i), __double.valueOf(x), accumulatorFunction))

    @overload
    def set(self, i: int, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDoubleArray.set(int,double)"""
        super(__AtomicDoubleArray, self).set(__int.valueOf(i), __double.valueOf(newValue))

    @overload
    def lazySet(self, i: int, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDoubleArray.lazySet(int,double)"""
        super(__AtomicDoubleArray, self).lazySet(__int.valueOf(i), __double.valueOf(newValue))

    @overload
    def __init__(self, length: int):
        """public com.google.common.util.concurrent.AtomicDoubleArray(int)"""
        val = __AtomicDoubleArray(__int.valueOf(length))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAndAccumulate(self, i: int, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndAccumulate(int,double,java.util.function.DoubleBinaryOperator)"""
        return float.__wrap(super(__AtomicDoubleArray, self).getAndAccumulate(__int.valueOf(i), __double.valueOf(x), accumulatorFunction))

    @overload
    def get(self, i: int) -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.get(int)"""
        return float.__wrap(super(__AtomicDoubleArray, self).get(__int.valueOf(i)))

    @overload
    def getAndAdd(self, i: int, delta: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndAdd(int,double)"""
        return float.__wrap(super(__AtomicDoubleArray, self).getAndAdd(__int.valueOf(i), __double.valueOf(delta)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def weakCompareAndSet(self, i: int, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDoubleArray.weakCompareAndSet(int,double,double)"""
        return bool.__wrap(super(__AtomicDoubleArray, self).weakCompareAndSet(__int.valueOf(i), __double.valueOf(expect), __double.valueOf(update)))

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
    def getAndUpdate(self, i: int, updaterFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndUpdate(int,java.util.function.DoubleUnaryOperator)"""
        return float.__wrap(super(__AtomicDoubleArray, self).getAndUpdate(__int.valueOf(i), updaterFunction))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def updateAndGet(self, i: int, updaterFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.updateAndGet(int,java.util.function.DoubleUnaryOperator)"""
        return float.__wrap(super(__AtomicDoubleArray, self).updateAndGet(__int.valueOf(i), updaterFunction))

    @overload
    def length(self) -> int:
        """public final int com.google.common.util.concurrent.AtomicDoubleArray.length()"""
        return int.__wrap(super(AtomicDoubleArray, self).length())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addAndGet(self, i: int, delta: float) -> float:
        """public double com.google.common.util.concurrent.AtomicDoubleArray.addAndGet(int,double)"""
        return float.__wrap(super(__AtomicDoubleArray, self).addAndGet(__int.valueOf(i), __double.valueOf(delta)))

    @overload
    def __init__(self, array: 'double'):
        """public com.google.common.util.concurrent.AtomicDoubleArray(double[])"""
        val = __AtomicDoubleArray(array)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.google.common.util.concurrent.AbstractExecutionThreadService
from builtins import str
from pyquantum_helper import override
import com.google.common.util.concurrent.Service as __Service
__Service = __Service
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import com.google.common.util.concurrent.AbstractExecutionThreadService as __AbstractExecutionThreadService
__AbstractExecutionThreadService = __AbstractExecutionThreadService
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.Service as __Service_State
__State = __Service_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractExecutionThreadService(ABC):
    """com.google.common.util.concurrent.AbstractExecutionThreadService"""
 
    @staticmethod
    def __wrap(java_value: __AbstractExecutionThreadService) -> 'AbstractExecutionThreadService':
        return AbstractExecutionThreadService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractExecutionThreadService):
        """
        Dynamic initializer for AbstractExecutionThreadService.
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
        """public java.lang.String com.google.common.util.concurrent.AbstractExecutionThreadService.toString()"""
        return str.__wrap(super(AbstractExecutionThreadService, self).toString())

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractExecutionThreadService.isRunning()"""
        return bool.__wrap(super(AbstractExecutionThreadService, self).isRunning())

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractExecutionThreadService, self).awaitRunning(timeout)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractExecutionThreadService.state()"""
        return 'State'.__wrap(super(AbstractExecutionThreadService, self).state())

    @override
    @overload
    def awaitRunning(self):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitRunning()"""
        super(AbstractExecutionThreadService, self).awaitRunning()

    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractExecutionThreadService, self).awaitRunning(__long.valueOf(timeout), unit)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitTerminated()"""
        super(AbstractExecutionThreadService, self).awaitTerminated()

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractExecutionThreadService.failureCause()"""
        return 'Throwable'.__wrap(super(AbstractExecutionThreadService, self).failureCause())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractExecutionThreadService.startAsync()"""
        return 'Service'.__wrap(super(AbstractExecutionThreadService, self).startAsync())

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractExecutionThreadService, self).awaitTerminated(__long.valueOf(timeout), unit)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(__AbstractExecutionThreadService, self).addListener(listener, executor)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractExecutionThreadService, self).awaitTerminated(timeout)

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractExecutionThreadService.stopAsync()"""
        return 'Service'.__wrap(super(AbstractExecutionThreadService, self).stopAsync())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractListeningExecutorService
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
import java.util.concurrent.AbstractExecutorService as __AbstractExecutorService
__AbstractExecutorService = __AbstractExecutorService
from builtins import type
import java.util.Collection as Collection
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.AbstractListeningExecutorService as __AbstractListeningExecutorService
__AbstractListeningExecutorService = __AbstractListeningExecutorService
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.Executor as __Executor
__Executor = __Executor
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
from builtins import object
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ListeningExecutorService as __ListeningExecutorService
__ListeningExecutorService = __ListeningExecutorService
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class AbstractListeningExecutorService(ABC):
    """com.google.common.util.concurrent.AbstractListeningExecutorService"""
 
    @staticmethod
    def __wrap(java_value: __AbstractListeningExecutorService) -> 'AbstractListeningExecutorService':
        return AbstractListeningExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractListeningExecutorService):
        """
        Dynamic initializer for AbstractListeningExecutorService.
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
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T java.util.concurrent.AbstractExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__AbstractExecutorService, self).invokeAny(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract boolean java.util.concurrent.ExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @overload
    def submit(self, task: 'Runnable') -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.AbstractListeningExecutorService.submit(java.lang.Runnable)"""
        return 'ListenableFuture'.__wrap(super(__AbstractListeningExecutorService, self).submit(task))

    @overload
    def submit(self, task: 'Runnable', result: object) -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.AbstractListeningExecutorService.submit(java.lang.Runnable,T)"""
        return 'ListenableFuture'.__wrap(super(__AbstractListeningExecutorService, self).submit(task, result))

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> java.util.concurrent.AbstractExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__AbstractExecutorService, self).invokeAll(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def execute(self, arg0: 'Runnable'):
        """public abstract void java.util.concurrent.Executor.execute(java.lang.Runnable)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.AbstractListeningExecutorService()"""
        val = __AbstractListeningExecutorService()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def isShutdown(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isShutdown()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ListeningExecutorService, self).invokeAll(tasks, timeout))

    @abstractmethod
    def shutdownNow(self, ):
        """public abstract java.util.List<java.lang.Runnable> java.util.concurrent.ExecutorService.shutdownNow()"""
        pass

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T java.util.concurrent.AbstractExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__AbstractExecutorService, self).invokeAny(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def submit(self, task: 'Callable') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.AbstractListeningExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'ListenableFuture'.__wrap(super(__AbstractListeningExecutorService, self).submit(task))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> java.util.concurrent.AbstractExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__AbstractExecutorService, self).invokeAll(arg0))

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.AbstractListeningExecutorService()"""
        val = __AbstractListeningExecutorService()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ListeningExecutorService, self).awaitTermination(timeout))

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ListeningExecutorService, self).invokeAny(tasks, timeout))

    @abstractmethod
    def shutdown(self, ):
        """public abstract void java.util.concurrent.ExecutorService.shutdown()"""
        pass

    @abstractmethod
    def isTerminated(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isTerminated()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.RateLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.util.concurrent.RateLimiter as __RateLimiter
__RateLimiter = __RateLimiter
import java.time.Duration as Duration
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RateLimiter(ABC):
    """com.google.common.util.concurrent.RateLimiter"""
 
    @staticmethod
    def __wrap(java_value: __RateLimiter) -> 'RateLimiter':
        return RateLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RateLimiter):
        """
        Dynamic initializer for RateLimiter.
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
    def tryAcquire(self, permits: int, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(int,long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(super(__RateLimiter, self).tryAcquire(__int.valueOf(permits), __long.valueOf(timeout), unit))

    @overload
    def acquire(self, permits: int) -> float:
        """public double com.google.common.util.concurrent.RateLimiter.acquire(int)"""
        return float.__wrap(super(__RateLimiter, self).acquire(__int.valueOf(permits)))

    @staticmethod
    @overload
    def create(permitsPerSecond: float) -> 'RateLimiter':
        """public static com.google.common.util.concurrent.RateLimiter com.google.common.util.concurrent.RateLimiter.create(double)"""
        return RateLimiter.__wrap(__RateLimiter.create(__double.valueOf(permitsPerSecond)))

    @staticmethod
    @overload
    def create(permitsPerSecond: float, warmupPeriod: 'Duration') -> 'RateLimiter':
        """public static com.google.common.util.concurrent.RateLimiter com.google.common.util.concurrent.RateLimiter.create(double,java.time.Duration)"""
        return RateLimiter.__wrap(__RateLimiter.create(__double.valueOf(permitsPerSecond), warmupPeriod))

    @overload
    def tryAcquire(self, permits: int, timeout: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(int,java.time.Duration)"""
        return bool.__wrap(super(__RateLimiter, self).tryAcquire(__int.valueOf(permits), timeout))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRate(self) -> float:
        """public final double com.google.common.util.concurrent.RateLimiter.getRate()"""
        return float.__wrap(super(RateLimiter, self).getRate())

    @staticmethod
    @overload
    def create(permitsPerSecond: float, warmupPeriod: int, unit: 'TimeUnit') -> 'RateLimiter':
        """public static com.google.common.util.concurrent.RateLimiter com.google.common.util.concurrent.RateLimiter.create(double,long,java.util.concurrent.TimeUnit)"""
        return RateLimiter.__wrap(__RateLimiter.create(__double.valueOf(permitsPerSecond), __long.valueOf(warmupPeriod), unit))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def tryAcquire(self, timeout: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(java.time.Duration)"""
        return bool.__wrap(super(__RateLimiter, self).tryAcquire(timeout))

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
    def tryAcquire(self) -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire()"""
        return bool.__wrap(super(RateLimiter, self).tryAcquire())

    @overload
    def acquire(self) -> float:
        """public double com.google.common.util.concurrent.RateLimiter.acquire()"""
        return float.__wrap(super(RateLimiter, self).acquire())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def tryAcquire(self, permits: int) -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(int)"""
        return bool.__wrap(super(__RateLimiter, self).tryAcquire(__int.valueOf(permits)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.RateLimiter.toString()"""
        return str.__wrap(super(RateLimiter, self).toString())

    @overload
    def tryAcquire(self, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(long,java.util.concurrent.TimeUnit)"""
        return bool.__wrap(super(__RateLimiter, self).tryAcquire(__long.valueOf(timeout), unit))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setRate(self, permitsPerSecond: float):
        """public final void com.google.common.util.concurrent.RateLimiter.setRate(double)"""
        super(__RateLimiter, self).setRate(__double.valueOf(permitsPerSecond))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$DeferredCloser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
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
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_DeferredCloser
__DeferredCloser = __ClosingFuture_DeferredCloser.DeferredCloser
from builtins import int
 
class DeferredCloser():
    """com.google.common.util.concurrent.ClosingFuture.DeferredCloser"""
 
    @staticmethod
    def __wrap(java_value: __DeferredCloser) -> 'DeferredCloser':
        return DeferredCloser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeferredCloser):
        """
        Dynamic initializer for DeferredCloser.
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def eventuallyClose(self, closeable: object, closingExecutor: 'Executor') -> object:
        """public <C extends java.lang.Object & java.lang.AutoCloseable> C com.google.common.util.concurrent.ClosingFuture$DeferredCloser.eventuallyClose(C,java.util.concurrent.Executor)"""
        return object.__wrap(super(__DeferredCloser, self).eventuallyClose(closeable, closingExecutor))

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
 
 
# CLASS: com.google.common.util.concurrent.SimpleTimeLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.util.concurrent.ExecutorService as ExecutorService
import java.time.Duration as Duration
import com.google.common.util.concurrent.TimeLimiter as __TimeLimiter
__TimeLimiter = __TimeLimiter
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
import com.google.common.util.concurrent.SimpleTimeLimiter as __SimpleTimeLimiter
__SimpleTimeLimiter = __SimpleTimeLimiter
from builtins import int
 
class SimpleTimeLimiter():
    """com.google.common.util.concurrent.SimpleTimeLimiter"""
 
    @staticmethod
    def __wrap(java_value: __SimpleTimeLimiter) -> 'SimpleTimeLimiter':
        return SimpleTimeLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleTimeLimiter):
        """
        Dynamic initializer for SimpleTimeLimiter.
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
    def runWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(__TimeLimiter, self).runWithTimeout(runnable, timeout)

    @staticmethod
    @overload
    def create(executor: 'ExecutorService') -> 'SimpleTimeLimiter':
        """public static com.google.common.util.concurrent.SimpleTimeLimiter com.google.common.util.concurrent.SimpleTimeLimiter.create(java.util.concurrent.ExecutorService)"""
        return SimpleTimeLimiter.__wrap(__SimpleTimeLimiter.create(executor))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.SimpleTimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__SimpleTimeLimiter, self).runUninterruptiblyWithTimeout(runnable, __long.valueOf(timeoutDuration), timeoutUnit)

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__TimeLimiter, self).runUninterruptiblyWithTimeout(runnable, timeout)

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.SimpleTimeLimiter.newProxy(T,java.lang.Class<T>,long,java.util.concurrent.TimeUnit)"""
        return object.__wrap(super(__SimpleTimeLimiter, self).newProxy(target, interfaceType, __long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def callWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.SimpleTimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__SimpleTimeLimiter, self).callWithTimeout(callable, __long.valueOf(timeoutDuration), timeoutUnit))

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__TimeLimiter, self).callUninterruptiblyWithTimeout(callable, timeout))

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
    def runWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.SimpleTimeLimiter.runWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(__SimpleTimeLimiter, self).runWithTimeout(runnable, __long.valueOf(timeoutDuration), timeoutUnit)

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,java.time.Duration)"""
        return object.__wrap(super(__TimeLimiter, self).newProxy(target, interfaceType, timeout))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def callWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__TimeLimiter, self).callWithTimeout(callable, timeout))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.SimpleTimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__SimpleTimeLimiter, self).callUninterruptiblyWithTimeout(callable, __long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture
__ClosingFuture = __ClosingFuture
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner
__Combiner = __ClosingFuture_Combiner.Combiner
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner3
__Combiner3 = __ClosingFuture_Combiner3.Combiner3
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Combiner3():
    """com.google.common.util.concurrent.ClosingFuture.Combiner3"""
 
    @staticmethod
    def __wrap(java_value: __Combiner3) -> 'Combiner3':
        return Combiner3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Combiner3):
        """
        Dynamic initializer for Combiner3.
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
    def call(self, function: 'ClosingFunction3', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner3.call(com.google.common.util.concurrent.ClosingFuture$Combiner3$ClosingFunction3<V1, V2, V3, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner3, self).call(function, executor))

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
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).call(combiningCallable, executor))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def callAsync(self, function: 'AsyncClosingFunction3', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner3.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner3$AsyncClosingFunction3<V1, V2, V3, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner3, self).callAsync(function, executor))

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).callAsync(combiningCallable, executor))

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
 
 
# CLASS: com.google.common.util.concurrent.AbstractIdleService
import com.google.common.util.concurrent.AbstractIdleService as __AbstractIdleService
__AbstractIdleService = __AbstractIdleService
from builtins import str
from pyquantum_helper import override
import com.google.common.util.concurrent.Service as __Service
__Service = __Service
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.Service as __Service_State
__State = __Service_State.State
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractIdleService(ABC):
    """com.google.common.util.concurrent.AbstractIdleService"""
 
    @staticmethod
    def __wrap(java_value: __AbstractIdleService) -> 'AbstractIdleService':
        return AbstractIdleService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractIdleService):
        """
        Dynamic initializer for AbstractIdleService.
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
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitTerminated()"""
        super(AbstractIdleService, self).awaitTerminated()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractIdleService.stopAsync()"""
        return 'Service'.__wrap(super(AbstractIdleService, self).stopAsync())

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractIdleService.failureCause()"""
        return 'Throwable'.__wrap(super(AbstractIdleService, self).failureCause())

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractIdleService.isRunning()"""
        return bool.__wrap(super(AbstractIdleService, self).isRunning())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractIdleService, self).awaitRunning(__long.valueOf(timeout), unit)

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(__AbstractIdleService, self).addListener(listener, executor)

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractIdleService.startAsync()"""
        return 'Service'.__wrap(super(AbstractIdleService, self).startAsync())

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
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractIdleService.toString()"""
        return str.__wrap(super(AbstractIdleService, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractIdleService.state()"""
        return 'State'.__wrap(super(AbstractIdleService, self).state())

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(__AbstractIdleService, self).awaitTerminated(__long.valueOf(timeout), unit)

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractIdleService, self).awaitTerminated(timeout)

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__AbstractIdleService, self).awaitRunning(timeout)

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
    def awaitRunning(self):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitRunning()"""
        super(AbstractIdleService, self).awaitRunning()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_ExampleStackTrace
__ExampleStackTrace = __CycleDetectingLockFactory_ExampleStackTrace.ExampleStackTrace
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_PotentialDeadlockException
__PotentialDeadlockException = __CycleDetectingLockFactory_PotentialDeadlockException.PotentialDeadlockException
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
 
class PotentialDeadlockException():
    """com.google.common.util.concurrent.CycleDetectingLockFactory.PotentialDeadlockException"""
 
    @staticmethod
    def __wrap(java_value: __PotentialDeadlockException) -> 'PotentialDeadlockException':
        return PotentialDeadlockException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PotentialDeadlockException):
        """
        Dynamic initializer for PotentialDeadlockException.
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
    def getMessage(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException.getMessage()"""
        return str.__wrap(super(PotentialDeadlockException, self).getMessage())

    @overload
    def getConflictingStackTrace(self) -> 'ExampleStackTrace':
        """public com.google.common.util.concurrent.CycleDetectingLockFactory$ExampleStackTrace com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException.getConflictingStackTrace()"""
        return 'ExampleStackTrace'.__wrap(super(PotentialDeadlockException, self).getConflictingStackTrace())

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner4
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner4
__Combiner4 = __ClosingFuture_Combiner4.Combiner4
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture
__ClosingFuture = __ClosingFuture
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner
__Combiner = __ClosingFuture_Combiner.Combiner
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
 
class Combiner4():
    """com.google.common.util.concurrent.ClosingFuture.Combiner4"""
 
    @staticmethod
    def __wrap(java_value: __Combiner4) -> 'Combiner4':
        return Combiner4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Combiner4):
        """
        Dynamic initializer for Combiner4.
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

    @overload
    def call(self, function: 'ClosingFunction4', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner4.call(com.google.common.util.concurrent.ClosingFuture$Combiner4$ClosingFunction4<V1, V2, V3, V4, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner4, self).call(function, executor))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).call(combiningCallable, executor))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).callAsync(combiningCallable, executor))

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
    def callAsync(self, function: 'AsyncClosingFunction4', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner4.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner4$AsyncClosingFunction4<V1, V2, V3, V4, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner4, self).callAsync(function, executor))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner4$ClosingFunction4
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner4_ClosingFunction4
__ClosingFunction4 = __ClosingFuture_Combiner4_ClosingFunction4.Combiner4.ClosingFunction4
from abc import abstractmethod, ABC
 
class ClosingFunction4(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner4.ClosingFunction4"""
 
    @staticmethod
    def __wrap(java_value: __ClosingFunction4) -> 'ClosingFunction4':
        return ClosingFunction4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingFunction4):
        """
        Dynamic initializer for ClosingFunction4.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner4$ClosingFunction4.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Futures$FutureCombiner
from builtins import str
import com.google.common.util.concurrent.Futures as __Futures_FutureCombiner
__FutureCombiner = __Futures_FutureCombiner.FutureCombiner
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FutureCombiner():
    """com.google.common.util.concurrent.Futures.FutureCombiner"""
 
    @staticmethod
    def __wrap(java_value: __FutureCombiner) -> 'FutureCombiner':
        return FutureCombiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FutureCombiner):
        """
        Dynamic initializer for FutureCombiner.
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
    def callAsync(self, combiner: 'AsyncCallable', executor: 'Executor') -> 'ListenableFuture':
        """public <C> com.google.common.util.concurrent.ListenableFuture<C> com.google.common.util.concurrent.Futures$FutureCombiner.callAsync(com.google.common.util.concurrent.AsyncCallable<C>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'.__wrap(super(__FutureCombiner, self).callAsync(combiner, executor))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def run(self, combiner: 'Runnable', executor: 'Executor') -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.Futures$FutureCombiner.run(java.lang.Runnable,java.util.concurrent.Executor)"""
        return 'ListenableFuture'.__wrap(super(__FutureCombiner, self).run(combiner, executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def call(self, combiner: 'Callable', executor: 'Executor') -> 'ListenableFuture':
        """public <C> com.google.common.util.concurrent.ListenableFuture<C> com.google.common.util.concurrent.Futures$FutureCombiner.call(java.util.concurrent.Callable<C>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'.__wrap(super(__FutureCombiner, self).call(combiner, executor))

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
 
 
# CLASS: com.google.common.util.concurrent.FakeTimeLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import com.google.common.util.concurrent.TimeLimiter as __TimeLimiter
__TimeLimiter = __TimeLimiter
from builtins import object
import com.google.common.util.concurrent.FakeTimeLimiter as __FakeTimeLimiter
__FakeTimeLimiter = __FakeTimeLimiter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FakeTimeLimiter():
    """com.google.common.util.concurrent.FakeTimeLimiter"""
 
    @staticmethod
    def __wrap(java_value: __FakeTimeLimiter) -> 'FakeTimeLimiter':
        return FakeTimeLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FakeTimeLimiter):
        """
        Dynamic initializer for FakeTimeLimiter.
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
    def runWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(__TimeLimiter, self).runWithTimeout(runnable, timeout)

    @override
    @overload
    def runWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.FakeTimeLimiter.runWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        super(__FakeTimeLimiter, self).runWithTimeout(runnable, __long.valueOf(timeoutDuration), timeoutUnit)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def callWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.FakeTimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__FakeTimeLimiter, self).callWithTimeout(callable, __long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(__TimeLimiter, self).runUninterruptiblyWithTimeout(runnable, timeout)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.FakeTimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        super(__FakeTimeLimiter, self).runUninterruptiblyWithTimeout(runnable, __long.valueOf(timeoutDuration), timeoutUnit)

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__TimeLimiter, self).callUninterruptiblyWithTimeout(callable, timeout))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.FakeTimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__FakeTimeLimiter, self).callUninterruptiblyWithTimeout(callable, __long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,java.time.Duration)"""
        return object.__wrap(super(__TimeLimiter, self).newProxy(target, interfaceType, timeout))

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.FakeTimeLimiter.newProxy(T,java.lang.Class<T>,long,java.util.concurrent.TimeUnit)"""
        return object.__wrap(super(__FakeTimeLimiter, self).newProxy(target, interfaceType, __long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def callWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__TimeLimiter, self).callWithTimeout(callable, timeout))

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.FakeTimeLimiter()"""
        val = __FakeTimeLimiter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.FakeTimeLimiter()"""
        val = __FakeTimeLimiter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$Policy
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_Policy
__Policy = __CycleDetectingLockFactory_Policy.Policy
from abc import abstractmethod, ABC
 
class Policy(ABC):
    """com.google.common.util.concurrent.CycleDetectingLockFactory.Policy"""
 
    @staticmethod
    def __wrap(java_value: __Policy) -> 'Policy':
        return Policy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Policy):
        """
        Dynamic initializer for Policy.
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
    def handlePotentialDeadlock(self, exception: 'PotentialDeadlockException'):
        """public abstract void com.google.common.util.concurrent.CycleDetectingLockFactory$Policy.handlePotentialDeadlock(com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.JdkFutureAdapters
from builtins import str
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.JdkFutureAdapters as __JdkFutureAdapters
__JdkFutureAdapters = __JdkFutureAdapters
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
 
class JdkFutureAdapters():
    """com.google.common.util.concurrent.JdkFutureAdapters"""
 
    @staticmethod
    def __wrap(java_value: __JdkFutureAdapters) -> 'JdkFutureAdapters':
        return JdkFutureAdapters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JdkFutureAdapters):
        """
        Dynamic initializer for JdkFutureAdapters.
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def listenInPoolThread(future: 'Future') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.JdkFutureAdapters.listenInPoolThread(java.util.concurrent.Future<V>)"""
        return ListenableFuture.__wrap(__JdkFutureAdapters.listenInPoolThread(future))

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

    @staticmethod
    @overload
    def listenInPoolThread(future: 'Future', executor: 'Executor') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.JdkFutureAdapters.listenInPoolThread(java.util.concurrent.Future<V>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__JdkFutureAdapters.listenInPoolThread(future, executor)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner5$AsyncClosingFunction5
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner5_AsyncClosingFunction5
__AsyncClosingFunction5 = __ClosingFuture_Combiner5_AsyncClosingFunction5.Combiner5.AsyncClosingFunction5
from abc import abstractmethod, ABC
 
class AsyncClosingFunction5(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner5.AsyncClosingFunction5"""
 
    @staticmethod
    def __wrap(java_value: __AsyncClosingFunction5) -> 'AsyncClosingFunction5':
        return AsyncClosingFunction5(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncClosingFunction5):
        """
        Dynamic initializer for AsyncClosingFunction5.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object, value5: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner5$AsyncClosingFunction5.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4,V5) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.AsyncFunction
import com.google.common.util.concurrent.AsyncFunction as __AsyncFunction
__AsyncFunction = __AsyncFunction
from abc import abstractmethod, ABC
 
class AsyncFunction(ABC):
    """com.google.common.util.concurrent.AsyncFunction"""
 
    @staticmethod
    def __wrap(java_value: __AsyncFunction) -> 'AsyncFunction':
        return AsyncFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncFunction):
        """
        Dynamic initializer for AsyncFunction.
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
    def apply(self, input: object):
        """public abstract com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.AsyncFunction.apply(I) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Service$State
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.google.common.util.concurrent.Service as __Service_State
__State = __Service_State.State
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
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
 
class State():
    """com.google.common.util.concurrent.Service.State"""
 
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

    @staticmethod
    @overload
    def valueOf(name: str) -> 'State':
        """public static com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.Service$State.valueOf(java.lang.String)"""
        return State.__wrap(__State.valueOf(name))

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

    @staticmethod
    @overload
    def values() -> List['State']:
        """public static com.google.common.util.concurrent.Service$State[] com.google.common.util.concurrent.Service$State.values()"""
        return List[State].__wrap(__State.values())

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner_AsyncCombiningCallable
__AsyncCombiningCallable = __ClosingFuture_Combiner_AsyncCombiningCallable.Combiner.AsyncCombiningCallable
 
class AsyncCombiningCallable(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner.AsyncCombiningCallable"""
 
    @staticmethod
    def __wrap(java_value: __AsyncCombiningCallable) -> 'AsyncCombiningCallable':
        return AsyncCombiningCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncCombiningCallable):
        """
        Dynamic initializer for AsyncCombiningCallable.
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
    def call(self, closer: 'DeferredCloser', peeker: 'Peeker'):
        """public abstract com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,com.google.common.util.concurrent.ClosingFuture$Peeker) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner
__Combiner = __ClosingFuture_Combiner.Combiner
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture
__ClosingFuture = __ClosingFuture
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
 
class Combiner():
    """com.google.common.util.concurrent.ClosingFuture.Combiner"""
 
    @staticmethod
    def __wrap(java_value: __Combiner) -> 'Combiner':
        return Combiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Combiner):
        """
        Dynamic initializer for Combiner.
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
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).call(combiningCallable, executor))

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
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).callAsync(combiningCallable, executor))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ExecutionSequencer
from builtins import str
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.ExecutionSequencer as __ExecutionSequencer
__ExecutionSequencer = __ExecutionSequencer
import java.util.concurrent.Callable as Callable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExecutionSequencer():
    """com.google.common.util.concurrent.ExecutionSequencer"""
 
    @staticmethod
    def __wrap(java_value: __ExecutionSequencer) -> 'ExecutionSequencer':
        return ExecutionSequencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExecutionSequencer):
        """
        Dynamic initializer for ExecutionSequencer.
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

    @staticmethod
    @overload
    def create() -> 'ExecutionSequencer':
        """public static com.google.common.util.concurrent.ExecutionSequencer com.google.common.util.concurrent.ExecutionSequencer.create()"""
        return ExecutionSequencer.__wrap(__ExecutionSequencer.create())

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
    def submitAsync(self, callable: 'AsyncCallable', executor: 'Executor') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ExecutionSequencer.submitAsync(com.google.common.util.concurrent.AsyncCallable<T>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'.__wrap(super(__ExecutionSequencer, self).submitAsync(callable, executor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def submit(self, callable: 'Callable', executor: 'Executor') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ExecutionSequencer.submit(java.util.concurrent.Callable<T>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'.__wrap(super(__ExecutionSequencer, self).submit(callable, executor)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$AsyncClosingCallable
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_AsyncClosingCallable
__AsyncClosingCallable = __ClosingFuture_AsyncClosingCallable.AsyncClosingCallable
from abc import abstractmethod, ABC
 
class AsyncClosingCallable(ABC):
    """com.google.common.util.concurrent.ClosingFuture.AsyncClosingCallable"""
 
    @staticmethod
    def __wrap(java_value: __AsyncClosingCallable) -> 'AsyncClosingCallable':
        return AsyncClosingCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncClosingCallable):
        """
        Dynamic initializer for AsyncClosingCallable.
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
    def call(self, closer: 'DeferredCloser'):
        """public abstract com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$AsyncClosingCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ServiceManager$Listener
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.ServiceManager as __ServiceManager_Listener
__Listener = __ServiceManager_Listener.Listener
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Listener(ABC):
    """com.google.common.util.concurrent.ServiceManager.Listener"""
 
    @staticmethod
    def __wrap(java_value: __Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Listener):
        """
        Dynamic initializer for Listener.
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
    def __init__(self):
        """public com.google.common.util.concurrent.ServiceManager$Listener()"""
        val = __Listener()
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def healthy(self):
        """public void com.google.common.util.concurrent.ServiceManager$Listener.healthy()"""
        super(Listener, self).healthy()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.ServiceManager$Listener()"""
        val = __Listener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def failure(self, service: 'Service'):
        """public void com.google.common.util.concurrent.ServiceManager$Listener.failure(com.google.common.util.concurrent.Service)"""
        super(__Listener, self).failure(service)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def stopped(self):
        """public void com.google.common.util.concurrent.ServiceManager$Listener.stopped()"""
        super(Listener, self).stopped()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingFuture$SimpleForwardingFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.lang.Long as __long
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import com.google.common.util.concurrent.ForwardingFuture as __ForwardingFuture_SimpleForwardingFuture
__SimpleForwardingFuture = __ForwardingFuture_SimpleForwardingFuture.SimpleForwardingFuture
from builtins import bool
import com.google.common.util.concurrent.ForwardingFuture as __ForwardingFuture
__ForwardingFuture = __ForwardingFuture
from builtins import int
 
class SimpleForwardingFuture(ABC):
    """com.google.common.util.concurrent.ForwardingFuture.SimpleForwardingFuture"""
 
    @staticmethod
    def __wrap(java_value: __SimpleForwardingFuture) -> 'SimpleForwardingFuture':
        return SimpleForwardingFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleForwardingFuture):
        """
        Dynamic initializer for SimpleForwardingFuture.
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
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ForwardingFuture, self).get(__long.valueOf(timeout), unit))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool.__wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(ForwardingFuture, self).get())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool.__wrap(super(__ForwardingFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

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
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

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
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool.__wrap(super(ForwardingFuture, self).isDone())

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
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object.__wrap(super(Future, self).resultNow())

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'.__wrap(super(Future, self).state()) 
 
 
# CLASS: com.google.common.util.concurrent.ListeningScheduledExecutorService
from pyquantum_helper import override
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
import java.util.List as __List
__List = __List
import com.google.common.util.concurrent.ListenableScheduledFuture as __ListenableScheduledFuture
__ListenableScheduledFuture = __ListenableScheduledFuture
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.ListeningExecutorService as __ListeningExecutorService
__ListeningExecutorService = __ListeningExecutorService
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.ListeningScheduledExecutorService as __ListeningScheduledExecutorService
__ListeningScheduledExecutorService = __ListeningScheduledExecutorService
import java.util.concurrent.Executor as __Executor
__Executor = __Executor
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.util.List as List
 
class ListeningScheduledExecutorService(ABC):
    """com.google.common.util.concurrent.ListeningScheduledExecutorService"""
 
    @staticmethod
    def __wrap(java_value: __ListeningScheduledExecutorService) -> 'ListeningScheduledExecutorService':
        return ListeningScheduledExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListeningScheduledExecutorService):
        """
        Dynamic initializer for ListeningScheduledExecutorService.
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
    def schedule(self, command: 'Runnable', delay: 'Duration') -> 'ListenableScheduledFuture':
        """public default com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.lang.Runnable,java.time.Duration)"""
        return 'ListenableScheduledFuture'.__wrap(super(__ListeningScheduledExecutorService, self).schedule(command, delay))

    @abstractmethod
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract boolean java.util.concurrent.ExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @abstractmethod
    def submit(self, task: 'Runnable', result: object):
        """public abstract <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable,T)"""
        pass

    @abstractmethod
    def invokeAny(self, arg0: 'Collection'):
        """public abstract <T> T java.util.concurrent.ExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def submit(self, task: 'Callable'):
        """public abstract <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ListeningExecutorService.submit(java.util.concurrent.Callable<T>)"""
        pass

    @abstractmethod
    def invokeAll(self, tasks: 'Collection'):
        """public abstract <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        pass

    @overload
    def scheduleWithFixedDelay(self, command: 'Runnable', initialDelay: 'Duration', delay: 'Duration') -> 'ListenableScheduledFuture':
        """public default com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.scheduleWithFixedDelay(java.lang.Runnable,java.time.Duration,java.time.Duration)"""
        return 'ListenableScheduledFuture'.__wrap(super(__ListeningScheduledExecutorService, self).scheduleWithFixedDelay(command, initialDelay, delay))

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @abstractmethod
    def schedule(self, callable: 'Callable', delay: int, unit: 'TimeUnit'):
        """public abstract <V> com.google.common.util.concurrent.ListenableScheduledFuture<V> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.util.concurrent.Callable<V>,long,java.util.concurrent.TimeUnit)"""
        pass

    @abstractmethod
    def execute(self, arg0: 'Runnable'):
        """public abstract void java.util.concurrent.Executor.execute(java.lang.Runnable)"""
        pass

    @abstractmethod
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit'):
        """public abstract <T> T java.util.concurrent.ExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def schedule(self, command: 'Runnable', delay: int, unit: 'TimeUnit'):
        """public abstract com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        pass

    @abstractmethod
    def scheduleWithFixedDelay(self, command: 'Runnable', initialDelay: int, delay: int, unit: 'TimeUnit'):
        """public abstract com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.scheduleWithFixedDelay(java.lang.Runnable,long,long,java.util.concurrent.TimeUnit)"""
        pass

    @abstractmethod
    def scheduleAtFixedRate(self, command: 'Runnable', initialDelay: int, period: int, unit: 'TimeUnit'):
        """public abstract com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.scheduleAtFixedRate(java.lang.Runnable,long,long,java.util.concurrent.TimeUnit)"""
        pass

    @overload
    def schedule(self, callable: 'Callable', delay: 'Duration') -> 'ListenableScheduledFuture':
        """public default <V> com.google.common.util.concurrent.ListenableScheduledFuture<V> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.util.concurrent.Callable<V>,java.time.Duration)"""
        return 'ListenableScheduledFuture'.__wrap(super(__ListeningScheduledExecutorService, self).schedule(callable, delay))

    @abstractmethod
    def isShutdown(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isShutdown()"""
        pass

    @overload
    def scheduleAtFixedRate(self, command: 'Runnable', initialDelay: 'Duration', period: 'Duration') -> 'ListenableScheduledFuture':
        """public default com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.scheduleAtFixedRate(java.lang.Runnable,java.time.Duration,java.time.Duration)"""
        return 'ListenableScheduledFuture'.__wrap(super(__ListeningScheduledExecutorService, self).scheduleAtFixedRate(command, initialDelay, period))

    @abstractmethod
    def submit(self, task: 'Runnable'):
        """public abstract com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable)"""
        pass

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ListeningExecutorService, self).invokeAll(tasks, timeout))

    @abstractmethod
    def shutdownNow(self, ):
        """public abstract java.util.List<java.lang.Runnable> java.util.concurrent.ExecutorService.shutdownNow()"""
        pass

    @abstractmethod
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit'):
        """public abstract <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @overload
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ListeningExecutorService, self).awaitTermination(timeout))

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ListeningExecutorService, self).invokeAny(tasks, timeout))

    @abstractmethod
    def shutdown(self, ):
        """public abstract void java.util.concurrent.ExecutorService.shutdown()"""
        pass

    @abstractmethod
    def isTerminated(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isTerminated()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Service$Listener
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
import com.google.common.util.concurrent.Service as __Service_Listener
__Listener = __Service_Listener.Listener
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Listener(ABC):
    """com.google.common.util.concurrent.Service.Listener"""
 
    @staticmethod
    def __wrap(java_value: __Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Listener):
        """
        Dynamic initializer for Listener.
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

    @overload
    def starting(self):
        """public void com.google.common.util.concurrent.Service$Listener.starting()"""
        super(Listener, self).starting()

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
    def failed(self, from: 'State', failure: 'Throwable'):
        """public void com.google.common.util.concurrent.Service$Listener.failed(com.google.common.util.concurrent.Service$State,java.lang.Throwable)"""
        super(__Listener, self).failed(from, failure)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.Service$Listener()"""
        val = __Listener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.Service$Listener()"""
        val = __Listener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def stopping(self, from: 'State'):
        """public void com.google.common.util.concurrent.Service$Listener.stopping(com.google.common.util.concurrent.Service$State)"""
        super(__Listener, self).stopping(from)

    @overload
    def running(self):
        """public void com.google.common.util.concurrent.Service$Listener.running()"""
        super(Listener, self).running()

    @overload
    def terminated(self, from: 'State'):
        """public void com.google.common.util.concurrent.Service$Listener.terminated(com.google.common.util.concurrent.Service$State)"""
        super(__Listener, self).terminated(from)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory
import java.util.concurrent.locks.ReentrantLock as ReentrantLock
from builtins import str
import java.lang.Boolean as __boolean
import java.util.concurrent.locks.ReentrantReadWriteLock as ReentrantReadWriteLock
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.locks.ReentrantLock as __ReentrantLock
__ReentrantLock = __ReentrantLock
import java.util.concurrent.locks.ReentrantReadWriteLock as __ReentrantReadWriteLock
__ReentrantReadWriteLock = __ReentrantReadWriteLock
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory_WithExplicitOrdering
__WithExplicitOrdering = __CycleDetectingLockFactory_WithExplicitOrdering.WithExplicitOrdering
import com.google.common.util.concurrent.CycleDetectingLockFactory as __CycleDetectingLockFactory
__CycleDetectingLockFactory = __CycleDetectingLockFactory
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
 
class CycleDetectingLockFactory():
    """com.google.common.util.concurrent.CycleDetectingLockFactory"""
 
    @staticmethod
    def __wrap(java_value: __CycleDetectingLockFactory) -> 'CycleDetectingLockFactory':
        return CycleDetectingLockFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CycleDetectingLockFactory):
        """
        Dynamic initializer for CycleDetectingLockFactory.
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
    def newInstanceWithExplicitOrdering(enumClass: 'Class', policy: 'Policy') -> 'WithExplicitOrdering':
        """public static <E extends java.lang.Enum<E>> com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering<E> com.google.common.util.concurrent.CycleDetectingLockFactory.newInstanceWithExplicitOrdering(java.lang.Class<E>,com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return WithExplicitOrdering.__wrap(__CycleDetectingLockFactory.newInstanceWithExplicitOrdering(enumClass, policy))

    @overload
    def newReentrantLock(self, lockName: str, fair: bool) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String,boolean)"""
        return 'ReentrantLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantLock(lockName, __boolean.valueOf(fair)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newReentrantReadWriteLock(self, lockName: str) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String)"""
        return 'ReentrantReadWriteLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newReentrantLock(self, lockName: str) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String)"""
        return 'ReentrantLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantLock(lockName))

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
    def newInstance(policy: 'Policy') -> 'CycleDetectingLockFactory':
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory com.google.common.util.concurrent.CycleDetectingLockFactory.newInstance(com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return CycleDetectingLockFactory.__wrap(__CycleDetectingLockFactory.newInstance(policy))

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
    def newReentrantReadWriteLock(self, lockName: str, fair: bool) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String,boolean)"""
        return 'ReentrantReadWriteLock'.__wrap(super(__CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName, __boolean.valueOf(fair)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.AtomicDouble
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.DoubleBinaryOperator as DoubleBinaryOperator
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.AtomicDouble as __AtomicDouble
__AtomicDouble = __AtomicDouble
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
import java.util.function.DoubleUnaryOperator as DoubleUnaryOperator
 
class AtomicDouble():
    """com.google.common.util.concurrent.AtomicDouble"""
 
    @staticmethod
    def __wrap(java_value: __AtomicDouble) -> 'AtomicDouble':
        return AtomicDouble(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtomicDouble):
        """
        Dynamic initializer for AtomicDouble.
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
    def floatValue(self) -> float:
        """public float com.google.common.util.concurrent.AtomicDouble.floatValue()"""
        return float.__wrap(super(AtomicDouble, self).floatValue())

    @overload
    def set(self, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDouble.set(double)"""
        super(__AtomicDouble, self).set(__double.valueOf(newValue))

    @overload
    def addAndGet(self, delta: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.addAndGet(double)"""
        return float.__wrap(super(__AtomicDouble, self).addAndGet(__double.valueOf(delta)))

    @overload
    def getAndSet(self, newValue: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndSet(double)"""
        return float.__wrap(super(__AtomicDouble, self).getAndSet(__double.valueOf(newValue)))

    @overload
    def get(self) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.get()"""
        return float.__wrap(super(AtomicDouble, self).get())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.common.util.concurrent.AtomicDouble.doubleValue()"""
        return float.__wrap(super(AtomicDouble, self).doubleValue())

    @overload
    def compareAndSet(self, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDouble.compareAndSet(double,double)"""
        return bool.__wrap(super(__AtomicDouble, self).compareAndSet(__double.valueOf(expect), __double.valueOf(update)))

    @overload
    def accumulateAndGet(self, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.accumulateAndGet(double,java.util.function.DoubleBinaryOperator)"""
        return float.__wrap(super(__AtomicDouble, self).accumulateAndGet(__double.valueOf(x), accumulatorFunction))

    @overload
    def updateAndGet(self, updateFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.updateAndGet(java.util.function.DoubleUnaryOperator)"""
        return float.__wrap(super(__AtomicDouble, self).updateAndGet(updateFunction))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAndAccumulate(self, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndAccumulate(double,java.util.function.DoubleBinaryOperator)"""
        return float.__wrap(super(__AtomicDouble, self).getAndAccumulate(__double.valueOf(x), accumulatorFunction))

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.AtomicDouble()"""
        val = __AtomicDouble()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def intValue(self) -> int:
        """public int com.google.common.util.concurrent.AtomicDouble.intValue()"""
        return int.__wrap(super(AtomicDouble, self).intValue())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AtomicDouble.toString()"""
        return str.__wrap(super(AtomicDouble, self).toString())

    @overload
    def lazySet(self, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDouble.lazySet(double)"""
        super(__AtomicDouble, self).lazySet(__double.valueOf(newValue))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, initialValue: float):
        """public com.google.common.util.concurrent.AtomicDouble(double)"""
        val = __AtomicDouble(__double.valueOf(initialValue))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def weakCompareAndSet(self, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDouble.weakCompareAndSet(double,double)"""
        return bool.__wrap(super(__AtomicDouble, self).weakCompareAndSet(__double.valueOf(expect), __double.valueOf(update)))

    @overload
    def getAndAdd(self, delta: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndAdd(double)"""
        return float.__wrap(super(__AtomicDouble, self).getAndAdd(__double.valueOf(delta)))

    @override
    @overload
    def longValue(self) -> int:
        """public long com.google.common.util.concurrent.AtomicDouble.longValue()"""
        return int.__wrap(super(AtomicDouble, self).longValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.AtomicDouble()"""
        val = __AtomicDouble()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAndUpdate(self, updateFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndUpdate(java.util.function.DoubleUnaryOperator)"""
        return float.__wrap(super(__AtomicDouble, self).getAndUpdate(updateFunction)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner_CombiningCallable
__CombiningCallable = __ClosingFuture_Combiner_CombiningCallable.Combiner.CombiningCallable
from abc import abstractmethod, ABC
 
class CombiningCallable(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner.CombiningCallable"""
 
    @staticmethod
    def __wrap(java_value: __CombiningCallable) -> 'CombiningCallable':
        return CombiningCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CombiningCallable):
        """
        Dynamic initializer for CombiningCallable.
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
    def call(self, closer: 'DeferredCloser', peeker: 'Peeker'):
        """public abstract V com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,com.google.common.util.concurrent.ClosingFuture$Peeker) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.AsyncCallable
import com.google.common.util.concurrent.AsyncCallable as __AsyncCallable
__AsyncCallable = __AsyncCallable
from abc import abstractmethod, ABC
 
class AsyncCallable(ABC):
    """com.google.common.util.concurrent.AsyncCallable"""
 
    @staticmethod
    def __wrap(java_value: __AsyncCallable) -> 'AsyncCallable':
        return AsyncCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncCallable):
        """
        Dynamic initializer for AsyncCallable.
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
    def call(self, ):
        """public abstract com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.AsyncCallable.call() throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingListeningExecutorService
import com.google.common.util.concurrent.ForwardingListeningExecutorService as __ForwardingListeningExecutorService
__ForwardingListeningExecutorService = __ForwardingListeningExecutorService
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from builtins import type
import java.util.Collection as Collection
import java.util.concurrent.ExecutorService as __ExecutorService
__ExecutorService = __ExecutorService
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.util.concurrent.ForwardingExecutorService as __ForwardingExecutorService
__ForwardingExecutorService = __ForwardingExecutorService
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
from builtins import object
import java.lang.Long as __long
import java.util.List as __List
__List = __List
import com.google.common.collect.ForwardingObject as __ForwardingObject
__ForwardingObject = __ForwardingObject
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ListeningExecutorService as __ListeningExecutorService
__ListeningExecutorService = __ListeningExecutorService
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class ForwardingListeningExecutorService(ABC):
    """com.google.common.util.concurrent.ForwardingListeningExecutorService"""
 
    @staticmethod
    def __wrap(java_value: __ForwardingListeningExecutorService) -> 'ForwardingListeningExecutorService':
        return ForwardingListeningExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ForwardingListeningExecutorService):
        """
        Dynamic initializer for ForwardingListeningExecutorService.
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
    def submit(self, task: 'Runnable') -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ForwardingListeningExecutorService.submit(java.lang.Runnable)"""
        return 'ListenableFuture'.__wrap(super(__ForwardingListeningExecutorService, self).submit(task))

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isShutdown()"""
        return bool.__wrap(super(ForwardingExecutorService, self).isShutdown())

    @overload
    def submit(self, task: 'Callable') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ForwardingListeningExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'ListenableFuture'.__wrap(super(__ForwardingListeningExecutorService, self).submit(task))

    @override
    @overload
    def execute(self, command: 'Runnable'):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.execute(java.lang.Runnable)"""
        super(__ForwardingExecutorService, self).execute(command)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def submit(self, task: 'Runnable', result: object) -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ForwardingListeningExecutorService.submit(java.lang.Runnable,T)"""
        return 'ListenableFuture'.__wrap(super(__ForwardingListeningExecutorService, self).submit(task, result))

    @overload
    def awaitTermination(self, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ForwardingExecutorService, self).awaitTermination(__long.valueOf(timeout), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str.__wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ListeningExecutorService, self).invokeAll(tasks, timeout))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> com.google.common.util.concurrent.ForwardingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(ForwardingExecutorService, self).shutdownNow())

    @override
    @overload
    def shutdown(self):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.shutdown()"""
        super(ForwardingExecutorService, self).shutdown()

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ForwardingExecutorService, self).invokeAny(tasks, __long.valueOf(timeout), unit))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isTerminated()"""
        return bool.__wrap(super(ForwardingExecutorService, self).isTerminated())

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
    def invokeAll(self, tasks: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ForwardingExecutorService, self).invokeAll(tasks))

    @overload
    def invokeAny(self, tasks: 'Collection') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__ForwardingExecutorService, self).invokeAny(tasks))

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return 'List'.__wrap(super(__ForwardingExecutorService, self).invokeAll(tasks, __long.valueOf(timeout), unit))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__ListeningExecutorService, self).awaitTermination(timeout))

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__ListeningExecutorService, self).invokeAny(tasks, timeout)) 
 
 
# CLASS: com.google.common.util.concurrent.UncheckedTimeoutException
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
import com.google.common.util.concurrent.UncheckedTimeoutException as __UncheckedTimeoutException
__UncheckedTimeoutException = __UncheckedTimeoutException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UncheckedTimeoutException():
    """com.google.common.util.concurrent.UncheckedTimeoutException"""
 
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
    def __init__(self, message: str, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedTimeoutException(java.lang.String,java.lang.Throwable)"""
        val = __UncheckedTimeoutException(message, cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, message: str):
        """public com.google.common.util.concurrent.UncheckedTimeoutException(java.lang.String)"""
        val = __UncheckedTimeoutException(message)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedTimeoutException(java.lang.Throwable)"""
        val = __UncheckedTimeoutException(cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.UncheckedTimeoutException()"""
        val = __UncheckedTimeoutException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.UncheckedTimeoutException()"""
        val = __UncheckedTimeoutException()
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

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.AbstractScheduledService as __AbstractScheduledService_Scheduler
__Scheduler = __AbstractScheduledService_Scheduler.Scheduler
import java.time.Duration as Duration
import java.lang.Long as __long
import com.google.common.util.concurrent.AbstractScheduledService as __AbstractScheduledService_CustomScheduler
__CustomScheduler = __AbstractScheduledService_CustomScheduler.CustomScheduler
import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CustomScheduler(ABC):
    """com.google.common.util.concurrent.AbstractScheduledService.CustomScheduler"""
 
    @staticmethod
    def __wrap(java_value: __CustomScheduler) -> 'CustomScheduler':
        return CustomScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CustomScheduler):
        """
        Dynamic initializer for CustomScheduler.
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
    def __init__(self):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler()"""
        val = __CustomScheduler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: 'Duration', delay: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler.__wrap(__Scheduler.newFixedDelaySchedule(initialDelay, delay))

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

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: int, period: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler.__wrap(__Scheduler.newFixedRateSchedule(__long.valueOf(initialDelay), __long.valueOf(period), unit))

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: 'Duration', period: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler.__wrap(__Scheduler.newFixedRateSchedule(initialDelay, period))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: int, delay: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler.__wrap(__Scheduler.newFixedDelaySchedule(__long.valueOf(initialDelay), __long.valueOf(delay), unit))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler()"""
        val = __CustomScheduler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ClosingFunction
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_ClosingFunction
__ClosingFunction = __ClosingFuture_ClosingFunction.ClosingFunction
 
class ClosingFunction(ABC):
    """com.google.common.util.concurrent.ClosingFuture.ClosingFunction"""
 
    @staticmethod
    def __wrap(java_value: __ClosingFunction) -> 'ClosingFunction':
        return ClosingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingFunction):
        """
        Dynamic initializer for ClosingFunction.
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
    def apply(self, closer: 'DeferredCloser', input: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$ClosingFunction.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,T) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ListenableFuture
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.util.concurrent.Future.State as State
import java.util.concurrent.Future as __Future
__Future = __Future
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
from builtins import object
import java.util.concurrent.Future as __Future_State
__State = __Future_State.State
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
 
class ListenableFuture(ABC):
    """com.google.common.util.concurrent.ListenableFuture"""
 
    @staticmethod
    def __wrap(java_value: __ListenableFuture) -> 'ListenableFuture':
        return ListenableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListenableFuture):
        """
        Dynamic initializer for ListenableFuture.
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
    def get(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract V java.util.concurrent.Future.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public abstract void com.google.common.util.concurrent.ListenableFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
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

    @abstractmethod
    def isCancelled(self, ):
        """public abstract boolean java.util.concurrent.Future.isCancelled()"""
        pass

    @abstractmethod
    def get(self, ):
        """public abstract V java.util.concurrent.Future.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        pass

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner5
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture
__ClosingFuture = __ClosingFuture
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner
__Combiner = __ClosingFuture_Combiner.Combiner
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner5
__Combiner5 = __ClosingFuture_Combiner5.Combiner5
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Combiner5():
    """com.google.common.util.concurrent.ClosingFuture.Combiner5"""
 
    @staticmethod
    def __wrap(java_value: __Combiner5) -> 'Combiner5':
        return Combiner5(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Combiner5):
        """
        Dynamic initializer for Combiner5.
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).call(combiningCallable, executor))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner, self).callAsync(combiningCallable, executor))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def call(self, function: 'ClosingFunction5', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner5.call(com.google.common.util.concurrent.ClosingFuture$Combiner5$ClosingFunction5<V1, V2, V3, V4, V5, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner5, self).call(function, executor))

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
    def callAsync(self, function: 'AsyncClosingFunction5', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner5.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner5$AsyncClosingFunction5<V1, V2, V3, V4, V5, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__Combiner5, self).callAsync(function, executor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ValueAndCloserConsumer
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_ValueAndCloserConsumer
__ValueAndCloserConsumer = __ClosingFuture_ValueAndCloserConsumer.ValueAndCloserConsumer
from abc import abstractmethod, ABC
 
class ValueAndCloserConsumer(ABC):
    """com.google.common.util.concurrent.ClosingFuture.ValueAndCloserConsumer"""
 
    @staticmethod
    def __wrap(java_value: __ValueAndCloserConsumer) -> 'ValueAndCloserConsumer':
        return ValueAndCloserConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueAndCloserConsumer):
        """
        Dynamic initializer for ValueAndCloserConsumer.
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
    def accept(self, valueAndCloser: 'ValueAndCloser'):
        """public abstract void com.google.common.util.concurrent.ClosingFuture$ValueAndCloserConsumer.accept(com.google.common.util.concurrent.ClosingFuture$ValueAndCloser<V>)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Futures
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
import com.google.common.util.concurrent.Futures as __Futures_FutureCombiner
__FutureCombiner = __Futures_FutureCombiner.FutureCombiner
from builtins import type
import java.util.concurrent.Future as __Future
__Future = __Future
import com.google.common.collect.ImmutableList as __ImmutableList
__ImmutableList = __ImmutableList
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Runnable as Runnable
import java.lang.Iterable as Iterable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.Long as __long
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.String as __String
__String = __String
import java.util.concurrent.Future as Future
import com.google.common.util.concurrent.Futures as __Futures
__Futures = __Futures
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import int
 
class Futures():
    """com.google.common.util.concurrent.Futures"""
 
    @staticmethod
    def __wrap(java_value: __Futures) -> 'Futures':
        return Futures(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Futures):
        """
        Dynamic initializer for Futures.
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
    def withTimeout(delegate: 'ListenableFuture', time: 'Duration', scheduledExecutor: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.withTimeout(com.google.common.util.concurrent.ListenableFuture<V>,java.time.Duration,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture.__wrap(__Futures.withTimeout(delegate, time, scheduledExecutor))

    @staticmethod
    @overload
    def lazyTransform(input: 'Future', function: 'Function') -> 'Future':
        """public static <I,O> java.util.concurrent.Future<O> com.google.common.util.concurrent.Futures.lazyTransform(java.util.concurrent.Future<I>,com.google.common.base.Function<? super I, ? extends O>)"""
        return Future.__wrap(__Futures.lazyTransform(input, function))

    @staticmethod
    @overload
    def getChecked(future: 'Future', exceptionClass: 'Class', timeout: int, unit: 'TimeUnit') -> object:
        """public static <V,X extends java.lang.Exception> V com.google.common.util.concurrent.Futures.getChecked(java.util.concurrent.Future<V>,java.lang.Class<X>,long,java.util.concurrent.TimeUnit) throws X"""
        return object.__wrap(__Futures.getChecked(future, exceptionClass, __long.valueOf(timeout), unit))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def immediateFuture(value: object) -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.immediateFuture(V)"""
        return ListenableFuture.__wrap(__Futures.immediateFuture(value))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def whenAllSucceed(*futures: 'ListenableFuture') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllSucceed(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return FutureCombiner.__wrap(__Futures.whenAllSucceed(futures))

    @staticmethod
    @overload
    def getChecked(future: 'Future', exceptionClass: 'Class') -> object:
        """public static <V,X extends java.lang.Exception> V com.google.common.util.concurrent.Futures.getChecked(java.util.concurrent.Future<V>,java.lang.Class<X>) throws X"""
        return object.__wrap(__Futures.getChecked(future, exceptionClass))

    @staticmethod
    @overload
    def allAsList(futures: 'Iterable') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.allAsList(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return ListenableFuture.__wrap(__Futures.allAsList(futures))

    @staticmethod
    @overload
    def scheduleAsync(callable: 'AsyncCallable', delay: 'Duration', executorService: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.scheduleAsync(com.google.common.util.concurrent.AsyncCallable<O>,java.time.Duration,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture.__wrap(__Futures.scheduleAsync(callable, delay, executorService))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def addCallback(future: 'ListenableFuture', callback: 'FutureCallback', executor: 'Executor'):
        """public static <V> void com.google.common.util.concurrent.Futures.addCallback(com.google.common.util.concurrent.ListenableFuture<V>,com.google.common.util.concurrent.FutureCallback<? super V>,java.util.concurrent.Executor)"""
        __Futures.addCallback(future, callback, executor)

    @staticmethod
    @overload
    def successfulAsList(*futures: 'ListenableFuture') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.successfulAsList(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return ListenableFuture.__wrap(__Futures.successfulAsList(futures))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def catching(input: 'ListenableFuture', exceptionType: 'Class', fallback: 'Function', executor: 'Executor') -> 'ListenableFuture':
        """public static <V,X extends java.lang.Throwable> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.catching(com.google.common.util.concurrent.ListenableFuture<? extends V>,java.lang.Class<X>,com.google.common.base.Function<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.catching(input, exceptionType, fallback, executor))

    @staticmethod
    @overload
    def scheduleAsync(callable: 'AsyncCallable', delay: int, timeUnit: 'TimeUnit', executorService: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.scheduleAsync(com.google.common.util.concurrent.AsyncCallable<O>,long,java.util.concurrent.TimeUnit,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture.__wrap(__Futures.scheduleAsync(callable, __long.valueOf(delay), timeUnit, executorService))

    @staticmethod
    @overload
    def allAsList(*futures: 'ListenableFuture') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.allAsList(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return ListenableFuture.__wrap(__Futures.allAsList(futures))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def catchingAsync(input: 'ListenableFuture', exceptionType: 'Class', fallback: 'AsyncFunction', executor: 'Executor') -> 'ListenableFuture':
        """public static <V,X extends java.lang.Throwable> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.catchingAsync(com.google.common.util.concurrent.ListenableFuture<? extends V>,java.lang.Class<X>,com.google.common.util.concurrent.AsyncFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.catchingAsync(input, exceptionType, fallback, executor))

    @staticmethod
    @overload
    def whenAllComplete(futures: 'Iterable') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllComplete(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return FutureCombiner.__wrap(__Futures.whenAllComplete(futures))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nonCancellationPropagating(future: 'ListenableFuture') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.nonCancellationPropagating(com.google.common.util.concurrent.ListenableFuture<V>)"""
        return ListenableFuture.__wrap(__Futures.nonCancellationPropagating(future))

    @staticmethod
    @overload
    def inCompletionOrder(futures: 'Iterable') -> 'pygcollect.ImmutableList':
        """public static <T> com.google.common.collect.ImmutableList<com.google.common.util.concurrent.ListenableFuture<T>> com.google.common.util.concurrent.Futures.inCompletionOrder(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends T>>)"""
        return pygcollect.ImmutableList.__wrap(__Futures.inCompletionOrder(futures))

    @staticmethod
    @overload
    def getUnchecked(future: 'Future') -> object:
        """public static <V> V com.google.common.util.concurrent.Futures.getUnchecked(java.util.concurrent.Future<V>)"""
        return object.__wrap(__Futures.getUnchecked(future))

    @staticmethod
    @overload
    def withTimeout(delegate: 'ListenableFuture', time: int, unit: 'TimeUnit', scheduledExecutor: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.withTimeout(com.google.common.util.concurrent.ListenableFuture<V>,long,java.util.concurrent.TimeUnit,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture.__wrap(__Futures.withTimeout(delegate, __long.valueOf(time), unit, scheduledExecutor))

    @staticmethod
    @overload
    def submitAsync(callable: 'AsyncCallable', executor: 'Executor') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.submitAsync(com.google.common.util.concurrent.AsyncCallable<O>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.submitAsync(callable, executor))

    @staticmethod
    @overload
    def successfulAsList(futures: 'Iterable') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.successfulAsList(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return ListenableFuture.__wrap(__Futures.successfulAsList(futures))

    @staticmethod
    @overload
    def immediateFailedFuture(throwable: 'Throwable') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.immediateFailedFuture(java.lang.Throwable)"""
        return ListenableFuture.__wrap(__Futures.immediateFailedFuture(throwable))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def submit(runnable: 'Runnable', executor: 'Executor') -> 'ListenableFuture':
        """public static com.google.common.util.concurrent.ListenableFuture<java.lang.Void> com.google.common.util.concurrent.Futures.submit(java.lang.Runnable,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.submit(runnable, executor))

    @staticmethod
    @overload
    def immediateVoidFuture() -> 'ListenableFuture':
        """public static com.google.common.util.concurrent.ListenableFuture<java.lang.Void> com.google.common.util.concurrent.Futures.immediateVoidFuture()"""
        return ListenableFuture.__wrap(__Futures.immediateVoidFuture())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def immediateCancelledFuture() -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.immediateCancelledFuture()"""
        return ListenableFuture.__wrap(__Futures.immediateCancelledFuture())

    @staticmethod
    @overload
    def whenAllComplete(*futures: 'ListenableFuture') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllComplete(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return FutureCombiner.__wrap(__Futures.whenAllComplete(futures))

    @staticmethod
    @overload
    def transformAsync(input: 'ListenableFuture', function: 'AsyncFunction', executor: 'Executor') -> 'ListenableFuture':
        """public static <I,O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.transformAsync(com.google.common.util.concurrent.ListenableFuture<I>,com.google.common.util.concurrent.AsyncFunction<? super I, ? extends O>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.transformAsync(input, function, executor))

    @staticmethod
    @overload
    def whenAllSucceed(futures: 'Iterable') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllSucceed(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return FutureCombiner.__wrap(__Futures.whenAllSucceed(futures))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transform(input: 'ListenableFuture', function: 'Function', executor: 'Executor') -> 'ListenableFuture':
        """public static <I,O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.transform(com.google.common.util.concurrent.ListenableFuture<I>,com.google.common.base.Function<? super I, ? extends O>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.transform(input, function, executor))

    @staticmethod
    @overload
    def submit(callable: 'Callable', executor: 'Executor') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.submit(java.util.concurrent.Callable<O>,java.util.concurrent.Executor)"""
        return ListenableFuture.__wrap(__Futures.submit(callable, executor))

    @staticmethod
    @overload
    def getChecked(future: 'Future', exceptionClass: 'Class', timeout: 'Duration') -> object:
        """public static <V,X extends java.lang.Exception> V com.google.common.util.concurrent.Futures.getChecked(java.util.concurrent.Future<V>,java.lang.Class<X>,java.time.Duration) throws X"""
        return object.__wrap(__Futures.getChecked(future, exceptionClass, timeout))

    @staticmethod
    @overload
    def getDone(future: 'Future') -> object:
        """public static <V> V com.google.common.util.concurrent.Futures.getDone(java.util.concurrent.Future<V>) throws java.util.concurrent.ExecutionException"""
        return object.__wrap(__Futures.getDone(future)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture
from builtins import str
import com.google.common.util.concurrent.ListenableFuture as __ListenableFuture
__ListenableFuture = __ListenableFuture
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_AsyncClosingFunction
__AsyncClosingFunction = __ClosingFuture_AsyncClosingFunction.AsyncClosingFunction
import java.lang.Iterable as Iterable
import com.google.common.util.concurrent.FluentFuture as __FluentFuture
__FluentFuture = __FluentFuture
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner4
__Combiner4 = __ClosingFuture_Combiner4.Combiner4
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture
__ClosingFuture = __ClosingFuture
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner
__Combiner = __ClosingFuture_Combiner.Combiner
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner5
__Combiner5 = __ClosingFuture_Combiner5.Combiner5
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner2
__Combiner2 = __ClosingFuture_Combiner2.Combiner2
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner3
__Combiner3 = __ClosingFuture_Combiner3.Combiner3
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClosingFuture():
    """com.google.common.util.concurrent.ClosingFuture"""
 
    @staticmethod
    def __wrap(java_value: __ClosingFuture) -> 'ClosingFuture':
        return ClosingFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingFuture):
        """
        Dynamic initializer for ClosingFuture.
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
    def transform(self, function: 'ClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture.transform(com.google.common.util.concurrent.ClosingFuture$ClosingFunction<? super V, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__ClosingFuture, self).transform(function, executor))

    @overload
    def transformAsync(self, function: 'AsyncClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture.transformAsync(com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction<? super V, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__ClosingFuture, self).transformAsync(function, executor))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture') -> 'Combiner2':
        """public static <V1,V2> com.google.common.util.concurrent.ClosingFuture$Combiner2<V1, V2> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>)"""
        return Combiner2.__wrap(__ClosingFuture.whenAllSucceed(future1, future2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def finishToValueAndCloser(self, consumer: 'ValueAndCloserConsumer', executor: 'Executor'):
        """public void com.google.common.util.concurrent.ClosingFuture.finishToValueAndCloser(com.google.common.util.concurrent.ClosingFuture$ValueAndCloserConsumer<? super V>,java.util.concurrent.Executor)"""
        super(__ClosingFuture, self).finishToValueAndCloser(consumer, executor)

    @staticmethod
    @overload
    def whenAllComplete(future1: 'ClosingFuture', *moreFutures: 'ClosingFuture') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllComplete(com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>...)"""
        return Combiner.__wrap(__ClosingFuture.whenAllComplete(future1, moreFutures))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def submit(callable: 'ClosingCallable', executor: 'Executor') -> 'ClosingFuture':
        """public static <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.submit(com.google.common.util.concurrent.ClosingFuture$ClosingCallable<V>,java.util.concurrent.Executor)"""
        return ClosingFuture.__wrap(__ClosingFuture.submit(callable, executor))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture', future4: 'ClosingFuture', future5: 'ClosingFuture') -> 'Combiner5':
        """public static <V1,V2,V3,V4,V5> com.google.common.util.concurrent.ClosingFuture$Combiner5<V1, V2, V3, V4, V5> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>,com.google.common.util.concurrent.ClosingFuture<V3>,com.google.common.util.concurrent.ClosingFuture<V4>,com.google.common.util.concurrent.ClosingFuture<V5>)"""
        return Combiner5.__wrap(__ClosingFuture.whenAllSucceed(future1, future2, future3, future4, future5))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.ClosingFuture.toString()"""
        return str.__wrap(super(ClosingFuture, self).toString())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ClosingFuture.cancel(boolean)"""
        return bool.__wrap(super(__ClosingFuture, self).cancel(__boolean.valueOf(mayInterruptIfRunning)))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture', future4: 'ClosingFuture', future5: 'ClosingFuture', future6: 'ClosingFuture', *moreFutures: 'ClosingFuture') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>...)"""
        return Combiner.__wrap(__ClosingFuture.whenAllSucceed(future1, future2, future3, future4, future5, future6, moreFutures))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def catchingAsync(self, exceptionType: 'Class', fallback: 'AsyncClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <X extends java.lang.Throwable> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.catchingAsync(java.lang.Class<X>,com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__ClosingFuture, self).catchingAsync(exceptionType, fallback, executor))

    @overload
    def statusFuture(self) -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ClosingFuture.statusFuture()"""
        return 'ListenableFuture'.__wrap(super(ClosingFuture, self).statusFuture())

    @staticmethod
    @overload
    def eventuallyClosing(future: 'ListenableFuture', closingExecutor: 'Executor') -> 'ClosingFuture':
        """public static <C extends java.lang.Object & java.lang.AutoCloseable> com.google.common.util.concurrent.ClosingFuture<C> com.google.common.util.concurrent.ClosingFuture.eventuallyClosing(com.google.common.util.concurrent.ListenableFuture<C>,java.util.concurrent.Executor)"""
        return ClosingFuture.__wrap(__ClosingFuture.eventuallyClosing(future, closingExecutor))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture', future4: 'ClosingFuture') -> 'Combiner4':
        """public static <V1,V2,V3,V4> com.google.common.util.concurrent.ClosingFuture$Combiner4<V1, V2, V3, V4> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>,com.google.common.util.concurrent.ClosingFuture<V3>,com.google.common.util.concurrent.ClosingFuture<V4>)"""
        return Combiner4.__wrap(__ClosingFuture.whenAllSucceed(future1, future2, future3, future4))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture') -> 'Combiner3':
        """public static <V1,V2,V3> com.google.common.util.concurrent.ClosingFuture$Combiner3<V1, V2, V3> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>,com.google.common.util.concurrent.ClosingFuture<V3>)"""
        return Combiner3.__wrap(__ClosingFuture.whenAllSucceed(future1, future2, future3))

    @staticmethod
    @overload
    def whenAllSucceed(futures: 'Iterable') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(java.lang.Iterable<? extends com.google.common.util.concurrent.ClosingFuture<?>>)"""
        return Combiner.__wrap(__ClosingFuture.whenAllSucceed(futures))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def finishToFuture(self) -> 'FluentFuture':
        """public com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.ClosingFuture.finishToFuture()"""
        return 'FluentFuture'.__wrap(super(ClosingFuture, self).finishToFuture())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def from(future: 'ListenableFuture') -> 'ClosingFuture':
        """public static <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.from(com.google.common.util.concurrent.ListenableFuture<V>)"""
        return ClosingFuture.__wrap(__ClosingFuture.from(future))

    @overload
    def catching(self, exceptionType: 'Class', fallback: 'ClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <X extends java.lang.Throwable> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.catching(java.lang.Class<X>,com.google.common.util.concurrent.ClosingFuture$ClosingFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'.__wrap(super(__ClosingFuture, self).catching(exceptionType, fallback, executor))

    @staticmethod
    @overload
    def whenAllComplete(futures: 'Iterable') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllComplete(java.lang.Iterable<? extends com.google.common.util.concurrent.ClosingFuture<?>>)"""
        return Combiner.__wrap(__ClosingFuture.whenAllComplete(futures))

    @staticmethod
    @overload
    def withoutCloser(function: 'AsyncFunction') -> 'AsyncClosingFunction':
        """public static <V,U> com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction<V, U> com.google.common.util.concurrent.ClosingFuture.withoutCloser(com.google.common.util.concurrent.AsyncFunction<V, U>)"""
        return AsyncClosingFunction.__wrap(__ClosingFuture.withoutCloser(function))

    @staticmethod
    @overload
    def submitAsync(callable: 'AsyncClosingCallable', executor: 'Executor') -> 'ClosingFuture':
        """public static <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.submitAsync(com.google.common.util.concurrent.ClosingFuture$AsyncClosingCallable<V>,java.util.concurrent.Executor)"""
        return ClosingFuture.__wrap(__ClosingFuture.submitAsync(callable, executor))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner4$AsyncClosingFunction4
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner4_AsyncClosingFunction4
__AsyncClosingFunction4 = __ClosingFuture_Combiner4_AsyncClosingFunction4.Combiner4.AsyncClosingFunction4
from abc import abstractmethod, ABC
 
class AsyncClosingFunction4(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner4.AsyncClosingFunction4"""
 
    @staticmethod
    def __wrap(java_value: __AsyncClosingFunction4) -> 'AsyncClosingFunction4':
        return AsyncClosingFunction4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncClosingFunction4):
        """
        Dynamic initializer for AsyncClosingFunction4.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner4$AsyncClosingFunction4.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ExecutionList
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.util.concurrent.ExecutionList as __ExecutionList
__ExecutionList = __ExecutionList
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExecutionList():
    """com.google.common.util.concurrent.ExecutionList"""
 
    @staticmethod
    def __wrap(java_value: __ExecutionList) -> 'ExecutionList':
        return ExecutionList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExecutionList):
        """
        Dynamic initializer for ExecutionList.
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

    @overload
    def execute(self):
        """public void com.google.common.util.concurrent.ExecutionList.execute()"""
        super(ExecutionList, self).execute()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def add(self, runnable: 'Runnable', executor: 'Executor'):
        """public void com.google.common.util.concurrent.ExecutionList.add(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(__ExecutionList, self).add(runnable, executor)

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
        """public com.google.common.util.concurrent.ExecutionList()"""
        val = __ExecutionList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.ExecutionList()"""
        val = __ExecutionList()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner2$AsyncClosingFunction2
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner2_AsyncClosingFunction2
__AsyncClosingFunction2 = __ClosingFuture_Combiner2_AsyncClosingFunction2.Combiner2.AsyncClosingFunction2
 
class AsyncClosingFunction2(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner2.AsyncClosingFunction2"""
 
    @staticmethod
    def __wrap(java_value: __AsyncClosingFunction2) -> 'AsyncClosingFunction2':
        return AsyncClosingFunction2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncClosingFunction2):
        """
        Dynamic initializer for AsyncClosingFunction2.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner2$AsyncClosingFunction2.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner3$ClosingFunction3
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner3_ClosingFunction3
__ClosingFunction3 = __ClosingFuture_Combiner3_ClosingFunction3.Combiner3.ClosingFunction3
from abc import abstractmethod, ABC
 
class ClosingFunction3(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner3.ClosingFunction3"""
 
    @staticmethod
    def __wrap(java_value: __ClosingFunction3) -> 'ClosingFunction3':
        return ClosingFunction3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingFunction3):
        """
        Dynamic initializer for ClosingFunction3.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner3$ClosingFunction3.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner2$ClosingFunction2
import com.google.common.util.concurrent.ClosingFuture as __ClosingFuture_Combiner2_ClosingFunction2
__ClosingFunction2 = __ClosingFuture_Combiner2_ClosingFunction2.Combiner2.ClosingFunction2
from abc import abstractmethod, ABC
 
class ClosingFunction2(ABC):
    """com.google.common.util.concurrent.ClosingFuture.Combiner2.ClosingFunction2"""
 
    @staticmethod
    def __wrap(java_value: __ClosingFunction2) -> 'ClosingFunction2':
        return ClosingFunction2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosingFunction2):
        """
        Dynamic initializer for ClosingFunction2.
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
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner2$ClosingFunction2.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2) throws java.lang.Exception"""
        pass