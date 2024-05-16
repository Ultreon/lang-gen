from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
import org.apache.logging.log4j.ThreadContext as __ThreadContext_ContextStack
__ContextStack = __ThreadContext_ContextStack.ContextStack
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ContextStack(ABC):
    """org.apache.logging.log4j.ThreadContext.ContextStack"""
 
    @staticmethod
    def __wrap(java_value: __ContextStack) -> 'ContextStack':
        return ContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContextStack):
        """
        Dynamic initializer for ContextStack.
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
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def copy(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.copy()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean java.util.Collection.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.containsAll(java.util.Collection<?>)"""
        pass

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

    @abstractmethod
    def pop(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.pop()"""
        pass

    @abstractmethod
    def peek(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.peek()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @abstractmethod
    def asList(self, ):
        """public abstract java.util.List<java.lang.String> org.apache.logging.log4j.ThreadContext$ContextStack.asList()"""
        pass

    @abstractmethod
    def trim(self, depth: int):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.trim(int)"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def push(self, message: str):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.push(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int org.apache.logging.log4j.ThreadContext$ContextStack.getDepth()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @abstractmethod
    def getImmutableStackOrNull(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.getImmutableStackOrNull()"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.ThreadContext$ContextStack
import java.util.function.Predicate as Predicate
import org.apache.logging.log4j.ThreadContext as __ThreadContext_ContextStack
__ContextStack = __ThreadContext_ContextStack.ContextStack
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ContextStack(ABC):
    """org.apache.logging.log4j.ThreadContext.ContextStack"""
 
    @staticmethod
    def __wrap(java_value: __ContextStack) -> 'ContextStack':
        return ContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContextStack):
        """
        Dynamic initializer for ContextStack.
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
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def copy(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.copy()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean java.util.Collection.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.containsAll(java.util.Collection<?>)"""
        pass

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

    @abstractmethod
    def pop(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.pop()"""
        pass

    @abstractmethod
    def peek(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.peek()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @abstractmethod
    def asList(self, ):
        """public abstract java.util.List<java.lang.String> org.apache.logging.log4j.ThreadContext$ContextStack.asList()"""
        pass

    @abstractmethod
    def trim(self, depth: int):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.trim(int)"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def push(self, message: str):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.push(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int org.apache.logging.log4j.ThreadContext$ContextStack.getDepth()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @abstractmethod
    def getImmutableStackOrNull(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.getImmutableStackOrNull()"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.ThreadContext$ContextStack 
 
 
# CLASS: org.apache.logging.log4j.CloseableThreadContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.CloseableThreadContext as __CloseableThreadContext_Instance
__Instance = __CloseableThreadContext_Instance.Instance
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.logging.log4j.CloseableThreadContext as __CloseableThreadContext
__CloseableThreadContext = __CloseableThreadContext
import java.util.Map as Map
from builtins import bool
import java.util.List as List
from builtins import int
 
class CloseableThreadContext():
    """org.apache.logging.log4j.CloseableThreadContext"""
 
    @staticmethod
    def __wrap(java_value: __CloseableThreadContext) -> 'CloseableThreadContext':
        return CloseableThreadContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CloseableThreadContext):
        """
        Dynamic initializer for CloseableThreadContext.
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
    def pushAll(messages: 'List') -> 'Instance':
        """public static org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext.pushAll(java.util.List<java.lang.String>)"""
        return Instance.__wrap(__CloseableThreadContext.pushAll(messages))

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
    def push(message: str) -> 'Instance':
        """public static org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext.push(java.lang.String)"""
        return Instance.__wrap(__CloseableThreadContext.push(message))

    @staticmethod
    @overload
    def putAll(values: 'Map') -> 'Instance':
        """public static org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        return Instance.__wrap(__CloseableThreadContext.putAll(values))

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
    def push(message: str, *args: object) -> 'Instance':
        """public static org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext.push(java.lang.String,java.lang.Object...)"""
        return Instance.__wrap(__CloseableThreadContext.push(message, args))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def put(key: str, value: str) -> 'Instance':
        """public static org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext.put(java.lang.String,java.lang.String)"""
        return Instance.__wrap(__CloseableThreadContext.put(key, value))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.CloseableThreadContext$Instance
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.CloseableThreadContext as __CloseableThreadContext_Instance
__Instance = __CloseableThreadContext_Instance.Instance
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import java.util.List as List
from builtins import int
 
class Instance():
    """org.apache.logging.log4j.CloseableThreadContext.Instance"""
 
    @staticmethod
    def __wrap(java_value: __Instance) -> 'Instance':
        return Instance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Instance):
        """
        Dynamic initializer for Instance.
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
    def put(self, key: str, value: str) -> 'Instance':
        """public org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext$Instance.put(java.lang.String,java.lang.String)"""
        return 'Instance'.__wrap(super(__Instance, self).put(key, value))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def push(self, message: str, args: 'Object') -> 'Instance':
        """public org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext$Instance.push(java.lang.String,java.lang.Object[])"""
        return 'Instance'.__wrap(super(__Instance, self).push(message, args))

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
    def push(self, message: str) -> 'Instance':
        """public org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext$Instance.push(java.lang.String)"""
        return 'Instance'.__wrap(super(__Instance, self).push(message))

    @override
    @overload
    def close(self):
        """public void org.apache.logging.log4j.CloseableThreadContext$Instance.close()"""
        super(Instance, self).close()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putAll(self, values: 'Map') -> 'Instance':
        """public org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext$Instance.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'Instance'.__wrap(super(__Instance, self).putAll(values))

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
    def pushAll(self, messages: 'List') -> 'Instance':
        """public org.apache.logging.log4j.CloseableThreadContext$Instance org.apache.logging.log4j.CloseableThreadContext$Instance.pushAll(java.util.List<java.lang.String>)"""
        return 'Instance'.__wrap(super(__Instance, self).pushAll(messages))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.MarkerManager
import org.apache.logging.log4j.Marker as __Marker
__Marker = __Marker
import org.apache.logging.log4j.MarkerManager as __MarkerManager
__MarkerManager = __MarkerManager
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
 
class MarkerManager():
    """org.apache.logging.log4j.MarkerManager"""
 
    @staticmethod
    def __wrap(java_value: __MarkerManager) -> 'MarkerManager':
        return MarkerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MarkerManager):
        """
        Dynamic initializer for MarkerManager.
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
        def clear():
            """public static void org.apache.logging.log4j.MarkerManager.clear()"""
            __MarkerManager.clear()

    @staticmethod
    @overload
    def getMarker(name: str, parent: 'Marker') -> 'Marker':
        """public static org.apache.logging.log4j.Marker org.apache.logging.log4j.MarkerManager.getMarker(java.lang.String,org.apache.logging.log4j.Marker)"""
        return Marker.__wrap(__MarkerManager.getMarker(name, parent))

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
    def getMarker(name: str) -> 'Marker':
        """public static org.apache.logging.log4j.Marker org.apache.logging.log4j.MarkerManager.getMarker(java.lang.String)"""
        return Marker.__wrap(__MarkerManager.getMarker(name))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getMarker(name: str, parent: str) -> 'Marker':
        """public static org.apache.logging.log4j.Marker org.apache.logging.log4j.MarkerManager.getMarker(java.lang.String,java.lang.String)"""
        return Marker.__wrap(__MarkerManager.getMarker(name, parent))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def exists(key: str) -> bool:
        """public static boolean org.apache.logging.log4j.MarkerManager.exists(java.lang.String)"""
        return bool.__wrap(__MarkerManager.exists(key)) 
 
 
# CLASS: org.apache.logging.log4j.MarkerManager$Log4jMarker
import org.apache.logging.log4j.Marker as __Marker
__Marker = __Marker
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import org.apache.logging.log4j.MarkerManager as __MarkerManager_Log4jMarker
__Log4jMarker = __MarkerManager_Log4jMarker.Log4jMarker
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Log4jMarker():
    """org.apache.logging.log4j.MarkerManager.Log4jMarker"""
 
    @staticmethod
    def __wrap(java_value: __Log4jMarker) -> 'Log4jMarker':
        return Log4jMarker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Log4jMarker):
        """
        Dynamic initializer for Log4jMarker.
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
    def isInstanceOf(self, markerName: str) -> bool:
        """public boolean org.apache.logging.log4j.MarkerManager$Log4jMarker.isInstanceOf(java.lang.String)"""
        return bool.__wrap(super(__Log4jMarker, self).isInstanceOf(markerName))

    @overload
    def isInstanceOf(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.MarkerManager$Log4jMarker.isInstanceOf(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__Log4jMarker, self).isInstanceOf(marker))

    @override
    @overload
    def formatTo(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.MarkerManager$Log4jMarker.formatTo(java.lang.StringBuilder)"""
        super(__Log4jMarker, self).formatTo(sb)

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.MarkerManager$Log4jMarker(java.lang.String)"""
        val = __Log4jMarker(name)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hasParents(self) -> bool:
        """public boolean org.apache.logging.log4j.MarkerManager$Log4jMarker.hasParents()"""
        return bool.__wrap(super(Log4jMarker, self).hasParents())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.MarkerManager$Log4jMarker.hashCode()"""
        return int.__wrap(super(Log4jMarker, self).hashCode())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.MarkerManager$Log4jMarker.equals(java.lang.Object)"""
        return bool.__wrap(super(__Log4jMarker, self).equals(o))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def remove(self, parent: 'Marker') -> bool:
        """public synchronized boolean org.apache.logging.log4j.MarkerManager$Log4jMarker.remove(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__Log4jMarker, self).remove(parent))

    @overload
    def setParents(self, *markers: 'Marker') -> 'Marker':
        """public org.apache.logging.log4j.Marker org.apache.logging.log4j.MarkerManager$Log4jMarker.setParents(org.apache.logging.log4j.Marker...)"""
        return 'Marker'.__wrap(super(__Log4jMarker, self).setParents(markers))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addParents(self, *parentMarkers: 'Marker') -> 'Marker':
        """public synchronized org.apache.logging.log4j.Marker org.apache.logging.log4j.MarkerManager$Log4jMarker.addParents(org.apache.logging.log4j.Marker...)"""
        return 'Marker'.__wrap(super(__Log4jMarker, self).addParents(parentMarkers))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.MarkerManager$Log4jMarker.getName()"""
        return str.__wrap(super(Log4jMarker, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.MarkerManager$Log4jMarker.toString()"""
        return str.__wrap(super(Log4jMarker, self).toString())

    @override
    @overload
    def getParents(self) -> List['Marker']:
        """public org.apache.logging.log4j.Marker[] org.apache.logging.log4j.MarkerManager$Log4jMarker.getParents()"""
        return List['Marker'].__wrap(super(Log4jMarker, self).getParents()) 
 
 
# CLASS: org.apache.logging.log4j.LogBuilder
from pyquantum_helper import import_once as __import_once__
import java.lang.CharSequence as CharSequence
import java.lang.Object as __object
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
import java.lang.String as __string
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Throwable as Throwable
from builtins import object
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import java.lang.StackTraceElement as StackTraceElement
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class LogBuilder(ABC):
    """org.apache.logging.log4j.LogBuilder"""
 
    @staticmethod
    def __wrap(java_value: __LogBuilder) -> 'LogBuilder':
        return LogBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LogBuilder):
        """
        Dynamic initializer for LogBuilder.
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
    def log(self, message: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.Object)"""
        super(__LogBuilder, self).log(message)

    @overload
    def log(self, message: str, *params: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object...)"""
        super(__LogBuilder, self).log(message, params)

    @overload
    def logAndGet(self, messageSupplier: 'Supplier') -> 'message.Message':
        """public default org.apache.logging.log4j.message.Message org.apache.logging.log4j.LogBuilder.logAndGet(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        return 'message.Message'.__wrap(super(__LogBuilder, self).logAndGet(messageSupplier))

    @overload
    def withLocation(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.LogBuilder.withLocation()"""
        return 'LogBuilder'.__wrap(super(LogBuilder, self).withLocation())

    @overload
    def log(self, message: str, p0: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0)

    @overload
    def withMarker(self, marker: 'Marker') -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.LogBuilder.withMarker(org.apache.logging.log4j.Marker)"""
        return 'LogBuilder'.__wrap(super(__LogBuilder, self).withMarker(marker))

    @overload
    def withThrowable(self, throwable: 'Throwable') -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.LogBuilder.withThrowable(java.lang.Throwable)"""
        return 'LogBuilder'.__wrap(super(__LogBuilder, self).withThrowable(throwable))

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3, p4, p5)

    @overload
    def log(self, message: str, p0: object, p1: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1)

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def log(self, messageSupplier: 'Supplier'):
        """public default void org.apache.logging.log4j.LogBuilder.log(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        super(__LogBuilder, self).log(messageSupplier)

    @overload
    def log(self, message: 'Message'):
        """public default void org.apache.logging.log4j.LogBuilder.log(org.apache.logging.log4j.message.Message)"""
        super(__LogBuilder, self).log(message)

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2)

    @overload
    def log(self, message: str, *params: 'util.Supplier'):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__LogBuilder, self).log(message, params)

    @overload
    def log(self, message: str):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String)"""
        super(__LogBuilder, self).log(message)

    @overload
    def withLocation(self, location: 'StackTraceElement') -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.LogBuilder.withLocation(java.lang.StackTraceElement)"""
        return 'LogBuilder'.__wrap(super(__LogBuilder, self).withLocation(location))

    @overload
    def log(self):
        """public default void org.apache.logging.log4j.LogBuilder.log()"""
        super(LogBuilder, self).log()

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3)

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def log(self, message: 'CharSequence'):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.CharSequence)"""
        super(__LogBuilder, self).log(message)

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3, p4)

    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public default void org.apache.logging.log4j.LogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__LogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7) 
 
 
# CLASS: org.apache.logging.log4j.LogManager
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.Logger as __Logger
__Logger = __Logger
from builtins import str
import java.lang.Boolean as __boolean
import java.net.URI as URI
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from log4py import spi
except ImportError:
    spi = __import_once__("log4py.spi")

import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.spi.LoggerContext as __LoggerContext
__LoggerContext = __LoggerContext
import java.lang.Integer as __int
import org.apache.logging.log4j.LogManager as __LogManager
__LogManager = __LogManager
from builtins import bool
import org.apache.logging.log4j.spi.LoggerContextFactory as __LoggerContextFactory
__LoggerContextFactory = __LoggerContextFactory
from builtins import int
 
class LogManager():
    """org.apache.logging.log4j.LogManager"""
 
    @staticmethod
    def __wrap(java_value: __LogManager) -> 'LogManager':
        return LogManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LogManager):
        """
        Dynamic initializer for LogManager.
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
    def getContext(loader: 'ClassLoader', currentContext: bool, externalContext: object, configLocation: 'URI', name: str) -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext(java.lang.ClassLoader,boolean,java.lang.Object,java.net.URI,java.lang.String)"""
        return spi.LoggerContext.__wrap(__LogManager.getContext(loader, __boolean.valueOf(currentContext), externalContext, configLocation, name))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getRootLogger() -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getRootLogger()"""
        return Logger.__wrap(__LogManager.getRootLogger())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getLogger() -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger()"""
        return Logger.__wrap(__LogManager.getLogger())

    @staticmethod
    @overload
    def getLogger(name: str) -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(java.lang.String)"""
        return Logger.__wrap(__LogManager.getLogger(name))

        @staticmethod
        @overload
        def shutdown():
            """public static void org.apache.logging.log4j.LogManager.shutdown()"""
            __LogManager.shutdown()

    @staticmethod
    @overload
    def getLogger(clazz: 'Class') -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(java.lang.Class<?>)"""
        return Logger.__wrap(__LogManager.getLogger(clazz))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getLogger(messageFactory: 'MessageFactory') -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(org.apache.logging.log4j.message.MessageFactory)"""
        return Logger.__wrap(__LogManager.getLogger(messageFactory))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getContext(loader: 'ClassLoader', currentContext: bool, externalContext: object) -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext(java.lang.ClassLoader,boolean,java.lang.Object)"""
        return spi.LoggerContext.__wrap(__LogManager.getContext(loader, __boolean.valueOf(currentContext), externalContext))

    @staticmethod
    @overload
    def setFactory(factory: 'LoggerContextFactory'):
        """public static void org.apache.logging.log4j.LogManager.setFactory(org.apache.logging.log4j.spi.LoggerContextFactory)"""
        __LogManager.setFactory(factory)

    @staticmethod
    @overload
    def shutdown(currentContext: bool, allContexts: bool):
        """public static void org.apache.logging.log4j.LogManager.shutdown(boolean,boolean)"""
        __LogManager.shutdown(__boolean.valueOf(currentContext), __boolean.valueOf(allContexts))

    @staticmethod
    @overload
    def getLogger(name: str, messageFactory: 'MessageFactory') -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return Logger.__wrap(__LogManager.getLogger(name, messageFactory))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def getContext(loader: 'ClassLoader', currentContext: bool, externalContext: object, configLocation: 'URI') -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext(java.lang.ClassLoader,boolean,java.lang.Object,java.net.URI)"""
        return spi.LoggerContext.__wrap(__LogManager.getContext(loader, __boolean.valueOf(currentContext), externalContext, configLocation))

    @staticmethod
    @overload
    def getContext() -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext()"""
        return spi.LoggerContext.__wrap(__LogManager.getContext())

    @staticmethod
    @overload
    def getFactory() -> 'spi.LoggerContextFactory':
        """public static org.apache.logging.log4j.spi.LoggerContextFactory org.apache.logging.log4j.LogManager.getFactory()"""
        return spi.LoggerContextFactory.__wrap(__LogManager.getFactory())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def exists(name: str) -> bool:
        """public static boolean org.apache.logging.log4j.LogManager.exists(java.lang.String)"""
        return bool.__wrap(__LogManager.exists(name))

    @staticmethod
    @overload
    def getLogger(clazz: 'Class', messageFactory: 'MessageFactory') -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(java.lang.Class<?>,org.apache.logging.log4j.message.MessageFactory)"""
        return Logger.__wrap(__LogManager.getLogger(clazz, messageFactory))

    @staticmethod
    @overload
    def getContext(currentContext: bool) -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext(boolean)"""
        return spi.LoggerContext.__wrap(__LogManager.getContext(__boolean.valueOf(currentContext)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getLogger(value: object) -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(java.lang.Object)"""
        return Logger.__wrap(__LogManager.getLogger(value))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getContext(loader: 'ClassLoader', currentContext: bool, configLocation: 'URI') -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext(java.lang.ClassLoader,boolean,java.net.URI)"""
        return spi.LoggerContext.__wrap(__LogManager.getContext(loader, __boolean.valueOf(currentContext), configLocation))

    @staticmethod
    @overload
    def getContext(loader: 'ClassLoader', currentContext: bool) -> 'spi.LoggerContext':
        """public static org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.LogManager.getContext(java.lang.ClassLoader,boolean)"""
        return spi.LoggerContext.__wrap(__LogManager.getContext(loader, __boolean.valueOf(currentContext)))

    @staticmethod
    @overload
    def getFormatterLogger() -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getFormatterLogger()"""
        return Logger.__wrap(__LogManager.getFormatterLogger())

    @staticmethod
    @overload
    def shutdown(currentContext: bool):
        """public static void org.apache.logging.log4j.LogManager.shutdown(boolean)"""
        __LogManager.shutdown(__boolean.valueOf(currentContext))

    @staticmethod
    @overload
    def shutdown(context: 'LoggerContext'):
        """public static void org.apache.logging.log4j.LogManager.shutdown(org.apache.logging.log4j.spi.LoggerContext)"""
        __LogManager.shutdown(context)

    @staticmethod
    @overload
    def getFormatterLogger(name: str) -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getFormatterLogger(java.lang.String)"""
        return Logger.__wrap(__LogManager.getFormatterLogger(name))

    @staticmethod
    @overload
    def getLogger(value: object, messageFactory: 'MessageFactory') -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getLogger(java.lang.Object,org.apache.logging.log4j.message.MessageFactory)"""
        return Logger.__wrap(__LogManager.getLogger(value, messageFactory))

    @staticmethod
    @overload
    def getFormatterLogger(value: object) -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getFormatterLogger(java.lang.Object)"""
        return Logger.__wrap(__LogManager.getFormatterLogger(value))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getFormatterLogger(clazz: 'Class') -> 'Logger':
        """public static org.apache.logging.log4j.Logger org.apache.logging.log4j.LogManager.getFormatterLogger(java.lang.Class<?>)"""
        return Logger.__wrap(__LogManager.getFormatterLogger(clazz)) 
 
 
# CLASS: org.apache.logging.log4j.EventLogger
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.EventLogger as __EventLogger
__EventLogger = __EventLogger
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

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
 
class EventLogger():
    """org.apache.logging.log4j.EventLogger"""
 
    @staticmethod
    def __wrap(java_value: __EventLogger) -> 'EventLogger':
        return EventLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventLogger):
        """
        Dynamic initializer for EventLogger.
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
    def logEvent(msg: 'StructuredDataMessage'):
        """public static void org.apache.logging.log4j.EventLogger.logEvent(org.apache.logging.log4j.message.StructuredDataMessage)"""
        __EventLogger.logEvent(msg)

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

    @staticmethod
    @overload
    def logEvent(msg: 'StructuredDataMessage', level: 'Level'):
        """public static void org.apache.logging.log4j.EventLogger.logEvent(org.apache.logging.log4j.message.StructuredDataMessage,org.apache.logging.log4j.Level)"""
        __EventLogger.logEvent(msg, level)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.Level
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from log4py import spi
except ImportError:
    spi = __import_once__("log4py.spi")

import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.spi.StandardLevel as __StandardLevel
__StandardLevel = __StandardLevel
import java.lang.Integer as __int
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
import org.apache.logging.log4j.Level as __Level
__Level = __Level
from builtins import int
 
class Level():
    """org.apache.logging.log4j.Level"""
 
    @staticmethod
    def __wrap(java_value: __Level) -> 'Level':
        return Level(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Level):
        """
        Dynamic initializer for Level.
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
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.Level.hashCode()"""
        return int.__wrap(super(Level, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isMoreSpecificThan(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.Level.isMoreSpecificThan(org.apache.logging.log4j.Level)"""
        return bool.__wrap(super(__Level, self).isMoreSpecificThan(level))

    @staticmethod
    @overload
    def valueOf(enumType: 'Class', name: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T org.apache.logging.log4j.Level.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Level.valueOf(enumType, name))

    @overload
    def clone(self) -> 'Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.Level.clone() throws java.lang.CloneNotSupportedException"""
        return 'Level'.__wrap(super(Level, self).clone())

    @staticmethod
    @overload
    def forName(name: str, intValue: int) -> 'Level':
        """public static org.apache.logging.log4j.Level org.apache.logging.log4j.Level.forName(java.lang.String,int)"""
        return Level.__wrap(__Level.forName(name, __int.valueOf(intValue)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compareTo(self, other: 'Level') -> int:
        """public int org.apache.logging.log4j.Level.compareTo(org.apache.logging.log4j.Level)"""
        return int.__wrap(super(__Level, self).compareTo(other))

    @overload
    def equals(self, other: object) -> bool:
        """public boolean org.apache.logging.log4j.Level.equals(java.lang.Object)"""
        return bool.__wrap(super(__Level, self).equals(other))

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Level':
        """public static org.apache.logging.log4j.Level org.apache.logging.log4j.Level.valueOf(java.lang.String)"""
        return Level.__wrap(__Level.valueOf(name))

    @overload
    def isLessSpecificThan(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.Level.isLessSpecificThan(org.apache.logging.log4j.Level)"""
        return bool.__wrap(super(__Level, self).isLessSpecificThan(level))

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class<org.apache.logging.log4j.Level> org.apache.logging.log4j.Level.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Level, self).getDeclaringClass())

    @overload
    def getStandardLevel(self) -> 'spi.StandardLevel':
        """public org.apache.logging.log4j.spi.StandardLevel org.apache.logging.log4j.Level.getStandardLevel()"""
        return 'spi.StandardLevel'.__wrap(super(Level, self).getStandardLevel())

    @staticmethod
    @overload
    def toLevel(level: str) -> 'Level':
        """public static org.apache.logging.log4j.Level org.apache.logging.log4j.Level.toLevel(java.lang.String)"""
        return Level.__wrap(__Level.toLevel(level))

    @staticmethod
    @overload
    def getLevel(name: str) -> 'Level':
        """public static org.apache.logging.log4j.Level org.apache.logging.log4j.Level.getLevel(java.lang.String)"""
        return Level.__wrap(__Level.getLevel(name))

    @overload
    def name(self) -> str:
        """public java.lang.String org.apache.logging.log4j.Level.name()"""
        return str.__wrap(super(Level, self).name())

    @overload
    def isInRange(self, minLevel: 'Level', maxLevel: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.Level.isInRange(org.apache.logging.log4j.Level,org.apache.logging.log4j.Level)"""
        return bool.__wrap(super(__Level, self).isInRange(minLevel, maxLevel))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.Level.toString()"""
        return str.__wrap(super(Level, self).toString())

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
    def values() -> List['Level']:
        """public static org.apache.logging.log4j.Level[] org.apache.logging.log4j.Level.values()"""
        return List[Level].__wrap(__Level.values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def intLevel(self) -> int:
        """public int org.apache.logging.log4j.Level.intLevel()"""
        return int.__wrap(super(Level, self).intLevel())

    @staticmethod
    @overload
    def toLevel(name: str, defaultLevel: 'Level') -> 'Level':
        """public static org.apache.logging.log4j.Level org.apache.logging.log4j.Level.toLevel(java.lang.String,org.apache.logging.log4j.Level)"""
        return Level.__wrap(__Level.toLevel(name, defaultLevel)) 
 
 
# CLASS: org.apache.logging.log4j.LoggingException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.LoggingException as __LoggingException
__LoggingException = __LoggingException
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
 
class LoggingException():
    """org.apache.logging.log4j.LoggingException"""
 
    @staticmethod
    def __wrap(java_value: __LoggingException) -> 'LoggingException':
        return LoggingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggingException):
        """
        Dynamic initializer for LoggingException.
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

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public org.apache.logging.log4j.LoggingException(java.lang.String,java.lang.Throwable)"""
        val = __LoggingException(message, cause)
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
    def __init__(self, cause: 'Throwable'):
        """public org.apache.logging.log4j.LoggingException(java.lang.Throwable)"""
        val = __LoggingException(cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, message: str):
        """public org.apache.logging.log4j.LoggingException(java.lang.String)"""
        val = __LoggingException(message)
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
 
 
# CLASS: org.apache.logging.log4j.Marker
import org.apache.logging.log4j.Marker as __Marker
__Marker = __Marker
from abc import abstractmethod, ABC
 
class Marker(ABC):
    """org.apache.logging.log4j.Marker"""
 
    @staticmethod
    def __wrap(java_value: __Marker) -> 'Marker':
        return Marker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Marker):
        """
        Dynamic initializer for Marker.
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
    def isInstanceOf(self, m: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Marker.isInstanceOf(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.apache.logging.log4j.Marker.hashCode()"""
        pass

    @abstractmethod
    def setParents(self, *markers: 'Marker'):
        """public abstract org.apache.logging.log4j.Marker org.apache.logging.log4j.Marker.setParents(org.apache.logging.log4j.Marker...)"""
        pass

    @abstractmethod
    def getParents(self, ):
        """public abstract org.apache.logging.log4j.Marker[] org.apache.logging.log4j.Marker.getParents()"""
        pass

    @abstractmethod
    def remove(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Marker.remove(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.Marker.getName()"""
        pass

    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean org.apache.logging.log4j.Marker.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def addParents(self, *markers: 'Marker'):
        """public abstract org.apache.logging.log4j.Marker org.apache.logging.log4j.Marker.addParents(org.apache.logging.log4j.Marker...)"""
        pass

    @abstractmethod
    def isInstanceOf(self, name: str):
        """public abstract boolean org.apache.logging.log4j.Marker.isInstanceOf(java.lang.String)"""
        pass

    @abstractmethod
    def hasParents(self, ):
        """public abstract boolean org.apache.logging.log4j.Marker.hasParents()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.BridgeAware
import org.apache.logging.log4j.BridgeAware as __BridgeAware
__BridgeAware = __BridgeAware
from abc import abstractmethod, ABC
 
class BridgeAware(ABC):
    """org.apache.logging.log4j.BridgeAware"""
 
    @staticmethod
    def __wrap(java_value: __BridgeAware) -> 'BridgeAware':
        return BridgeAware(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BridgeAware):
        """
        Dynamic initializer for BridgeAware.
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
    def setEntryPoint(self, fqcn: str):
        """public abstract void org.apache.logging.log4j.BridgeAware.setEntryPoint(java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.ThreadContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.logging.log4j.ThreadContext as __ThreadContext_ContextStack
__ContextStack = __ThreadContext_ContextStack.ContextStack
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.ThreadContext as __ThreadContext
__ThreadContext = __ThreadContext
import java.util.Map as __Map
__Map = __Map
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from log4py import spi
except ImportError:
    spi = __import_once__("log4py.spi")

import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.spi.ReadOnlyThreadContextMap as __ReadOnlyThreadContextMap
__ReadOnlyThreadContextMap = __ReadOnlyThreadContextMap
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class ThreadContext():
    """org.apache.logging.log4j.ThreadContext"""
 
    @staticmethod
    def __wrap(java_value: __ThreadContext) -> 'ThreadContext':
        return ThreadContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadContext):
        """
        Dynamic initializer for ThreadContext.
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
    def get(key: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.ThreadContext.get(java.lang.String)"""
        return str.__wrap(__ThreadContext.get(key))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def peek() -> str:
        """public static java.lang.String org.apache.logging.log4j.ThreadContext.peek()"""
        return str.__wrap(__ThreadContext.peek())

    @staticmethod
    @overload
    def getImmutableContext() -> 'Map':
        """public static java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.ThreadContext.getImmutableContext()"""
        return Map.__wrap(__ThreadContext.getImmutableContext())

        @staticmethod
        @overload
        def removeStack():
            """public static void org.apache.logging.log4j.ThreadContext.removeStack()"""
            __ThreadContext.removeStack()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def clearAll():
            """public static void org.apache.logging.log4j.ThreadContext.clearAll()"""
            __ThreadContext.clearAll()

    @staticmethod
    @overload
    def trim(depth: int):
        """public static void org.apache.logging.log4j.ThreadContext.trim(int)"""
        __ThreadContext.trim(__int.valueOf(depth))

    @staticmethod
    @overload
    def put(key: str, value: str):
        """public static void org.apache.logging.log4j.ThreadContext.put(java.lang.String,java.lang.String)"""
        __ThreadContext.put(key, value)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def init():
            """public static void org.apache.logging.log4j.ThreadContext.init()"""
            __ThreadContext.init()

        @staticmethod
        @overload
        def clearMap():
            """public static void org.apache.logging.log4j.ThreadContext.clearMap()"""
            __ThreadContext.clearMap()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def remove(key: str):
        """public static void org.apache.logging.log4j.ThreadContext.remove(java.lang.String)"""
        __ThreadContext.remove(key)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def containsKey(key: str) -> bool:
        """public static boolean org.apache.logging.log4j.ThreadContext.containsKey(java.lang.String)"""
        return bool.__wrap(__ThreadContext.containsKey(key))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def cloneStack() -> 'ContextStack':
        """public static org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext.cloneStack()"""
        return ContextStack.__wrap(__ThreadContext.cloneStack())

    @staticmethod
    @overload
    def push(message: str, *args: object):
        """public static void org.apache.logging.log4j.ThreadContext.push(java.lang.String,java.lang.Object...)"""
        __ThreadContext.push(message, args)

    @staticmethod
    @overload
    def getDepth() -> int:
        """public static int org.apache.logging.log4j.ThreadContext.getDepth()"""
        return int.__wrap(__ThreadContext.getDepth())

    @staticmethod
    @overload
    def isEmpty() -> bool:
        """public static boolean org.apache.logging.log4j.ThreadContext.isEmpty()"""
        return bool.__wrap(__ThreadContext.isEmpty())

    @staticmethod
    @overload
    def removeAll(keys: 'Iterable'):
        """public static void org.apache.logging.log4j.ThreadContext.removeAll(java.lang.Iterable<java.lang.String>)"""
        __ThreadContext.removeAll(keys)

    @staticmethod
    @overload
    def putIfNull(key: str, value: str):
        """public static void org.apache.logging.log4j.ThreadContext.putIfNull(java.lang.String,java.lang.String)"""
        __ThreadContext.putIfNull(key, value)

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
    def getThreadContextMap() -> 'spi.ReadOnlyThreadContextMap':
        """public static org.apache.logging.log4j.spi.ReadOnlyThreadContextMap org.apache.logging.log4j.ThreadContext.getThreadContextMap()"""
        return spi.ReadOnlyThreadContextMap.__wrap(__ThreadContext.getThreadContextMap())

        @staticmethod
        @overload
        def clearStack():
            """public static void org.apache.logging.log4j.ThreadContext.clearStack()"""
            __ThreadContext.clearStack()

    @staticmethod
    @overload
    def push(message: str):
        """public static void org.apache.logging.log4j.ThreadContext.push(java.lang.String)"""
        __ThreadContext.push(message)

    @staticmethod
    @overload
    def putAll(m: 'Map'):
        """public static void org.apache.logging.log4j.ThreadContext.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        __ThreadContext.putAll(m)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getContext() -> 'Map':
        """public static java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.ThreadContext.getContext()"""
        return Map.__wrap(__ThreadContext.getContext())

    @staticmethod
    @overload
    def getImmutableStack() -> 'ContextStack':
        """public static org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext.getImmutableStack()"""
        return ContextStack.__wrap(__ThreadContext.getImmutableStack())

    @staticmethod
    @overload
    def pop() -> str:
        """public static java.lang.String org.apache.logging.log4j.ThreadContext.pop()"""
        return str.__wrap(__ThreadContext.pop())

    @staticmethod
    @overload
    def setStack(stack: 'Collection'):
        """public static void org.apache.logging.log4j.ThreadContext.setStack(java.util.Collection<java.lang.String>)"""
        __ThreadContext.setStack(stack) 
 
 
# CLASS: org.apache.logging.log4j.Logger
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.Logger as __Logger
__Logger = __Logger
import java.lang.CharSequence as CharSequence
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
import java.lang.String as __string
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import java.lang.StackTraceElement as StackTraceElement
 
class Logger(ABC):
    """org.apache.logging.log4j.Logger"""
 
    @staticmethod
    def __wrap(java_value: __Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Logger):
        """
        Dynamic initializer for Logger.
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
    def error(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def exit(self, ):
        """public abstract void org.apache.logging.log4j.Logger.exit()"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isInfoEnabled()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceEntry(self, format: str, *params: object):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isDebugEnabled()"""
        pass

    @abstractmethod
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def printf(self, level: 'Level', format: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'EntryMessage'):
        """public abstract void org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceEntry(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.Logger.getName()"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public default void org.apache.logging.log4j.Logger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__Logger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @abstractmethod
    def throwing(self, throwable: 'Throwable'):
        """public abstract <T extends java.lang.Throwable> T org.apache.logging.log4j.Logger.throwing(T)"""
        pass

    @abstractmethod
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def catching(self, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.catching(java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'Message', result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        pass

    @abstractmethod
    def error(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def atTrace(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atTrace()"""
        return 'LogBuilder'.__wrap(super(Logger, self).atTrace())

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def atInfo(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atInfo()"""
        return 'LogBuilder'.__wrap(super(Logger, self).atInfo())

    @abstractmethod
    def fatal(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def entry(self, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.entry(java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(R)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def error(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String)"""
        pass

    @abstractmethod
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getMessageFactory(self, ):
        """public abstract <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.Logger.getMessageFactory()"""
        pass

    @abstractmethod
    def traceExit(self, message: 'EntryMessage', result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getFlowMessageFactory(self, ):
        """public abstract org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.Logger.getFlowMessageFactory()"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @overload
    def atLevel(self, level: 'Level') -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atLevel(org.apache.logging.log4j.Level)"""
        return 'LogBuilder'.__wrap(super(__Logger, self).atLevel(level))

    @abstractmethod
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def atWarn(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atWarn()"""
        return 'LogBuilder'.__wrap(super(Logger, self).atWarn())

    @abstractmethod
    def error(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isTraceEnabled()"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level'):
        """public abstract boolean org.apache.logging.log4j.Logger.isEnabled(org.apache.logging.log4j.Level)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @overload
    def atError(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atError()"""
        return 'LogBuilder'.__wrap(super(Logger, self).atError())

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def throwing(self, level: 'Level', throwable: 'Throwable'):
        """public abstract <T extends java.lang.Throwable> T org.apache.logging.log4j.Logger.throwing(org.apache.logging.log4j.Level,T)"""
        pass

    @abstractmethod
    def isFatalEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isFatalEnabled()"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def traceEntry(self, ):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry()"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, ):
        """public abstract void org.apache.logging.log4j.Logger.traceExit()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def always(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.always()"""
        return 'LogBuilder'.__wrap(super(Logger, self).always())

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def isFatalEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String)"""
        pass

    @overload
    def atFatal(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atFatal()"""
        return 'LogBuilder'.__wrap(super(Logger, self).atFatal())

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def exit(self, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.exit(R)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isErrorEnabled()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.Object,java.lang.Throwable)"""
        pass

    @overload
    def atDebug(self) -> 'LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atDebug()"""
        return 'LogBuilder'.__wrap(super(Logger, self).atDebug())

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def traceExit(self, format: str, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(java.lang.String,R)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def entry(self, ):
        """public abstract void org.apache.logging.log4j.Logger.entry()"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isWarnEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.Logger.getLevel()"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def warn(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def fatal(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceEntry(self, *paramSuppliers: 'util.Supplier'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def trace(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def info(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass