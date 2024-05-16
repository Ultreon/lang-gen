from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import com.google.common.util.concurrent.Service as _Service_State
_State = _Service_State.State
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class State():
    """com.google.common.util.concurrent.Service.State"""
 
    @staticmethod
    def _wrap(java_value: _State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _State):
        """
        Dynamic initializer for State.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_State__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_State__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['State']:
        """public static com.google.common.util.concurrent.Service$State[] com.google.common.util.concurrent.Service$State.values()"""
        return List[State]._wrap(_State.values())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'State':
        """public static com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.Service$State.valueOf(java.lang.String)"""
        return State._wrap(_State.valueOf(name))

 
 
 
# CLASS: com.google.common.util.concurrent.Service$State
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import com.google.common.util.concurrent.Service as _Service_State
_State = _Service_State.State
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class State():
    """com.google.common.util.concurrent.Service.State"""
 
    @staticmethod
    def _wrap(java_value: _State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _State):
        """
        Dynamic initializer for State.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_State__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_State__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['State']:
        """public static com.google.common.util.concurrent.Service$State[] com.google.common.util.concurrent.Service$State.values()"""
        return List[State]._wrap(_State.values())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'State':
        """public static com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.Service$State.valueOf(java.lang.String)"""
        return State._wrap(_State.valueOf(name))

 
 
 
# CLASS: com.google.common.util.concurrent.Service$State 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$Policy
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_Policy
_Policy = _CycleDetectingLockFactory_Policy.Policy
 
class Policy():
    """com.google.common.util.concurrent.CycleDetectingLockFactory.Policy"""
 
    @staticmethod
    def _wrap(java_value: _Policy) -> 'Policy':
        return Policy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Policy):
        """
        Dynamic initializer for Policy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Policy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Policy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def handlePotentialDeadlock(self, exception: 'PotentialDeadlockException'):
        """public abstract void com.google.common.util.concurrent.CycleDetectingLockFactory$Policy.handlePotentialDeadlock(com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner5$ClosingFunction5
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner5_ClosingFunction5
_ClosingFunction5 = _ClosingFuture_Combiner5_ClosingFunction5.Combiner5.ClosingFunction5
from abc import abstractmethod, ABC
 
class ClosingFunction5():
    """com.google.common.util.concurrent.ClosingFuture.Combiner5.ClosingFunction5"""
 
    @staticmethod
    def _wrap(java_value: _ClosingFunction5) -> 'ClosingFunction5':
        return ClosingFunction5(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingFunction5):
        """
        Dynamic initializer for ClosingFunction5.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingFunction5__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingFunction5__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object, value5: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner5$ClosingFunction5.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4,V5) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingListenableFuture$SimpleForwardingListenableFuture
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import com.google.common.util.concurrent.ForwardingFuture as _ForwardingFuture
_ForwardingFuture = _ForwardingFuture
import java.lang.Boolean as _boolean
import com.google.common.util.concurrent.ForwardingListenableFuture as _ForwardingListenableFuture
_ForwardingListenableFuture = _ForwardingListenableFuture
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import com.google.common.util.concurrent.ForwardingListenableFuture as _ForwardingListenableFuture_SimpleForwardingListenableFuture
_SimpleForwardingListenableFuture = _ForwardingListenableFuture_SimpleForwardingListenableFuture.SimpleForwardingListenableFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class SimpleForwardingListenableFuture():
    """com.google.common.util.concurrent.ForwardingListenableFuture.SimpleForwardingListenableFuture"""
 
    @staticmethod
    def _wrap(java_value: _SimpleForwardingListenableFuture) -> 'SimpleForwardingListenableFuture':
        return SimpleForwardingListenableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleForwardingListenableFuture):
        """
        Dynamic initializer for SimpleForwardingListenableFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleForwardingListenableFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleForwardingListenableFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addListener(self, listener: 'Runnable', exec: 'Executor'):
        """public void com.google.common.util.concurrent.ForwardingListenableFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_ForwardingListenableFuture, self).addListener(listener, exec)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ForwardingFuture, self).get(_long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool._wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool._wrap(super(ForwardingFuture, self).isDone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool._wrap(super(_ForwardingFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(ForwardingFuture, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractListeningExecutorService
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ListeningExecutorService as _ListeningExecutorService
_ListeningExecutorService = _ListeningExecutorService
import java.util.concurrent.Executor as _Executor
_Executor = _Executor
import java.util.concurrent.Callable as Callable
import java.util.concurrent.AbstractExecutorService as _AbstractExecutorService
_AbstractExecutorService = _AbstractExecutorService
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import com.google.common.util.concurrent.AbstractListeningExecutorService as _AbstractListeningExecutorService
_AbstractListeningExecutorService = _AbstractListeningExecutorService
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractListeningExecutorService():
    """com.google.common.util.concurrent.AbstractListeningExecutorService"""
 
    @staticmethod
    def _wrap(java_value: _AbstractListeningExecutorService) -> 'AbstractListeningExecutorService':
        return AbstractListeningExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractListeningExecutorService):
        """
        Dynamic initializer for AbstractListeningExecutorService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractListeningExecutorService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractListeningExecutorService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> java.util.concurrent.AbstractExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_AbstractExecutorService, self).invokeAll(arg0))

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ListeningExecutorService, self).invokeAny(tasks, timeout))

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
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ListeningExecutorService, self).invokeAll(tasks, timeout))

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> java.util.concurrent.AbstractExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_AbstractExecutorService, self).invokeAll(arg0, _long.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T java.util.concurrent.AbstractExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_AbstractExecutorService, self).invokeAny(arg0))

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

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.AbstractListeningExecutorService()"""
        val = _AbstractListeningExecutorService()
        self.__wrapper = val

    @abstractmethod
    def execute(self, arg0: 'Runnable'):
        """public abstract void java.util.concurrent.Executor.execute(java.lang.Runnable)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def isShutdown(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isShutdown()"""
        pass

    @overload
    def submit(self, task: 'Callable') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.AbstractListeningExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'ListenableFuture'._wrap(super(_AbstractListeningExecutorService, self).submit(task))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def shutdownNow(self, ):
        """public abstract java.util.List<java.lang.Runnable> java.util.concurrent.ExecutorService.shutdownNow()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T java.util.concurrent.AbstractExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_AbstractExecutorService, self).invokeAny(arg0, _long.valueOf(arg1), arg2))

    @overload
    def submit(self, task: 'Runnable') -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.AbstractListeningExecutorService.submit(java.lang.Runnable)"""
        return 'ListenableFuture'._wrap(super(_AbstractListeningExecutorService, self).submit(task))

    @overload
    def submit(self, task: 'Runnable', result: object) -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.AbstractListeningExecutorService.submit(java.lang.Runnable,T)"""
        return 'ListenableFuture'._wrap(super(_AbstractListeningExecutorService, self).submit(task, result))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.AbstractListeningExecutorService()"""
        val = _AbstractListeningExecutorService()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ListeningExecutorService, self).awaitTermination(timeout))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @abstractmethod
    def shutdown(self, ):
        """public abstract void java.util.concurrent.ExecutorService.shutdown()"""
        pass

    @abstractmethod
    def isTerminated(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isTerminated()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingBlockingQueue
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import com.google.common.collect.ForwardingCollection as _ForwardingCollection
_ForwardingCollection = _ForwardingCollection
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import com.google.common.collect.ForwardingQueue as _ForwardingQueue
_ForwardingQueue = _ForwardingQueue
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
import com.google.common.util.concurrent.ForwardingBlockingQueue as _ForwardingBlockingQueue
_ForwardingBlockingQueue = _ForwardingBlockingQueue
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForwardingBlockingQueue():
    """com.google.common.util.concurrent.ForwardingBlockingQueue"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingBlockingQueue) -> 'ForwardingBlockingQueue':
        return ForwardingBlockingQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingBlockingQueue):
        """
        Dynamic initializer for ForwardingBlockingQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingBlockingQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingBlockingQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def element(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.element()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).element())

    @overload
    def contains(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).contains(object))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def poll(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingQueue.poll(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object._wrap(super(_ForwardingBlockingQueue, self).poll(_long.valueOf(timeout), unit))

    @overload
    def drainTo(self, c: 'Collection') -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingQueue.drainTo(java.util.Collection<? super E>)"""
        return int._wrap(super(_ForwardingBlockingQueue, self).drainTo(c))

    @overload
    def addAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).addAll(collection))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingCollection.iterator()"""
        return 'Iterator'._wrap(super(pygcollect.ForwardingCollection, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.isEmpty()"""
        return bool._wrap(super(pygcollect.ForwardingCollection, self).isEmpty())

    @overload
    def offer(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingQueue.offer(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ForwardingBlockingQueue, self).offer(e, _long.valueOf(timeout), unit))

    @overload
    def removeAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).removeAll(collection))

    @override
    @overload
    def remove(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.remove()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).remove())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingCollection.size()"""
        return int._wrap(super(pygcollect.ForwardingCollection, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.common.collect.ForwardingCollection.toArray()"""
        return List[object]._wrap(super(pygcollect.ForwardingCollection, self).toArray())

    @overload
    def toArray(self, array: 'Object') -> List[object]:
        """public <T> T[] com.google.common.collect.ForwardingCollection.toArray(T[])"""
        return List[object]._wrap(super(_pygcollect.ForwardingCollection, self).toArray(array))

    @override
    @overload
    def take(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingQueue.take() throws java.lang.InterruptedException"""
        return object._wrap(super(ForwardingBlockingQueue, self).take())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def put(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingQueue.put(E) throws java.lang.InterruptedException"""
        super(_ForwardingBlockingQueue, self).put(e)

    @override
    @overload
    def poll(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.poll()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).poll())

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingCollection.clear()"""
        super(pygcollect.ForwardingCollection, self).clear()

    @overload
    def containsAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).containsAll(collection))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def drainTo(self, c: 'Collection', maxElements: int) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingQueue.drainTo(java.util.Collection<? super E>,int)"""
        return int._wrap(super(_ForwardingBlockingQueue, self).drainTo(c, _int.valueOf(maxElements)))

    @override
    @overload
    def remainingCapacity(self) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingQueue.remainingCapacity()"""
        return int._wrap(super(ForwardingBlockingQueue, self).remainingCapacity())

    @overload
    def retainAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).retainAll(collection))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def peek(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.peek()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).peek())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def remove(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).remove(object))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def offer(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingQueue.offer(E)"""
        return bool._wrap(super(_pygcollect.ForwardingQueue, self).offer(o))

    @overload
    def add(self, element: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.add(E)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).add(element))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ListenableScheduledFuture
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
from builtins import object
import java.util.concurrent.Delayed as _Delayed
_Delayed = _Delayed
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.ListenableScheduledFuture as _ListenableScheduledFuture
_ListenableScheduledFuture = _ListenableScheduledFuture
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
import java.util.concurrent.Future as _Future
_Future = _Future
 
class ListenableScheduledFuture():
    """com.google.common.util.concurrent.ListenableScheduledFuture"""
 
    @staticmethod
    def _wrap(java_value: _ListenableScheduledFuture) -> 'ListenableScheduledFuture':
        return ListenableScheduledFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListenableScheduledFuture):
        """
        Dynamic initializer for ListenableScheduledFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListenableScheduledFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListenableScheduledFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

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

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @abstractmethod
    def compareTo(self, arg0: object):
        """public abstract int java.lang.Comparable.compareTo(T)"""
        pass

    @abstractmethod
    def isDone(self, ):
        """public abstract boolean java.util.concurrent.Future.isDone()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$DeferredCloser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_DeferredCloser
_DeferredCloser = _ClosingFuture_DeferredCloser.DeferredCloser
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeferredCloser():
    """com.google.common.util.concurrent.ClosingFuture.DeferredCloser"""
 
    @staticmethod
    def _wrap(java_value: _DeferredCloser) -> 'DeferredCloser':
        return DeferredCloser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeferredCloser):
        """
        Dynamic initializer for DeferredCloser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeferredCloser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeferredCloser__wrapper":
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
    def eventuallyClose(self, closeable: object, closingExecutor: 'Executor') -> object:
        """public <C extends java.lang.Object & java.lang.AutoCloseable> C com.google.common.util.concurrent.ClosingFuture$DeferredCloser.eventuallyClose(C,java.util.concurrent.Executor)"""
        return object._wrap(super(_DeferredCloser, self).eventuallyClose(closeable, closingExecutor))

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
 
 
# CLASS: com.google.common.util.concurrent.Atomics
import com.google.common.util.concurrent.Atomics as _Atomics
_Atomics = _Atomics
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.atomic.AtomicReference as _AtomicReference
_AtomicReference = _AtomicReference
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.concurrent.atomic.AtomicReferenceArray as AtomicReferenceArray
import java.lang.Integer as _int
import java.util.concurrent.atomic.AtomicReferenceArray as _AtomicReferenceArray
_AtomicReferenceArray = _AtomicReferenceArray
import java.util.concurrent.atomic.AtomicReference as AtomicReference
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Atomics():
    """com.google.common.util.concurrent.Atomics"""
 
    @staticmethod
    def _wrap(java_value: _Atomics) -> 'Atomics':
        return Atomics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Atomics):
        """
        Dynamic initializer for Atomics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Atomics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Atomics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newReferenceArray(array: 'Object') -> 'AtomicReferenceArray':
        """public static <E> java.util.concurrent.atomic.AtomicReferenceArray<E> com.google.common.util.concurrent.Atomics.newReferenceArray(E[])"""
        return AtomicReferenceArray._wrap(_Atomics.newReferenceArray(array))

    @staticmethod
    @overload
    def newReference() -> 'AtomicReference':
        """public static <V> java.util.concurrent.atomic.AtomicReference<V> com.google.common.util.concurrent.Atomics.newReference()"""
        return AtomicReference._wrap(_Atomics.newReference())

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

    @staticmethod
    @overload
    def newReferenceArray(length: int) -> 'AtomicReferenceArray':
        """public static <E> java.util.concurrent.atomic.AtomicReferenceArray<E> com.google.common.util.concurrent.Atomics.newReferenceArray(int)"""
        return AtomicReferenceArray._wrap(_Atomics.newReferenceArray(_int.valueOf(length)))

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
    def newReference(initialValue: object) -> 'AtomicReference':
        """public static <V> java.util.concurrent.atomic.AtomicReference<V> com.google.common.util.concurrent.Atomics.newReference(V)"""
        return AtomicReference._wrap(_Atomics.newReference(initialValue))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner3$AsyncClosingFunction3
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner3_AsyncClosingFunction3
_AsyncClosingFunction3 = _ClosingFuture_Combiner3_AsyncClosingFunction3.Combiner3.AsyncClosingFunction3
from abc import abstractmethod, ABC
 
class AsyncClosingFunction3():
    """com.google.common.util.concurrent.ClosingFuture.Combiner3.AsyncClosingFunction3"""
 
    @staticmethod
    def _wrap(java_value: _AsyncClosingFunction3) -> 'AsyncClosingFunction3':
        return AsyncClosingFunction3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncClosingFunction3):
        """
        Dynamic initializer for AsyncClosingFunction3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncClosingFunction3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncClosingFunction3__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner3$AsyncClosingFunction3.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ListeningExecutorService
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
import com.google.common.util.concurrent.ListeningExecutorService as _ListeningExecutorService
_ListeningExecutorService = _ListeningExecutorService
import java.util.List as _List
_List = _List
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.Executor as _Executor
_Executor = _Executor
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.util.List as List
 
class ListeningExecutorService():
    """com.google.common.util.concurrent.ListeningExecutorService"""
 
    @staticmethod
    def _wrap(java_value: _ListeningExecutorService) -> 'ListeningExecutorService':
        return ListeningExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListeningExecutorService):
        """
        Dynamic initializer for ListeningExecutorService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListeningExecutorService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListeningExecutorService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ListeningExecutorService, self).invokeAny(tasks, timeout))

    @abstractmethod
    def isShutdown(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isShutdown()"""
        pass

    @abstractmethod
    def submit(self, task: 'Runnable'):
        """public abstract com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable)"""
        pass

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

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ListeningExecutorService, self).invokeAll(tasks, timeout))

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
        return bool._wrap(super(_ListeningExecutorService, self).awaitTermination(timeout))

    @abstractmethod
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit'):
        """public abstract <T> T java.util.concurrent.ExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def shutdown(self, ):
        """public abstract void java.util.concurrent.ExecutorService.shutdown()"""
        pass

    @abstractmethod
    def isTerminated(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isTerminated()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ThreadFactoryBuilder
from builtins import str
import com.google.common.util.concurrent.ThreadFactoryBuilder as _ThreadFactoryBuilder
_ThreadFactoryBuilder = _ThreadFactoryBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.ThreadFactory as _ThreadFactory
_ThreadFactory = _ThreadFactory
from builtins import bool
import java.util.concurrent.ThreadFactory as ThreadFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadFactoryBuilder():
    """com.google.common.util.concurrent.ThreadFactoryBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ThreadFactoryBuilder) -> 'ThreadFactoryBuilder':
        return ThreadFactoryBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadFactoryBuilder):
        """
        Dynamic initializer for ThreadFactoryBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadFactoryBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadFactoryBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setPriority(self, priority: int) -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setPriority(int)"""
        return 'ThreadFactoryBuilder'._wrap(super(_ThreadFactoryBuilder, self).setPriority(_int.valueOf(priority)))

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
    def setUncaughtExceptionHandler(self, uncaughtExceptionHandler: 'UncaughtExceptionHandler') -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setUncaughtExceptionHandler(java.lang.Thread$UncaughtExceptionHandler)"""
        return 'ThreadFactoryBuilder'._wrap(super(_ThreadFactoryBuilder, self).setUncaughtExceptionHandler(uncaughtExceptionHandler))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setDaemon(self, daemon: bool) -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setDaemon(boolean)"""
        return 'ThreadFactoryBuilder'._wrap(super(_ThreadFactoryBuilder, self).setDaemon(_boolean.valueOf(daemon)))

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.ThreadFactoryBuilder()"""
        val = _ThreadFactoryBuilder()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.ThreadFactoryBuilder()"""
        val = _ThreadFactoryBuilder()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setThreadFactory(self, backingThreadFactory: 'ThreadFactory') -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setThreadFactory(java.util.concurrent.ThreadFactory)"""
        return 'ThreadFactoryBuilder'._wrap(super(_ThreadFactoryBuilder, self).setThreadFactory(backingThreadFactory))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def build(self) -> 'ThreadFactory':
        """public java.util.concurrent.ThreadFactory com.google.common.util.concurrent.ThreadFactoryBuilder.build()"""
        return 'ThreadFactory'._wrap(super(ThreadFactoryBuilder, self).build())

    @overload
    def setNameFormat(self, nameFormat: str) -> 'ThreadFactoryBuilder':
        """public com.google.common.util.concurrent.ThreadFactoryBuilder com.google.common.util.concurrent.ThreadFactoryBuilder.setNameFormat(java.lang.String)"""
        return 'ThreadFactoryBuilder'._wrap(super(_ThreadFactoryBuilder, self).setNameFormat(nameFormat))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingListeningExecutorService
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.Collection as Collection
import com.google.common.util.concurrent.ListeningExecutorService as _ListeningExecutorService
_ListeningExecutorService = _ListeningExecutorService
import com.google.common.util.concurrent.ForwardingListeningExecutorService as _ForwardingListeningExecutorService
_ForwardingListeningExecutorService = _ForwardingListeningExecutorService
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.lang.Long as _long
import com.google.common.util.concurrent.ForwardingExecutorService as _ForwardingExecutorService
_ForwardingExecutorService = _ForwardingExecutorService
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForwardingListeningExecutorService():
    """com.google.common.util.concurrent.ForwardingListeningExecutorService"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingListeningExecutorService) -> 'ForwardingListeningExecutorService':
        return ForwardingListeningExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingListeningExecutorService):
        """
        Dynamic initializer for ForwardingListeningExecutorService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingListeningExecutorService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingListeningExecutorService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invokeAll(self, tasks: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ForwardingExecutorService, self).invokeAll(tasks))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> com.google.common.util.concurrent.ForwardingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(ForwardingExecutorService, self).shutdownNow())

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ListeningExecutorService, self).invokeAny(tasks, timeout))

    @overload
    def submit(self, task: 'Callable') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ForwardingListeningExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'ListenableFuture'._wrap(super(_ForwardingListeningExecutorService, self).submit(task))

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ForwardingExecutorService, self).invokeAll(tasks, _long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isShutdown()"""
        return bool._wrap(super(ForwardingExecutorService, self).isShutdown())

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ForwardingExecutorService, self).invokeAny(tasks, _long.valueOf(timeout), unit))

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ListeningExecutorService, self).invokeAll(tasks, timeout))

    @overload
    def submit(self, task: 'Runnable', result: object) -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ForwardingListeningExecutorService.submit(java.lang.Runnable,T)"""
        return 'ListenableFuture'._wrap(super(_ForwardingListeningExecutorService, self).submit(task, result))

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
    def isTerminated(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isTerminated()"""
        return bool._wrap(super(ForwardingExecutorService, self).isTerminated())

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @overload
    def invokeAny(self, tasks: 'Collection') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingExecutorService, self).invokeAny(tasks))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def awaitTermination(self, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ForwardingExecutorService, self).awaitTermination(_long.valueOf(timeout), unit))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def submit(self, task: 'Runnable') -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ForwardingListeningExecutorService.submit(java.lang.Runnable)"""
        return 'ListenableFuture'._wrap(super(_ForwardingListeningExecutorService, self).submit(task))

    @override
    @overload
    def shutdown(self):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.shutdown()"""
        super(ForwardingExecutorService, self).shutdown()

    @override
    @overload
    def execute(self, command: 'Runnable'):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.execute(java.lang.Runnable)"""
        super(_ForwardingExecutorService, self).execute(command)

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
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ListeningExecutorService, self).awaitTermination(timeout))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.MoreExecutors
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
import com.google.common.util.concurrent.ListeningExecutorService as _ListeningExecutorService
_ListeningExecutorService = _ListeningExecutorService
import java.util.concurrent.ScheduledExecutorService as _ScheduledExecutorService
_ScheduledExecutorService = _ScheduledExecutorService
import com.google.common.util.concurrent.ListeningScheduledExecutorService as _ListeningScheduledExecutorService
_ListeningScheduledExecutorService = _ListeningScheduledExecutorService
import java.util.concurrent.ScheduledThreadPoolExecutor as ScheduledThreadPoolExecutor
import java.util.concurrent.Executor as _Executor
_Executor = _Executor
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
import com.google.common.util.concurrent.MoreExecutors as _MoreExecutors
_MoreExecutors = _MoreExecutors
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.ThreadFactory as _ThreadFactory
_ThreadFactory = _ThreadFactory
import java.util.concurrent.ThreadPoolExecutor as ThreadPoolExecutor
import java.util.concurrent.ThreadFactory as ThreadFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MoreExecutors():
    """com.google.common.util.concurrent.MoreExecutors"""
 
    @staticmethod
    def _wrap(java_value: _MoreExecutors) -> 'MoreExecutors':
        return MoreExecutors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MoreExecutors):
        """
        Dynamic initializer for MoreExecutors.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MoreExecutors__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MoreExecutors__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def platformThreadFactory() -> 'ThreadFactory':
        """public static java.util.concurrent.ThreadFactory com.google.common.util.concurrent.MoreExecutors.platformThreadFactory()"""
        return ThreadFactory._wrap(_MoreExecutors.platformThreadFactory())

    @staticmethod
    @overload
    def getExitingExecutorService(executor: 'ThreadPoolExecutor') -> 'ExecutorService':
        """public static java.util.concurrent.ExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingExecutorService(java.util.concurrent.ThreadPoolExecutor)"""
        return ExecutorService._wrap(_MoreExecutors.getExitingExecutorService(executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getExitingScheduledExecutorService(executor: 'ScheduledThreadPoolExecutor', terminationTimeout: 'Duration') -> 'ScheduledExecutorService':
        """public static java.util.concurrent.ScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor,java.time.Duration)"""
        return ScheduledExecutorService._wrap(_MoreExecutors.getExitingScheduledExecutorService(executor, terminationTimeout))

    @staticmethod
    @overload
    def getExitingExecutorService(executor: 'ThreadPoolExecutor', terminationTimeout: 'Duration') -> 'ExecutorService':
        """public static java.util.concurrent.ExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingExecutorService(java.util.concurrent.ThreadPoolExecutor,java.time.Duration)"""
        return ExecutorService._wrap(_MoreExecutors.getExitingExecutorService(executor, terminationTimeout))

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
    def getExitingExecutorService(executor: 'ThreadPoolExecutor', terminationTimeout: int, timeUnit: 'TimeUnit') -> 'ExecutorService':
        """public static java.util.concurrent.ExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingExecutorService(java.util.concurrent.ThreadPoolExecutor,long,java.util.concurrent.TimeUnit)"""
        return ExecutorService._wrap(_MoreExecutors.getExitingExecutorService(executor, _long.valueOf(terminationTimeout), timeUnit))

    @staticmethod
    @overload
    def addDelayedShutdownHook(service: 'ExecutorService', terminationTimeout: 'Duration'):
        """public static void com.google.common.util.concurrent.MoreExecutors.addDelayedShutdownHook(java.util.concurrent.ExecutorService,java.time.Duration)"""
        _MoreExecutors.addDelayedShutdownHook(service, terminationTimeout)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def listeningDecorator(delegate: 'ScheduledExecutorService') -> 'ListeningScheduledExecutorService':
        """public static com.google.common.util.concurrent.ListeningScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.listeningDecorator(java.util.concurrent.ScheduledExecutorService)"""
        return ListeningScheduledExecutorService._wrap(_MoreExecutors.listeningDecorator(delegate))

    @staticmethod
    @overload
    def listeningDecorator(delegate: 'ExecutorService') -> 'ListeningExecutorService':
        """public static com.google.common.util.concurrent.ListeningExecutorService com.google.common.util.concurrent.MoreExecutors.listeningDecorator(java.util.concurrent.ExecutorService)"""
        return ListeningExecutorService._wrap(_MoreExecutors.listeningDecorator(delegate))

    @staticmethod
    @overload
    def addDelayedShutdownHook(service: 'ExecutorService', terminationTimeout: int, timeUnit: 'TimeUnit'):
        """public static void com.google.common.util.concurrent.MoreExecutors.addDelayedShutdownHook(java.util.concurrent.ExecutorService,long,java.util.concurrent.TimeUnit)"""
        _MoreExecutors.addDelayedShutdownHook(service, _long.valueOf(terminationTimeout), timeUnit)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def newDirectExecutorService() -> 'ListeningExecutorService':
        """public static com.google.common.util.concurrent.ListeningExecutorService com.google.common.util.concurrent.MoreExecutors.newDirectExecutorService()"""
        return ListeningExecutorService._wrap(_MoreExecutors.newDirectExecutorService())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def shutdownAndAwaitTermination(service: 'ExecutorService', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.MoreExecutors.shutdownAndAwaitTermination(java.util.concurrent.ExecutorService,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_MoreExecutors.shutdownAndAwaitTermination(service, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def shutdownAndAwaitTermination(service: 'ExecutorService', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.MoreExecutors.shutdownAndAwaitTermination(java.util.concurrent.ExecutorService,java.time.Duration)"""
        return bool._wrap(_MoreExecutors.shutdownAndAwaitTermination(service, timeout))

    @staticmethod
    @overload
    def getExitingScheduledExecutorService(executor: 'ScheduledThreadPoolExecutor', terminationTimeout: int, timeUnit: 'TimeUnit') -> 'ScheduledExecutorService':
        """public static java.util.concurrent.ScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor,long,java.util.concurrent.TimeUnit)"""
        return ScheduledExecutorService._wrap(_MoreExecutors.getExitingScheduledExecutorService(executor, _long.valueOf(terminationTimeout), timeUnit))

    @staticmethod
    @overload
    def directExecutor() -> 'Executor':
        """public static java.util.concurrent.Executor com.google.common.util.concurrent.MoreExecutors.directExecutor()"""
        return Executor._wrap(_MoreExecutors.directExecutor())

    @staticmethod
    @overload
    def newSequentialExecutor(delegate: 'Executor') -> 'Executor':
        """public static java.util.concurrent.Executor com.google.common.util.concurrent.MoreExecutors.newSequentialExecutor(java.util.concurrent.Executor)"""
        return Executor._wrap(_MoreExecutors.newSequentialExecutor(delegate))

    @staticmethod
    @overload
    def getExitingScheduledExecutorService(executor: 'ScheduledThreadPoolExecutor') -> 'ScheduledExecutorService':
        """public static java.util.concurrent.ScheduledExecutorService com.google.common.util.concurrent.MoreExecutors.getExitingScheduledExecutorService(java.util.concurrent.ScheduledThreadPoolExecutor)"""
        return ScheduledExecutorService._wrap(_MoreExecutors.getExitingScheduledExecutorService(executor))

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
 
 
# CLASS: com.google.common.util.concurrent.FluentFuture
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.util.concurrent.FluentFuture as _FluentFuture
_FluentFuture = _FluentFuture
import java.lang.Boolean as _boolean
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.AbstractFuture as _AbstractFuture
_AbstractFuture = _AbstractFuture
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class FluentFuture():
    """com.google.common.util.concurrent.FluentFuture"""
 
    @staticmethod
    def _wrap(java_value: _FluentFuture) -> 'FluentFuture':
        return FluentFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FluentFuture):
        """
        Dynamic initializer for FluentFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FluentFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FluentFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isCancelled()"""
        return bool._wrap(super(AbstractFuture, self).isCancelled())

    @overload
    def addCallback(self, callback: 'FutureCallback', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.FluentFuture.addCallback(com.google.common.util.concurrent.FutureCallback<? super V>,java.util.concurrent.Executor)"""
        super(_FluentFuture, self).addCallback(callback, executor)

    @override
    @overload
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public void com.google.common.util.concurrent.AbstractFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_AbstractFuture, self).addListener(listener, executor)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def transform(self, function: 'Function', executor: 'Executor') -> 'FluentFuture':
        """public final <T> com.google.common.util.concurrent.FluentFuture<T> com.google.common.util.concurrent.FluentFuture.transform(com.google.common.base.Function<? super V, T>,java.util.concurrent.Executor)"""
        return 'FluentFuture'._wrap(super(_FluentFuture, self).transform(function, executor))

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(AbstractFuture, self).get())

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_AbstractFuture, self).get(_long.valueOf(timeout), unit))

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
    def withTimeout(self, timeout: 'Duration', scheduledExecutor: 'ScheduledExecutorService') -> 'FluentFuture':
        """public final com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.withTimeout(java.time.Duration,java.util.concurrent.ScheduledExecutorService)"""
        return 'FluentFuture'._wrap(super(_FluentFuture, self).withTimeout(timeout, scheduledExecutor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isDone()"""
        return bool._wrap(super(AbstractFuture, self).isDone())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.cancel(boolean)"""
        return bool._wrap(super(_AbstractFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @overload
    def catchingAsync(self, exceptionType: 'Class', fallback: 'AsyncFunction', executor: 'Executor') -> 'FluentFuture':
        """public final <X extends java.lang.Throwable> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.catchingAsync(java.lang.Class<X>,com.google.common.util.concurrent.AsyncFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'FluentFuture'._wrap(super(_FluentFuture, self).catchingAsync(exceptionType, fallback, executor))

    @staticmethod
    @overload
    def from(future: 'ListenableFuture') -> 'FluentFuture':
        """public static <V> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.from(com.google.common.util.concurrent.ListenableFuture<V>)"""
        return FluentFuture._wrap(_FluentFuture.from(future))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @overload
    def withTimeout(self, timeout: int, unit: 'TimeUnit', scheduledExecutor: 'ScheduledExecutorService') -> 'FluentFuture':
        """public final com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.withTimeout(long,java.util.concurrent.TimeUnit,java.util.concurrent.ScheduledExecutorService)"""
        return 'FluentFuture'._wrap(super(_FluentFuture, self).withTimeout(_long.valueOf(timeout), unit, scheduledExecutor))

    @staticmethod
    @overload
    def from(future: 'FluentFuture') -> 'FluentFuture':
        """public static <V> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.from(com.google.common.util.concurrent.FluentFuture<V>)"""
        return FluentFuture._wrap(_FluentFuture.from(future))

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @overload
    def transformAsync(self, function: 'AsyncFunction', executor: 'Executor') -> 'FluentFuture':
        """public final <T> com.google.common.util.concurrent.FluentFuture<T> com.google.common.util.concurrent.FluentFuture.transformAsync(com.google.common.util.concurrent.AsyncFunction<? super V, T>,java.util.concurrent.Executor)"""
        return 'FluentFuture'._wrap(super(_FluentFuture, self).transformAsync(function, executor))

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def catching(self, exceptionType: 'Class', fallback: 'Function', executor: 'Executor') -> 'FluentFuture':
        """public final <X extends java.lang.Throwable> com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.FluentFuture.catching(java.lang.Class<X>,com.google.common.base.Function<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'FluentFuture'._wrap(super(_FluentFuture, self).catching(exceptionType, fallback, executor))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractFuture.toString()"""
        return str._wrap(super(AbstractFuture, self).toString())

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
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory
import java.util.concurrent.locks.ReentrantLock as ReentrantLock
from builtins import str
import java.util.concurrent.locks.ReentrantReadWriteLock as ReentrantReadWriteLock
from pyquantum_helper import override
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_WithExplicitOrdering
_WithExplicitOrdering = _CycleDetectingLockFactory_WithExplicitOrdering.WithExplicitOrdering
import java.util.concurrent.locks.ReentrantReadWriteLock as _ReentrantReadWriteLock
_ReentrantReadWriteLock = _ReentrantReadWriteLock
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.concurrent.locks.ReentrantLock as _ReentrantLock
_ReentrantLock = _ReentrantLock
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory
_CycleDetectingLockFactory = _CycleDetectingLockFactory
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CycleDetectingLockFactory():
    """com.google.common.util.concurrent.CycleDetectingLockFactory"""
 
    @staticmethod
    def _wrap(java_value: _CycleDetectingLockFactory) -> 'CycleDetectingLockFactory':
        return CycleDetectingLockFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CycleDetectingLockFactory):
        """
        Dynamic initializer for CycleDetectingLockFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CycleDetectingLockFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CycleDetectingLockFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newInstanceWithExplicitOrdering(enumClass: 'Class', policy: 'Policy') -> 'WithExplicitOrdering':
        """public static <E extends java.lang.Enum<E>> com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering<E> com.google.common.util.concurrent.CycleDetectingLockFactory.newInstanceWithExplicitOrdering(java.lang.Class<E>,com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return WithExplicitOrdering._wrap(_CycleDetectingLockFactory.newInstanceWithExplicitOrdering(enumClass, policy))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def newInstance(policy: 'Policy') -> 'CycleDetectingLockFactory':
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory com.google.common.util.concurrent.CycleDetectingLockFactory.newInstance(com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return CycleDetectingLockFactory._wrap(_CycleDetectingLockFactory.newInstance(policy))

    @overload
    def newReentrantReadWriteLock(self, lockName: str) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String)"""
        return 'ReentrantReadWriteLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName))

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
    def newReentrantLock(self, lockName: str, fair: bool) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String,boolean)"""
        return 'ReentrantLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantLock(lockName, _boolean.valueOf(fair)))

    @overload
    def newReentrantReadWriteLock(self, lockName: str, fair: bool) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String,boolean)"""
        return 'ReentrantReadWriteLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName, _boolean.valueOf(fair)))

    @overload
    def newReentrantLock(self, lockName: str) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String)"""
        return 'ReentrantLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantLock(lockName))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.Monitor$Guard
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.Monitor as _Monitor_Guard
_Guard = _Monitor_Guard.Guard
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Guard():
    """com.google.common.util.concurrent.Monitor.Guard"""
 
    @staticmethod
    def _wrap(java_value: _Guard) -> 'Guard':
        return Guard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Guard):
        """
        Dynamic initializer for Guard.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Guard__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Guard__wrapper":
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

    @abstractmethod
    def isSatisfied(self, ):
        """public abstract boolean com.google.common.util.concurrent.Monitor$Guard.isSatisfied()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner2$ClosingFunction2
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner2_ClosingFunction2
_ClosingFunction2 = _ClosingFuture_Combiner2_ClosingFunction2.Combiner2.ClosingFunction2
 
class ClosingFunction2():
    """com.google.common.util.concurrent.ClosingFuture.Combiner2.ClosingFunction2"""
 
    @staticmethod
    def _wrap(java_value: _ClosingFunction2) -> 'ClosingFunction2':
        return ClosingFunction2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingFunction2):
        """
        Dynamic initializer for ClosingFunction2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingFunction2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingFunction2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner2$ClosingFunction2.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ClosingFunction
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_ClosingFunction
_ClosingFunction = _ClosingFuture_ClosingFunction.ClosingFunction
from abc import abstractmethod, ABC
 
class ClosingFunction():
    """com.google.common.util.concurrent.ClosingFuture.ClosingFunction"""
 
    @staticmethod
    def _wrap(java_value: _ClosingFunction) -> 'ClosingFunction':
        return ClosingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingFunction):
        """
        Dynamic initializer for ClosingFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', input: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$ClosingFunction.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,T) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner
_Combiner = _ClosingFuture_Combiner.Combiner
import java.lang.Integer as _int
from builtins import bool
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture
_ClosingFuture = _ClosingFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Combiner():
    """com.google.common.util.concurrent.ClosingFuture.Combiner"""
 
    @staticmethod
    def _wrap(java_value: _Combiner) -> 'Combiner':
        return Combiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Combiner):
        """
        Dynamic initializer for Combiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Combiner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Combiner__wrapper":
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
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).callAsync(combiningCallable, executor))

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
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).call(combiningCallable, executor))

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture
from builtins import str
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner2
_Combiner2 = _ClosingFuture_Combiner2.Combiner2
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner3
_Combiner3 = _ClosingFuture_Combiner3.Combiner3
from pyquantum_helper import override
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner5
_Combiner5 = _ClosingFuture_Combiner5.Combiner5
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner4
_Combiner4 = _ClosingFuture_Combiner4.Combiner4
import java.lang.Iterable as Iterable
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_AsyncClosingFunction
_AsyncClosingFunction = _ClosingFuture_AsyncClosingFunction.AsyncClosingFunction
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner
_Combiner = _ClosingFuture_Combiner.Combiner
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import com.google.common.util.concurrent.FluentFuture as _FluentFuture
_FluentFuture = _FluentFuture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture
_ClosingFuture = _ClosingFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClosingFuture():
    """com.google.common.util.concurrent.ClosingFuture"""
 
    @staticmethod
    def _wrap(java_value: _ClosingFuture) -> 'ClosingFuture':
        return ClosingFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingFuture):
        """
        Dynamic initializer for ClosingFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def finishToFuture(self) -> 'FluentFuture':
        """public com.google.common.util.concurrent.FluentFuture<V> com.google.common.util.concurrent.ClosingFuture.finishToFuture()"""
        return 'FluentFuture'._wrap(super(ClosingFuture, self).finishToFuture())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ClosingFuture.cancel(boolean)"""
        return bool._wrap(super(_ClosingFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.ClosingFuture.toString()"""
        return str._wrap(super(ClosingFuture, self).toString())

    @staticmethod
    @overload
    def withoutCloser(function: 'AsyncFunction') -> 'AsyncClosingFunction':
        """public static <V,U> com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction<V, U> com.google.common.util.concurrent.ClosingFuture.withoutCloser(com.google.common.util.concurrent.AsyncFunction<V, U>)"""
        return AsyncClosingFunction._wrap(_ClosingFuture.withoutCloser(function))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture', future4: 'ClosingFuture') -> 'Combiner4':
        """public static <V1,V2,V3,V4> com.google.common.util.concurrent.ClosingFuture$Combiner4<V1, V2, V3, V4> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>,com.google.common.util.concurrent.ClosingFuture<V3>,com.google.common.util.concurrent.ClosingFuture<V4>)"""
        return Combiner4._wrap(_ClosingFuture.whenAllSucceed(future1, future2, future3, future4))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture') -> 'Combiner2':
        """public static <V1,V2> com.google.common.util.concurrent.ClosingFuture$Combiner2<V1, V2> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>)"""
        return Combiner2._wrap(_ClosingFuture.whenAllSucceed(future1, future2))

    @staticmethod
    @overload
    def submit(callable: 'ClosingCallable', executor: 'Executor') -> 'ClosingFuture':
        """public static <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.submit(com.google.common.util.concurrent.ClosingFuture$ClosingCallable<V>,java.util.concurrent.Executor)"""
        return ClosingFuture._wrap(_ClosingFuture.submit(callable, executor))

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
    def catching(self, exceptionType: 'Class', fallback: 'ClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <X extends java.lang.Throwable> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.catching(java.lang.Class<X>,com.google.common.util.concurrent.ClosingFuture$ClosingFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_ClosingFuture, self).catching(exceptionType, fallback, executor))

    @overload
    def transformAsync(self, function: 'AsyncClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture.transformAsync(com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction<? super V, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_ClosingFuture, self).transformAsync(function, executor))

    @overload
    def catchingAsync(self, exceptionType: 'Class', fallback: 'AsyncClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <X extends java.lang.Throwable> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.catchingAsync(java.lang.Class<X>,com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_ClosingFuture, self).catchingAsync(exceptionType, fallback, executor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def statusFuture(self) -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ClosingFuture.statusFuture()"""
        return 'ListenableFuture'._wrap(super(ClosingFuture, self).statusFuture())

    @staticmethod
    @overload
    def from(future: 'ListenableFuture') -> 'ClosingFuture':
        """public static <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.from(com.google.common.util.concurrent.ListenableFuture<V>)"""
        return ClosingFuture._wrap(_ClosingFuture.from(future))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture', future4: 'ClosingFuture', future5: 'ClosingFuture', future6: 'ClosingFuture', *moreFutures: 'ClosingFuture') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>...)"""
        return Combiner._wrap(_ClosingFuture.whenAllSucceed(future1, future2, future3, future4, future5, future6, moreFutures))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def whenAllSucceed(futures: 'Iterable') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(java.lang.Iterable<? extends com.google.common.util.concurrent.ClosingFuture<?>>)"""
        return Combiner._wrap(_ClosingFuture.whenAllSucceed(futures))

    @staticmethod
    @overload
    def submitAsync(callable: 'AsyncClosingCallable', executor: 'Executor') -> 'ClosingFuture':
        """public static <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture.submitAsync(com.google.common.util.concurrent.ClosingFuture$AsyncClosingCallable<V>,java.util.concurrent.Executor)"""
        return ClosingFuture._wrap(_ClosingFuture.submitAsync(callable, executor))

    @staticmethod
    @overload
    def whenAllComplete(future1: 'ClosingFuture', *moreFutures: 'ClosingFuture') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllComplete(com.google.common.util.concurrent.ClosingFuture<?>,com.google.common.util.concurrent.ClosingFuture<?>...)"""
        return Combiner._wrap(_ClosingFuture.whenAllComplete(future1, moreFutures))

    @overload
    def transform(self, function: 'ClosingFunction', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture.transform(com.google.common.util.concurrent.ClosingFuture$ClosingFunction<? super V, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_ClosingFuture, self).transform(function, executor))

    @overload
    def finishToValueAndCloser(self, consumer: 'ValueAndCloserConsumer', executor: 'Executor'):
        """public void com.google.common.util.concurrent.ClosingFuture.finishToValueAndCloser(com.google.common.util.concurrent.ClosingFuture$ValueAndCloserConsumer<? super V>,java.util.concurrent.Executor)"""
        super(_ClosingFuture, self).finishToValueAndCloser(consumer, executor)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture', future4: 'ClosingFuture', future5: 'ClosingFuture') -> 'Combiner5':
        """public static <V1,V2,V3,V4,V5> com.google.common.util.concurrent.ClosingFuture$Combiner5<V1, V2, V3, V4, V5> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>,com.google.common.util.concurrent.ClosingFuture<V3>,com.google.common.util.concurrent.ClosingFuture<V4>,com.google.common.util.concurrent.ClosingFuture<V5>)"""
        return Combiner5._wrap(_ClosingFuture.whenAllSucceed(future1, future2, future3, future4, future5))

    @staticmethod
    @overload
    def whenAllComplete(futures: 'Iterable') -> 'Combiner':
        """public static com.google.common.util.concurrent.ClosingFuture$Combiner com.google.common.util.concurrent.ClosingFuture.whenAllComplete(java.lang.Iterable<? extends com.google.common.util.concurrent.ClosingFuture<?>>)"""
        return Combiner._wrap(_ClosingFuture.whenAllComplete(futures))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def eventuallyClosing(future: 'ListenableFuture', closingExecutor: 'Executor') -> 'ClosingFuture':
        """public static <C extends java.lang.Object & java.lang.AutoCloseable> com.google.common.util.concurrent.ClosingFuture<C> com.google.common.util.concurrent.ClosingFuture.eventuallyClosing(com.google.common.util.concurrent.ListenableFuture<C>,java.util.concurrent.Executor)"""
        return ClosingFuture._wrap(_ClosingFuture.eventuallyClosing(future, closingExecutor))

    @staticmethod
    @overload
    def whenAllSucceed(future1: 'ClosingFuture', future2: 'ClosingFuture', future3: 'ClosingFuture') -> 'Combiner3':
        """public static <V1,V2,V3> com.google.common.util.concurrent.ClosingFuture$Combiner3<V1, V2, V3> com.google.common.util.concurrent.ClosingFuture.whenAllSucceed(com.google.common.util.concurrent.ClosingFuture<V1>,com.google.common.util.concurrent.ClosingFuture<V2>,com.google.common.util.concurrent.ClosingFuture<V3>)"""
        return Combiner3._wrap(_ClosingFuture.whenAllSucceed(future1, future2, future3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingFuture$SimpleForwardingFuture
import com.google.common.util.concurrent.ForwardingFuture as _ForwardingFuture_SimpleForwardingFuture
_SimpleForwardingFuture = _ForwardingFuture_SimpleForwardingFuture.SimpleForwardingFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Future.State as State
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ForwardingFuture as _ForwardingFuture
_ForwardingFuture = _ForwardingFuture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class SimpleForwardingFuture():
    """com.google.common.util.concurrent.ForwardingFuture.SimpleForwardingFuture"""
 
    @staticmethod
    def _wrap(java_value: _SimpleForwardingFuture) -> 'SimpleForwardingFuture':
        return SimpleForwardingFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleForwardingFuture):
        """
        Dynamic initializer for SimpleForwardingFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleForwardingFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleForwardingFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ForwardingFuture, self).get(_long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool._wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool._wrap(super(ForwardingFuture, self).isDone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool._wrap(super(_ForwardingFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(ForwardingFuture, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ExecutionList
import com.google.common.util.concurrent.ExecutionList as _ExecutionList
_ExecutionList = _ExecutionList
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExecutionList():
    """com.google.common.util.concurrent.ExecutionList"""
 
    @staticmethod
    def _wrap(java_value: _ExecutionList) -> 'ExecutionList':
        return ExecutionList(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExecutionList):
        """
        Dynamic initializer for ExecutionList.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExecutionList__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExecutionList__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, ):
        """public com.google.common.util.concurrent.ExecutionList()"""
        val = _ExecutionList()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def execute(self):
        """public void com.google.common.util.concurrent.ExecutionList.execute()"""
        super(ExecutionList, self).execute()

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.ExecutionList()"""
        val = _ExecutionList()
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def add(self, runnable: 'Runnable', executor: 'Executor'):
        """public void com.google.common.util.concurrent.ExecutionList.add(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_ExecutionList, self).add(runnable, executor)

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
 
 
# CLASS: com.google.common.util.concurrent.AtomicDoubleArray
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.google.common.util.concurrent.AtomicDoubleArray as _AtomicDoubleArray
_AtomicDoubleArray = _AtomicDoubleArray
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.function.DoubleBinaryOperator as DoubleBinaryOperator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.function.DoubleUnaryOperator as DoubleUnaryOperator
import java.lang.Class as _Class
_Class = _Class
 
class AtomicDoubleArray():
    """com.google.common.util.concurrent.AtomicDoubleArray"""
 
    @staticmethod
    def _wrap(java_value: _AtomicDoubleArray) -> 'AtomicDoubleArray':
        return AtomicDoubleArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtomicDoubleArray):
        """
        Dynamic initializer for AtomicDoubleArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtomicDoubleArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtomicDoubleArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAndAccumulate(self, i: int, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndAccumulate(int,double,java.util.function.DoubleBinaryOperator)"""
        return float._wrap(super(_AtomicDoubleArray, self).getAndAccumulate(_int.valueOf(i), _double.valueOf(x), accumulatorFunction))

    @overload
    def addAndGet(self, i: int, delta: float) -> float:
        """public double com.google.common.util.concurrent.AtomicDoubleArray.addAndGet(int,double)"""
        return float._wrap(super(_AtomicDoubleArray, self).addAndGet(_int.valueOf(i), _double.valueOf(delta)))

    @overload
    def __init__(self, array: 'double'):
        """public com.google.common.util.concurrent.AtomicDoubleArray(double[])"""
        val = _AtomicDoubleArray(array)
        self.__wrapper = val

    @overload
    def length(self) -> int:
        """public final int com.google.common.util.concurrent.AtomicDoubleArray.length()"""
        return int._wrap(super(AtomicDoubleArray, self).length())

    @overload
    def set(self, i: int, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDoubleArray.set(int,double)"""
        super(_AtomicDoubleArray, self).set(_int.valueOf(i), _double.valueOf(newValue))

    @overload
    def getAndSet(self, i: int, newValue: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndSet(int,double)"""
        return float._wrap(super(_AtomicDoubleArray, self).getAndSet(_int.valueOf(i), _double.valueOf(newValue)))

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
    def __init__(self, length: int):
        """public com.google.common.util.concurrent.AtomicDoubleArray(int)"""
        val = _AtomicDoubleArray(_int.valueOf(length))
        self.__wrapper = val

    @overload
    def compareAndSet(self, i: int, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDoubleArray.compareAndSet(int,double,double)"""
        return bool._wrap(super(_AtomicDoubleArray, self).compareAndSet(_int.valueOf(i), _double.valueOf(expect), _double.valueOf(update)))

    @overload
    def getAndUpdate(self, i: int, updaterFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndUpdate(int,java.util.function.DoubleUnaryOperator)"""
        return float._wrap(super(_AtomicDoubleArray, self).getAndUpdate(_int.valueOf(i), updaterFunction))

    @overload
    def getAndAdd(self, i: int, delta: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.getAndAdd(int,double)"""
        return float._wrap(super(_AtomicDoubleArray, self).getAndAdd(_int.valueOf(i), _double.valueOf(delta)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def lazySet(self, i: int, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDoubleArray.lazySet(int,double)"""
        super(_AtomicDoubleArray, self).lazySet(_int.valueOf(i), _double.valueOf(newValue))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def weakCompareAndSet(self, i: int, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDoubleArray.weakCompareAndSet(int,double,double)"""
        return bool._wrap(super(_AtomicDoubleArray, self).weakCompareAndSet(_int.valueOf(i), _double.valueOf(expect), _double.valueOf(update)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AtomicDoubleArray.toString()"""
        return str._wrap(super(AtomicDoubleArray, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, i: int) -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.get(int)"""
        return float._wrap(super(_AtomicDoubleArray, self).get(_int.valueOf(i)))

    @overload
    def updateAndGet(self, i: int, updaterFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.updateAndGet(int,java.util.function.DoubleUnaryOperator)"""
        return float._wrap(super(_AtomicDoubleArray, self).updateAndGet(_int.valueOf(i), updaterFunction))

    @overload
    def accumulateAndGet(self, i: int, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDoubleArray.accumulateAndGet(int,double,java.util.function.DoubleBinaryOperator)"""
        return float._wrap(super(_AtomicDoubleArray, self).accumulateAndGet(_int.valueOf(i), _double.valueOf(x), accumulatorFunction))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingBlockingDeque
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import com.google.common.collect.ForwardingCollection as _ForwardingCollection
_ForwardingCollection = _ForwardingCollection
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import com.google.common.collect.ForwardingQueue as _ForwardingQueue
_ForwardingQueue = _ForwardingQueue
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import com.google.common.collect.ForwardingDeque as _ForwardingDeque
_ForwardingDeque = _ForwardingDeque
import java.util.Deque as Deque
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.ForwardingBlockingDeque as _ForwardingBlockingDeque
_ForwardingBlockingDeque = _ForwardingBlockingDeque
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForwardingBlockingDeque():
    """com.google.common.util.concurrent.ForwardingBlockingDeque"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingBlockingDeque) -> 'ForwardingBlockingDeque':
        return ForwardingBlockingDeque(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingBlockingDeque):
        """
        Dynamic initializer for ForwardingBlockingDeque.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingBlockingDeque__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingBlockingDeque__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removeFirstOccurrence(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.removeFirstOccurrence(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingDeque, self).removeFirstOccurrence(o))

    @override
    @overload
    def takeFirst(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.takeFirst() throws java.lang.InterruptedException"""
        return object._wrap(super(ForwardingBlockingDeque, self).takeFirst())

    @overload
    def offerFirst(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingDeque.offerFirst(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ForwardingBlockingDeque, self).offerFirst(e, _long.valueOf(timeout), unit))

    @override
    @overload
    def addFirst(self, e: object):
        """public void com.google.common.collect.ForwardingDeque.addFirst(E)"""
        super(_pygcollect.ForwardingDeque, self).addFirst(e)

    @override
    @overload
    def putLast(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingDeque.putLast(E) throws java.lang.InterruptedException"""
        super(_ForwardingBlockingDeque, self).putLast(e)

    @override
    @overload
    def element(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.element()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).element())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.isEmpty()"""
        return bool._wrap(super(pygcollect.ForwardingCollection, self).isEmpty())

    @override
    @overload
    def removeFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.removeFirst()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).removeFirst())

    @override
    @overload
    def putFirst(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingDeque.putFirst(E) throws java.lang.InterruptedException"""
        super(_ForwardingBlockingDeque, self).putFirst(e)

    @overload
    def drainTo(self, c: 'Collection') -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingDeque.drainTo(java.util.Collection<? super E>)"""
        return int._wrap(super(_ForwardingBlockingDeque, self).drainTo(c))

    @override
    @overload
    def remove(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.remove()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).remove())

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
    def drainTo(self, c: 'Collection', maxElements: int) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingDeque.drainTo(java.util.Collection<? super E>,int)"""
        return int._wrap(super(_ForwardingBlockingDeque, self).drainTo(c, _int.valueOf(maxElements)))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.common.collect.ForwardingCollection.toArray()"""
        return List[object]._wrap(super(pygcollect.ForwardingCollection, self).toArray())

    @override
    @overload
    def peekFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.peekFirst()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).peekFirst())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def pop(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.pop()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).pop())

    @override
    @overload
    def poll(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.poll()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).poll())

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingCollection.clear()"""
        super(pygcollect.ForwardingCollection, self).clear()

    @overload
    def containsAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).containsAll(collection))

    @override
    @overload
    def put(self, e: object):
        """public void com.google.common.util.concurrent.ForwardingBlockingDeque.put(E) throws java.lang.InterruptedException"""
        super(_ForwardingBlockingDeque, self).put(e)

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def pollFirst(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.pollFirst(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object._wrap(super(_ForwardingBlockingDeque, self).pollFirst(_long.valueOf(timeout), unit))

    @override
    @overload
    def peek(self) -> object:
        """public E com.google.common.collect.ForwardingQueue.peek()"""
        return object._wrap(super(pygcollect.ForwardingQueue, self).peek())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def remove(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).remove(object))

    @override
    @overload
    def getFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.getFirst()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).getFirst())

    @override
    @overload
    def take(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.take() throws java.lang.InterruptedException"""
        return object._wrap(super(ForwardingBlockingDeque, self).take())

    @overload
    def add(self, element: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.add(E)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).add(element))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def offerLast(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingDeque.offerLast(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ForwardingBlockingDeque, self).offerLast(e, _long.valueOf(timeout), unit))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def peekLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.peekLast()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).peekLast())

    @override
    @overload
    def reversed(self) -> 'Deque':
        """public default java.util.Deque<E> java.util.Deque.reversed()"""
        return 'Deque'._wrap(super(Deque, self).reversed())

    @overload
    def removeLastOccurrence(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.removeLastOccurrence(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingDeque, self).removeLastOccurrence(o))

    @overload
    def contains(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).contains(object))

    @overload
    def addAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).addAll(collection))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingCollection.iterator()"""
        return 'Iterator'._wrap(super(pygcollect.ForwardingCollection, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def poll(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.poll(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object._wrap(super(_ForwardingBlockingDeque, self).poll(_long.valueOf(timeout), unit))

    @overload
    def pollLast(self, timeout: int, unit: 'TimeUnit') -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.pollLast(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return object._wrap(super(_ForwardingBlockingDeque, self).pollLast(_long.valueOf(timeout), unit))

    @overload
    def offerLast(self, e: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.offerLast(E)"""
        return bool._wrap(super(_pygcollect.ForwardingDeque, self).offerLast(e))

    @overload
    def removeAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).removeAll(collection))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def takeLast(self) -> object:
        """public E com.google.common.util.concurrent.ForwardingBlockingDeque.takeLast() throws java.lang.InterruptedException"""
        return object._wrap(super(ForwardingBlockingDeque, self).takeLast())

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingCollection.size()"""
        return int._wrap(super(pygcollect.ForwardingCollection, self).size())

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingDeque.descendingIterator()"""
        return 'Iterator'._wrap(super(pygcollect.ForwardingDeque, self).descendingIterator())

    @overload
    def toArray(self, array: 'Object') -> List[object]:
        """public <T> T[] com.google.common.collect.ForwardingCollection.toArray(T[])"""
        return List[object]._wrap(super(_pygcollect.ForwardingCollection, self).toArray(array))

    @override
    @overload
    def addLast(self, e: object):
        """public void com.google.common.collect.ForwardingDeque.addLast(E)"""
        super(_pygcollect.ForwardingDeque, self).addLast(e)

    @override
    @overload
    def getLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.getLast()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).getLast())

    @overload
    def offerFirst(self, e: object) -> bool:
        """public boolean com.google.common.collect.ForwardingDeque.offerFirst(E)"""
        return bool._wrap(super(_pygcollect.ForwardingDeque, self).offerFirst(e))

    @override
    @overload
    def pollLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.pollLast()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).pollLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def pollFirst(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.pollFirst()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).pollFirst())

    @overload
    def retainAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).retainAll(collection))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def offer(self, e: object, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingBlockingDeque.offer(E,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ForwardingBlockingDeque, self).offer(e, _long.valueOf(timeout), unit))

    @overload
    def offer(self, o: object) -> bool:
        """public boolean com.google.common.collect.ForwardingQueue.offer(E)"""
        return bool._wrap(super(_pygcollect.ForwardingQueue, self).offer(o))

    @override
    @overload
    def removeLast(self) -> object:
        """public E com.google.common.collect.ForwardingDeque.removeLast()"""
        return object._wrap(super(pygcollect.ForwardingDeque, self).removeLast())

    @override
    @overload
    def push(self, e: object):
        """public void com.google.common.collect.ForwardingDeque.push(E)"""
        super(_pygcollect.ForwardingDeque, self).push(e)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def remainingCapacity(self) -> int:
        """public int com.google.common.util.concurrent.ForwardingBlockingDeque.remainingCapacity()"""
        return int._wrap(super(ForwardingBlockingDeque, self).remainingCapacity()) 
 
 
# CLASS: com.google.common.util.concurrent.FakeTimeLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.util.concurrent.TimeLimiter as _TimeLimiter
_TimeLimiter = _TimeLimiter
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.FakeTimeLimiter as _FakeTimeLimiter
_FakeTimeLimiter = _FakeTimeLimiter
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FakeTimeLimiter():
    """com.google.common.util.concurrent.FakeTimeLimiter"""
 
    @staticmethod
    def _wrap(java_value: _FakeTimeLimiter) -> 'FakeTimeLimiter':
        return FakeTimeLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FakeTimeLimiter):
        """
        Dynamic initializer for FakeTimeLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FakeTimeLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FakeTimeLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.FakeTimeLimiter.newProxy(T,java.lang.Class<T>,long,java.util.concurrent.TimeUnit)"""
        return object._wrap(super(_FakeTimeLimiter, self).newProxy(target, interfaceType, _long.valueOf(timeoutDuration), timeoutUnit))

    @overload
    def callWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.FakeTimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_FakeTimeLimiter, self).callWithTimeout(callable, _long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.FakeTimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        super(_FakeTimeLimiter, self).runUninterruptiblyWithTimeout(runnable, _long.valueOf(timeoutDuration), timeoutUnit)

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_TimeLimiter, self).callUninterruptiblyWithTimeout(callable, timeout))

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.FakeTimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_FakeTimeLimiter, self).callUninterruptiblyWithTimeout(callable, _long.valueOf(timeoutDuration), timeoutUnit))

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
    def runWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.FakeTimeLimiter.runWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        super(_FakeTimeLimiter, self).runWithTimeout(runnable, _long.valueOf(timeoutDuration), timeoutUnit)

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.FakeTimeLimiter()"""
        val = _FakeTimeLimiter()
        self.__wrapper = val

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
    def runWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(_TimeLimiter, self).runWithTimeout(runnable, timeout)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_TimeLimiter, self).runUninterruptiblyWithTimeout(runnable, timeout)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def callWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_TimeLimiter, self).callWithTimeout(callable, timeout))

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,java.time.Duration)"""
        return object._wrap(super(_TimeLimiter, self).newProxy(target, interfaceType, timeout))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.FakeTimeLimiter()"""
        val = _FakeTimeLimiter()
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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ClosingCallable
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_ClosingCallable
_ClosingCallable = _ClosingFuture_ClosingCallable.ClosingCallable
from abc import abstractmethod, ABC
 
class ClosingCallable():
    """com.google.common.util.concurrent.ClosingFuture.ClosingCallable"""
 
    @staticmethod
    def _wrap(java_value: _ClosingCallable) -> 'ClosingCallable':
        return ClosingCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingCallable):
        """
        Dynamic initializer for ClosingCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, closer: 'DeferredCloser'):
        """public abstract V com.google.common.util.concurrent.ClosingFuture$ClosingCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner3$ClosingFunction3
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner3_ClosingFunction3
_ClosingFunction3 = _ClosingFuture_Combiner3_ClosingFunction3.Combiner3.ClosingFunction3
from abc import abstractmethod, ABC
 
class ClosingFunction3():
    """com.google.common.util.concurrent.ClosingFuture.Combiner3.ClosingFunction3"""
 
    @staticmethod
    def _wrap(java_value: _ClosingFunction3) -> 'ClosingFunction3':
        return ClosingFunction3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingFunction3):
        """
        Dynamic initializer for ClosingFunction3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingFunction3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingFunction3__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner3$ClosingFunction3.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.AsyncCallable
import com.google.common.util.concurrent.AsyncCallable as _AsyncCallable
_AsyncCallable = _AsyncCallable
from abc import abstractmethod, ABC
 
class AsyncCallable():
    """com.google.common.util.concurrent.AsyncCallable"""
 
    @staticmethod
    def _wrap(java_value: _AsyncCallable) -> 'AsyncCallable':
        return AsyncCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncCallable):
        """
        Dynamic initializer for AsyncCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, ):
        """public abstract com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.AsyncCallable.call() throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Service$Listener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.Service as _Service_Listener
_Listener = _Service_Listener.Listener
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Listener():
    """com.google.common.util.concurrent.Service.Listener"""
 
    @staticmethod
    def _wrap(java_value: _Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Listener):
        """
        Dynamic initializer for Listener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Listener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Listener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.Service$Listener()"""
        val = _Listener()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def stopping(self, from: 'State'):
        """public void com.google.common.util.concurrent.Service$Listener.stopping(com.google.common.util.concurrent.Service$State)"""
        super(_Listener, self).stopping(from)

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def failed(self, from: 'State', failure: 'Throwable'):
        """public void com.google.common.util.concurrent.Service$Listener.failed(com.google.common.util.concurrent.Service$State,java.lang.Throwable)"""
        super(_Listener, self).failed(from, failure)

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
    def terminated(self, from: 'State'):
        """public void com.google.common.util.concurrent.Service$Listener.terminated(com.google.common.util.concurrent.Service$State)"""
        super(_Listener, self).terminated(from)

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.Service$Listener()"""
        val = _Listener()
        self.__wrapper = val

    @overload
    def running(self):
        """public void com.google.common.util.concurrent.Service$Listener.running()"""
        super(Listener, self).running()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Peeker
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Peeker
_Peeker = _ClosingFuture_Peeker.Peeker
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Peeker():
    """com.google.common.util.concurrent.ClosingFuture.Peeker"""
 
    @staticmethod
    def _wrap(java_value: _Peeker) -> 'Peeker':
        return Peeker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Peeker):
        """
        Dynamic initializer for Peeker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Peeker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Peeker__wrapper":
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
    def getDone(self, closingFuture: 'ClosingFuture') -> object:
        """public final <D> D com.google.common.util.concurrent.ClosingFuture$Peeker.getDone(com.google.common.util.concurrent.ClosingFuture<D>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(_Peeker, self).getDone(closingFuture))

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
 
 
# CLASS: com.google.common.util.concurrent.Striped
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
from builtins import bool
import java.lang.Long as _long
import com.google.common.util.concurrent.Striped as _Striped
_Striped = _Striped
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Striped():
    """com.google.common.util.concurrent.Striped"""
 
    @staticmethod
    def _wrap(java_value: _Striped) -> 'Striped':
        return Striped(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Striped):
        """
        Dynamic initializer for Striped.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Striped__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Striped__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def bulkGet(self, keys: 'Iterable') -> 'Iterable':
        """public java.lang.Iterable<L> com.google.common.util.concurrent.Striped.bulkGet(java.lang.Iterable<?>)"""
        return 'Iterable'._wrap(super(_Striped, self).bulkGet(keys))

    @staticmethod
    @overload
    def lock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.Lock> com.google.common.util.concurrent.Striped.lock(int)"""
        return Striped._wrap(_Striped.lock(_int.valueOf(stripes)))

    @staticmethod
    @overload
    def lazyWeakLock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.Lock> com.google.common.util.concurrent.Striped.lazyWeakLock(int)"""
        return Striped._wrap(_Striped.lazyWeakLock(_int.valueOf(stripes)))

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

    @staticmethod
    @overload
    def lazyWeakSemaphore(stripes: int, permits: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.Semaphore> com.google.common.util.concurrent.Striped.lazyWeakSemaphore(int,int)"""
        return Striped._wrap(_Striped.lazyWeakSemaphore(_int.valueOf(stripes), _int.valueOf(permits)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def semaphore(stripes: int, permits: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.Semaphore> com.google.common.util.concurrent.Striped.semaphore(int,int)"""
        return Striped._wrap(_Striped.semaphore(_int.valueOf(stripes), _int.valueOf(permits)))

    @abstractmethod
    def getAt(self, index: int):
        """public abstract L com.google.common.util.concurrent.Striped.getAt(int)"""
        pass

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

    @abstractmethod
    def size(self, ):
        """public abstract int com.google.common.util.concurrent.Striped.size()"""
        pass

    @abstractmethod
    def get(self, key: object):
        """public abstract L com.google.common.util.concurrent.Striped.get(java.lang.Object)"""
        pass

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
    def readWriteLock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.ReadWriteLock> com.google.common.util.concurrent.Striped.readWriteLock(int)"""
        return Striped._wrap(_Striped.readWriteLock(_int.valueOf(stripes)))

    @staticmethod
    @overload
    def lazyWeakReadWriteLock(stripes: int) -> 'Striped':
        """public static com.google.common.util.concurrent.Striped<java.util.concurrent.locks.ReadWriteLock> com.google.common.util.concurrent.Striped.lazyWeakReadWriteLock(int)"""
        return Striped._wrap(_Striped.lazyWeakReadWriteLock(_int.valueOf(stripes)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner_CombiningCallable
_CombiningCallable = _ClosingFuture_Combiner_CombiningCallable.Combiner.CombiningCallable
from abc import abstractmethod, ABC
 
class CombiningCallable():
    """com.google.common.util.concurrent.ClosingFuture.Combiner.CombiningCallable"""
 
    @staticmethod
    def _wrap(java_value: _CombiningCallable) -> 'CombiningCallable':
        return CombiningCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CombiningCallable):
        """
        Dynamic initializer for CombiningCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CombiningCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CombiningCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, closer: 'DeferredCloser', peeker: 'Peeker'):
        """public abstract V com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,com.google.common.util.concurrent.ClosingFuture$Peeker) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ValueAndCloser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_ValueAndCloser
_ValueAndCloser = _ClosingFuture_ValueAndCloser.ValueAndCloser
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValueAndCloser():
    """com.google.common.util.concurrent.ClosingFuture.ValueAndCloser"""
 
    @staticmethod
    def _wrap(java_value: _ValueAndCloser) -> 'ValueAndCloser':
        return ValueAndCloser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueAndCloser):
        """
        Dynamic initializer for ValueAndCloser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueAndCloser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueAndCloser__wrapper":
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

    @overload
    def closeAsync(self):
        """public void com.google.common.util.concurrent.ClosingFuture$ValueAndCloser.closeAsync()"""
        super(ValueAndCloser, self).closeAsync()

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
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ClosingFuture$ValueAndCloser.get() throws java.util.concurrent.ExecutionException"""
        return object._wrap(super(ValueAndCloser, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$ValueAndCloserConsumer
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_ValueAndCloserConsumer
_ValueAndCloserConsumer = _ClosingFuture_ValueAndCloserConsumer.ValueAndCloserConsumer
from abc import abstractmethod, ABC
 
class ValueAndCloserConsumer():
    """com.google.common.util.concurrent.ClosingFuture.ValueAndCloserConsumer"""
 
    @staticmethod
    def _wrap(java_value: _ValueAndCloserConsumer) -> 'ValueAndCloserConsumer':
        return ValueAndCloserConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueAndCloserConsumer):
        """
        Dynamic initializer for ValueAndCloserConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueAndCloserConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueAndCloserConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, valueAndCloser: 'ValueAndCloser'):
        """public abstract void com.google.common.util.concurrent.ClosingFuture$ValueAndCloserConsumer.accept(com.google.common.util.concurrent.ClosingFuture$ValueAndCloser<V>)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner5
from builtins import str
from pyquantum_helper import override
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner5
_Combiner5 = _ClosingFuture_Combiner5.Combiner5
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner
_Combiner = _ClosingFuture_Combiner.Combiner
import java.lang.Integer as _int
from builtins import bool
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture
_ClosingFuture = _ClosingFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Combiner5():
    """com.google.common.util.concurrent.ClosingFuture.Combiner5"""
 
    @staticmethod
    def _wrap(java_value: _Combiner5) -> 'Combiner5':
        return Combiner5(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Combiner5):
        """
        Dynamic initializer for Combiner5.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Combiner5__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Combiner5__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def call(self, function: 'ClosingFunction5', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner5.call(com.google.common.util.concurrent.ClosingFuture$Combiner5$ClosingFunction5<V1, V2, V3, V4, V5, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner5, self).call(function, executor))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).callAsync(combiningCallable, executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).call(combiningCallable, executor))

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

    @overload
    def callAsync(self, function: 'AsyncClosingFunction5', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner5.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner5$AsyncClosingFunction5<V1, V2, V3, V4, V5, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner5, self).callAsync(function, executor))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.SimpleTimeLimiter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.util.concurrent.TimeLimiter as _TimeLimiter
_TimeLimiter = _TimeLimiter
import java.lang.Runnable as Runnable
import java.util.concurrent.ExecutorService as ExecutorService
import java.time.Duration as Duration
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.util.concurrent.SimpleTimeLimiter as _SimpleTimeLimiter
_SimpleTimeLimiter = _SimpleTimeLimiter
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleTimeLimiter():
    """com.google.common.util.concurrent.SimpleTimeLimiter"""
 
    @staticmethod
    def _wrap(java_value: _SimpleTimeLimiter) -> 'SimpleTimeLimiter':
        return SimpleTimeLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleTimeLimiter):
        """
        Dynamic initializer for SimpleTimeLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleTimeLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleTimeLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.SimpleTimeLimiter.newProxy(T,java.lang.Class<T>,long,java.util.concurrent.TimeUnit)"""
        return object._wrap(super(_SimpleTimeLimiter, self).newProxy(target, interfaceType, _long.valueOf(timeoutDuration), timeoutUnit))

    @staticmethod
    @overload
    def create(executor: 'ExecutorService') -> 'SimpleTimeLimiter':
        """public static com.google.common.util.concurrent.SimpleTimeLimiter com.google.common.util.concurrent.SimpleTimeLimiter.create(java.util.concurrent.ExecutorService)"""
        return SimpleTimeLimiter._wrap(_SimpleTimeLimiter.create(executor))

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_TimeLimiter, self).callUninterruptiblyWithTimeout(callable, timeout))

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
    def callWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.SimpleTimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_SimpleTimeLimiter, self).callWithTimeout(callable, _long.valueOf(timeoutDuration), timeoutUnit))

    @override
    @overload
    def runWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.SimpleTimeLimiter.runWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(_SimpleTimeLimiter, self).runWithTimeout(runnable, _long.valueOf(timeoutDuration), timeoutUnit)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def runWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(_TimeLimiter, self).runWithTimeout(runnable, timeout)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.SimpleTimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_SimpleTimeLimiter, self).runUninterruptiblyWithTimeout(runnable, _long.valueOf(timeoutDuration), timeoutUnit)

    @override
    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_TimeLimiter, self).runUninterruptiblyWithTimeout(runnable, timeout)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def callWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_TimeLimiter, self).callWithTimeout(callable, timeout))

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,java.time.Duration)"""
        return object._wrap(super(_TimeLimiter, self).newProxy(target, interfaceType, timeout))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.SimpleTimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_SimpleTimeLimiter, self).callUninterruptiblyWithTimeout(callable, _long.valueOf(timeoutDuration), timeoutUnit))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.Service as _Service
_Service = _Service
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.AbstractScheduledService as _AbstractScheduledService
_AbstractScheduledService = _AbstractScheduledService
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import com.google.common.util.concurrent.Service as _Service_State
_State = _Service_State.State
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractScheduledService():
    """com.google.common.util.concurrent.AbstractScheduledService"""
 
    @staticmethod
    def _wrap(java_value: _AbstractScheduledService) -> 'AbstractScheduledService':
        return AbstractScheduledService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractScheduledService):
        """
        Dynamic initializer for AbstractScheduledService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractScheduledService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractScheduledService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractScheduledService.state()"""
        return 'State'._wrap(super(AbstractScheduledService, self).state())

    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractScheduledService, self).awaitRunning(_long.valueOf(timeout), unit)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractScheduledService.toString()"""
        return str._wrap(super(AbstractScheduledService, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(_AbstractScheduledService, self).addListener(listener, executor)

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractScheduledService, self).awaitRunning(timeout)

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractScheduledService.startAsync()"""
        return 'Service'._wrap(super(AbstractScheduledService, self).startAsync())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractScheduledService, self).awaitTerminated(timeout)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractScheduledService, self).awaitTerminated(_long.valueOf(timeout), unit)

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractScheduledService.awaitTerminated()"""
        super(AbstractScheduledService, self).awaitTerminated()

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractScheduledService.failureCause()"""
        return 'Throwable'._wrap(super(AbstractScheduledService, self).failureCause())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractScheduledService.isRunning()"""
        return bool._wrap(super(AbstractScheduledService, self).isRunning())

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractScheduledService.stopAsync()"""
        return 'Service'._wrap(super(AbstractScheduledService, self).stopAsync())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Future.State as State
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ForwardingFuture as _ForwardingFuture
_ForwardingFuture = _ForwardingFuture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class ForwardingFuture():
    """com.google.common.util.concurrent.ForwardingFuture"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingFuture) -> 'ForwardingFuture':
        return ForwardingFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingFuture):
        """
        Dynamic initializer for ForwardingFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ForwardingFuture, self).get(_long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool._wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool._wrap(super(ForwardingFuture, self).isDone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool._wrap(super(_ForwardingFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(ForwardingFuture, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ServiceManager$Listener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.ServiceManager as _ServiceManager_Listener
_Listener = _ServiceManager_Listener.Listener
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Listener():
    """com.google.common.util.concurrent.ServiceManager.Listener"""
 
    @staticmethod
    def _wrap(java_value: _Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Listener):
        """
        Dynamic initializer for Listener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Listener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Listener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def failure(self, service: 'Service'):
        """public void com.google.common.util.concurrent.ServiceManager$Listener.failure(com.google.common.util.concurrent.Service)"""
        super(_Listener, self).failure(service)

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.ServiceManager$Listener()"""
        val = _Listener()
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
    def healthy(self):
        """public void com.google.common.util.concurrent.ServiceManager$Listener.healthy()"""
        super(Listener, self).healthy()

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
    def stopped(self):
        """public void com.google.common.util.concurrent.ServiceManager$Listener.stopped()"""
        super(Listener, self).stopped()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.ServiceManager$Listener()"""
        val = _Listener()
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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner3
from builtins import str
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner3
_Combiner3 = _ClosingFuture_Combiner3.Combiner3
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner
_Combiner = _ClosingFuture_Combiner.Combiner
import java.lang.Integer as _int
from builtins import bool
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture
_ClosingFuture = _ClosingFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Combiner3():
    """com.google.common.util.concurrent.ClosingFuture.Combiner3"""
 
    @staticmethod
    def _wrap(java_value: _Combiner3) -> 'Combiner3':
        return Combiner3(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Combiner3):
        """
        Dynamic initializer for Combiner3.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Combiner3__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Combiner3__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def call(self, function: 'ClosingFunction3', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner3.call(com.google.common.util.concurrent.ClosingFuture$Combiner3$ClosingFunction3<V1, V2, V3, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner3, self).call(function, executor))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).callAsync(combiningCallable, executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).call(combiningCallable, executor))

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

    @overload
    def callAsync(self, function: 'AsyncClosingFunction3', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner3.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner3$AsyncClosingFunction3<V1, V2, V3, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner3, self).callAsync(function, executor))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AtomicLongMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.function.LongUnaryOperator as LongUnaryOperator
import java.util.function.LongBinaryOperator as LongBinaryOperator
from builtins import type
import com.google.common.util.concurrent.AtomicLongMap as _AtomicLongMap
_AtomicLongMap = _AtomicLongMap
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtomicLongMap():
    """com.google.common.util.concurrent.AtomicLongMap"""
 
    @staticmethod
    def _wrap(java_value: _AtomicLongMap) -> 'AtomicLongMap':
        return AtomicLongMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtomicLongMap):
        """
        Dynamic initializer for AtomicLongMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtomicLongMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtomicLongMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def clear(self):
        """public void com.google.common.util.concurrent.AtomicLongMap.clear()"""
        super(AtomicLongMap, self).clear()

    @overload
    def get(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.get(K)"""
        return int._wrap(super(_AtomicLongMap, self).get(key))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def decrementAndGet(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.decrementAndGet(K)"""
        return int._wrap(super(_AtomicLongMap, self).decrementAndGet(key))

    @overload
    def asMap(self) -> 'Map':
        """public java.util.Map<K, java.lang.Long> com.google.common.util.concurrent.AtomicLongMap.asMap()"""
        return 'Map'._wrap(super(AtomicLongMap, self).asMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getAndIncrement(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndIncrement(K)"""
        return int._wrap(super(_AtomicLongMap, self).getAndIncrement(key))

    @staticmethod
    @overload
    def create(m: 'Map') -> 'AtomicLongMap':
        """public static <K> com.google.common.util.concurrent.AtomicLongMap<K> com.google.common.util.concurrent.AtomicLongMap.create(java.util.Map<? extends K, ? extends java.lang.Long>)"""
        return AtomicLongMap._wrap(_AtomicLongMap.create(m))

    @overload
    def accumulateAndGet(self, key: object, x: int, accumulatorFunction: 'LongBinaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.accumulateAndGet(K,long,java.util.function.LongBinaryOperator)"""
        return int._wrap(super(_AtomicLongMap, self).accumulateAndGet(key, _long.valueOf(x), accumulatorFunction))

    @overload
    def put(self, key: object, newValue: int) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.put(K,long)"""
        return int._wrap(super(_AtomicLongMap, self).put(key, _long.valueOf(newValue)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def sum(self) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.sum()"""
        return int._wrap(super(AtomicLongMap, self).sum())

    @overload
    def addAndGet(self, key: object, delta: int) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.addAndGet(K,long)"""
        return int._wrap(super(_AtomicLongMap, self).addAndGet(key, _long.valueOf(delta)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAndDecrement(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndDecrement(K)"""
        return int._wrap(super(_AtomicLongMap, self).getAndDecrement(key))

    @overload
    def getAndAdd(self, key: object, delta: int) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndAdd(K,long)"""
        return int._wrap(super(_AtomicLongMap, self).getAndAdd(key, _long.valueOf(delta)))

    @overload
    def putAll(self, m: 'Map'):
        """public void com.google.common.util.concurrent.AtomicLongMap.putAll(java.util.Map<? extends K, ? extends java.lang.Long>)"""
        super(_AtomicLongMap, self).putAll(m)

    @overload
    def getAndUpdate(self, key: object, updaterFunction: 'LongUnaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndUpdate(K,java.util.function.LongUnaryOperator)"""
        return int._wrap(super(_AtomicLongMap, self).getAndUpdate(key, updaterFunction))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.util.concurrent.AtomicLongMap.isEmpty()"""
        return bool._wrap(super(AtomicLongMap, self).isEmpty())

    @overload
    def containsKey(self, key: object) -> bool:
        """public boolean com.google.common.util.concurrent.AtomicLongMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_AtomicLongMap, self).containsKey(key))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AtomicLongMap.toString()"""
        return str._wrap(super(AtomicLongMap, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def size(self) -> int:
        """public int com.google.common.util.concurrent.AtomicLongMap.size()"""
        return int._wrap(super(AtomicLongMap, self).size())

    @staticmethod
    @overload
    def create() -> 'AtomicLongMap':
        """public static <K> com.google.common.util.concurrent.AtomicLongMap<K> com.google.common.util.concurrent.AtomicLongMap.create()"""
        return AtomicLongMap._wrap(_AtomicLongMap.create())

    @overload
    def removeIfZero(self, key: object) -> bool:
        """public boolean com.google.common.util.concurrent.AtomicLongMap.removeIfZero(K)"""
        return bool._wrap(super(_AtomicLongMap, self).removeIfZero(key))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def incrementAndGet(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.incrementAndGet(K)"""
        return int._wrap(super(_AtomicLongMap, self).incrementAndGet(key))

    @overload
    def updateAndGet(self, key: object, updaterFunction: 'LongUnaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.updateAndGet(K,java.util.function.LongUnaryOperator)"""
        return int._wrap(super(_AtomicLongMap, self).updateAndGet(key, updaterFunction))

    @overload
    def remove(self, key: object) -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.remove(K)"""
        return int._wrap(super(_AtomicLongMap, self).remove(key))

    @overload
    def getAndAccumulate(self, key: object, x: int, accumulatorFunction: 'LongBinaryOperator') -> int:
        """public long com.google.common.util.concurrent.AtomicLongMap.getAndAccumulate(K,long,java.util.function.LongBinaryOperator)"""
        return int._wrap(super(_AtomicLongMap, self).getAndAccumulate(key, _long.valueOf(x), accumulatorFunction))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.Futures
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ImmutableList as _ImmutableList
_ImmutableList = _ImmutableList
import com.google.common.util.concurrent.Futures as _Futures_FutureCombiner
_FutureCombiner = _Futures_FutureCombiner.FutureCombiner
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
import java.util.concurrent.Callable as Callable
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.lang.Iterable as Iterable
import java.time.Duration as Duration
import com.google.common.util.concurrent.Futures as _Futures
_Futures = _Futures
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as Future
import java.lang.Throwable as Throwable
import java.lang.Long as _long
import java.util.concurrent.Future as _Future
_Future = _Future
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Futures():
    """com.google.common.util.concurrent.Futures"""
 
    @staticmethod
    def _wrap(java_value: _Futures) -> 'Futures':
        return Futures(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Futures):
        """
        Dynamic initializer for Futures.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Futures__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Futures__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lazyTransform(input: 'Future', function: 'Function') -> 'Future':
        """public static <I,O> java.util.concurrent.Future<O> com.google.common.util.concurrent.Futures.lazyTransform(java.util.concurrent.Future<I>,com.google.common.base.Function<? super I, ? extends O>)"""
        return Future._wrap(_Futures.lazyTransform(input, function))

    @staticmethod
    @overload
    def whenAllComplete(futures: 'Iterable') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllComplete(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return FutureCombiner._wrap(_Futures.whenAllComplete(futures))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def withTimeout(delegate: 'ListenableFuture', time: int, unit: 'TimeUnit', scheduledExecutor: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.withTimeout(com.google.common.util.concurrent.ListenableFuture<V>,long,java.util.concurrent.TimeUnit,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture._wrap(_Futures.withTimeout(delegate, _long.valueOf(time), unit, scheduledExecutor))

    @staticmethod
    @overload
    def immediateFuture(value: object) -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.immediateFuture(V)"""
        return ListenableFuture._wrap(_Futures.immediateFuture(value))

    @staticmethod
    @overload
    def inCompletionOrder(futures: 'Iterable') -> 'pygcollect.ImmutableList':
        """public static <T> com.google.common.collect.ImmutableList<com.google.common.util.concurrent.ListenableFuture<T>> com.google.common.util.concurrent.Futures.inCompletionOrder(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends T>>)"""
        return pygcollect.ImmutableList._wrap(_Futures.inCompletionOrder(futures))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def catching(input: 'ListenableFuture', exceptionType: 'Class', fallback: 'Function', executor: 'Executor') -> 'ListenableFuture':
        """public static <V,X extends java.lang.Throwable> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.catching(com.google.common.util.concurrent.ListenableFuture<? extends V>,java.lang.Class<X>,com.google.common.base.Function<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.catching(input, exceptionType, fallback, executor))

    @staticmethod
    @overload
    def submit(runnable: 'Runnable', executor: 'Executor') -> 'ListenableFuture':
        """public static com.google.common.util.concurrent.ListenableFuture<java.lang.Void> com.google.common.util.concurrent.Futures.submit(java.lang.Runnable,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.submit(runnable, executor))

    @staticmethod
    @overload
    def submitAsync(callable: 'AsyncCallable', executor: 'Executor') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.submitAsync(com.google.common.util.concurrent.AsyncCallable<O>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.submitAsync(callable, executor))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def transformAsync(input: 'ListenableFuture', function: 'AsyncFunction', executor: 'Executor') -> 'ListenableFuture':
        """public static <I,O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.transformAsync(com.google.common.util.concurrent.ListenableFuture<I>,com.google.common.util.concurrent.AsyncFunction<? super I, ? extends O>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.transformAsync(input, function, executor))

    @staticmethod
    @overload
    def immediateVoidFuture() -> 'ListenableFuture':
        """public static com.google.common.util.concurrent.ListenableFuture<java.lang.Void> com.google.common.util.concurrent.Futures.immediateVoidFuture()"""
        return ListenableFuture._wrap(_Futures.immediateVoidFuture())

    @staticmethod
    @overload
    def submit(callable: 'Callable', executor: 'Executor') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.submit(java.util.concurrent.Callable<O>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.submit(callable, executor))

    @staticmethod
    @overload
    def withTimeout(delegate: 'ListenableFuture', time: 'Duration', scheduledExecutor: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.withTimeout(com.google.common.util.concurrent.ListenableFuture<V>,java.time.Duration,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture._wrap(_Futures.withTimeout(delegate, time, scheduledExecutor))

    @staticmethod
    @overload
    def whenAllComplete(*futures: 'ListenableFuture') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllComplete(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return FutureCombiner._wrap(_Futures.whenAllComplete(futures))

    @staticmethod
    @overload
    def whenAllSucceed(futures: 'Iterable') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllSucceed(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return FutureCombiner._wrap(_Futures.whenAllSucceed(futures))

    @staticmethod
    @overload
    def allAsList(futures: 'Iterable') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.allAsList(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return ListenableFuture._wrap(_Futures.allAsList(futures))

    @staticmethod
    @overload
    def getChecked(future: 'Future', exceptionClass: 'Class') -> object:
        """public static <V,X extends java.lang.Exception> V com.google.common.util.concurrent.Futures.getChecked(java.util.concurrent.Future<V>,java.lang.Class<X>) throws X"""
        return object._wrap(_Futures.getChecked(future, exceptionClass))

    @staticmethod
    @overload
    def nonCancellationPropagating(future: 'ListenableFuture') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.nonCancellationPropagating(com.google.common.util.concurrent.ListenableFuture<V>)"""
        return ListenableFuture._wrap(_Futures.nonCancellationPropagating(future))

    @staticmethod
    @overload
    def addCallback(future: 'ListenableFuture', callback: 'FutureCallback', executor: 'Executor'):
        """public static <V> void com.google.common.util.concurrent.Futures.addCallback(com.google.common.util.concurrent.ListenableFuture<V>,com.google.common.util.concurrent.FutureCallback<? super V>,java.util.concurrent.Executor)"""
        _Futures.addCallback(future, callback, executor)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def successfulAsList(*futures: 'ListenableFuture') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.successfulAsList(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return ListenableFuture._wrap(_Futures.successfulAsList(futures))

    @staticmethod
    @overload
    def getDone(future: 'Future') -> object:
        """public static <V> V com.google.common.util.concurrent.Futures.getDone(java.util.concurrent.Future<V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(_Futures.getDone(future))

    @staticmethod
    @overload
    def transform(input: 'ListenableFuture', function: 'Function', executor: 'Executor') -> 'ListenableFuture':
        """public static <I,O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.transform(com.google.common.util.concurrent.ListenableFuture<I>,com.google.common.base.Function<? super I, ? extends O>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.transform(input, function, executor))

    @staticmethod
    @overload
    def immediateCancelledFuture() -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.immediateCancelledFuture()"""
        return ListenableFuture._wrap(_Futures.immediateCancelledFuture())

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

    @staticmethod
    @overload
    def scheduleAsync(callable: 'AsyncCallable', delay: int, timeUnit: 'TimeUnit', executorService: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.scheduleAsync(com.google.common.util.concurrent.AsyncCallable<O>,long,java.util.concurrent.TimeUnit,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture._wrap(_Futures.scheduleAsync(callable, _long.valueOf(delay), timeUnit, executorService))

    @staticmethod
    @overload
    def scheduleAsync(callable: 'AsyncCallable', delay: 'Duration', executorService: 'ScheduledExecutorService') -> 'ListenableFuture':
        """public static <O> com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.Futures.scheduleAsync(com.google.common.util.concurrent.AsyncCallable<O>,java.time.Duration,java.util.concurrent.ScheduledExecutorService)"""
        return ListenableFuture._wrap(_Futures.scheduleAsync(callable, delay, executorService))

    @staticmethod
    @overload
    def getChecked(future: 'Future', exceptionClass: 'Class', timeout: 'Duration') -> object:
        """public static <V,X extends java.lang.Exception> V com.google.common.util.concurrent.Futures.getChecked(java.util.concurrent.Future<V>,java.lang.Class<X>,java.time.Duration) throws X"""
        return object._wrap(_Futures.getChecked(future, exceptionClass, timeout))

    @staticmethod
    @overload
    def immediateFailedFuture(throwable: 'Throwable') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.immediateFailedFuture(java.lang.Throwable)"""
        return ListenableFuture._wrap(_Futures.immediateFailedFuture(throwable))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getUnchecked(future: 'Future') -> object:
        """public static <V> V com.google.common.util.concurrent.Futures.getUnchecked(java.util.concurrent.Future<V>)"""
        return object._wrap(_Futures.getUnchecked(future))

    @staticmethod
    @overload
    def catchingAsync(input: 'ListenableFuture', exceptionType: 'Class', fallback: 'AsyncFunction', executor: 'Executor') -> 'ListenableFuture':
        """public static <V,X extends java.lang.Throwable> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.Futures.catchingAsync(com.google.common.util.concurrent.ListenableFuture<? extends V>,java.lang.Class<X>,com.google.common.util.concurrent.AsyncFunction<? super X, ? extends V>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_Futures.catchingAsync(input, exceptionType, fallback, executor))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def whenAllSucceed(*futures: 'ListenableFuture') -> 'FutureCombiner':
        """public static <V> com.google.common.util.concurrent.Futures$FutureCombiner<V> com.google.common.util.concurrent.Futures.whenAllSucceed(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return FutureCombiner._wrap(_Futures.whenAllSucceed(futures))

    @staticmethod
    @overload
    def allAsList(*futures: 'ListenableFuture') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.allAsList(com.google.common.util.concurrent.ListenableFuture<? extends V>...)"""
        return ListenableFuture._wrap(_Futures.allAsList(futures))

    @staticmethod
    @overload
    def getChecked(future: 'Future', exceptionClass: 'Class', timeout: int, unit: 'TimeUnit') -> object:
        """public static <V,X extends java.lang.Exception> V com.google.common.util.concurrent.Futures.getChecked(java.util.concurrent.Future<V>,java.lang.Class<X>,long,java.util.concurrent.TimeUnit) throws X"""
        return object._wrap(_Futures.getChecked(future, exceptionClass, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def successfulAsList(futures: 'Iterable') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<java.util.List<V>> com.google.common.util.concurrent.Futures.successfulAsList(java.lang.Iterable<? extends com.google.common.util.concurrent.ListenableFuture<? extends V>>)"""
        return ListenableFuture._wrap(_Futures.successfulAsList(futures))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.Service
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.Service as _Service
_Service = _Service
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
 
class Service():
    """com.google.common.util.concurrent.Service"""
 
    @staticmethod
    def _wrap(java_value: _Service) -> 'Service':
        return Service(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Service):
        """
        Dynamic initializer for Service.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Service__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Service__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def stopAsync(self, ):
        """public abstract com.google.common.util.concurrent.Service com.google.common.util.concurrent.Service.stopAsync()"""
        pass

    @abstractmethod
    def failureCause(self, ):
        """public abstract java.lang.Throwable com.google.common.util.concurrent.Service.failureCause()"""
        pass

    @abstractmethod
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public abstract void com.google.common.util.concurrent.Service.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        pass

    @abstractmethod
    def state(self, ):
        """public abstract com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.Service.state()"""
        pass

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

    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.Service.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_Service, self).awaitTerminated(timeout)

    @abstractmethod
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public abstract void com.google.common.util.concurrent.Service.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        pass

    @abstractmethod
    def isRunning(self, ):
        """public abstract boolean com.google.common.util.concurrent.Service.isRunning()"""
        pass

    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.Service.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_Service, self).awaitRunning(timeout) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner_AsyncCombiningCallable
_AsyncCombiningCallable = _ClosingFuture_Combiner_AsyncCombiningCallable.Combiner.AsyncCombiningCallable
from abc import abstractmethod, ABC
 
class AsyncCombiningCallable():
    """com.google.common.util.concurrent.ClosingFuture.Combiner.AsyncCombiningCallable"""
 
    @staticmethod
    def _wrap(java_value: _AsyncCombiningCallable) -> 'AsyncCombiningCallable':
        return AsyncCombiningCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncCombiningCallable):
        """
        Dynamic initializer for AsyncCombiningCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncCombiningCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncCombiningCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, closer: 'DeferredCloser', peeker: 'Peeker'):
        """public abstract com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,com.google.common.util.concurrent.ClosingFuture$Peeker) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Runnables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.Runnables as _Runnables
_Runnables = _Runnables
import java.lang.Integer as _int
import java.lang.Runnable as _Runnable
_Runnable = _Runnable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Runnables():
    """com.google.common.util.concurrent.Runnables"""
 
    @staticmethod
    def _wrap(java_value: _Runnables) -> 'Runnables':
        return Runnables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Runnables):
        """
        Dynamic initializer for Runnables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Runnables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Runnables__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def doNothing() -> 'Runnable':
        """public static java.lang.Runnable com.google.common.util.concurrent.Runnables.doNothing()"""
        return Runnable._wrap(_Runnables.doNothing())

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
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler$Schedule
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.AbstractScheduledService as _AbstractScheduledService_CustomScheduler_Schedule
_Schedule = _AbstractScheduledService_CustomScheduler_Schedule.CustomScheduler.Schedule
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Schedule():
    """com.google.common.util.concurrent.AbstractScheduledService.CustomScheduler.Schedule"""
 
    @staticmethod
    def _wrap(java_value: _Schedule) -> 'Schedule':
        return Schedule(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Schedule):
        """
        Dynamic initializer for Schedule.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Schedule__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Schedule__wrapper":
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
    def __init__(self, delay: 'Duration'):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler$Schedule(java.time.Duration)"""
        val = _Schedule(delay)
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
    def __init__(self, delay: int, unit: 'TimeUnit'):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler$Schedule(long,java.util.concurrent.TimeUnit)"""
        val = _Schedule(_long.valueOf(delay), unit)
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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$AsyncClosingCallable
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_AsyncClosingCallable
_AsyncClosingCallable = _ClosingFuture_AsyncClosingCallable.AsyncClosingCallable
 
class AsyncClosingCallable():
    """com.google.common.util.concurrent.ClosingFuture.AsyncClosingCallable"""
 
    @staticmethod
    def _wrap(java_value: _AsyncClosingCallable) -> 'AsyncClosingCallable':
        return AsyncClosingCallable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncClosingCallable):
        """
        Dynamic initializer for AsyncClosingCallable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncClosingCallable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncClosingCallable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, closer: 'DeferredCloser'):
        """public abstract com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$AsyncClosingCallable.call(com.google.common.util.concurrent.ClosingFuture$DeferredCloser) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ServiceManager
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.ServiceManager as _ServiceManager
_ServiceManager = _ServiceManager
import java.lang.String as _String
_String = _String
import com.google.common.collect.ImmutableSetMultimap as _ImmutableSetMultimap
_ImmutableSetMultimap = _ImmutableSetMultimap
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Integer as _int
import com.google.common.collect.ImmutableMap as _ImmutableMap
_ImmutableMap = _ImmutableMap
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServiceManager():
    """com.google.common.util.concurrent.ServiceManager"""
 
    @staticmethod
    def _wrap(java_value: _ServiceManager) -> 'ServiceManager':
        return ServiceManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServiceManager):
        """
        Dynamic initializer for ServiceManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServiceManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServiceManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def servicesByState(self) -> 'pygcollect.ImmutableSetMultimap':
        """public com.google.common.collect.ImmutableSetMultimap<com.google.common.util.concurrent.Service$State, com.google.common.util.concurrent.Service> com.google.common.util.concurrent.ServiceManager.servicesByState()"""
        return 'pygcollect.ImmutableSetMultimap'._wrap(super(ServiceManager, self).servicesByState())

    @overload
    def awaitHealthy(self, timeout: 'Duration'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitHealthy(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_ServiceManager, self).awaitHealthy(timeout)

    @overload
    def isHealthy(self) -> bool:
        """public boolean com.google.common.util.concurrent.ServiceManager.isHealthy()"""
        return bool._wrap(super(ServiceManager, self).isHealthy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def startupDurations(self) -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<com.google.common.util.concurrent.Service, java.time.Duration> com.google.common.util.concurrent.ServiceManager.startupDurations()"""
        return 'pygcollect.ImmutableMap'._wrap(super(ServiceManager, self).startupDurations())

    @overload
    def __init__(self, services: 'Iterable'):
        """public com.google.common.util.concurrent.ServiceManager(java.lang.Iterable<? extends com.google.common.util.concurrent.Service>)"""
        val = _ServiceManager(services)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.ServiceManager.toString()"""
        return str._wrap(super(ServiceManager, self).toString())

    @overload
    def stopAsync(self) -> 'ServiceManager':
        """public com.google.common.util.concurrent.ServiceManager com.google.common.util.concurrent.ServiceManager.stopAsync()"""
        return 'ServiceManager'._wrap(super(ServiceManager, self).stopAsync())

    @overload
    def startupTimes(self) -> 'pygcollect.ImmutableMap':
        """public com.google.common.collect.ImmutableMap<com.google.common.util.concurrent.Service, java.lang.Long> com.google.common.util.concurrent.ServiceManager.startupTimes()"""
        return 'pygcollect.ImmutableMap'._wrap(super(ServiceManager, self).startupTimes())

    @overload
    def awaitStopped(self, timeout: 'Duration'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitStopped(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_ServiceManager, self).awaitStopped(timeout)

    @overload
    def startAsync(self) -> 'ServiceManager':
        """public com.google.common.util.concurrent.ServiceManager com.google.common.util.concurrent.ServiceManager.startAsync()"""
        return 'ServiceManager'._wrap(super(ServiceManager, self).startAsync())

    @overload
    def awaitStopped(self, timeout: int, unit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitStopped(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_ServiceManager, self).awaitStopped(_long.valueOf(timeout), unit)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public void com.google.common.util.concurrent.ServiceManager.addListener(com.google.common.util.concurrent.ServiceManager$Listener,java.util.concurrent.Executor)"""
        super(_ServiceManager, self).addListener(listener, executor)

    @overload
    def awaitHealthy(self):
        """public void com.google.common.util.concurrent.ServiceManager.awaitHealthy()"""
        super(ServiceManager, self).awaitHealthy()

    @overload
    def awaitHealthy(self, timeout: int, unit: 'TimeUnit'):
        """public void com.google.common.util.concurrent.ServiceManager.awaitHealthy(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_ServiceManager, self).awaitHealthy(_long.valueOf(timeout), unit)

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
    def awaitStopped(self):
        """public void com.google.common.util.concurrent.ServiceManager.awaitStopped()"""
        super(ServiceManager, self).awaitStopped()

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
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.AbstractScheduledService as _AbstractScheduledService_Scheduler
_Scheduler = _AbstractScheduledService_Scheduler.Scheduler
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
import com.google.common.util.concurrent.AbstractScheduledService as _AbstractScheduledService_CustomScheduler
_CustomScheduler = _AbstractScheduledService_CustomScheduler.CustomScheduler
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CustomScheduler():
    """com.google.common.util.concurrent.AbstractScheduledService.CustomScheduler"""
 
    @staticmethod
    def _wrap(java_value: _CustomScheduler) -> 'CustomScheduler':
        return CustomScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CustomScheduler):
        """
        Dynamic initializer for CustomScheduler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CustomScheduler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CustomScheduler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler()"""
        val = _CustomScheduler()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: int, delay: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler._wrap(_Scheduler.newFixedDelaySchedule(_long.valueOf(initialDelay), _long.valueOf(delay), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: 'Duration', period: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler._wrap(_Scheduler.newFixedRateSchedule(initialDelay, period))

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

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: int, period: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler._wrap(_Scheduler.newFixedRateSchedule(_long.valueOf(initialDelay), _long.valueOf(period), unit))

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: 'Duration', delay: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler._wrap(_Scheduler.newFixedDelaySchedule(initialDelay, delay))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.AbstractScheduledService$CustomScheduler()"""
        val = _CustomScheduler()
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
 
 
# CLASS: com.google.common.util.concurrent.AbstractFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.AbstractFuture as _AbstractFuture
_AbstractFuture = _AbstractFuture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class AbstractFuture():
    """com.google.common.util.concurrent.AbstractFuture"""
 
    @staticmethod
    def _wrap(java_value: _AbstractFuture) -> 'AbstractFuture':
        return AbstractFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractFuture):
        """
        Dynamic initializer for AbstractFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isDone()"""
        return bool._wrap(super(AbstractFuture, self).isDone())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.isCancelled()"""
        return bool._wrap(super(AbstractFuture, self).isCancelled())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.AbstractFuture.cancel(boolean)"""
        return bool._wrap(super(_AbstractFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public void com.google.common.util.concurrent.AbstractFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_AbstractFuture, self).addListener(listener, executor)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(AbstractFuture, self).get())

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.AbstractFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_AbstractFuture, self).get(_long.valueOf(timeout), unit))

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
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractFuture.toString()"""
        return str._wrap(super(AbstractFuture, self).toString())

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
 
 
# CLASS: com.google.common.util.concurrent.ListenableFutureTask
from builtins import str
from pyquantum_helper import override
import java.util.concurrent.FutureTask as _FutureTask
_FutureTask = _FutureTask
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.concurrent.Future.State as State
from builtins import type
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import com.google.common.util.concurrent.ListenableFutureTask as _ListenableFutureTask
_ListenableFutureTask = _ListenableFutureTask
import java.lang.Throwable as Throwable
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ListenableFutureTask():
    """com.google.common.util.concurrent.ListenableFutureTask"""
 
    @staticmethod
    def _wrap(java_value: _ListenableFutureTask) -> 'ListenableFutureTask':
        return ListenableFutureTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListenableFutureTask):
        """
        Dynamic initializer for ListenableFutureTask.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListenableFutureTask__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListenableFutureTask__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resultNow(self) -> object:
        """public V java.util.concurrent.FutureTask.resultNow()"""
        return object._wrap(super(FutureTask, self).resultNow())

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ListenableFutureTask.get(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ListenableFutureTask, self).get(_long.valueOf(timeout), unit))

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean java.util.concurrent.FutureTask.isDone()"""
        return bool._wrap(super(FutureTask, self).isDone())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean java.util.concurrent.FutureTask.isCancelled()"""
        return bool._wrap(super(FutureTask, self).isCancelled())

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
    def run(self):
        """public void java.util.concurrent.FutureTask.run()"""
        super(FutureTask, self).run()

    @staticmethod
    @overload
    def create(callable: 'Callable') -> 'ListenableFutureTask':
        """public static <V> com.google.common.util.concurrent.ListenableFutureTask<V> com.google.common.util.concurrent.ListenableFutureTask.create(java.util.concurrent.Callable<V>)"""
        return ListenableFutureTask._wrap(_ListenableFutureTask.create(callable))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.concurrent.FutureTask.toString()"""
        return str._wrap(super(FutureTask, self).toString())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public java.lang.Throwable java.util.concurrent.FutureTask.exceptionNow()"""
        return 'Throwable'._wrap(super(FutureTask, self).exceptionNow())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public java.util.concurrent.Future$State java.util.concurrent.FutureTask.state()"""
        return 'State.Future$State'._wrap(super(FutureTask, self).state())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def cancel(self, arg0: bool) -> bool:
        """public boolean java.util.concurrent.FutureTask.cancel(boolean)"""
        return bool._wrap(super(_FutureTask, self).cancel(_boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def get(self) -> object:
        """public V java.util.concurrent.FutureTask.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(FutureTask, self).get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addListener(self, listener: 'Runnable', exec: 'Executor'):
        """public void com.google.common.util.concurrent.ListenableFutureTask.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_ListenableFutureTask, self).addListener(listener, exec)

    @staticmethod
    @overload
    def create(runnable: 'Runnable', result: object) -> 'ListenableFutureTask':
        """public static <V> com.google.common.util.concurrent.ListenableFutureTask<V> com.google.common.util.concurrent.ListenableFutureTask.create(java.lang.Runnable,V)"""
        return ListenableFutureTask._wrap(_ListenableFutureTask.create(runnable, result))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner5$AsyncClosingFunction5
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner5_AsyncClosingFunction5
_AsyncClosingFunction5 = _ClosingFuture_Combiner5_AsyncClosingFunction5.Combiner5.AsyncClosingFunction5
from abc import abstractmethod, ABC
 
class AsyncClosingFunction5():
    """com.google.common.util.concurrent.ClosingFuture.Combiner5.AsyncClosingFunction5"""
 
    @staticmethod
    def _wrap(java_value: _AsyncClosingFunction5) -> 'AsyncClosingFunction5':
        return AsyncClosingFunction5(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncClosingFunction5):
        """
        Dynamic initializer for AsyncClosingFunction5.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncClosingFunction5__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncClosingFunction5__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object, value5: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner5$AsyncClosingFunction5.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4,V5) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.AbstractService
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.Service as _Service
_Service = _Service
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.AbstractService as _AbstractService
_AbstractService = _AbstractService
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import com.google.common.util.concurrent.Service as _Service_State
_State = _Service_State.State
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractService():
    """com.google.common.util.concurrent.AbstractService"""
 
    @staticmethod
    def _wrap(java_value: _AbstractService) -> 'AbstractService':
        return AbstractService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractService):
        """
        Dynamic initializer for AbstractService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractService, self).awaitRunning(_long.valueOf(timeout), unit)

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractService, self).awaitTerminated(_long.valueOf(timeout), unit)

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
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractService.stopAsync()"""
        return 'Service'._wrap(super(AbstractService, self).stopAsync())

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractService, self).awaitRunning(timeout)

    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractService.state()"""
        return 'State'._wrap(super(AbstractService, self).state())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractService.toString()"""
        return str._wrap(super(AbstractService, self).toString())

    @override
    @overload
    def awaitRunning(self):
        """public final void com.google.common.util.concurrent.AbstractService.awaitRunning()"""
        super(AbstractService, self).awaitRunning()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(_AbstractService, self).addListener(listener, executor)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractService.startAsync()"""
        return 'Service'._wrap(super(AbstractService, self).startAsync())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractService.failureCause()"""
        return 'Throwable'._wrap(super(AbstractService, self).failureCause())

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractService.awaitTerminated()"""
        super(AbstractService, self).awaitTerminated()

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractService, self).awaitTerminated(timeout)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractService.isRunning()"""
        return bool._wrap(super(AbstractService, self).isRunning())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.RateLimiter
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.RateLimiter as _RateLimiter
_RateLimiter = _RateLimiter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RateLimiter():
    """com.google.common.util.concurrent.RateLimiter"""
 
    @staticmethod
    def _wrap(java_value: _RateLimiter) -> 'RateLimiter':
        return RateLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RateLimiter):
        """
        Dynamic initializer for RateLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RateLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RateLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setRate(self, permitsPerSecond: float):
        """public final void com.google.common.util.concurrent.RateLimiter.setRate(double)"""
        super(_RateLimiter, self).setRate(_double.valueOf(permitsPerSecond))

    @overload
    def tryAcquire(self, permits: int, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(int,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(super(_RateLimiter, self).tryAcquire(_int.valueOf(permits), _long.valueOf(timeout), unit))

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
        """public java.lang.String com.google.common.util.concurrent.RateLimiter.toString()"""
        return str._wrap(super(RateLimiter, self).toString())

    @overload
    def tryAcquire(self, permits: int) -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(int)"""
        return bool._wrap(super(_RateLimiter, self).tryAcquire(_int.valueOf(permits)))

    @staticmethod
    @overload
    def create(permitsPerSecond: float, warmupPeriod: int, unit: 'TimeUnit') -> 'RateLimiter':
        """public static com.google.common.util.concurrent.RateLimiter com.google.common.util.concurrent.RateLimiter.create(double,long,java.util.concurrent.TimeUnit)"""
        return RateLimiter._wrap(_RateLimiter.create(_double.valueOf(permitsPerSecond), _long.valueOf(warmupPeriod), unit))

    @staticmethod
    @overload
    def create(permitsPerSecond: float, warmupPeriod: 'Duration') -> 'RateLimiter':
        """public static com.google.common.util.concurrent.RateLimiter com.google.common.util.concurrent.RateLimiter.create(double,java.time.Duration)"""
        return RateLimiter._wrap(_RateLimiter.create(_double.valueOf(permitsPerSecond), warmupPeriod))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def tryAcquire(self) -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire()"""
        return bool._wrap(super(RateLimiter, self).tryAcquire())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def tryAcquire(self, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(super(_RateLimiter, self).tryAcquire(_long.valueOf(timeout), unit))

    @overload
    def acquire(self) -> float:
        """public double com.google.common.util.concurrent.RateLimiter.acquire()"""
        return float._wrap(super(RateLimiter, self).acquire())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def acquire(self, permits: int) -> float:
        """public double com.google.common.util.concurrent.RateLimiter.acquire(int)"""
        return float._wrap(super(_RateLimiter, self).acquire(_int.valueOf(permits)))

    @overload
    def tryAcquire(self, timeout: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(java.time.Duration)"""
        return bool._wrap(super(_RateLimiter, self).tryAcquire(timeout))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRate(self) -> float:
        """public final double com.google.common.util.concurrent.RateLimiter.getRate()"""
        return float._wrap(super(RateLimiter, self).getRate())

    @staticmethod
    @overload
    def create(permitsPerSecond: float) -> 'RateLimiter':
        """public static com.google.common.util.concurrent.RateLimiter com.google.common.util.concurrent.RateLimiter.create(double)"""
        return RateLimiter._wrap(_RateLimiter.create(_double.valueOf(permitsPerSecond)))

    @overload
    def tryAcquire(self, permits: int, timeout: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.RateLimiter.tryAcquire(int,java.time.Duration)"""
        return bool._wrap(super(_RateLimiter, self).tryAcquire(_int.valueOf(permits), timeout))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.Monitor
import java.lang.Thread as Thread
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.time.Duration as Duration
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.Monitor as _Monitor_Guard
_Guard = _Monitor_Guard.Guard
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.google.common.util.concurrent.Monitor as _Monitor
_Monitor = _Monitor
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Monitor():
    """com.google.common.util.concurrent.Monitor"""
 
    @staticmethod
    def _wrap(java_value: _Monitor) -> 'Monitor':
        return Monitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Monitor):
        """
        Dynamic initializer for Monitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Monitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Monitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def waitFor(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitFor(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).waitFor(guard, _long.valueOf(time), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, fair: bool):
        """public com.google.common.util.concurrent.Monitor(boolean)"""
        val = _Monitor(_boolean.valueOf(fair))
        self.__wrapper = val

    @overload
    def enterIfInterruptibly(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIfInterruptibly(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterIfInterruptibly(guard, time))

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.Monitor()"""
        val = _Monitor()
        self.__wrapper = val

    @overload
    def enterIf(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIf(com.google.common.util.concurrent.Monitor$Guard)"""
        return bool._wrap(super(_Monitor, self).enterIf(guard))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def waitFor(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitFor(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).waitFor(guard, time))

    @overload
    def getQueueLength(self) -> int:
        """public int com.google.common.util.concurrent.Monitor.getQueueLength()"""
        return int._wrap(super(Monitor, self).getQueueLength())

    @overload
    def enterWhen(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhen(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterWhen(guard, _long.valueOf(time), unit))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def enterWhen(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhen(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterWhen(guard, time))

    @overload
    def getWaitQueueLength(self, guard: 'Guard') -> int:
        """public int com.google.common.util.concurrent.Monitor.getWaitQueueLength(com.google.common.util.concurrent.Monitor$Guard)"""
        return int._wrap(super(_Monitor, self).getWaitQueueLength(guard))

    @overload
    def enterWhen(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.enterWhen(com.google.common.util.concurrent.Monitor$Guard) throws java.lang.InterruptedException"""
        super(_Monitor, self).enterWhen(guard)

    @overload
    def enterInterruptibly(self, time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterInterruptibly(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterInterruptibly(_long.valueOf(time), unit))

    @overload
    def isOccupiedByCurrentThread(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.isOccupiedByCurrentThread()"""
        return bool._wrap(super(Monitor, self).isOccupiedByCurrentThread())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newGuard(self, isSatisfied: 'BooleanSupplier') -> 'Guard':
        """public com.google.common.util.concurrent.Monitor$Guard com.google.common.util.concurrent.Monitor.newGuard(java.util.function.BooleanSupplier)"""
        return 'Guard'._wrap(super(_Monitor, self).newGuard(isSatisfied))

    @overload
    def enterInterruptibly(self, time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterInterruptibly(java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterInterruptibly(time))

    @overload
    def leave(self):
        """public void com.google.common.util.concurrent.Monitor.leave()"""
        super(Monitor, self).leave()

    @overload
    def hasQueuedThread(self, thread: 'Thread') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.hasQueuedThread(java.lang.Thread)"""
        return bool._wrap(super(_Monitor, self).hasQueuedThread(thread))

    @overload
    def enterInterruptibly(self):
        """public void com.google.common.util.concurrent.Monitor.enterInterruptibly() throws java.lang.InterruptedException"""
        super(Monitor, self).enterInterruptibly()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def waitForUninterruptibly(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.waitForUninterruptibly(com.google.common.util.concurrent.Monitor$Guard)"""
        super(_Monitor, self).waitForUninterruptibly(guard)

    @overload
    def enterWhenUninterruptibly(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.enterWhenUninterruptibly(com.google.common.util.concurrent.Monitor$Guard)"""
        super(_Monitor, self).enterWhenUninterruptibly(guard)

    @overload
    def enter(self, time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enter(java.time.Duration)"""
        return bool._wrap(super(_Monitor, self).enter(time))

    @overload
    def enter(self, time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enter(long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(super(_Monitor, self).enter(_long.valueOf(time), unit))

    @overload
    def getOccupiedDepth(self) -> int:
        """public int com.google.common.util.concurrent.Monitor.getOccupiedDepth()"""
        return int._wrap(super(Monitor, self).getOccupiedDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.Monitor()"""
        val = _Monitor()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def tryEnterIf(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.tryEnterIf(com.google.common.util.concurrent.Monitor$Guard)"""
        return bool._wrap(super(_Monitor, self).tryEnterIf(guard))

    @overload
    def enterIfInterruptibly(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIfInterruptibly(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterIfInterruptibly(guard, _long.valueOf(time), unit))

    @overload
    def hasQueuedThreads(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.hasQueuedThreads()"""
        return bool._wrap(super(Monitor, self).hasQueuedThreads())

    @overload
    def isFair(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.isFair()"""
        return bool._wrap(super(Monitor, self).isFair())

    @overload
    def waitForUninterruptibly(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitForUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(super(_Monitor, self).waitForUninterruptibly(guard, _long.valueOf(time), unit))

    @overload
    def waitFor(self, guard: 'Guard'):
        """public void com.google.common.util.concurrent.Monitor.waitFor(com.google.common.util.concurrent.Monitor$Guard) throws java.lang.InterruptedException"""
        super(_Monitor, self).waitFor(guard)

    @overload
    def enter(self):
        """public void com.google.common.util.concurrent.Monitor.enter()"""
        super(Monitor, self).enter()

    @overload
    def tryEnter(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.tryEnter()"""
        return bool._wrap(super(Monitor, self).tryEnter())

    @overload
    def waitForUninterruptibly(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.waitForUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration)"""
        return bool._wrap(super(_Monitor, self).waitForUninterruptibly(guard, time))

    @overload
    def enterWhenUninterruptibly(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhenUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration)"""
        return bool._wrap(super(_Monitor, self).enterWhenUninterruptibly(guard, time))

    @overload
    def enterWhenUninterruptibly(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterWhenUninterruptibly(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(super(_Monitor, self).enterWhenUninterruptibly(guard, _long.valueOf(time), unit))

    @overload
    def hasWaiters(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.hasWaiters(com.google.common.util.concurrent.Monitor$Guard)"""
        return bool._wrap(super(_Monitor, self).hasWaiters(guard))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def enterIfInterruptibly(self, guard: 'Guard') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIfInterruptibly(com.google.common.util.concurrent.Monitor$Guard) throws java.lang.InterruptedException"""
        return bool._wrap(super(_Monitor, self).enterIfInterruptibly(guard))

    @overload
    def isOccupied(self) -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.isOccupied()"""
        return bool._wrap(super(Monitor, self).isOccupied())

    @overload
    def enterIf(self, guard: 'Guard', time: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIf(com.google.common.util.concurrent.Monitor$Guard,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(super(_Monitor, self).enterIf(guard, _long.valueOf(time), unit))

    @overload
    def enterIf(self, guard: 'Guard', time: 'Duration') -> bool:
        """public boolean com.google.common.util.concurrent.Monitor.enterIf(com.google.common.util.concurrent.Monitor$Guard,java.time.Duration)"""
        return bool._wrap(super(_Monitor, self).enterIf(guard, time))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass()) 
 
 
# CLASS: com.google.common.util.concurrent.Callables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.util.concurrent.Callables as _Callables
_Callables = _Callables
import java.util.concurrent.Callable as _Callable
_Callable = _Callable
import com.google.common.util.concurrent.AsyncCallable as _AsyncCallable
_AsyncCallable = _AsyncCallable
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Callables():
    """com.google.common.util.concurrent.Callables"""
 
    @staticmethod
    def _wrap(java_value: _Callables) -> 'Callables':
        return Callables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Callables):
        """
        Dynamic initializer for Callables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Callables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Callables__wrapper":
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

    @staticmethod
    @overload
    def returning(value: object) -> 'Callable':
        """public static <T> java.util.concurrent.Callable<T> com.google.common.util.concurrent.Callables.returning(T)"""
        return Callable._wrap(_Callables.returning(value))

    @staticmethod
    @overload
    def asAsyncCallable(callable: 'Callable', listeningExecutorService: 'ListeningExecutorService') -> 'AsyncCallable':
        """public static <T> com.google.common.util.concurrent.AsyncCallable<T> com.google.common.util.concurrent.Callables.asAsyncCallable(java.util.concurrent.Callable<T>,com.google.common.util.concurrent.ListeningExecutorService)"""
        return AsyncCallable._wrap(_Callables.asAsyncCallable(callable, listeningExecutorService))

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner4$ClosingFunction4
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner4_ClosingFunction4
_ClosingFunction4 = _ClosingFuture_Combiner4_ClosingFunction4.Combiner4.ClosingFunction4
from abc import abstractmethod, ABC
 
class ClosingFunction4():
    """com.google.common.util.concurrent.ClosingFuture.Combiner4.ClosingFunction4"""
 
    @staticmethod
    def _wrap(java_value: _ClosingFunction4) -> 'ClosingFunction4':
        return ClosingFunction4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClosingFunction4):
        """
        Dynamic initializer for ClosingFunction4.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClosingFunction4__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClosingFunction4__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object):
        """public abstract U com.google.common.util.concurrent.ClosingFuture$Combiner4$ClosingFunction4.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ListenableFuture
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from abc import abstractmethod, ABC
from builtins import object
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.util.concurrent.Future as _Future
_Future = _Future
 
class ListenableFuture():
    """com.google.common.util.concurrent.ListenableFuture"""
 
    @staticmethod
    def _wrap(java_value: _ListenableFuture) -> 'ListenableFuture':
        return ListenableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListenableFuture):
        """
        Dynamic initializer for ListenableFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListenableFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListenableFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

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
        return object._wrap(super(Future, self).resultNow())

    @abstractmethod
    def isDone(self, ):
        """public abstract boolean java.util.concurrent.Future.isDone()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.TimeLimiter
import java.lang.Object as _Object
_Object = _Object
import com.google.common.util.concurrent.TimeLimiter as _TimeLimiter
_TimeLimiter = _TimeLimiter
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import type
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.util.concurrent.Callable as Callable
from abc import abstractmethod, ABC
from builtins import object
 
class TimeLimiter():
    """com.google.common.util.concurrent.TimeLimiter"""
 
    @staticmethod
    def _wrap(java_value: _TimeLimiter) -> 'TimeLimiter':
        return TimeLimiter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeLimiter):
        """
        Dynamic initializer for TimeLimiter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeLimiter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeLimiter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def callWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_TimeLimiter, self).callWithTimeout(callable, timeout))

    @overload
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,java.time.Duration) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_TimeLimiter, self).callUninterruptiblyWithTimeout(callable, timeout))

    @overload
    def newProxy(self, target: object, interfaceType: 'Class', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,java.time.Duration)"""
        return object._wrap(super(_TimeLimiter, self).newProxy(target, interfaceType, timeout))

    @overload
    def runUninterruptiblyWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runUninterruptiblyWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_TimeLimiter, self).runUninterruptiblyWithTimeout(runnable, timeout)

    @overload
    def runWithTimeout(self, runnable: 'Runnable', timeout: 'Duration'):
        """public default void com.google.common.util.concurrent.TimeLimiter.runWithTimeout(java.lang.Runnable,java.time.Duration) throws java.util.concurrent.TimeoutException,java.lang.InterruptedException"""
        super(_TimeLimiter, self).runWithTimeout(runnable, timeout)

    @abstractmethod
    def callUninterruptiblyWithTimeout(self, callable: 'Callable', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract <T> T com.google.common.util.concurrent.TimeLimiter.callUninterruptiblyWithTimeout(java.util.concurrent.Callable<T>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException,java.util.concurrent.ExecutionException"""
        pass

    @abstractmethod
    def newProxy(self, target: object, interfaceType: 'Class', timeoutDuration: int, timeoutUnit: 'TimeUnit'):
        """public abstract <T> T com.google.common.util.concurrent.TimeLimiter.newProxy(T,java.lang.Class<T>,long,java.util.concurrent.TimeUnit)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.UncheckedExecutionException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import com.google.common.util.concurrent.UncheckedExecutionException as _UncheckedExecutionException
_UncheckedExecutionException = _UncheckedExecutionException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedExecutionException():
    """com.google.common.util.concurrent.UncheckedExecutionException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedExecutionException) -> 'UncheckedExecutionException':
        return UncheckedExecutionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedExecutionException):
        """
        Dynamic initializer for UncheckedExecutionException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedExecutionException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedExecutionException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedExecutionException(java.lang.String,java.lang.Throwable)"""
        val = _UncheckedExecutionException(message, cause)
        self.__wrapper = val

    @overload
    def __init__(self, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedExecutionException(java.lang.Throwable)"""
        val = _UncheckedExecutionException(cause)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$Policies
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_Policies
_Policies = _CycleDetectingLockFactory_Policies.Policies
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_Policy
_Policy = _CycleDetectingLockFactory_Policy.Policy
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Policies():
    """com.google.common.util.concurrent.CycleDetectingLockFactory.Policies"""
 
    @staticmethod
    def _wrap(java_value: _Policies) -> 'Policies':
        return Policies(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Policies):
        """
        Dynamic initializer for Policies.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Policies__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Policies__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def values() -> List['Policies']:
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory$Policies[] com.google.common.util.concurrent.CycleDetectingLockFactory$Policies.values()"""
        return List[Policies]._wrap(_Policies.values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Policies':
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory$Policies com.google.common.util.concurrent.CycleDetectingLockFactory$Policies.valueOf(java.lang.String)"""
        return Policies._wrap(_Policies.valueOf(name))

    @abstractmethod
    def handlePotentialDeadlock(self, exception: 'PotentialDeadlockException'):
        """public abstract void com.google.common.util.concurrent.CycleDetectingLockFactory$Policy.handlePotentialDeadlock(com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException)"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_AsyncClosingFunction
_AsyncClosingFunction = _ClosingFuture_AsyncClosingFunction.AsyncClosingFunction
 
class AsyncClosingFunction():
    """com.google.common.util.concurrent.ClosingFuture.AsyncClosingFunction"""
 
    @staticmethod
    def _wrap(java_value: _AsyncClosingFunction) -> 'AsyncClosingFunction':
        return AsyncClosingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncClosingFunction):
        """
        Dynamic initializer for AsyncClosingFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncClosingFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncClosingFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', input: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$AsyncClosingFunction.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,T) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingExecutorService
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.lang.Runnable as Runnable
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.Future as Future
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
import com.google.common.util.concurrent.ForwardingExecutorService as _ForwardingExecutorService
_ForwardingExecutorService = _ForwardingExecutorService
import java.util.concurrent.Future as _Future
_Future = _Future
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ForwardingExecutorService():
    """com.google.common.util.concurrent.ForwardingExecutorService"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingExecutorService) -> 'ForwardingExecutorService':
        return ForwardingExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingExecutorService):
        """
        Dynamic initializer for ForwardingExecutorService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingExecutorService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingExecutorService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invokeAll(self, tasks: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ForwardingExecutorService, self).invokeAll(tasks))

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> com.google.common.util.concurrent.ForwardingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(ForwardingExecutorService, self).shutdownNow())

    @overload
    def submit(self, task: 'Callable') -> 'Future':
        """public <T> java.util.concurrent.Future<T> com.google.common.util.concurrent.ForwardingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'Future'._wrap(super(_ForwardingExecutorService, self).submit(task))

    @overload
    def submit(self, task: 'Runnable', result: object) -> 'Future':
        """public <T> java.util.concurrent.Future<T> com.google.common.util.concurrent.ForwardingExecutorService.submit(java.lang.Runnable,T)"""
        return 'Future'._wrap(super(_ForwardingExecutorService, self).submit(task, result))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ForwardingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ForwardingExecutorService, self).invokeAll(tasks, _long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def shutdown(self):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.shutdown()"""
        super(ForwardingExecutorService, self).shutdown()

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isShutdown()"""
        return bool._wrap(super(ForwardingExecutorService, self).isShutdown())

    @overload
    def invokeAny(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ForwardingExecutorService, self).invokeAny(tasks, _long.valueOf(timeout), unit))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def submit(self, task: 'Runnable') -> 'Future':
        """public java.util.concurrent.Future<?> com.google.common.util.concurrent.ForwardingExecutorService.submit(java.lang.Runnable)"""
        return 'Future'._wrap(super(_ForwardingExecutorService, self).submit(task))

    @override
    @overload
    def execute(self, command: 'Runnable'):
        """public void com.google.common.util.concurrent.ForwardingExecutorService.execute(java.lang.Runnable)"""
        super(_ForwardingExecutorService, self).execute(command)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.isTerminated()"""
        return bool._wrap(super(ForwardingExecutorService, self).isTerminated())

    @override
    @overload
    def close(self):
        """public default void java.util.concurrent.ExecutorService.close()"""
        super(ExecutorService, self).close()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def invokeAny(self, tasks: 'Collection') -> object:
        """public <T> T com.google.common.util.concurrent.ForwardingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_ForwardingExecutorService, self).invokeAny(tasks))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def awaitTermination(self, timeout: int, unit: 'TimeUnit') -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ForwardingExecutorService, self).awaitTermination(_long.valueOf(timeout), unit))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractExecutionThreadService
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.Service as _Service
_Service = _Service
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import com.google.common.util.concurrent.AbstractExecutionThreadService as _AbstractExecutionThreadService
_AbstractExecutionThreadService = _AbstractExecutionThreadService
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import com.google.common.util.concurrent.Service as _Service_State
_State = _Service_State.State
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractExecutionThreadService():
    """com.google.common.util.concurrent.AbstractExecutionThreadService"""
 
    @staticmethod
    def _wrap(java_value: _AbstractExecutionThreadService) -> 'AbstractExecutionThreadService':
        return AbstractExecutionThreadService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractExecutionThreadService):
        """
        Dynamic initializer for AbstractExecutionThreadService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractExecutionThreadService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractExecutionThreadService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractExecutionThreadService.state()"""
        return 'State'._wrap(super(AbstractExecutionThreadService, self).state())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractExecutionThreadService.isRunning()"""
        return bool._wrap(super(AbstractExecutionThreadService, self).isRunning())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def awaitRunning(self):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitRunning()"""
        super(AbstractExecutionThreadService, self).awaitRunning()

    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(_AbstractExecutionThreadService, self).addListener(listener, executor)

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractExecutionThreadService, self).awaitRunning(timeout)

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitTerminated()"""
        super(AbstractExecutionThreadService, self).awaitTerminated()

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractExecutionThreadService.startAsync()"""
        return 'Service'._wrap(super(AbstractExecutionThreadService, self).startAsync())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractExecutionThreadService, self).awaitTerminated(timeout)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractExecutionThreadService.failureCause()"""
        return 'Throwable'._wrap(super(AbstractExecutionThreadService, self).failureCause())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractExecutionThreadService.stopAsync()"""
        return 'Service'._wrap(super(AbstractExecutionThreadService, self).stopAsync())

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractExecutionThreadService, self).awaitTerminated(_long.valueOf(timeout), unit)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractExecutionThreadService.toString()"""
        return str._wrap(super(AbstractExecutionThreadService, self).toString())

    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractExecutionThreadService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractExecutionThreadService, self).awaitRunning(_long.valueOf(timeout), unit)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.UncaughtExceptionHandlers
import com.google.common.util.concurrent.UncaughtExceptionHandlers as _UncaughtExceptionHandlers
_UncaughtExceptionHandlers = _UncaughtExceptionHandlers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.Thread as _Thread_UncaughtExceptionHandler
_UncaughtExceptionHandler = _Thread_UncaughtExceptionHandler.UncaughtExceptionHandler
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncaughtExceptionHandlers():
    """com.google.common.util.concurrent.UncaughtExceptionHandlers"""
 
    @staticmethod
    def _wrap(java_value: _UncaughtExceptionHandlers) -> 'UncaughtExceptionHandlers':
        return UncaughtExceptionHandlers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncaughtExceptionHandlers):
        """
        Dynamic initializer for UncaughtExceptionHandlers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncaughtExceptionHandlers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncaughtExceptionHandlers__wrapper":
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def systemExit() -> 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler':
        """public static java.lang.Thread$UncaughtExceptionHandler com.google.common.util.concurrent.UncaughtExceptionHandlers.systemExit()"""
        return UncaughtExceptionHandler.Thread$UncaughtExceptionHandler._wrap(_UncaughtExceptionHandlers.systemExit())

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
 
 
# CLASS: com.google.common.util.concurrent.FutureCallback
import com.google.common.util.concurrent.FutureCallback as _FutureCallback
_FutureCallback = _FutureCallback
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class FutureCallback():
    """com.google.common.util.concurrent.FutureCallback"""
 
    @staticmethod
    def _wrap(java_value: _FutureCallback) -> 'FutureCallback':
        return FutureCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FutureCallback):
        """
        Dynamic initializer for FutureCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FutureCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FutureCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.util.concurrent.Futures$FutureCombiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.Futures as _Futures_FutureCombiner
_FutureCombiner = _Futures_FutureCombiner.FutureCombiner
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FutureCombiner():
    """com.google.common.util.concurrent.Futures.FutureCombiner"""
 
    @staticmethod
    def _wrap(java_value: _FutureCombiner) -> 'FutureCombiner':
        return FutureCombiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FutureCombiner):
        """
        Dynamic initializer for FutureCombiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FutureCombiner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FutureCombiner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def run(self, combiner: 'Runnable', executor: 'Executor') -> 'ListenableFuture':
        """public com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.Futures$FutureCombiner.run(java.lang.Runnable,java.util.concurrent.Executor)"""
        return 'ListenableFuture'._wrap(super(_FutureCombiner, self).run(combiner, executor))

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
    def call(self, combiner: 'Callable', executor: 'Executor') -> 'ListenableFuture':
        """public <C> com.google.common.util.concurrent.ListenableFuture<C> com.google.common.util.concurrent.Futures$FutureCombiner.call(java.util.concurrent.Callable<C>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'._wrap(super(_FutureCombiner, self).call(combiner, executor))

    @overload
    def callAsync(self, combiner: 'AsyncCallable', executor: 'Executor') -> 'ListenableFuture':
        """public <C> com.google.common.util.concurrent.ListenableFuture<C> com.google.common.util.concurrent.Futures$FutureCombiner.callAsync(com.google.common.util.concurrent.AsyncCallable<C>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'._wrap(super(_FutureCombiner, self).callAsync(combiner, executor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner4
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner4
_Combiner4 = _ClosingFuture_Combiner4.Combiner4
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner
_Combiner = _ClosingFuture_Combiner.Combiner
import java.lang.Integer as _int
from builtins import bool
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture
_ClosingFuture = _ClosingFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Combiner4():
    """com.google.common.util.concurrent.ClosingFuture.Combiner4"""
 
    @staticmethod
    def _wrap(java_value: _Combiner4) -> 'Combiner4':
        return Combiner4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Combiner4):
        """
        Dynamic initializer for Combiner4.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Combiner4__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Combiner4__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).callAsync(combiningCallable, executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).call(combiningCallable, executor))

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
    def callAsync(self, function: 'AsyncClosingFunction4', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner4.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner4$AsyncClosingFunction4<V1, V2, V3, V4, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner4, self).callAsync(function, executor))

    @overload
    def call(self, function: 'ClosingFunction4', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner4.call(com.google.common.util.concurrent.ClosingFuture$Combiner4$ClosingFunction4<V1, V2, V3, V4, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner4, self).call(function, executor))

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
 
 
# CLASS: com.google.common.util.concurrent.ExecutionError
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Error as Error
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import com.google.common.util.concurrent.ExecutionError as _ExecutionError
_ExecutionError = _ExecutionError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExecutionError():
    """com.google.common.util.concurrent.ExecutionError"""
 
    @staticmethod
    def _wrap(java_value: _ExecutionError) -> 'ExecutionError':
        return ExecutionError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExecutionError):
        """
        Dynamic initializer for ExecutionError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExecutionError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExecutionError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self, cause: 'Error'):
        """public com.google.common.util.concurrent.ExecutionError(java.lang.Error)"""
        val = _ExecutionError(cause)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, message: str, cause: 'Error'):
        """public com.google.common.util.concurrent.ExecutionError(java.lang.String,java.lang.Error)"""
        val = _ExecutionError(message, cause)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ForwardingListenableFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Future.State as State
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ForwardingFuture as _ForwardingFuture
_ForwardingFuture = _ForwardingFuture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.ForwardingListenableFuture as _ForwardingListenableFuture
_ForwardingListenableFuture = _ForwardingListenableFuture
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class ForwardingListenableFuture():
    """com.google.common.util.concurrent.ForwardingListenableFuture"""
 
    @staticmethod
    def _wrap(java_value: _ForwardingListenableFuture) -> 'ForwardingListenableFuture':
        return ForwardingListenableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ForwardingListenableFuture):
        """
        Dynamic initializer for ForwardingListenableFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ForwardingListenableFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ForwardingListenableFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addListener(self, listener: 'Runnable', exec: 'Executor'):
        """public void com.google.common.util.concurrent.ForwardingListenableFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_ForwardingListenableFuture, self).addListener(listener, exec)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ForwardingFuture, self).get(_long.valueOf(timeout), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isCancelled()"""
        return bool._wrap(super(ForwardingFuture, self).isCancelled())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isDone(self) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.isDone()"""
        return bool._wrap(super(ForwardingFuture, self).isDone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public boolean com.google.common.util.concurrent.ForwardingFuture.cancel(boolean)"""
        return bool._wrap(super(_ForwardingFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public V com.google.common.util.concurrent.ForwardingFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(ForwardingFuture, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.SettableFuture
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Future.State as State
import java.lang.Runnable as Runnable
import java.util.concurrent.Executor as Executor
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.SettableFuture as _SettableFuture
_SettableFuture = _SettableFuture
import com.google.common.util.concurrent.AbstractFuture as _AbstractFuture
_AbstractFuture = _AbstractFuture
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import com.google.common.util.concurrent.AbstractFuture as _AbstractFuture_TrustedFuture
_TrustedFuture = _AbstractFuture_TrustedFuture.TrustedFuture
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.concurrent.Future as _Future
_Future = _Future
 
class SettableFuture():
    """com.google.common.util.concurrent.SettableFuture"""
 
    @staticmethod
    def _wrap(java_value: _SettableFuture) -> 'SettableFuture':
        return SettableFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SettableFuture):
        """
        Dynamic initializer for SettableFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SettableFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SettableFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def get(self) -> object:
        """public final V com.google.common.util.concurrent.AbstractFuture$TrustedFuture.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(TrustedFuture, self).get())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, value: object) -> bool:
        """public boolean com.google.common.util.concurrent.SettableFuture.set(V)"""
        return bool._wrap(super(_SettableFuture, self).set(value))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractFuture$TrustedFuture.isCancelled()"""
        return bool._wrap(super(TrustedFuture, self).isCancelled())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @staticmethod
    @overload
    def create() -> 'SettableFuture':
        """public static <V> com.google.common.util.concurrent.SettableFuture<V> com.google.common.util.concurrent.SettableFuture.create()"""
        return SettableFuture._wrap(_SettableFuture.create())

    @overload
    def setFuture(self, future: 'ListenableFuture') -> bool:
        """public boolean com.google.common.util.concurrent.SettableFuture.setFuture(com.google.common.util.concurrent.ListenableFuture<? extends V>)"""
        return bool._wrap(super(_SettableFuture, self).setFuture(future))

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
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @overload
    def setException(self, throwable: 'Throwable') -> bool:
        """public boolean com.google.common.util.concurrent.SettableFuture.setException(java.lang.Throwable)"""
        return bool._wrap(super(_SettableFuture, self).setException(throwable))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self, timeout: int, unit: 'TimeUnit') -> object:
        """public final V com.google.common.util.concurrent.AbstractFuture$TrustedFuture.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_TrustedFuture, self).get(_long.valueOf(timeout), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractFuture.toString()"""
        return str._wrap(super(AbstractFuture, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractFuture$TrustedFuture.cancel(boolean)"""
        return bool._wrap(super(_TrustedFuture, self).cancel(_boolean.valueOf(mayInterruptIfRunning)))

    @override
    @overload
    def addListener(self, listener: 'Runnable', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractFuture$TrustedFuture.addListener(java.lang.Runnable,java.util.concurrent.Executor)"""
        super(_TrustedFuture, self).addListener(listener, executor)

    @override
    @overload
    def isDone(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractFuture$TrustedFuture.isDone()"""
        return bool._wrap(super(TrustedFuture, self).isDone())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ExecutionSequencer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.concurrent.Callable as Callable
import com.google.common.util.concurrent.ExecutionSequencer as _ExecutionSequencer
_ExecutionSequencer = _ExecutionSequencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExecutionSequencer():
    """com.google.common.util.concurrent.ExecutionSequencer"""
 
    @staticmethod
    def _wrap(java_value: _ExecutionSequencer) -> 'ExecutionSequencer':
        return ExecutionSequencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExecutionSequencer):
        """
        Dynamic initializer for ExecutionSequencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExecutionSequencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExecutionSequencer__wrapper":
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
    def submitAsync(self, callable: 'AsyncCallable', executor: 'Executor') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ExecutionSequencer.submitAsync(com.google.common.util.concurrent.AsyncCallable<T>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'._wrap(super(_ExecutionSequencer, self).submitAsync(callable, executor))

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

    @staticmethod
    @overload
    def create() -> 'ExecutionSequencer':
        """public static com.google.common.util.concurrent.ExecutionSequencer com.google.common.util.concurrent.ExecutionSequencer.create()"""
        return ExecutionSequencer._wrap(_ExecutionSequencer.create())

    @overload
    def submit(self, callable: 'Callable', executor: 'Executor') -> 'ListenableFuture':
        """public <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ExecutionSequencer.submit(java.util.concurrent.Callable<T>,java.util.concurrent.Executor)"""
        return 'ListenableFuture'._wrap(super(_ExecutionSequencer, self).submit(callable, executor))

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
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_ExampleStackTrace
_ExampleStackTrace = _CycleDetectingLockFactory_ExampleStackTrace.ExampleStackTrace
import java.lang.StackTraceElement as StackTraceElement
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_PotentialDeadlockException
_PotentialDeadlockException = _CycleDetectingLockFactory_PotentialDeadlockException.PotentialDeadlockException
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PotentialDeadlockException():
    """com.google.common.util.concurrent.CycleDetectingLockFactory.PotentialDeadlockException"""
 
    @staticmethod
    def _wrap(java_value: _PotentialDeadlockException) -> 'PotentialDeadlockException':
        return PotentialDeadlockException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PotentialDeadlockException):
        """
        Dynamic initializer for PotentialDeadlockException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PotentialDeadlockException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PotentialDeadlockException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def getConflictingStackTrace(self) -> 'ExampleStackTrace':
        """public com.google.common.util.concurrent.CycleDetectingLockFactory$ExampleStackTrace com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException.getConflictingStackTrace()"""
        return 'ExampleStackTrace'._wrap(super(PotentialDeadlockException, self).getConflictingStackTrace())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.CycleDetectingLockFactory$PotentialDeadlockException.getMessage()"""
        return str._wrap(super(PotentialDeadlockException, self).getMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner2
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner2
_Combiner2 = _ClosingFuture_Combiner2.Combiner2
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner
_Combiner = _ClosingFuture_Combiner.Combiner
import java.lang.Integer as _int
from builtins import bool
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture
_ClosingFuture = _ClosingFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Combiner2():
    """com.google.common.util.concurrent.ClosingFuture.Combiner2"""
 
    @staticmethod
    def _wrap(java_value: _Combiner2) -> 'Combiner2':
        return Combiner2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Combiner2):
        """
        Dynamic initializer for Combiner2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Combiner2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Combiner2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def callAsync(self, function: 'AsyncClosingFunction2', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner2.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner2$AsyncClosingFunction2<V1, V2, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner2, self).callAsync(function, executor))

    @overload
    def callAsync(self, combiningCallable: 'AsyncCombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.callAsync(com.google.common.util.concurrent.ClosingFuture$Combiner$AsyncCombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).callAsync(combiningCallable, executor))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def call(self, function: 'ClosingFunction2', executor: 'Executor') -> 'ClosingFuture':
        """public <U> com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner2.call(com.google.common.util.concurrent.ClosingFuture$Combiner2$ClosingFunction2<V1, V2, U>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner2, self).call(function, executor))

    @overload
    def call(self, combiningCallable: 'CombiningCallable', executor: 'Executor') -> 'ClosingFuture':
        """public <V> com.google.common.util.concurrent.ClosingFuture<V> com.google.common.util.concurrent.ClosingFuture$Combiner.call(com.google.common.util.concurrent.ClosingFuture$Combiner$CombiningCallable<V>,java.util.concurrent.Executor)"""
        return 'ClosingFuture'._wrap(super(_Combiner, self).call(combiningCallable, executor))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AtomicDouble
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.function.DoubleBinaryOperator as DoubleBinaryOperator
import java.lang.Integer as _int
import com.google.common.util.concurrent.AtomicDouble as _AtomicDouble
_AtomicDouble = _AtomicDouble
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.function.DoubleUnaryOperator as DoubleUnaryOperator
import java.lang.Class as _Class
_Class = _Class
 
class AtomicDouble():
    """com.google.common.util.concurrent.AtomicDouble"""
 
    @staticmethod
    def _wrap(java_value: _AtomicDouble) -> 'AtomicDouble':
        return AtomicDouble(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtomicDouble):
        """
        Dynamic initializer for AtomicDouble.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtomicDouble__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtomicDouble__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAndAdd(self, delta: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndAdd(double)"""
        return float._wrap(super(_AtomicDouble, self).getAndAdd(_double.valueOf(delta)))

    @overload
    def getAndAccumulate(self, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndAccumulate(double,java.util.function.DoubleBinaryOperator)"""
        return float._wrap(super(_AtomicDouble, self).getAndAccumulate(_double.valueOf(x), accumulatorFunction))

    @overload
    def getAndUpdate(self, updateFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndUpdate(java.util.function.DoubleUnaryOperator)"""
        return float._wrap(super(_AtomicDouble, self).getAndUpdate(updateFunction))

    @overload
    def accumulateAndGet(self, x: float, accumulatorFunction: 'DoubleBinaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.accumulateAndGet(double,java.util.function.DoubleBinaryOperator)"""
        return float._wrap(super(_AtomicDouble, self).accumulateAndGet(_double.valueOf(x), accumulatorFunction))

    @overload
    def lazySet(self, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDouble.lazySet(double)"""
        super(_AtomicDouble, self).lazySet(_double.valueOf(newValue))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AtomicDouble.toString()"""
        return str._wrap(super(AtomicDouble, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def updateAndGet(self, updateFunction: 'DoubleUnaryOperator') -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.updateAndGet(java.util.function.DoubleUnaryOperator)"""
        return float._wrap(super(_AtomicDouble, self).updateAndGet(updateFunction))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double com.google.common.util.concurrent.AtomicDouble.doubleValue()"""
        return float._wrap(super(AtomicDouble, self).doubleValue())

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
    def longValue(self) -> int:
        """public long com.google.common.util.concurrent.AtomicDouble.longValue()"""
        return int._wrap(super(AtomicDouble, self).longValue())

    @overload
    def addAndGet(self, delta: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.addAndGet(double)"""
        return float._wrap(super(_AtomicDouble, self).addAndGet(_double.valueOf(delta)))

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def floatValue(self) -> float:
        """public float com.google.common.util.concurrent.AtomicDouble.floatValue()"""
        return float._wrap(super(AtomicDouble, self).floatValue())

    @override
    @overload
    def intValue(self) -> int:
        """public int com.google.common.util.concurrent.AtomicDouble.intValue()"""
        return int._wrap(super(AtomicDouble, self).intValue())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getAndSet(self, newValue: float) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.getAndSet(double)"""
        return float._wrap(super(_AtomicDouble, self).getAndSet(_double.valueOf(newValue)))

    @overload
    def weakCompareAndSet(self, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDouble.weakCompareAndSet(double,double)"""
        return bool._wrap(super(_AtomicDouble, self).weakCompareAndSet(_double.valueOf(expect), _double.valueOf(update)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, initialValue: float):
        """public com.google.common.util.concurrent.AtomicDouble(double)"""
        val = _AtomicDouble(_double.valueOf(initialValue))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.AtomicDouble()"""
        val = _AtomicDouble()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.AtomicDouble()"""
        val = _AtomicDouble()
        self.__wrapper = val

    @overload
    def set(self, newValue: float):
        """public final void com.google.common.util.concurrent.AtomicDouble.set(double)"""
        super(_AtomicDouble, self).set(_double.valueOf(newValue))

    @overload
    def compareAndSet(self, expect: float, update: float) -> bool:
        """public final boolean com.google.common.util.concurrent.AtomicDouble.compareAndSet(double,double)"""
        return bool._wrap(super(_AtomicDouble, self).compareAndSet(_double.valueOf(expect), _double.valueOf(update)))

    @overload
    def get(self) -> float:
        """public final double com.google.common.util.concurrent.AtomicDouble.get()"""
        return float._wrap(super(AtomicDouble, self).get())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AbstractIdleService
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.Service as _Service
_Service = _Service
import java.time.Duration as Duration
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import com.google.common.util.concurrent.AbstractIdleService as _AbstractIdleService
_AbstractIdleService = _AbstractIdleService
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import com.google.common.util.concurrent.Service as _Service_State
_State = _Service_State.State
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractIdleService():
    """com.google.common.util.concurrent.AbstractIdleService"""
 
    @staticmethod
    def _wrap(java_value: _AbstractIdleService) -> 'AbstractIdleService':
        return AbstractIdleService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractIdleService):
        """
        Dynamic initializer for AbstractIdleService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractIdleService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractIdleService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addListener(self, listener: 'Listener', executor: 'Executor'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.addListener(com.google.common.util.concurrent.Service$Listener,java.util.concurrent.Executor)"""
        super(_AbstractIdleService, self).addListener(listener, executor)

    @override
    @overload
    def awaitTerminated(self):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitTerminated()"""
        super(AbstractIdleService, self).awaitTerminated()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isRunning(self) -> bool:
        """public final boolean com.google.common.util.concurrent.AbstractIdleService.isRunning()"""
        return bool._wrap(super(AbstractIdleService, self).isRunning())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def awaitRunning(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitRunning(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractIdleService, self).awaitRunning(timeout)

    @override
    @overload
    def stopAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractIdleService.stopAsync()"""
        return 'Service'._wrap(super(AbstractIdleService, self).stopAsync())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.util.concurrent.AbstractIdleService.toString()"""
        return str._wrap(super(AbstractIdleService, self).toString())

    @override
    @overload
    def state(self) -> 'State':
        """public final com.google.common.util.concurrent.Service$State com.google.common.util.concurrent.AbstractIdleService.state()"""
        return 'State'._wrap(super(AbstractIdleService, self).state())

    @override
    @overload
    def failureCause(self) -> 'Throwable':
        """public final java.lang.Throwable com.google.common.util.concurrent.AbstractIdleService.failureCause()"""
        return 'Throwable'._wrap(super(AbstractIdleService, self).failureCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def awaitTerminated(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitTerminated(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractIdleService, self).awaitTerminated(_long.valueOf(timeout), unit)

    @override
    @overload
    def awaitRunning(self, timeout: int, unit: 'TimeUnit'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitRunning(long,java.util.concurrent.TimeUnit) throws java.util.concurrent.TimeoutException"""
        super(_AbstractIdleService, self).awaitRunning(_long.valueOf(timeout), unit)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def startAsync(self) -> 'Service':
        """public final com.google.common.util.concurrent.Service com.google.common.util.concurrent.AbstractIdleService.startAsync()"""
        return 'Service'._wrap(super(AbstractIdleService, self).startAsync())

    @override
    @overload
    def awaitTerminated(self, timeout: 'Duration'):
        """public final void com.google.common.util.concurrent.AbstractIdleService.awaitTerminated(java.time.Duration) throws java.util.concurrent.TimeoutException"""
        super(_AbstractIdleService, self).awaitTerminated(timeout)

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
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering
import java.util.concurrent.locks.ReentrantLock as ReentrantLock
from builtins import str
import java.util.concurrent.locks.ReentrantReadWriteLock as ReentrantReadWriteLock
from pyquantum_helper import override
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory_WithExplicitOrdering
_WithExplicitOrdering = _CycleDetectingLockFactory_WithExplicitOrdering.WithExplicitOrdering
import java.util.concurrent.locks.ReentrantReadWriteLock as _ReentrantReadWriteLock
_ReentrantReadWriteLock = _ReentrantReadWriteLock
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.concurrent.locks.ReentrantLock as _ReentrantLock
_ReentrantLock = _ReentrantLock
import java.lang.String as _String
_String = _String
import java.lang.Enum as Enum
import java.lang.String as _string
import com.google.common.util.concurrent.CycleDetectingLockFactory as _CycleDetectingLockFactory
_CycleDetectingLockFactory = _CycleDetectingLockFactory
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WithExplicitOrdering():
    """com.google.common.util.concurrent.CycleDetectingLockFactory.WithExplicitOrdering"""
 
    @staticmethod
    def _wrap(java_value: _WithExplicitOrdering) -> 'WithExplicitOrdering':
        return WithExplicitOrdering(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WithExplicitOrdering):
        """
        Dynamic initializer for WithExplicitOrdering.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WithExplicitOrdering__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WithExplicitOrdering__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newInstanceWithExplicitOrdering(enumClass: 'Class', policy: 'Policy') -> 'WithExplicitOrdering':
        """public static <E extends java.lang.Enum<E>> com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering<E> com.google.common.util.concurrent.CycleDetectingLockFactory.newInstanceWithExplicitOrdering(java.lang.Class<E>,com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return WithExplicitOrdering._wrap(_CycleDetectingLockFactory.newInstanceWithExplicitOrdering(enumClass, policy))

    @overload
    def newReentrantLock(self, rank: 'Enum', fair: bool) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantLock(E,boolean)"""
        return 'ReentrantLock'._wrap(super(_WithExplicitOrdering, self).newReentrantLock(rank, _boolean.valueOf(fair)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newReentrantLock(self, rank: 'Enum') -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantLock(E)"""
        return 'ReentrantLock'._wrap(super(_WithExplicitOrdering, self).newReentrantLock(rank))

    @staticmethod
    @overload
    def newInstance(policy: 'Policy') -> 'CycleDetectingLockFactory':
        """public static com.google.common.util.concurrent.CycleDetectingLockFactory com.google.common.util.concurrent.CycleDetectingLockFactory.newInstance(com.google.common.util.concurrent.CycleDetectingLockFactory$Policy)"""
        return CycleDetectingLockFactory._wrap(_CycleDetectingLockFactory.newInstance(policy))

    @overload
    def newReentrantReadWriteLock(self, lockName: str) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String)"""
        return 'ReentrantReadWriteLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName))

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
    def newReentrantReadWriteLock(self, rank: 'Enum') -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantReadWriteLock(E)"""
        return 'ReentrantReadWriteLock'._wrap(super(_WithExplicitOrdering, self).newReentrantReadWriteLock(rank))

    @overload
    def newReentrantReadWriteLock(self, rank: 'Enum', fair: bool) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory$WithExplicitOrdering.newReentrantReadWriteLock(E,boolean)"""
        return 'ReentrantReadWriteLock'._wrap(super(_WithExplicitOrdering, self).newReentrantReadWriteLock(rank, _boolean.valueOf(fair)))

    @overload
    def newReentrantLock(self, lockName: str, fair: bool) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String,boolean)"""
        return 'ReentrantLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantLock(lockName, _boolean.valueOf(fair)))

    @overload
    def newReentrantReadWriteLock(self, lockName: str, fair: bool) -> 'ReentrantReadWriteLock':
        """public java.util.concurrent.locks.ReentrantReadWriteLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantReadWriteLock(java.lang.String,boolean)"""
        return 'ReentrantReadWriteLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantReadWriteLock(lockName, _boolean.valueOf(fair)))

    @overload
    def newReentrantLock(self, lockName: str) -> 'ReentrantLock':
        """public java.util.concurrent.locks.ReentrantLock com.google.common.util.concurrent.CycleDetectingLockFactory.newReentrantLock(java.lang.String)"""
        return 'ReentrantLock'._wrap(super(_CycleDetectingLockFactory, self).newReentrantLock(lockName))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.AsyncFunction
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.AsyncFunction as _AsyncFunction
_AsyncFunction = _AsyncFunction
 
class AsyncFunction():
    """com.google.common.util.concurrent.AsyncFunction"""
 
    @staticmethod
    def _wrap(java_value: _AsyncFunction) -> 'AsyncFunction':
        return AsyncFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncFunction):
        """
        Dynamic initializer for AsyncFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, input: object):
        """public abstract com.google.common.util.concurrent.ListenableFuture<O> com.google.common.util.concurrent.AsyncFunction.apply(I) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.AbstractScheduledService$Scheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.util.concurrent.AbstractScheduledService as _AbstractScheduledService_Scheduler
_Scheduler = _AbstractScheduledService_Scheduler.Scheduler
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Scheduler():
    """com.google.common.util.concurrent.AbstractScheduledService.Scheduler"""
 
    @staticmethod
    def _wrap(java_value: _Scheduler) -> 'Scheduler':
        return Scheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Scheduler):
        """
        Dynamic initializer for Scheduler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Scheduler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Scheduler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: int, delay: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler._wrap(_Scheduler.newFixedDelaySchedule(_long.valueOf(initialDelay), _long.valueOf(delay), unit))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: 'Duration', period: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler._wrap(_Scheduler.newFixedRateSchedule(initialDelay, period))

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

    @staticmethod
    @overload
    def newFixedRateSchedule(initialDelay: int, period: int, unit: 'TimeUnit') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedRateSchedule(long,long,java.util.concurrent.TimeUnit)"""
        return Scheduler._wrap(_Scheduler.newFixedRateSchedule(_long.valueOf(initialDelay), _long.valueOf(period), unit))

    @staticmethod
    @overload
    def newFixedDelaySchedule(initialDelay: 'Duration', delay: 'Duration') -> 'Scheduler':
        """public static com.google.common.util.concurrent.AbstractScheduledService$Scheduler com.google.common.util.concurrent.AbstractScheduledService$Scheduler.newFixedDelaySchedule(java.time.Duration,java.time.Duration)"""
        return Scheduler._wrap(_Scheduler.newFixedDelaySchedule(initialDelay, delay))

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
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner2$AsyncClosingFunction2
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner2_AsyncClosingFunction2
_AsyncClosingFunction2 = _ClosingFuture_Combiner2_AsyncClosingFunction2.Combiner2.AsyncClosingFunction2
from abc import abstractmethod, ABC
 
class AsyncClosingFunction2():
    """com.google.common.util.concurrent.ClosingFuture.Combiner2.AsyncClosingFunction2"""
 
    @staticmethod
    def _wrap(java_value: _AsyncClosingFunction2) -> 'AsyncClosingFunction2':
        return AsyncClosingFunction2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncClosingFunction2):
        """
        Dynamic initializer for AsyncClosingFunction2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncClosingFunction2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncClosingFunction2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner2$AsyncClosingFunction2.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.ListeningScheduledExecutorService
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Runnable as Runnable
import java.time.Duration as Duration
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
import com.google.common.util.concurrent.ListeningExecutorService as _ListeningExecutorService
_ListeningExecutorService = _ListeningExecutorService
import java.util.List as _List
_List = _List
import com.google.common.util.concurrent.ListeningScheduledExecutorService as _ListeningScheduledExecutorService
_ListeningScheduledExecutorService = _ListeningScheduledExecutorService
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import com.google.common.util.concurrent.ListenableScheduledFuture as _ListenableScheduledFuture
_ListenableScheduledFuture = _ListenableScheduledFuture
import java.util.concurrent.Executor as _Executor
_Executor = _Executor
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.util.List as List
 
class ListeningScheduledExecutorService():
    """com.google.common.util.concurrent.ListeningScheduledExecutorService"""
 
    @staticmethod
    def _wrap(java_value: _ListeningScheduledExecutorService) -> 'ListeningScheduledExecutorService':
        return ListeningScheduledExecutorService(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListeningScheduledExecutorService):
        """
        Dynamic initializer for ListeningScheduledExecutorService.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListeningScheduledExecutorService__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListeningScheduledExecutorService__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invokeAny(self, tasks: 'Collection', timeout: 'Duration') -> object:
        """public default <T> T com.google.common.util.concurrent.ListeningExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_ListeningExecutorService, self).invokeAny(tasks, timeout))

    @abstractmethod
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract boolean java.util.concurrent.ExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @abstractmethod
    def submit(self, task: 'Runnable', result: object):
        """public abstract <T> com.google.common.util.concurrent.ListenableFuture<T> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable,T)"""
        pass

    @overload
    def invokeAll(self, tasks: 'Collection', timeout: 'Duration') -> 'List':
        """public default <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,java.time.Duration) throws java.lang.InterruptedException"""
        return 'List'._wrap(super(_ListeningExecutorService, self).invokeAll(tasks, timeout))

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
    def schedule(self, callable: 'Callable', delay: int, unit: 'TimeUnit'):
        """public abstract <V> com.google.common.util.concurrent.ListenableScheduledFuture<V> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.util.concurrent.Callable<V>,long,java.util.concurrent.TimeUnit)"""
        pass

    @overload
    def scheduleAtFixedRate(self, command: 'Runnable', initialDelay: 'Duration', period: 'Duration') -> 'ListenableScheduledFuture':
        """public default com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.scheduleAtFixedRate(java.lang.Runnable,java.time.Duration,java.time.Duration)"""
        return 'ListenableScheduledFuture'._wrap(super(_ListeningScheduledExecutorService, self).scheduleAtFixedRate(command, initialDelay, period))

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

    @abstractmethod
    def isShutdown(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isShutdown()"""
        pass

    @abstractmethod
    def submit(self, task: 'Runnable'):
        """public abstract com.google.common.util.concurrent.ListenableFuture<?> com.google.common.util.concurrent.ListeningExecutorService.submit(java.lang.Runnable)"""
        pass

    @abstractmethod
    def shutdownNow(self, ):
        """public abstract java.util.List<java.lang.Runnable> java.util.concurrent.ExecutorService.shutdownNow()"""
        pass

    @overload
    def schedule(self, command: 'Runnable', delay: 'Duration') -> 'ListenableScheduledFuture':
        """public default com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.lang.Runnable,java.time.Duration)"""
        return 'ListenableScheduledFuture'._wrap(super(_ListeningScheduledExecutorService, self).schedule(command, delay))

    @abstractmethod
    def invokeAll(self, tasks: 'Collection', timeout: int, unit: 'TimeUnit'):
        """public abstract <T> java.util.List<java.util.concurrent.Future<T>> com.google.common.util.concurrent.ListeningExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        pass

    @overload
    def schedule(self, callable: 'Callable', delay: 'Duration') -> 'ListenableScheduledFuture':
        """public default <V> com.google.common.util.concurrent.ListenableScheduledFuture<V> com.google.common.util.concurrent.ListeningScheduledExecutorService.schedule(java.util.concurrent.Callable<V>,java.time.Duration)"""
        return 'ListenableScheduledFuture'._wrap(super(_ListeningScheduledExecutorService, self).schedule(callable, delay))

    @overload
    def scheduleWithFixedDelay(self, command: 'Runnable', initialDelay: 'Duration', delay: 'Duration') -> 'ListenableScheduledFuture':
        """public default com.google.common.util.concurrent.ListenableScheduledFuture<?> com.google.common.util.concurrent.ListeningScheduledExecutorService.scheduleWithFixedDelay(java.lang.Runnable,java.time.Duration,java.time.Duration)"""
        return 'ListenableScheduledFuture'._wrap(super(_ListeningScheduledExecutorService, self).scheduleWithFixedDelay(command, initialDelay, delay))

    @overload
    def awaitTermination(self, timeout: 'Duration') -> bool:
        """public default boolean com.google.common.util.concurrent.ListeningExecutorService.awaitTermination(java.time.Duration) throws java.lang.InterruptedException"""
        return bool._wrap(super(_ListeningExecutorService, self).awaitTermination(timeout))

    @abstractmethod
    def shutdown(self, ):
        """public abstract void java.util.concurrent.ExecutorService.shutdown()"""
        pass

    @abstractmethod
    def isTerminated(self, ):
        """public abstract boolean java.util.concurrent.ExecutorService.isTerminated()"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.UncheckedTimeoutException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import com.google.common.util.concurrent.UncheckedTimeoutException as _UncheckedTimeoutException
_UncheckedTimeoutException = _UncheckedTimeoutException
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedTimeoutException():
    """com.google.common.util.concurrent.UncheckedTimeoutException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedTimeoutException) -> 'UncheckedTimeoutException':
        return UncheckedTimeoutException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedTimeoutException):
        """
        Dynamic initializer for UncheckedTimeoutException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedTimeoutException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedTimeoutException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedTimeoutException(java.lang.Throwable)"""
        val = _UncheckedTimeoutException(cause)
        self.__wrapper = val

    @overload
    def __init__(self, message: str):
        """public com.google.common.util.concurrent.UncheckedTimeoutException(java.lang.String)"""
        val = _UncheckedTimeoutException(message)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self):
        """public com.google.common.util.concurrent.UncheckedTimeoutException()"""
        val = _UncheckedTimeoutException()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public com.google.common.util.concurrent.UncheckedTimeoutException(java.lang.String,java.lang.Throwable)"""
        val = _UncheckedTimeoutException(message, cause)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.google.common.util.concurrent.UncheckedTimeoutException()"""
        val = _UncheckedTimeoutException()
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

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
 
 
# CLASS: com.google.common.util.concurrent.JdkFutureAdapters
from builtins import str
from pyquantum_helper import override
import com.google.common.util.concurrent.JdkFutureAdapters as _JdkFutureAdapters
_JdkFutureAdapters = _JdkFutureAdapters
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.ListenableFuture as _ListenableFuture
_ListenableFuture = _ListenableFuture
import java.lang.Integer as _int
import java.util.concurrent.Future as Future
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JdkFutureAdapters():
    """com.google.common.util.concurrent.JdkFutureAdapters"""
 
    @staticmethod
    def _wrap(java_value: _JdkFutureAdapters) -> 'JdkFutureAdapters':
        return JdkFutureAdapters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JdkFutureAdapters):
        """
        Dynamic initializer for JdkFutureAdapters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JdkFutureAdapters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JdkFutureAdapters__wrapper":
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

    @staticmethod
    @overload
    def listenInPoolThread(future: 'Future') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.JdkFutureAdapters.listenInPoolThread(java.util.concurrent.Future<V>)"""
        return ListenableFuture._wrap(_JdkFutureAdapters.listenInPoolThread(future))

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

    @staticmethod
    @overload
    def listenInPoolThread(future: 'Future', executor: 'Executor') -> 'ListenableFuture':
        """public static <V> com.google.common.util.concurrent.ListenableFuture<V> com.google.common.util.concurrent.JdkFutureAdapters.listenInPoolThread(java.util.concurrent.Future<V>,java.util.concurrent.Executor)"""
        return ListenableFuture._wrap(_JdkFutureAdapters.listenInPoolThread(future, executor))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.util.concurrent.ClosingFuture$Combiner4$AsyncClosingFunction4
from abc import abstractmethod, ABC
import com.google.common.util.concurrent.ClosingFuture as _ClosingFuture_Combiner4_AsyncClosingFunction4
_AsyncClosingFunction4 = _ClosingFuture_Combiner4_AsyncClosingFunction4.Combiner4.AsyncClosingFunction4
 
class AsyncClosingFunction4():
    """com.google.common.util.concurrent.ClosingFuture.Combiner4.AsyncClosingFunction4"""
 
    @staticmethod
    def _wrap(java_value: _AsyncClosingFunction4) -> 'AsyncClosingFunction4':
        return AsyncClosingFunction4(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncClosingFunction4):
        """
        Dynamic initializer for AsyncClosingFunction4.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncClosingFunction4__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncClosingFunction4__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, closer: 'DeferredCloser', value1: object, value2: object, value3: object, value4: object):
        """public abstract com.google.common.util.concurrent.ClosingFuture<U> com.google.common.util.concurrent.ClosingFuture$Combiner4$AsyncClosingFunction4.apply(com.google.common.util.concurrent.ClosingFuture$DeferredCloser,V1,V2,V3,V4) throws java.lang.Exception"""
        pass 
 
 
# CLASS: com.google.common.util.concurrent.Uninterruptibles
import java.lang.Thread as Thread
import java.util.concurrent.locks.Condition as Condition
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import java.util.concurrent.Semaphore as Semaphore
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
import java.time.Duration as Duration
from builtins import object
import java.lang.String as _String
_String = _String
import com.google.common.util.concurrent.Uninterruptibles as _Uninterruptibles
_Uninterruptibles = _Uninterruptibles
import java.util.concurrent.locks.Lock as Lock
import java.util.concurrent.BlockingQueue as BlockingQueue
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.CountDownLatch as CountDownLatch
import java.util.concurrent.Future as Future
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Uninterruptibles():
    """com.google.common.util.concurrent.Uninterruptibles"""
 
    @staticmethod
    def _wrap(java_value: _Uninterruptibles) -> 'Uninterruptibles':
        return Uninterruptibles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Uninterruptibles):
        """
        Dynamic initializer for Uninterruptibles.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Uninterruptibles__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Uninterruptibles__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def sleepUninterruptibly(sleepFor: 'Duration'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.sleepUninterruptibly(java.time.Duration)"""
        _Uninterruptibles.sleepUninterruptibly(sleepFor)

    @staticmethod
    @overload
    def awaitUninterruptibly(latch: 'CountDownLatch', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.CountDownLatch,java.time.Duration)"""
        return bool._wrap(_Uninterruptibles.awaitUninterruptibly(latch, timeout))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getUninterruptibly(future: 'Future') -> object:
        """public static <V> V com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly(java.util.concurrent.Future<V>) throws java.util.concurrent.ExecutionException"""
        return object._wrap(_Uninterruptibles.getUninterruptibly(future))

    @staticmethod
    @overload
    def getUninterruptibly(future: 'Future', timeout: int, unit: 'TimeUnit') -> object:
        """public static <V> V com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly(java.util.concurrent.Future<V>,long,java.util.concurrent.TimeUnit) throws java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(_Uninterruptibles.getUninterruptibly(future, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def joinUninterruptibly(toJoin: 'Thread'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.joinUninterruptibly(java.lang.Thread)"""
        _Uninterruptibles.joinUninterruptibly(toJoin)

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', permits: int, timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,int,java.time.Duration)"""
        return bool._wrap(_Uninterruptibles.tryAcquireUninterruptibly(semaphore, _int.valueOf(permits), timeout))

    @staticmethod
    @overload
    def tryLockUninterruptibly(lock: 'Lock', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryLockUninterruptibly(java.util.concurrent.locks.Lock,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_Uninterruptibles.tryLockUninterruptibly(lock, _long.valueOf(timeout), unit))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def awaitTerminationUninterruptibly(executor: 'ExecutorService', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly(java.util.concurrent.ExecutorService,java.time.Duration)"""
        return bool._wrap(_Uninterruptibles.awaitTerminationUninterruptibly(executor, timeout))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def awaitUninterruptibly(latch: 'CountDownLatch'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.CountDownLatch)"""
        _Uninterruptibles.awaitUninterruptibly(latch)

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,java.time.Duration)"""
        return bool._wrap(_Uninterruptibles.tryAcquireUninterruptibly(semaphore, timeout))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def awaitUninterruptibly(condition: 'Condition', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.locks.Condition,java.time.Duration)"""
        return bool._wrap(_Uninterruptibles.awaitUninterruptibly(condition, timeout))

    @staticmethod
    @overload
    def awaitTerminationUninterruptibly(executor: 'ExecutorService', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly(java.util.concurrent.ExecutorService,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_Uninterruptibles.awaitTerminationUninterruptibly(executor, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def awaitUninterruptibly(latch: 'CountDownLatch', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.CountDownLatch,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_Uninterruptibles.awaitUninterruptibly(latch, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def takeUninterruptibly(queue: 'BlockingQueue') -> object:
        """public static <E> E com.google.common.util.concurrent.Uninterruptibles.takeUninterruptibly(java.util.concurrent.BlockingQueue<E>)"""
        return object._wrap(_Uninterruptibles.takeUninterruptibly(queue))

    @staticmethod
    @overload
    def joinUninterruptibly(toJoin: 'Thread', timeout: int, unit: 'TimeUnit'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.joinUninterruptibly(java.lang.Thread,long,java.util.concurrent.TimeUnit)"""
        _Uninterruptibles.joinUninterruptibly(toJoin, _long.valueOf(timeout), unit)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def awaitUninterruptibly(condition: 'Condition', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly(java.util.concurrent.locks.Condition,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_Uninterruptibles.awaitUninterruptibly(condition, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', permits: int, timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,int,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_Uninterruptibles.tryAcquireUninterruptibly(semaphore, _int.valueOf(permits), _long.valueOf(timeout), unit))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def tryAcquireUninterruptibly(semaphore: 'Semaphore', timeout: int, unit: 'TimeUnit') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryAcquireUninterruptibly(java.util.concurrent.Semaphore,long,java.util.concurrent.TimeUnit)"""
        return bool._wrap(_Uninterruptibles.tryAcquireUninterruptibly(semaphore, _long.valueOf(timeout), unit))

    @staticmethod
    @overload
    def tryLockUninterruptibly(lock: 'Lock', timeout: 'Duration') -> bool:
        """public static boolean com.google.common.util.concurrent.Uninterruptibles.tryLockUninterruptibly(java.util.concurrent.locks.Lock,java.time.Duration)"""
        return bool._wrap(_Uninterruptibles.tryLockUninterruptibly(lock, timeout))

    @staticmethod
    @overload
    def putUninterruptibly(queue: 'BlockingQueue', element: object):
        """public static <E> void com.google.common.util.concurrent.Uninterruptibles.putUninterruptibly(java.util.concurrent.BlockingQueue<E>,E)"""
        _Uninterruptibles.putUninterruptibly(queue, element)

    @staticmethod
    @overload
    def awaitTerminationUninterruptibly(executor: 'ExecutorService'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly(java.util.concurrent.ExecutorService)"""
        _Uninterruptibles.awaitTerminationUninterruptibly(executor)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def joinUninterruptibly(toJoin: 'Thread', timeout: 'Duration'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.joinUninterruptibly(java.lang.Thread,java.time.Duration)"""
        _Uninterruptibles.joinUninterruptibly(toJoin, timeout)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getUninterruptibly(future: 'Future', timeout: 'Duration') -> object:
        """public static <V> V com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly(java.util.concurrent.Future<V>,java.time.Duration) throws java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(_Uninterruptibles.getUninterruptibly(future, timeout))

    @staticmethod
    @overload
    def sleepUninterruptibly(sleepFor: int, unit: 'TimeUnit'):
        """public static void com.google.common.util.concurrent.Uninterruptibles.sleepUninterruptibly(long,java.util.concurrent.TimeUnit)"""
        _Uninterruptibles.sleepUninterruptibly(_long.valueOf(sleepFor), unit)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())