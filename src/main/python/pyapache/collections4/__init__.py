from __future__ import annotations
from overload import overload


 
import org.apache.commons.collections4.BoundedCollection as __BoundedCollection
__BoundedCollection = __BoundedCollection
import java.util.function.Predicate as Predicate
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
 
class BoundedCollection(ABC, __Collection, Collection):
    """org.apache.commons.collections4.BoundedCollection"""
 
    @staticmethod
    def __wrap(java_value: __BoundedCollection) -> 'BoundedCollection':
        return BoundedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundedCollection):
        """
        Dynamic initializer for BoundedCollection.
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
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def maxSize(self, ):
        """public abstract int org.apache.commons.collections4.BoundedCollection.maxSize()"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

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

    @abstractmethod
    def isFull(self, ):
        """public abstract boolean org.apache.commons.collections4.BoundedCollection.isFull()"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

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

 
 
 
# CLASS: org.apache.commons.collections4.BoundedCollection
import org.apache.commons.collections4.BoundedCollection as __BoundedCollection
__BoundedCollection = __BoundedCollection
import java.util.function.Predicate as Predicate
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
 
class BoundedCollection(ABC, __Collection, Collection):
    """org.apache.commons.collections4.BoundedCollection"""
 
    @staticmethod
    def __wrap(java_value: __BoundedCollection) -> 'BoundedCollection':
        return BoundedCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundedCollection):
        """
        Dynamic initializer for BoundedCollection.
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
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def maxSize(self, ):
        """public abstract int org.apache.commons.collections4.BoundedCollection.maxSize()"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

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

    @abstractmethod
    def isFull(self, ):
        """public abstract boolean org.apache.commons.collections4.BoundedCollection.isFull()"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

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

 
 
 
# CLASS: org.apache.commons.collections4.BoundedCollection 
 
 
# CLASS: org.apache.commons.collections4.OrderedMapIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.function.Consumer as Consumer
 
class OrderedMapIterator(ABC, __MapIterator, MapIterator, __OrderedIterator, OrderedIterator):
    """org.apache.commons.collections4.OrderedMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMapIterator) -> 'OrderedMapIterator':
        return OrderedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMapIterator):
        """
        Dynamic initializer for OrderedMapIterator.
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
    def remove(self, ):
        """public abstract void org.apache.commons.collections4.MapIterator.remove()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMapIterator.previous()"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract V org.apache.commons.collections4.MapIterator.getValue()"""
        pass

    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean org.apache.commons.collections4.OrderedMapIterator.hasPrevious()"""
        pass

    @abstractmethod
    def next(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.next()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.getKey()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean org.apache.commons.collections4.MapIterator.hasNext()"""
        pass

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract V org.apache.commons.collections4.MapIterator.setValue(V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Factory
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from abc import abstractmethod, ABC
 
class Factory(ABC):
    """org.apache.commons.collections4.Factory"""
 
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
    def create(self, ):
        """public abstract T org.apache.commons.collections4.Factory.create()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.IterableUtils
from builtins import str
import org.apache.commons.collections4.IterableUtils as __IterableUtils
__IterableUtils = __IterableUtils
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
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
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IterableUtils():
    """org.apache.commons.collections4.IterableUtils"""
 
    @staticmethod
    def __wrap(java_value: __IterableUtils) -> 'IterableUtils':
        return IterableUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IterableUtils):
        """
        Dynamic initializer for IterableUtils.
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
    def emptyIterable() -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.emptyIterable()"""
        return Iterable.__wrap(__IterableUtils.emptyIterable())

    @staticmethod
    @overload
    def unmodifiableIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.unmodifiableIterable(java.lang.Iterable<E>)"""
        return Iterable.__wrap(__IterableUtils.unmodifiableIterable(arg0))

    @staticmethod
    @overload
    def contains(arg0: 'Iterable', arg1: object) -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.contains(java.lang.Iterable<E>,java.lang.Object)"""
        return bool.__wrap(__IterableUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def boundedIterable(arg0: 'Iterable', arg1: int) -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.boundedIterable(java.lang.Iterable<E>,long)"""
        return Iterable.__wrap(__IterableUtils.boundedIterable(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def loopingIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.loopingIterable(java.lang.Iterable<E>)"""
        return Iterable.__wrap(__IterableUtils.loopingIterable(arg0))

    @staticmethod
    @overload
    def transformedIterable(arg0: 'Iterable', arg1: 'Transformer') -> 'Iterable':
        """public static <I,O> java.lang.Iterable<O> org.apache.commons.collections4.IterableUtils.transformedIterable(java.lang.Iterable<I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Iterable.__wrap(__IterableUtils.transformedIterable(arg0, arg1))

    @staticmethod
    @overload
    def find(arg0: 'Iterable', arg1: 'Predicate') -> object:
        """public static <E> E org.apache.commons.collections4.IterableUtils.find(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return object.__wrap(__IterableUtils.find(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def partition(arg0: 'Iterable', arg1: 'Factory', *arg2: 'Predicate') -> 'List':
        """public static <O,R extends java.util.Collection<O>> java.util.List<R> org.apache.commons.collections4.IterableUtils.partition(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Factory<R>,org.apache.commons.collections4.Predicate<? super O>...)"""
        return List.__wrap(__IterableUtils.partition(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def first(arg0: 'Iterable') -> object:
        """public static <T> T org.apache.commons.collections4.IterableUtils.first(java.lang.Iterable<T>)"""
        return object.__wrap(__IterableUtils.first(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def indexOf(arg0: 'Iterable', arg1: 'Predicate') -> int:
        """public static <E> int org.apache.commons.collections4.IterableUtils.indexOf(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return int.__wrap(__IterableUtils.indexOf(arg0, arg1))

    @staticmethod
    @overload
    def countMatches(arg0: 'Iterable', arg1: 'Predicate') -> int:
        """public static <E> long org.apache.commons.collections4.IterableUtils.countMatches(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return int.__wrap(__IterableUtils.countMatches(arg0, arg1))

    @staticmethod
    @overload
    def partition(arg0: 'Iterable', arg1: 'Predicate') -> 'List':
        """public static <O> java.util.List<java.util.List<O>> org.apache.commons.collections4.IterableUtils.partition(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>)"""
        return List.__wrap(__IterableUtils.partition(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'Iterable') -> bool:
        """public static boolean org.apache.commons.collections4.IterableUtils.isEmpty(java.lang.Iterable<?>)"""
        return bool.__wrap(__IterableUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def chainedIterable(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable.__wrap(__IterableUtils.chainedIterable(arg0, arg1, arg2))

    @staticmethod
    @overload
    def size(arg0: 'Iterable') -> int:
        """public static int org.apache.commons.collections4.IterableUtils.size(java.lang.Iterable<?>)"""
        return int.__wrap(__IterableUtils.size(arg0))

    @staticmethod
    @overload
    def chainedIterable(*arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>...)"""
        return Iterable.__wrap(__IterableUtils.chainedIterable(arg0))

    @staticmethod
    @overload
    def reversedIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.reversedIterable(java.lang.Iterable<E>)"""
        return Iterable.__wrap(__IterableUtils.reversedIterable(arg0))

    @staticmethod
    @overload
    def zippingIterable(arg0: 'Iterable', *arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.zippingIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>...)"""
        return Iterable.__wrap(__IterableUtils.zippingIterable(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: 'Iterable', arg1: 'Transformer') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IterableUtils.toString(java.lang.Iterable<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>)"""
        return str.__wrap(__IterableUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Iterable', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.IterableUtils.get(java.lang.Iterable<T>,int)"""
        return object.__wrap(__IterableUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toString(arg0: 'Iterable') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IterableUtils.toString(java.lang.Iterable<E>)"""
        return str.__wrap(__IterableUtils.toString(arg0))

    @staticmethod
    @overload
    def frequency(arg0: 'Iterable', arg1: object) -> int:
        """public static <E,T extends E> int org.apache.commons.collections4.IterableUtils.frequency(java.lang.Iterable<E>,T)"""
        return int.__wrap(__IterableUtils.frequency(arg0, arg1))

    @staticmethod
    @overload
    def toList(arg0: 'Iterable') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.IterableUtils.toList(java.lang.Iterable<E>)"""
        return List.__wrap(__IterableUtils.toList(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.IterableUtils()"""
        val = __IterableUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def chainedIterable(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Iterable', arg3: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable.__wrap(__IterableUtils.chainedIterable(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def collatedIterable(arg0: 'Comparator', arg1: 'Iterable', arg2: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.collatedIterable(java.util.Comparator<? super E>,java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable.__wrap(__IterableUtils.collatedIterable(arg0, arg1, arg2))

    @staticmethod
    @overload
    def toString(arg0: 'Iterable', arg1: 'Transformer', arg2: str, arg3: str, arg4: str) -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IterableUtils.toString(java.lang.Iterable<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>,java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__IterableUtils.toString(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def chainedIterable(arg0: 'Iterable', arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.chainedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable.__wrap(__IterableUtils.chainedIterable(arg0, arg1))

    @staticmethod
    @overload
    def uniqueIterable(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.uniqueIterable(java.lang.Iterable<E>)"""
        return Iterable.__wrap(__IterableUtils.uniqueIterable(arg0))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.emptyIfNull(java.lang.Iterable<E>)"""
        return Iterable.__wrap(__IterableUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def forEachButLast(arg0: 'Iterable', arg1: 'Closure') -> object:
        """public static <E> E org.apache.commons.collections4.IterableUtils.forEachButLast(java.lang.Iterable<E>,org.apache.commons.collections4.Closure<? super E>)"""
        return object.__wrap(__IterableUtils.forEachButLast(arg0, arg1))

    @staticmethod
    @overload
    def forEach(arg0: 'Iterable', arg1: 'Closure'):
        """public static <E> void org.apache.commons.collections4.IterableUtils.forEach(java.lang.Iterable<E>,org.apache.commons.collections4.Closure<? super E>)"""
        __IterableUtils.forEach(arg0, arg1)

    @staticmethod
    @overload
    def matchesAny(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.matchesAny(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool.__wrap(__IterableUtils.matchesAny(arg0, arg1))

    @staticmethod
    @overload
    def collatedIterable(arg0: 'Iterable', arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.collatedIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable.__wrap(__IterableUtils.collatedIterable(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def matchesAll(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.matchesAll(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool.__wrap(__IterableUtils.matchesAll(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def contains(arg0: 'Iterable', arg1: object, arg2: 'Equator') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IterableUtils.contains(java.lang.Iterable<? extends E>,E,org.apache.commons.collections4.Equator<? super E>)"""
        return bool.__wrap(__IterableUtils.contains(arg0, arg1, arg2))

    @staticmethod
    @overload
    def partition(arg0: 'Iterable', *arg1: 'Predicate') -> 'List':
        """public static <O> java.util.List<java.util.List<O>> org.apache.commons.collections4.IterableUtils.partition(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>...)"""
        return List.__wrap(__IterableUtils.partition(arg0, arg1))

    @staticmethod
    @overload
    def skippingIterable(arg0: 'Iterable', arg1: int) -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.skippingIterable(java.lang.Iterable<E>,long)"""
        return Iterable.__wrap(__IterableUtils.skippingIterable(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def zippingIterable(arg0: 'Iterable', arg1: 'Iterable') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.zippingIterable(java.lang.Iterable<? extends E>,java.lang.Iterable<? extends E>)"""
        return Iterable.__wrap(__IterableUtils.zippingIterable(arg0, arg1))

    @staticmethod
    @overload
    def filteredIterable(arg0: 'Iterable', arg1: 'Predicate') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IterableUtils.filteredIterable(java.lang.Iterable<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Iterable.__wrap(__IterableUtils.filteredIterable(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.IterableUtils()"""
        val = __IterableUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.Transformer
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
 
class Transformer(ABC):
    """org.apache.commons.collections4.Transformer"""
 
    @staticmethod
    def __wrap(java_value: __Transformer) -> 'Transformer':
        return Transformer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Transformer):
        """
        Dynamic initializer for Transformer.
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
    def transform(self, arg0: object):
        """public abstract O org.apache.commons.collections4.Transformer.transform(I)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.BoundedMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.lang.Object as __object
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.BoundedMap as __BoundedMap
__BoundedMap = __BoundedMap
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.IterableGet as __IterableGet
__IterableGet = __IterableGet
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class BoundedMap(ABC, __IterableMap, IterableMap):
    """org.apache.commons.collections4.BoundedMap"""
 
    @staticmethod
    def __wrap(java_value: __BoundedMap) -> 'BoundedMap':
        return BoundedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundedMap):
        """
        Dynamic initializer for BoundedMap.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def maxSize(self, ):
        """public abstract int org.apache.commons.collections4.BoundedMap.maxSize()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @abstractmethod
    def isFull(self, ):
        """public abstract boolean org.apache.commons.collections4.BoundedMap.isFull()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Unmodifiable
import org.apache.commons.collections4.Unmodifiable as __Unmodifiable
__Unmodifiable = __Unmodifiable
 
class Unmodifiable(ABC):
    """org.apache.commons.collections4.Unmodifiable"""
 
    @staticmethod
    def __wrap(java_value: __Unmodifiable) -> 'Unmodifiable':
        return Unmodifiable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Unmodifiable):
        """
        Dynamic initializer for Unmodifiable.
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
 
 
# CLASS: org.apache.commons.collections4.OrderedMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.lang.Object as __object
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class OrderedMap(ABC, __IterableMap, IterableMap):
    """org.apache.commons.collections4.OrderedMap"""
 
    @staticmethod
    def __wrap(java_value: __OrderedMap) -> 'OrderedMap':
        return OrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedMap):
        """
        Dynamic initializer for OrderedMap.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.KeyValue
import org.apache.commons.collections4.KeyValue as __KeyValue
__KeyValue = __KeyValue
from abc import abstractmethod, ABC
 
class KeyValue(ABC):
    """org.apache.commons.collections4.KeyValue"""
 
    @staticmethod
    def __wrap(java_value: __KeyValue) -> 'KeyValue':
        return KeyValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyValue):
        """
        Dynamic initializer for KeyValue.
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
    def getValue(self, ):
        """public abstract V org.apache.commons.collections4.KeyValue.getValue()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract K org.apache.commons.collections4.KeyValue.getKey()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.SetValuedMap
import org.apache.commons.collections4.SetValuedMap as __SetValuedMap
__SetValuedMap = __SetValuedMap
import java.lang.Iterable as Iterable
import org.apache.commons.collections4.MultiValuedMap as __MultiValuedMap
__MultiValuedMap = __MultiValuedMap
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class SetValuedMap(ABC, __MultiValuedMap, MultiValuedMap):
    """org.apache.commons.collections4.SetValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __SetValuedMap) -> 'SetValuedMap':
        return SetValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetValuedMap):
        """
        Dynamic initializer for SetValuedMap.
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
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.MultiValuedMap.mapIterator()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.util.Set<V> org.apache.commons.collections4.SetValuedMap.get(K)"""
        pass

    @abstractmethod
    def putAll(self, arg0: object, arg1: 'Iterable'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.MultiValuedMap.clear()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.values()"""
        pass

    @abstractmethod
    def containsMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.isEmpty()"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.MultiValuedMap.keys()"""
        pass

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.MultiValuedMap.entries()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.put(K,V)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.MultiValuedMap.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'MultiValuedMap'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiValuedMap.size()"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.MultiValuedMap.asMap()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.util.Set<V> org.apache.commons.collections4.SetValuedMap.remove(java.lang.Object)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.SortedBidiMap
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.lang.Object as __object
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.SortedBidiMap as __SortedBidiMap
__SortedBidiMap = __SortedBidiMap
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.function.Function as Function
import java.util.SequencedSet as SequencedSet
from builtins import bool
import java.util.Map as Map
 
class SortedBidiMap(ABC, __OrderedBidiMap, OrderedBidiMap, __SortedMap, SortedMap):
    """org.apache.commons.collections4.SortedBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __SortedBidiMap) -> 'SortedBidiMap':
        return SortedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedBidiMap):
        """
        Dynamic initializer for SortedBidiMap.
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
    def getKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.getKey(java.lang.Object)"""
        pass

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.SortedMap.entrySet()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Set<V> org.apache.commons.collections4.BidiMap.values()"""
        pass

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V org.apache.commons.collections4.BidiMap.put(K,V)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.SortedMap.keySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.SortedMap.values()"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @abstractmethod
    def valueComparator(self, ):
        """public abstract java.util.Comparator<? super V> org.apache.commons.collections4.SortedBidiMap.valueComparator()"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def removeValue(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.removeValue(java.lang.Object)"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def inverseBidiMap(self, ):
        """public abstract org.apache.commons.collections4.SortedBidiMap<V, K> org.apache.commons.collections4.SortedBidiMap.inverseBidiMap()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Equator
import org.apache.commons.collections4.Equator as __Equator
__Equator = __Equator
from abc import abstractmethod, ABC
 
class Equator(ABC):
    """org.apache.commons.collections4.Equator"""
 
    @staticmethod
    def __wrap(java_value: __Equator) -> 'Equator':
        return Equator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Equator):
        """
        Dynamic initializer for Equator.
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
    def equate(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.Equator.equate(T,T)"""
        pass

    @abstractmethod
    def hash(self, arg0: object):
        """public abstract int org.apache.commons.collections4.Equator.hash(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.EnumerationUtils
import org.apache.commons.collections4.EnumerationUtils as __EnumerationUtils
__EnumerationUtils = __EnumerationUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.Enumeration as Enumeration
import java.lang.Object as __Object
__Object = __Object
import java.util.StringTokenizer as StringTokenizer
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class EnumerationUtils():
    """org.apache.commons.collections4.EnumerationUtils"""
 
    @staticmethod
    def __wrap(java_value: __EnumerationUtils) -> 'EnumerationUtils':
        return EnumerationUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumerationUtils):
        """
        Dynamic initializer for EnumerationUtils.
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
    def toList(arg0: 'StringTokenizer') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.collections4.EnumerationUtils.toList(java.util.StringTokenizer)"""
        return List.__wrap(__EnumerationUtils.toList(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Enumeration', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.EnumerationUtils.get(java.util.Enumeration<T>,int)"""
        return object.__wrap(__EnumerationUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toList(arg0: 'Enumeration') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.EnumerationUtils.toList(java.util.Enumeration<? extends E>)"""
        return List.__wrap(__EnumerationUtils.toList(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.MapIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.function.Consumer as Consumer
 
class MapIterator(ABC, __Iterator, Iterator):
    """org.apache.commons.collections4.MapIterator"""
 
    @staticmethod
    def __wrap(java_value: __MapIterator) -> 'MapIterator':
        return MapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapIterator):
        """
        Dynamic initializer for MapIterator.
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
    def remove(self, ):
        """public abstract void org.apache.commons.collections4.MapIterator.remove()"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract V org.apache.commons.collections4.MapIterator.getValue()"""
        pass

    @abstractmethod
    def next(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.next()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract K org.apache.commons.collections4.MapIterator.getKey()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean org.apache.commons.collections4.MapIterator.hasNext()"""
        pass

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract V org.apache.commons.collections4.MapIterator.setValue(V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MultiSet$Entry
import org.apache.commons.collections4.MultiSet as __MultiSet_Entry
__Entry = __MultiSet_Entry.Entry
from abc import abstractmethod, ABC
 
class Entry(ABC):
    """org.apache.commons.collections4.MultiSet.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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
    def hashCode(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet$Entry.hashCode()"""
        pass

    @abstractmethod
    def getElement(self, ):
        """public abstract E org.apache.commons.collections4.MultiSet$Entry.getElement()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet$Entry.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def getCount(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet$Entry.getCount()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.ComparatorUtils
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import org.apache.commons.collections4.ComparatorUtils as __ComparatorUtils
__ComparatorUtils = __ComparatorUtils
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
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
 
class ComparatorUtils():
    """org.apache.commons.collections4.ComparatorUtils"""
 
    @staticmethod
    def __wrap(java_value: __ComparatorUtils) -> 'ComparatorUtils':
        return ComparatorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComparatorUtils):
        """
        Dynamic initializer for ComparatorUtils.
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
    def chainedComparator(*arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.chainedComparator(java.util.Comparator<E>...)"""
        return Comparator.__wrap(__ComparatorUtils.chainedComparator(arg0))

    @staticmethod
    @overload
    def nullHighComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.nullHighComparator(java.util.Comparator<E>)"""
        return Comparator.__wrap(__ComparatorUtils.nullHighComparator(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nullLowComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.nullLowComparator(java.util.Comparator<E>)"""
        return Comparator.__wrap(__ComparatorUtils.nullLowComparator(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def min(arg0: object, arg1: object, arg2: 'Comparator') -> object:
        """public static <E> E org.apache.commons.collections4.ComparatorUtils.min(E,E,java.util.Comparator<E>)"""
        return object.__wrap(__ComparatorUtils.min(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def reversedComparator(arg0: 'Comparator') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.reversedComparator(java.util.Comparator<E>)"""
        return Comparator.__wrap(__ComparatorUtils.reversedComparator(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def max(arg0: object, arg1: object, arg2: 'Comparator') -> object:
        """public static <E> E org.apache.commons.collections4.ComparatorUtils.max(E,E,java.util.Comparator<E>)"""
        return object.__wrap(__ComparatorUtils.max(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def naturalComparator() -> 'Comparator':
        """public static <E extends java.lang.Comparable<? super E>> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.naturalComparator()"""
        return Comparator.__wrap(__ComparatorUtils.naturalComparator())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def booleanComparator(arg0: bool) -> 'Comparator':
        """public static java.util.Comparator<java.lang.Boolean> org.apache.commons.collections4.ComparatorUtils.booleanComparator(boolean)"""
        return Comparator.__wrap(__ComparatorUtils.booleanComparator(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def transformedComparator(arg0: 'Comparator', arg1: 'Transformer') -> 'Comparator':
        """public static <I,O> java.util.Comparator<I> org.apache.commons.collections4.ComparatorUtils.transformedComparator(java.util.Comparator<O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Comparator.__wrap(__ComparatorUtils.transformedComparator(arg0, arg1))

    @staticmethod
    @overload
    def chainedComparator(arg0: 'Collection') -> 'Comparator':
        """public static <E> java.util.Comparator<E> org.apache.commons.collections4.ComparatorUtils.chainedComparator(java.util.Collection<java.util.Comparator<E>>)"""
        return Comparator.__wrap(__ComparatorUtils.chainedComparator(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.FactoryUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.Factory as __Factory
__Factory = __Factory
from builtins import type
from builtins import object
import org.apache.commons.collections4.FactoryUtils as __FactoryUtils
__FactoryUtils = __FactoryUtils
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
 
class FactoryUtils():
    """org.apache.commons.collections4.FactoryUtils"""
 
    @staticmethod
    def __wrap(java_value: __FactoryUtils) -> 'FactoryUtils':
        return FactoryUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FactoryUtils):
        """
        Dynamic initializer for FactoryUtils.
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
    def nullFactory() -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.nullFactory()"""
        return Factory.__wrap(__FactoryUtils.nullFactory())

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
    def instantiateFactory(arg0: 'Class', arg1: 'Class', arg2: 'Object') -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.instantiateFactory(java.lang.Class<T>,java.lang.Class<?>[],java.lang.Object[])"""
        return Factory.__wrap(__FactoryUtils.instantiateFactory(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def constantFactory(arg0: object) -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.constantFactory(T)"""
        return Factory.__wrap(__FactoryUtils.constantFactory(arg0))

    @staticmethod
    @overload
    def instantiateFactory(arg0: 'Class') -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.instantiateFactory(java.lang.Class<T>)"""
        return Factory.__wrap(__FactoryUtils.instantiateFactory(arg0))

    @staticmethod
    @overload
    def exceptionFactory() -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.exceptionFactory()"""
        return Factory.__wrap(__FactoryUtils.exceptionFactory())

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

    @staticmethod
    @overload
    def prototypeFactory(arg0: object) -> 'Factory':
        """public static <T> org.apache.commons.collections4.Factory<T> org.apache.commons.collections4.FactoryUtils.prototypeFactory(T)"""
        return Factory.__wrap(__FactoryUtils.prototypeFactory(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.Closure
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from abc import abstractmethod, ABC
 
class Closure(ABC):
    """org.apache.commons.collections4.Closure"""
 
    @staticmethod
    def __wrap(java_value: __Closure) -> 'Closure':
        return Closure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Closure):
        """
        Dynamic initializer for Closure.
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
    def execute(self, arg0: object):
        """public abstract void org.apache.commons.collections4.Closure.execute(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.CollectionUtils
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Map.Entry as Entry
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.util.Enumeration as Enumeration
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.CollectionUtils as __CollectionUtils
__CollectionUtils = __CollectionUtils
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class CollectionUtils():
    """org.apache.commons.collections4.CollectionUtils"""
 
    @staticmethod
    def __wrap(java_value: __CollectionUtils) -> 'CollectionUtils':
        return CollectionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectionUtils):
        """
        Dynamic initializer for CollectionUtils.
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
    def collate(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Comparator') -> 'List':
        """public static <O> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,java.util.Comparator<? super O>)"""
        return List.__wrap(__CollectionUtils.collate(arg0, arg1, arg2))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Comparator', arg3: bool) -> 'List':
        """public static <O> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,java.util.Comparator<? super O>,boolean)"""
        return List.__wrap(__CollectionUtils.collate(arg0, arg1, arg2, __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def isFull(arg0: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isFull(java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.isFull(arg0))

    @staticmethod
    @overload
    def permutations(arg0: 'Collection') -> 'Collection':
        """public static <E> java.util.Collection<java.util.List<E>> org.apache.commons.collections4.CollectionUtils.permutations(java.util.Collection<E>)"""
        return Collection.__wrap(__CollectionUtils.permutations(arg0))

    @staticmethod
    @overload
    def collect(arg0: 'Iterable', arg1: 'Transformer', arg2: 'Collection') -> 'Collection':
        """public static <I,O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.collect(java.lang.Iterable<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,R)"""
        return Collection.__wrap(__CollectionUtils.collect(arg0, arg1, arg2))

    @staticmethod
    @overload
    def sizeIsEmpty(arg0: object) -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.sizeIsEmpty(java.lang.Object)"""
        return bool.__wrap(__CollectionUtils.sizeIsEmpty(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def addIgnoreNull(arg0: 'Collection', arg1: object) -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.addIgnoreNull(java.util.Collection<T>,T)"""
        return bool.__wrap(__CollectionUtils.addIgnoreNull(arg0, arg1))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable') -> 'List':
        """public static <O extends java.lang.Comparable<? super O>> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return List.__wrap(__CollectionUtils.collate(arg0, arg1))

    @staticmethod
    @overload
    def union(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.union(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection.__wrap(__CollectionUtils.union(arg0, arg1))

    @staticmethod
    @overload
    def collect(arg0: 'Iterator', arg1: 'Transformer') -> 'Collection':
        """public static <I,O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.collect(java.util.Iterator<I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Collection.__wrap(__CollectionUtils.collect(arg0, arg1))

    @staticmethod
    @overload
    def disjunction(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.disjunction(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection.__wrap(__CollectionUtils.disjunction(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isEmpty(arg0: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isEmpty(java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def forAllButLastDo(arg0: 'Iterable', arg1: 'Closure') -> object:
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> T org.apache.commons.collections4.CollectionUtils.forAllButLastDo(java.lang.Iterable<T>,C)"""
        return object.__wrap(__CollectionUtils.forAllButLastDo(arg0, arg1))

    @staticmethod
    @overload
    def collate(arg0: 'Iterable', arg1: 'Iterable', arg2: bool) -> 'List':
        """public static <O extends java.lang.Comparable<? super O>> java.util.List<O> org.apache.commons.collections4.CollectionUtils.collate(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,boolean)"""
        return List.__wrap(__CollectionUtils.collate(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def isProperSubCollection(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isProperSubCollection(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.isProperSubCollection(arg0, arg1))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.predicatedCollection(java.util.Collection<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return Collection.__wrap(__CollectionUtils.predicatedCollection(arg0, arg1))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', arg1: 'Iterator') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,java.util.Iterator<? extends C>)"""
        return bool.__wrap(__CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableCollection(arg0: 'Collection') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.unmodifiableCollection(java.util.Collection<? extends C>)"""
        return Collection.__wrap(__CollectionUtils.unmodifiableCollection(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def collect(arg0: 'Iterator', arg1: 'Transformer', arg2: 'Collection') -> 'Collection':
        """public static <I,O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.collect(java.util.Iterator<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,R)"""
        return Collection.__wrap(__CollectionUtils.collect(arg0, arg1, arg2))

    @staticmethod
    @overload
    def removeAll(arg0: 'Collection', arg1: 'Collection') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.removeAll(java.util.Collection<E>,java.util.Collection<?>)"""
        return Collection.__wrap(__CollectionUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def select(arg0: 'Iterable', arg1: 'Predicate', arg2: 'Collection') -> 'Collection':
        """public static <O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.select(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>,R)"""
        return Collection.__wrap(__CollectionUtils.select(arg0, arg1, arg2))

    @staticmethod
    @overload
    def retainAll(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Equator') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.retainAll(java.lang.Iterable<E>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Equator<? super E>)"""
        return Collection.__wrap(__CollectionUtils.retainAll(arg0, arg1, arg2))

    @staticmethod
    @overload
    def forAllDo(arg0: 'Iterable', arg1: 'Closure') -> 'Closure':
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> C org.apache.commons.collections4.CollectionUtils.forAllDo(java.lang.Iterable<T>,C)"""
        return Closure.__wrap(__CollectionUtils.forAllDo(arg0, arg1))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', arg1: 'Enumeration') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,java.util.Enumeration<? extends C>)"""
        return bool.__wrap(__CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: object, arg1: int) -> object:
        """public static java.lang.Object org.apache.commons.collections4.CollectionUtils.get(java.lang.Object,int)"""
        return object.__wrap(__CollectionUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def containsAll(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.containsAll(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.containsAll(arg0, arg1))

    @staticmethod
    @overload
    def isSubCollection(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isSubCollection(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.isSubCollection(arg0, arg1))

    @staticmethod
    @overload
    def isEqualCollection(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isEqualCollection(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.isEqualCollection(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Map', arg1: int) -> 'Entry.Map$Entry':
        """public static <K,V> java.util.Map$Entry<K, V> org.apache.commons.collections4.CollectionUtils.get(java.util.Map<K, V>,int)"""
        return Entry.Map$Entry.__wrap(__CollectionUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def synchronizedCollection(arg0: 'Collection') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.synchronizedCollection(java.util.Collection<C>)"""
        return Collection.__wrap(__CollectionUtils.synchronizedCollection(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def cardinality(arg0: object, arg1: 'Iterable') -> int:
        """public static <O> int org.apache.commons.collections4.CollectionUtils.cardinality(O,java.lang.Iterable<? super O>)"""
        return int.__wrap(__CollectionUtils.cardinality(arg0, arg1))

    @staticmethod
    @overload
    def extractSingleton(arg0: 'Collection') -> object:
        """public static <E> E org.apache.commons.collections4.CollectionUtils.extractSingleton(java.util.Collection<E>)"""
        return object.__wrap(__CollectionUtils.extractSingleton(arg0))

    @staticmethod
    @overload
    def filterInverse(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.filterInverse(java.lang.Iterable<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return bool.__wrap(__CollectionUtils.filterInverse(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def forAllDo(arg0: 'Iterator', arg1: 'Closure') -> 'Closure':
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> C org.apache.commons.collections4.CollectionUtils.forAllDo(java.util.Iterator<T>,C)"""
        return Closure.__wrap(__CollectionUtils.forAllDo(arg0, arg1))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Collection') -> 'Collection':
        """public static <T> java.util.Collection<T> org.apache.commons.collections4.CollectionUtils.emptyIfNull(java.util.Collection<T>)"""
        return Collection.__wrap(__CollectionUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def select(arg0: 'Iterable', arg1: 'Predicate') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.select(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>)"""
        return Collection.__wrap(__CollectionUtils.select(arg0, arg1))

    @staticmethod
    @overload
    def getCardinalityMap(arg0: 'Iterable') -> 'Map':
        """public static <O> java.util.Map<O, java.lang.Integer> org.apache.commons.collections4.CollectionUtils.getCardinalityMap(java.lang.Iterable<? extends O>)"""
        return Map.__wrap(__CollectionUtils.getCardinalityMap(arg0))

    @staticmethod
    @overload
    def isEqualCollection(arg0: 'Collection', arg1: 'Collection', arg2: 'Equator') -> bool:
        """public static <E> boolean org.apache.commons.collections4.CollectionUtils.isEqualCollection(java.util.Collection<? extends E>,java.util.Collection<? extends E>,org.apache.commons.collections4.Equator<? super E>)"""
        return bool.__wrap(__CollectionUtils.isEqualCollection(arg0, arg1, arg2))

    @staticmethod
    @overload
    def selectRejected(arg0: 'Iterable', arg1: 'Predicate', arg2: 'Collection') -> 'Collection':
        """public static <O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.selectRejected(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>,R)"""
        return Collection.__wrap(__CollectionUtils.selectRejected(arg0, arg1, arg2))

    @staticmethod
    @overload
    def countMatches(arg0: 'Iterable', arg1: 'Predicate') -> int:
        """public static <C> int org.apache.commons.collections4.CollectionUtils.countMatches(java.lang.Iterable<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return int.__wrap(__CollectionUtils.countMatches(arg0, arg1))

    @staticmethod
    @overload
    def removeAll(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Equator') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.removeAll(java.lang.Iterable<E>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Equator<? super E>)"""
        return Collection.__wrap(__CollectionUtils.removeAll(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def subtract(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.subtract(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection.__wrap(__CollectionUtils.subtract(arg0, arg1))

    @staticmethod
    @overload
    def select(arg0: 'Iterable', arg1: 'Predicate', arg2: 'Collection', arg3: 'Collection') -> 'Collection':
        """public static <O,R extends java.util.Collection<? super O>> R org.apache.commons.collections4.CollectionUtils.select(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>,R,R)"""
        return Collection.__wrap(__CollectionUtils.select(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def filter(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.filter(java.lang.Iterable<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return bool.__wrap(__CollectionUtils.filter(arg0, arg1))

    @staticmethod
    @overload
    def containsAny(arg0: 'Collection', *arg1: object) -> bool:
        """public static <T> boolean org.apache.commons.collections4.CollectionUtils.containsAny(java.util.Collection<?>,T...)"""
        return bool.__wrap(__CollectionUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def collect(arg0: 'Iterable', arg1: 'Transformer') -> 'Collection':
        """public static <I,O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.collect(java.lang.Iterable<I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Collection.__wrap(__CollectionUtils.collect(arg0, arg1))

    @staticmethod
    @overload
    def intersection(arg0: 'Iterable', arg1: 'Iterable') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.intersection(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>)"""
        return Collection.__wrap(__CollectionUtils.intersection(arg0, arg1))

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'Collection':
        """public static <E> java.util.Collection<E> org.apache.commons.collections4.CollectionUtils.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Collection.__wrap(__CollectionUtils.transformingCollection(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Iterable', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.CollectionUtils.get(java.lang.Iterable<T>,int)"""
        return object.__wrap(__CollectionUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def retainAll(arg0: 'Collection', arg1: 'Collection') -> 'Collection':
        """public static <C> java.util.Collection<C> org.apache.commons.collections4.CollectionUtils.retainAll(java.util.Collection<C>,java.util.Collection<?>)"""
        return Collection.__wrap(__CollectionUtils.retainAll(arg0, arg1))

    @staticmethod
    @overload
    def emptyCollection() -> 'Collection':
        """public static <T> java.util.Collection<T> org.apache.commons.collections4.CollectionUtils.emptyCollection()"""
        return Collection.__wrap(__CollectionUtils.emptyCollection())

    @staticmethod
    @overload
    def forAllButLastDo(arg0: 'Iterator', arg1: 'Closure') -> object:
        """public static <T,C extends org.apache.commons.collections4.Closure<? super T>> T org.apache.commons.collections4.CollectionUtils.forAllButLastDo(java.util.Iterator<T>,C)"""
        return object.__wrap(__CollectionUtils.forAllButLastDo(arg0, arg1))

    @staticmethod
    @overload
    def subtract(arg0: 'Iterable', arg1: 'Iterable', arg2: 'Predicate') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.subtract(java.lang.Iterable<? extends O>,java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<O>)"""
        return Collection.__wrap(__CollectionUtils.subtract(arg0, arg1, arg2))

    @staticmethod
    @overload
    def containsAny(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.containsAny(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.containsAny(arg0, arg1))

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.CollectionUtils.isNotEmpty(java.util.Collection<?>)"""
        return bool.__wrap(__CollectionUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def matchesAll(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.matchesAll(java.lang.Iterable<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return bool.__wrap(__CollectionUtils.matchesAll(arg0, arg1))

    @staticmethod
    @overload
    def size(arg0: object) -> int:
        """public static int org.apache.commons.collections4.CollectionUtils.size(java.lang.Object)"""
        return int.__wrap(__CollectionUtils.size(arg0))

    @staticmethod
    @overload
    def find(arg0: 'Iterable', arg1: 'Predicate') -> object:
        """public static <T> T org.apache.commons.collections4.CollectionUtils.find(java.lang.Iterable<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return object.__wrap(__CollectionUtils.find(arg0, arg1))

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', arg1: 'Iterable') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,java.lang.Iterable<? extends C>)"""
        return bool.__wrap(__CollectionUtils.addAll(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def selectRejected(arg0: 'Iterable', arg1: 'Predicate') -> 'Collection':
        """public static <O> java.util.Collection<O> org.apache.commons.collections4.CollectionUtils.selectRejected(java.lang.Iterable<? extends O>,org.apache.commons.collections4.Predicate<? super O>)"""
        return Collection.__wrap(__CollectionUtils.selectRejected(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def maxSize(arg0: 'Collection') -> int:
        """public static int org.apache.commons.collections4.CollectionUtils.maxSize(java.util.Collection<?>)"""
        return int.__wrap(__CollectionUtils.maxSize(arg0))

    @staticmethod
    @overload
    def transform(arg0: 'Collection', arg1: 'Transformer'):
        """public static <C> void org.apache.commons.collections4.CollectionUtils.transform(java.util.Collection<C>,org.apache.commons.collections4.Transformer<? super C, ? extends C>)"""
        __CollectionUtils.transform(arg0, arg1)

    @staticmethod
    @overload
    def addAll(arg0: 'Collection', *arg1: object) -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.addAll(java.util.Collection<C>,C...)"""
        return bool.__wrap(__CollectionUtils.addAll(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Iterator', arg1: int) -> object:
        """public static <T> T org.apache.commons.collections4.CollectionUtils.get(java.util.Iterator<T>,int)"""
        return object.__wrap(__CollectionUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def reverseArray(arg0: 'Object'):
        """public static void org.apache.commons.collections4.CollectionUtils.reverseArray(java.lang.Object[])"""
        __CollectionUtils.reverseArray(arg0)

    @staticmethod
    @overload
    def exists(arg0: 'Iterable', arg1: 'Predicate') -> bool:
        """public static <C> boolean org.apache.commons.collections4.CollectionUtils.exists(java.lang.Iterable<C>,org.apache.commons.collections4.Predicate<? super C>)"""
        return bool.__wrap(__CollectionUtils.exists(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.Bag
import java.util.function.Predicate as Predicate
import java.util.function.IntFunction as IntFunction
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
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
 
class Bag(ABC, __Collection, Collection):
    """org.apache.commons.collections4.Bag"""
 
    @staticmethod
    def __wrap(java_value: __Bag) -> 'Bag':
        return Bag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Bag):
        """
        Dynamic initializer for Bag.
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
    def add(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E,int)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def uniqueSet(self, ):
        """public abstract java.util.Set<E> org.apache.commons.collections4.Bag.uniqueSet()"""
        pass

    @abstractmethod
    def getCount(self, arg0: object):
        """public abstract int org.apache.commons.collections4.Bag.getCount(java.lang.Object)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.containsAll(java.util.Collection<?>)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def remove(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object,int)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Bag.size()"""
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
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
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
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.retainAll(java.util.Collection<?>)"""
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
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> org.apache.commons.collections4.Bag.iterator()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.IterableGet
import org.apache.commons.collections4.IterableGet as __IterableGet
__IterableGet = __IterableGet
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
 
class IterableGet(ABC, __Get, Get):
    """org.apache.commons.collections4.IterableGet"""
 
    @staticmethod
    def __wrap(java_value: __IterableGet) -> 'IterableGet':
        return IterableGet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IterableGet):
        """
        Dynamic initializer for IterableGet.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.SplitMapUtils
from builtins import str
import org.apache.commons.collections4.IterableMap as __IterableMap
__IterableMap = __IterableMap
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.SplitMapUtils as __SplitMapUtils
__SplitMapUtils = __SplitMapUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class SplitMapUtils():
    """org.apache.commons.collections4.SplitMapUtils"""
 
    @staticmethod
    def __wrap(java_value: __SplitMapUtils) -> 'SplitMapUtils':
        return SplitMapUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SplitMapUtils):
        """
        Dynamic initializer for SplitMapUtils.
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
    def readableMap(arg0: 'Get') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.SplitMapUtils.readableMap(org.apache.commons.collections4.Get<K, V>)"""
        return IterableMap.__wrap(__SplitMapUtils.readableMap(arg0))

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
    def writableMap(arg0: 'Put') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.SplitMapUtils.writableMap(org.apache.commons.collections4.Put<K, V>)"""
        return Map.__wrap(__SplitMapUtils.writableMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.SortedBag
import java.util.function.Predicate as Predicate
import java.util.function.IntFunction as IntFunction
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.SortedBag as __SortedBag
__SortedBag = __SortedBag
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SortedBag(ABC, __Bag, Bag):
    """org.apache.commons.collections4.SortedBag"""
 
    @staticmethod
    def __wrap(java_value: __SortedBag) -> 'SortedBag':
        return SortedBag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedBag):
        """
        Dynamic initializer for SortedBag.
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
    def add(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E,int)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def uniqueSet(self, ):
        """public abstract java.util.Set<E> org.apache.commons.collections4.Bag.uniqueSet()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super E> org.apache.commons.collections4.SortedBag.comparator()"""
        pass

    @abstractmethod
    def getCount(self, arg0: object):
        """public abstract int org.apache.commons.collections4.Bag.getCount(java.lang.Object)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.containsAll(java.util.Collection<?>)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def remove(self, arg0: object, arg1: int):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object,int)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Bag.size()"""
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
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def first(self, ):
        """public abstract E org.apache.commons.collections4.SortedBag.first()"""
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
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.Bag.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def last(self, ):
        """public abstract E org.apache.commons.collections4.SortedBag.last()"""
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
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.add(E)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> org.apache.commons.collections4.Bag.iterator()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Bag.remove(java.lang.Object)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.IterableSortedMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.lang.Object as __object
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import org.apache.commons.collections4.IterableSortedMap as __IterableSortedMap
__IterableSortedMap = __IterableSortedMap
import java.util.SortedMap as SortedMap
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class IterableSortedMap(ABC, __SortedMap, SortedMap, __OrderedMap, OrderedMap):
    """org.apache.commons.collections4.IterableSortedMap"""
 
    @staticmethod
    def __wrap(java_value: __IterableSortedMap) -> 'IterableSortedMap':
        return IterableSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IterableSortedMap):
        """
        Dynamic initializer for IterableSortedMap.
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
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.SortedMap.entrySet()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.SortedMap.keySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.SortedMap.values()"""
        pass

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.QueueUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.QueueUtils as __QueueUtils
__QueueUtils = __QueueUtils
import java.util.Queue as Queue
import java.util.Queue as __Queue
__Queue = __Queue
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
 
class QueueUtils():
    """org.apache.commons.collections4.QueueUtils"""
 
    @staticmethod
    def __wrap(java_value: __QueueUtils) -> 'QueueUtils':
        return QueueUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QueueUtils):
        """
        Dynamic initializer for QueueUtils.
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
    def transformingQueue(arg0: 'Queue', arg1: 'Transformer') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.transformingQueue(java.util.Queue<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Queue.__wrap(__QueueUtils.transformingQueue(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableQueue(arg0: 'Queue') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.unmodifiableQueue(java.util.Queue<? extends E>)"""
        return Queue.__wrap(__QueueUtils.unmodifiableQueue(arg0))

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
    def synchronizedQueue(arg0: 'Queue') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.synchronizedQueue(java.util.Queue<E>)"""
        return Queue.__wrap(__QueueUtils.synchronizedQueue(arg0))

    @staticmethod
    @overload
    def predicatedQueue(arg0: 'Queue', arg1: 'Predicate') -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.predicatedQueue(java.util.Queue<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Queue.__wrap(__QueueUtils.predicatedQueue(arg0, arg1))

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
    def emptyQueue() -> 'Queue':
        """public static <E> java.util.Queue<E> org.apache.commons.collections4.QueueUtils.emptyQueue()"""
        return Queue.__wrap(__QueueUtils.emptyQueue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.FunctorException
from builtins import str
from pyquantum_helper import override
import org.apache.commons.collections4.FunctorException as __FunctorException
__FunctorException = __FunctorException
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
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FunctorException(__RuntimeException, RuntimeException):
    """org.apache.commons.collections4.FunctorException"""
 
    @staticmethod
    def __wrap(java_value: __FunctorException) -> 'FunctorException':
        return FunctorException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FunctorException):
        """
        Dynamic initializer for FunctorException.
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

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.collections4.FunctorException(java.lang.String)"""
        val = __FunctorException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.collections4.FunctorException(java.lang.Throwable)"""
        val = __FunctorException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public org.apache.commons.collections4.FunctorException()"""
        val = __FunctorException()
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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.collections4.FunctorException(java.lang.String,java.lang.Throwable)"""
        val = __FunctorException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.FunctorException()"""
        val = __FunctorException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.collections4.SetUtils$SetView
import java.util.function.Predicate as Predicate
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
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
from builtins import bool
import java.util.AbstractSet as __AbstractSet
__AbstractSet = __AbstractSet
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.SetUtils as __SetUtils_SetView
__SetView = __SetUtils_SetView.SetView
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class SetView(ABC, __AbstractSet, AbstractSet):
    """org.apache.commons.collections4.SetUtils.SetView"""
 
    @staticmethod
    def __wrap(java_value: __SetView) -> 'SetView':
        return SetView(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetView):
        """
        Dynamic initializer for SetView.
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
    def toSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.SetUtils$SetView.toSet()"""
        return 'Set'.__wrap(super(SetView, self).toSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.SetUtils$SetView()"""
        val = __SetView()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.add(E)"""
        return bool.__wrap(super(__AbstractCollection, self).add(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.SetUtils$SetView.iterator()"""
        return 'Iterator'.__wrap(super(SetView, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.SetUtils$SetView()"""
        val = __SetView()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.SetUtils$SetView.size()"""
        return int.__wrap(super(SetView, self).size())

    @override
    @overload
    def clear(self):
        """public void java.util.AbstractCollection.clear()"""
        super(AbstractCollection, self).clear()

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.remove(java.lang.Object)"""
        return bool.__wrap(super(__AbstractCollection, self).remove(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @overload
    def copyInto(self, arg0: 'Set'):
        """public <S extends java.util.Set<E>> void org.apache.commons.collections4.SetUtils$SetView.copyInto(S)"""
        super(__SetView, self).copyInto(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.AbstractCollection.contains(java.lang.Object)"""
        return bool.__wrap(super(__AbstractCollection, self).contains(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.BagUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
import org.apache.commons.collections4.BagUtils as __BagUtils
__BagUtils = __BagUtils
import org.apache.commons.collections4.SortedBag as __SortedBag
__SortedBag = __SortedBag
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
 
class BagUtils():
    """org.apache.commons.collections4.BagUtils"""
 
    @staticmethod
    def __wrap(java_value: __BagUtils) -> 'BagUtils':
        return BagUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BagUtils):
        """
        Dynamic initializer for BagUtils.
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
    def emptyBag() -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.emptyBag()"""
        return Bag.__wrap(__BagUtils.emptyBag())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def collectionBag(arg0: 'Bag') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.collectionBag(org.apache.commons.collections4.Bag<E>)"""
        return Bag.__wrap(__BagUtils.collectionBag(arg0))

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

    @staticmethod
    @overload
    def unmodifiableSortedBag(arg0: 'SortedBag') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.unmodifiableSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return SortedBag.__wrap(__BagUtils.unmodifiableSortedBag(arg0))

    @staticmethod
    @overload
    def synchronizedSortedBag(arg0: 'SortedBag') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.synchronizedSortedBag(org.apache.commons.collections4.SortedBag<E>)"""
        return SortedBag.__wrap(__BagUtils.synchronizedSortedBag(arg0))

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
    def transformingBag(arg0: 'Bag', arg1: 'Transformer') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.transformingBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Bag.__wrap(__BagUtils.transformingBag(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedBag(arg0: 'Bag') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.synchronizedBag(org.apache.commons.collections4.Bag<E>)"""
        return Bag.__wrap(__BagUtils.synchronizedBag(arg0))

    @staticmethod
    @overload
    def predicatedSortedBag(arg0: 'SortedBag', arg1: 'Predicate') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.predicatedSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return SortedBag.__wrap(__BagUtils.predicatedSortedBag(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def unmodifiableBag(arg0: 'Bag') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.unmodifiableBag(org.apache.commons.collections4.Bag<? extends E>)"""
        return Bag.__wrap(__BagUtils.unmodifiableBag(arg0))

    @staticmethod
    @overload
    def transformingSortedBag(arg0: 'SortedBag', arg1: 'Transformer') -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.transformingSortedBag(org.apache.commons.collections4.SortedBag<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return SortedBag.__wrap(__BagUtils.transformingSortedBag(arg0, arg1))

    @staticmethod
    @overload
    def predicatedBag(arg0: 'Bag', arg1: 'Predicate') -> 'Bag':
        """public static <E> org.apache.commons.collections4.Bag<E> org.apache.commons.collections4.BagUtils.predicatedBag(org.apache.commons.collections4.Bag<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Bag.__wrap(__BagUtils.predicatedBag(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def emptySortedBag() -> 'SortedBag':
        """public static <E> org.apache.commons.collections4.SortedBag<E> org.apache.commons.collections4.BagUtils.emptySortedBag()"""
        return SortedBag.__wrap(__BagUtils.emptySortedBag())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.FluentIterable
import java.util.Enumeration as __Enumeration
__Enumeration = __Enumeration
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.FluentIterable as __FluentIterable
__FluentIterable = __FluentIterable
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.util.Enumeration as Enumeration
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class FluentIterable(__Iterable, Iterable):
    """org.apache.commons.collections4.FluentIterable"""
 
    @staticmethod
    def __wrap(java_value: __FluentIterable) -> 'FluentIterable':
        return FluentIterable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FluentIterable):
        """
        Dynamic initializer for FluentIterable.
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
    def unique(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.unique()"""
        return 'FluentIterable'.__wrap(super(FluentIterable, self).unique())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def limit(self, arg0: int) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.limit(long)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).limit(__long.valueOf(arg0)))

    @overload
    def unmodifiable(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.unmodifiable()"""
        return 'FluentIterable'.__wrap(super(FluentIterable, self).unmodifiable())

    @staticmethod
    @overload
    def of(*arg0: object) -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.of(T...)"""
        return FluentIterable.__wrap(__FluentIterable.of(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.contains(java.lang.Object)"""
        return bool.__wrap(super(__FluentIterable, self).contains(arg0))

    @overload
    def anyMatch(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.anyMatch(org.apache.commons.collections4.Predicate<? super E>)"""
        return bool.__wrap(super(__FluentIterable, self).anyMatch(arg0))

    @overload
    def collate(self, arg0: 'Iterable', arg1: 'Comparator') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.collate(java.lang.Iterable<? extends E>,java.util.Comparator<? super E>)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).collate(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def collate(self, arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.collate(java.lang.Iterable<? extends E>)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).collate(arg0))

    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.FluentIterable.size()"""
        return int.__wrap(super(FluentIterable, self).size())

    @overload
    def reverse(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.reverse()"""
        return 'FluentIterable'.__wrap(super(FluentIterable, self).reverse())

    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.isEmpty()"""
        return bool.__wrap(super(FluentIterable, self).isEmpty())

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.FluentIterable.get(int)"""
        return object.__wrap(super(__FluentIterable, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toList(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.FluentIterable.toList()"""
        return 'List'.__wrap(super(FluentIterable, self).toList())

    @overload
    def transform(self, arg0: 'Transformer') -> 'FluentIterable':
        """public <O> org.apache.commons.collections4.FluentIterable<O> org.apache.commons.collections4.FluentIterable.transform(org.apache.commons.collections4.Transformer<? super E, ? extends O>)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).transform(arg0))

    @overload
    def zip(self, arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.zip(java.lang.Iterable<? extends E>)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).zip(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.FluentIterable.toString()"""
        return str.__wrap(super(FluentIterable, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def copyInto(self, arg0: 'Collection'):
        """public void org.apache.commons.collections4.FluentIterable.copyInto(java.util.Collection<? super E>)"""
        super(__FluentIterable, self).copyInto(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def loop(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.loop()"""
        return 'FluentIterable'.__wrap(super(FluentIterable, self).loop())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def zip(self, *arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.zip(java.lang.Iterable<? extends E>...)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).zip(arg0))

    @overload
    def asEnumeration(self) -> 'Enumeration':
        """public java.util.Enumeration<E> org.apache.commons.collections4.FluentIterable.asEnumeration()"""
        return 'Enumeration'.__wrap(super(FluentIterable, self).asEnumeration())

    @overload
    def skip(self, arg0: int) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.skip(long)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).skip(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def of(arg0: 'Iterable') -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.of(java.lang.Iterable<T>)"""
        return FluentIterable.__wrap(__FluentIterable.of(arg0))

    @overload
    def append(self, arg0: 'Iterable') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.append(java.lang.Iterable<? extends E>)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).append(arg0))

    @overload
    def forEach(self, arg0: 'Closure'):
        """public void org.apache.commons.collections4.FluentIterable.forEach(org.apache.commons.collections4.Closure<? super E>)"""
        super(__FluentIterable, self).forEach(arg0)

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
    def allMatch(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.FluentIterable.allMatch(org.apache.commons.collections4.Predicate<? super E>)"""
        return bool.__wrap(super(__FluentIterable, self).allMatch(arg0))

    @overload
    def filter(self, arg0: 'Predicate') -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.filter(org.apache.commons.collections4.Predicate<? super E>)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).filter(arg0))

    @overload
    def toArray(self, arg0: 'Class') -> List[object]:
        """public E[] org.apache.commons.collections4.FluentIterable.toArray(java.lang.Class<E>)"""
        return List[object].__wrap(super(__FluentIterable, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.FluentIterable.iterator()"""
        return 'Iterator'.__wrap(super(FluentIterable, self).iterator())

    @overload
    def eval(self) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.eval()"""
        return 'FluentIterable'.__wrap(super(FluentIterable, self).eval())

    @staticmethod
    @overload
    def of(arg0: object) -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.of(T)"""
        return FluentIterable.__wrap(__FluentIterable.of(arg0))

    @overload
    def append(self, *arg0: object) -> 'FluentIterable':
        """public org.apache.commons.collections4.FluentIterable<E> org.apache.commons.collections4.FluentIterable.append(E...)"""
        return 'FluentIterable'.__wrap(super(__FluentIterable, self).append(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @staticmethod
    @overload
    def empty() -> 'FluentIterable':
        """public static <T> org.apache.commons.collections4.FluentIterable<T> org.apache.commons.collections4.FluentIterable.empty()"""
        return FluentIterable.__wrap(__FluentIterable.empty()) 
 
 
# CLASS: org.apache.commons.collections4.PredicateUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
import org.apache.commons.collections4.PredicateUtils as __PredicateUtils
__PredicateUtils = __PredicateUtils
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
 
class PredicateUtils():
    """org.apache.commons.collections4.PredicateUtils"""
 
    @staticmethod
    def __wrap(java_value: __PredicateUtils) -> 'PredicateUtils':
        return PredicateUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicateUtils):
        """
        Dynamic initializer for PredicateUtils.
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
    def exceptionPredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.exceptionPredicate()"""
        return Predicate.__wrap(__PredicateUtils.exceptionPredicate())

    @staticmethod
    @overload
    def nullIsExceptionPredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullIsExceptionPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.nullIsExceptionPredicate(arg0))

    @staticmethod
    @overload
    def falsePredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.falsePredicate()"""
        return Predicate.__wrap(__PredicateUtils.falsePredicate())

    @staticmethod
    @overload
    def uniquePredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.uniquePredicate()"""
        return Predicate.__wrap(__PredicateUtils.uniquePredicate())

    @staticmethod
    @overload
    def eitherPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.eitherPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.eitherPredicate(arg0, arg1))

    @staticmethod
    @overload
    def nonePredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nonePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate.__wrap(__PredicateUtils.nonePredicate(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def truePredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.truePredicate()"""
        return Predicate.__wrap(__PredicateUtils.truePredicate())

    @staticmethod
    @overload
    def allPredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.allPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate.__wrap(__PredicateUtils.allPredicate(arg0))

    @staticmethod
    @overload
    def notNullPredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.notNullPredicate()"""
        return Predicate.__wrap(__PredicateUtils.notNullPredicate())

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
    def notPredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.notPredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.notPredicate(arg0))

    @staticmethod
    @overload
    def nullPredicate() -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullPredicate()"""
        return Predicate.__wrap(__PredicateUtils.nullPredicate())

    @staticmethod
    @overload
    def andPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.andPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.andPredicate(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def neitherPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.neitherPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.neitherPredicate(arg0, arg1))

    @staticmethod
    @overload
    def nullIsTruePredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullIsTruePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.nullIsTruePredicate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def asPredicate(arg0: 'Transformer') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.asPredicate(org.apache.commons.collections4.Transformer<? super T, java.lang.Boolean>)"""
        return Predicate.__wrap(__PredicateUtils.asPredicate(arg0))

    @staticmethod
    @overload
    def invokerPredicate(arg0: str, arg1: 'Class', arg2: 'Object') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.invokerPredicate(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return Predicate.__wrap(__PredicateUtils.invokerPredicate(arg0, arg1, arg2))

    @staticmethod
    @overload
    def anyPredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.anyPredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate.__wrap(__PredicateUtils.anyPredicate(arg0))

    @staticmethod
    @overload
    def anyPredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.anyPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate.__wrap(__PredicateUtils.anyPredicate(arg0))

    @staticmethod
    @overload
    def instanceofPredicate(arg0: 'Class') -> 'Predicate':
        """public static org.apache.commons.collections4.Predicate<java.lang.Object> org.apache.commons.collections4.PredicateUtils.instanceofPredicate(java.lang.Class<?>)"""
        return Predicate.__wrap(__PredicateUtils.instanceofPredicate(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def invokerPredicate(arg0: str) -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.invokerPredicate(java.lang.String)"""
        return Predicate.__wrap(__PredicateUtils.invokerPredicate(arg0))

    @staticmethod
    @overload
    def nullIsFalsePredicate(arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nullIsFalsePredicate(org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.nullIsFalsePredicate(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def onePredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.onePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate.__wrap(__PredicateUtils.onePredicate(arg0))

    @staticmethod
    @overload
    def transformedPredicate(arg0: 'Transformer', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.transformedPredicate(org.apache.commons.collections4.Transformer<? super T, ? extends T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.transformedPredicate(arg0, arg1))

    @staticmethod
    @overload
    def onePredicate(arg0: 'Collection') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.onePredicate(java.util.Collection<? extends org.apache.commons.collections4.Predicate<? super T>>)"""
        return Predicate.__wrap(__PredicateUtils.onePredicate(arg0))

    @staticmethod
    @overload
    def orPredicate(arg0: 'Predicate', arg1: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.orPredicate(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return Predicate.__wrap(__PredicateUtils.orPredicate(arg0, arg1))

    @staticmethod
    @overload
    def identityPredicate(arg0: object) -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.identityPredicate(T)"""
        return Predicate.__wrap(__PredicateUtils.identityPredicate(arg0))

    @staticmethod
    @overload
    def equalPredicate(arg0: object) -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.equalPredicate(T)"""
        return Predicate.__wrap(__PredicateUtils.equalPredicate(arg0))

    @staticmethod
    @overload
    def nonePredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.nonePredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate.__wrap(__PredicateUtils.nonePredicate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def allPredicate(*arg0: 'Predicate') -> 'Predicate':
        """public static <T> org.apache.commons.collections4.Predicate<T> org.apache.commons.collections4.PredicateUtils.allPredicate(org.apache.commons.collections4.Predicate<? super T>...)"""
        return Predicate.__wrap(__PredicateUtils.allPredicate(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.Put
import org.apache.commons.collections4.Put as __Put
__Put = __Put
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class Put(ABC):
    """org.apache.commons.collections4.Put"""
 
    @staticmethod
    def __wrap(java_value: __Put) -> 'Put':
        return Put(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Put):
        """
        Dynamic initializer for Put.
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
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MultiValuedMap
import java.lang.Iterable as Iterable
import org.apache.commons.collections4.MultiValuedMap as __MultiValuedMap
__MultiValuedMap = __MultiValuedMap
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class MultiValuedMap(ABC):
    """org.apache.commons.collections4.MultiValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __MultiValuedMap) -> 'MultiValuedMap':
        return MultiValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiValuedMap):
        """
        Dynamic initializer for MultiValuedMap.
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
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.MultiValuedMap.mapIterator()"""
        pass

    @abstractmethod
    def putAll(self, arg0: object, arg1: 'Iterable'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.MultiValuedMap.clear()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.values()"""
        pass

    @abstractmethod
    def containsMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.isEmpty()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.MultiValuedMap.keys()"""
        pass

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.MultiValuedMap.entries()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.put(K,V)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.MultiValuedMap.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'MultiValuedMap'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.get(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiValuedMap.size()"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.MultiValuedMap.asMap()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Predicate
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Predicate as __Predicate
__Predicate = __Predicate
 
class Predicate(ABC):
    """org.apache.commons.collections4.Predicate"""
 
    @staticmethod
    def __wrap(java_value: __Predicate) -> 'Predicate':
        return Predicate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Predicate):
        """
        Dynamic initializer for Predicate.
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
    def evaluate(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Predicate.evaluate(T)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MapUtils
from pyquantum_helper import import_once as __import_once__
import java.lang.Long as Long
import java.lang.Boolean as __boolean
import org.apache.commons.collections4.MapUtils as __MapUtils
__MapUtils = __MapUtils
import java.lang.Short as Short
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import java.util.ResourceBundle as ResourceBundle
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.util.SortedMap as SortedMap
import org.apache.commons.collections4.IterableSortedMap as __IterableSortedMap
__IterableSortedMap = __IterableSortedMap
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.lang.Double as __double
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Number as Number
import org.apache.commons.collections4.IterableMap as __IterableMap
__IterableMap = __IterableMap
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Properties as __Properties
__Properties = __Properties
from builtins import float
import java.lang.Float as Float
import java.lang.Iterable as Iterable
from builtins import object
import java.lang.Byte as Byte
try:
    from pyapache.collections4 import map
except ImportError:
    map = __import_once__("pyapache.collections4.map")

import java.lang.Long as __long
import java.lang.Float as __float
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
import java.util.Map as Map
import java.lang.Double as Double
import org.apache.commons.collections4.map.MultiValueMap as __MultiValueMap
__MultiValueMap = __MultiValueMap
from builtins import int
 
class MapUtils():
    """org.apache.commons.collections4.MapUtils"""
 
    @staticmethod
    def __wrap(java_value: __MapUtils) -> 'MapUtils':
        return MapUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapUtils):
        """
        Dynamic initializer for MapUtils.
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
    def getString(arg0: 'Map', arg1: object) -> str:
        """public static <K> java.lang.String org.apache.commons.collections4.MapUtils.getString(java.util.Map<? super K, ?>,K)"""
        return str.__wrap(__MapUtils.getString(arg0, arg1))

    @staticmethod
    @overload
    def getByte(getByte) -> 'Byte':
        """public static <K> java.lang.Byte org.apache.commons.collections4.MapUtils.getByte(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Byte'Value()

    @staticmethod
    @overload
    def populateMap(arg0: 'Map', arg1: 'Iterable', arg2: 'Transformer'):
        """public static <K,V> void org.apache.commons.collections4.MapUtils.populateMap(java.util.Map<K, V>,java.lang.Iterable<? extends V>,org.apache.commons.collections4.Transformer<V, K>)"""
        __MapUtils.populateMap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getLongValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> long org.apache.commons.collections4.MapUtils.getLongValue(java.util.Map<? super K, ?>,K)"""
        return int.__wrap(__MapUtils.getLongValue(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getShortValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> short org.apache.commons.collections4.MapUtils.getShortValue(java.util.Map<? super K, ?>,K,short)"""
        return int.__wrap(__MapUtils.getShortValue(arg0, arg1, __short.valueOf(arg2)))

    @staticmethod
    @overload
    def unmodifiableMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.unmodifiableMap(java.util.Map<? extends K, ? extends V>)"""
        return Map.__wrap(__MapUtils.unmodifiableMap(arg0))

    @staticmethod
    @overload
    def getFloatValue(arg0: 'Map', arg1: object) -> float:
        """public static <K> float org.apache.commons.collections4.MapUtils.getFloatValue(java.util.Map<? super K, ?>,K)"""
        return float.__wrap(__MapUtils.getFloatValue(arg0, arg1))

    @staticmethod
    @overload
    def getDouble(getDouble) -> 'Double':
        """public static <K> java.lang.Double org.apache.commons.collections4.MapUtils.getDouble(java.util.Map<? super K, ?>,K,java.lang.Double)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Double')).'Double'Value()

    @staticmethod
    @overload
    def getBooleanValue(arg0: 'Map', arg1: object) -> bool:
        """public static <K> boolean org.apache.commons.collections4.MapUtils.getBooleanValue(java.util.Map<? super K, ?>,K)"""
        return bool.__wrap(__MapUtils.getBooleanValue(arg0, arg1))

    @staticmethod
    @overload
    def getNumber(getNumber) -> 'Number':
        """public static <K> java.lang.Number org.apache.commons.collections4.MapUtils.getNumber(java.util.Map<? super K, ?>,K,java.lang.Number)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Number')).'Number'Value()

    @staticmethod
    @overload
    def toMap(arg0: 'ResourceBundle') -> 'Map':
        """public static java.util.Map<java.lang.String, java.lang.Object> org.apache.commons.collections4.MapUtils.toMap(java.util.ResourceBundle)"""
        return Map.__wrap(__MapUtils.toMap(arg0))

    @staticmethod
    @overload
    def getDouble(getDouble) -> 'Double':
        """public static <K> java.lang.Double org.apache.commons.collections4.MapUtils.getDouble(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Double'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isEmpty(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.collections4.MapUtils.isEmpty(java.util.Map<?, ?>)"""
        return bool.__wrap(__MapUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Factory') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return SortedMap.__wrap(__MapUtils.lazySortedMap(arg0, arg1))

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Class') -> 'map.MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.MapUtils.multiValueMap(java.util.Map<K, C>,java.lang.Class<C>)"""
        return map.MultiValueMap.__wrap(__MapUtils.multiValueMap(arg0, arg1))

    @staticmethod
    @overload
    def getIntValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> int org.apache.commons.collections4.MapUtils.getIntValue(java.util.Map<? super K, ?>,K)"""
        return int.__wrap(__MapUtils.getIntValue(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def getDoubleValue(arg0: 'Map', arg1: object, arg2: float) -> float:
        """public static <K> double org.apache.commons.collections4.MapUtils.getDoubleValue(java.util.Map<? super K, ?>,K,double)"""
        return float.__wrap(__MapUtils.getDoubleValue(arg0, arg1, __double.valueOf(arg2)))

    @staticmethod
    @overload
    def getIntValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> int org.apache.commons.collections4.MapUtils.getIntValue(java.util.Map<? super K, ?>,K,int)"""
        return int.__wrap(__MapUtils.getIntValue(arg0, arg1, __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def populateMap(arg0: 'Map', arg1: 'Iterable', arg2: 'Transformer', arg3: 'Transformer'):
        """public static <K,V,E> void org.apache.commons.collections4.MapUtils.populateMap(java.util.Map<K, V>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Transformer<E, K>,org.apache.commons.collections4.Transformer<E, V>)"""
        __MapUtils.populateMap(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def getByteValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> byte org.apache.commons.collections4.MapUtils.getByteValue(java.util.Map<? super K, ?>,K)"""
        return int.__wrap(__MapUtils.getByteValue(arg0, arg1))

    @staticmethod
    @overload
    def getFloat(getFloat) -> 'Float':
        """public static <K> java.lang.Float org.apache.commons.collections4.MapUtils.getFloat(java.util.Map<? super K, ?>,K,java.lang.Float)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Float')).'Float'Value()

    @staticmethod
    @overload
    def getLong(getLong) -> 'Long':
        """public static <K> java.lang.Long org.apache.commons.collections4.MapUtils.getLong(java.util.Map<? super K, ?>,K,java.lang.Long)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Long')).'Long'Value()

    @staticmethod
    @overload
    def isNotEmpty(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.collections4.MapUtils.isNotEmpty(java.util.Map<?, ?>)"""
        return bool.__wrap(__MapUtils.isNotEmpty(arg0))

    @staticmethod
    @overload
    def getShort(getShort) -> 'Short':
        """public static <K> java.lang.Short org.apache.commons.collections4.MapUtils.getShort(java.util.Map<? super K, ?>,K,java.lang.Short)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Short')).'Short'Value()

    @staticmethod
    @overload
    def getObject(arg0: 'Map', arg1: object, arg2: object) -> object:
        """public static <K,V> V org.apache.commons.collections4.MapUtils.getObject(java.util.Map<K, V>,K,V)"""
        return object.__wrap(__MapUtils.getObject(arg0, arg1, arg2))

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Transformer') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return SortedMap.__wrap(__MapUtils.lazySortedMap(arg0, arg1))

    @staticmethod
    @overload
    def getByteValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> byte org.apache.commons.collections4.MapUtils.getByteValue(java.util.Map<? super K, ?>,K,byte)"""
        return int.__wrap(__MapUtils.getByteValue(arg0, arg1, __byte.valueOf(arg2)))

    @staticmethod
    @overload
    def populateMap(arg0: 'MultiMap', arg1: 'Iterable', arg2: 'Transformer', arg3: 'Transformer'):
        """public static <K,V,E> void org.apache.commons.collections4.MapUtils.populateMap(org.apache.commons.collections4.MultiMap<K, V>,java.lang.Iterable<? extends E>,org.apache.commons.collections4.Transformer<E, K>,org.apache.commons.collections4.Transformer<E, V>)"""
        __MapUtils.populateMap(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def unmodifiableSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.unmodifiableSortedMap(java.util.SortedMap<K, ? extends V>)"""
        return SortedMap.__wrap(__MapUtils.unmodifiableSortedMap(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def orderedMap(arg0: 'Map') -> 'OrderedMap':
        """public static <K,V> org.apache.commons.collections4.OrderedMap<K, V> org.apache.commons.collections4.MapUtils.orderedMap(java.util.Map<K, V>)"""
        return OrderedMap.__wrap(__MapUtils.orderedMap(arg0))

    @staticmethod
    @overload
    def getByte(getByte) -> 'Byte':
        """public static <K> java.lang.Byte org.apache.commons.collections4.MapUtils.getByte(java.util.Map<? super K, ?>,K,java.lang.Byte)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Byte')).'Byte'Value()

    @staticmethod
    @overload
    def getLong(getLong) -> 'Long':
        """public static <K> java.lang.Long org.apache.commons.collections4.MapUtils.getLong(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Long'Value()

    @staticmethod
    @overload
    def getInteger(getInteger) -> 'Integer':
        """public static <K> java.lang.Integer org.apache.commons.collections4.MapUtils.getInteger(java.util.Map<? super K, ?>,K,java.lang.Integer)"""
        return __transform(__arg0, arg1, arg2.MapUtils(arg0: 'Map', arg1: object, arg2: 'Integer')).'Integer'Value()

    @staticmethod
    @overload
    def getString(arg0: 'Map', arg1: object, arg2: str) -> str:
        """public static <K> java.lang.String org.apache.commons.collections4.MapUtils.getString(java.util.Map<? super K, ?>,K,java.lang.String)"""
        return str.__wrap(__MapUtils.getString(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getLongValue(arg0: 'Map', arg1: object, arg2: int) -> int:
        """public static <K> long org.apache.commons.collections4.MapUtils.getLongValue(java.util.Map<? super K, ?>,K,long)"""
        return int.__wrap(__MapUtils.getLongValue(arg0, arg1, __long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getShort(getShort) -> 'Short':
        """public static <K> java.lang.Short org.apache.commons.collections4.MapUtils.getShort(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Short'Value()

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Factory') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return IterableMap.__wrap(__MapUtils.lazyMap(arg0, arg1))

    @staticmethod
    @overload
    def fixedSizeSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.fixedSizeSortedMap(java.util.SortedMap<K, V>)"""
        return SortedMap.__wrap(__MapUtils.fixedSizeSortedMap(arg0))

    @staticmethod
    @overload
    def safeAddToMap(arg0: 'Map', arg1: object, arg2: object):
        """public static <K> void org.apache.commons.collections4.MapUtils.safeAddToMap(java.util.Map<? super K, java.lang.Object>,K,java.lang.Object) throws java.lang.NullPointerException"""
        __MapUtils.safeAddToMap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getInteger(getInteger) -> 'Integer':
        """public static <K> java.lang.Integer org.apache.commons.collections4.MapUtils.getInteger(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Integer'Value()

    @staticmethod
    @overload
    def getMap(arg0: 'Map', arg1: object, arg2: 'Map') -> 'Map':
        """public static <K> java.util.Map<?, ?> org.apache.commons.collections4.MapUtils.getMap(java.util.Map<? super K, ?>,K,java.util.Map<?, ?>)"""
        return Map.__wrap(__MapUtils.getMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getMap(arg0: 'Map', arg1: object) -> 'Map':
        """public static <K> java.util.Map<?, ?> org.apache.commons.collections4.MapUtils.getMap(java.util.Map<? super K, ?>,K)"""
        return Map.__wrap(__MapUtils.getMap(arg0, arg1))

    @staticmethod
    @overload
    def getObject(arg0: 'Map', arg1: object) -> object:
        """public static <K,V> V org.apache.commons.collections4.MapUtils.getObject(java.util.Map<? super K, V>,K)"""
        return object.__wrap(__MapUtils.getObject(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.synchronizedSortedMap(java.util.SortedMap<K, V>)"""
        return SortedMap.__wrap(__MapUtils.synchronizedSortedMap(arg0))

    @staticmethod
    @overload
    def transformedMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.transformedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return IterableMap.__wrap(__MapUtils.transformedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getBoolean(arg0: 'Map', arg1: object, arg2: 'Boolean') -> 'Boolean':
        """public static <K> java.lang.Boolean org.apache.commons.collections4.MapUtils.getBoolean(java.util.Map<? super K, ?>,K,java.lang.Boolean)"""
        return Boolean.__wrap(__MapUtils.getBoolean(arg0, arg1, arg2))

    @staticmethod
    @overload
    def populateMap(arg0: 'MultiMap', arg1: 'Iterable', arg2: 'Transformer'):
        """public static <K,V> void org.apache.commons.collections4.MapUtils.populateMap(org.apache.commons.collections4.MultiMap<K, V>,java.lang.Iterable<? extends V>,org.apache.commons.collections4.Transformer<V, K>)"""
        __MapUtils.populateMap(arg0, arg1, arg2)

    @staticmethod
    @overload
    def predicatedMap(arg0: 'Map', arg1: 'Predicate', arg2: 'Predicate') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.predicatedMap(java.util.Map<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return IterableMap.__wrap(__MapUtils.predicatedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def synchronizedMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.synchronizedMap(java.util.Map<K, V>)"""
        return Map.__wrap(__MapUtils.synchronizedMap(arg0))

    @staticmethod
    @overload
    def size(arg0: 'Map') -> int:
        """public static int org.apache.commons.collections4.MapUtils.size(java.util.Map<?, ?>)"""
        return int.__wrap(__MapUtils.size(arg0))

    @staticmethod
    @overload
    def getFloatValue(arg0: 'Map', arg1: object, arg2: float) -> float:
        """public static <K> float org.apache.commons.collections4.MapUtils.getFloatValue(java.util.Map<? super K, ?>,K,float)"""
        return float.__wrap(__MapUtils.getFloatValue(arg0, arg1, __float.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map') -> 'map.MultiValueMap':
        """public static <K,V> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.MapUtils.multiValueMap(java.util.Map<K, ? super java.util.Collection<V>>)"""
        return map.MultiValueMap.__wrap(__MapUtils.multiValueMap(arg0))

    @staticmethod
    @overload
    def getNumber(getNumber) -> 'Number':
        """public static <K> java.lang.Number org.apache.commons.collections4.MapUtils.getNumber(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Number'Value()

    @staticmethod
    @overload
    def getBoolean(arg0: 'Map', arg1: object) -> 'Boolean':
        """public static <K> java.lang.Boolean org.apache.commons.collections4.MapUtils.getBoolean(java.util.Map<? super K, ?>,K)"""
        return Boolean.__wrap(__MapUtils.getBoolean(arg0, arg1))

    @staticmethod
    @overload
    def invertMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<V, K> org.apache.commons.collections4.MapUtils.invertMap(java.util.Map<K, V>)"""
        return Map.__wrap(__MapUtils.invertMap(arg0))

    @staticmethod
    @overload
    def iterableMap(arg0: 'Map') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.iterableMap(java.util.Map<K, V>)"""
        return IterableMap.__wrap(__MapUtils.iterableMap(arg0))

    @staticmethod
    @overload
    def getBooleanValue(arg0: 'Map', arg1: object, arg2: bool) -> bool:
        """public static <K> boolean org.apache.commons.collections4.MapUtils.getBooleanValue(java.util.Map<? super K, ?>,K,boolean)"""
        return bool.__wrap(__MapUtils.getBooleanValue(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def iterableSortedMap(arg0: 'SortedMap') -> 'IterableSortedMap':
        """public static <K,V> org.apache.commons.collections4.IterableSortedMap<K, V> org.apache.commons.collections4.MapUtils.iterableSortedMap(java.util.SortedMap<K, V>)"""
        return IterableSortedMap.__wrap(__MapUtils.iterableSortedMap(arg0))

    @staticmethod
    @overload
    def getFloat(getFloat) -> 'Float':
        """public static <K> java.lang.Float org.apache.commons.collections4.MapUtils.getFloat(java.util.Map<? super K, ?>,K)"""
        return __transform(__arg0, arg1.MapUtils(arg0: 'Map', arg1: object)).'Float'Value()

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Factory') -> 'map.MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.MapUtils.multiValueMap(java.util.Map<K, C>,org.apache.commons.collections4.Factory<C>)"""
        return map.MultiValueMap.__wrap(__MapUtils.multiValueMap(arg0, arg1))

    @staticmethod
    @overload
    def fixedSizeMap(arg0: 'Map') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.fixedSizeMap(java.util.Map<K, V>)"""
        return IterableMap.__wrap(__MapUtils.fixedSizeMap(arg0))

    @staticmethod
    @overload
    def getShortValue(arg0: 'Map', arg1: object) -> int:
        """public static <K> short org.apache.commons.collections4.MapUtils.getShortValue(java.util.Map<? super K, ?>,K)"""
        return int.__wrap(__MapUtils.getShortValue(arg0, arg1))

    @staticmethod
    @overload
    def verbosePrint(arg0: 'PrintStream', arg1: object, arg2: 'Map'):
        """public static void org.apache.commons.collections4.MapUtils.verbosePrint(java.io.PrintStream,java.lang.Object,java.util.Map<?, ?>)"""
        __MapUtils.verbosePrint(arg0, arg1, arg2)

    @staticmethod
    @overload
    def debugPrint(arg0: 'PrintStream', arg1: object, arg2: 'Map'):
        """public static void org.apache.commons.collections4.MapUtils.debugPrint(java.io.PrintStream,java.lang.Object,java.util.Map<?, ?>)"""
        __MapUtils.debugPrint(arg0, arg1, arg2)

    @staticmethod
    @overload
    def toProperties(arg0: 'Map') -> 'Properties':
        """public static <K,V> java.util.Properties org.apache.commons.collections4.MapUtils.toProperties(java.util.Map<K, V>)"""
        return Properties.__wrap(__MapUtils.toProperties(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.emptyIfNull(java.util.Map<K, V>)"""
        return Map.__wrap(__MapUtils.emptyIfNull(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getDoubleValue(arg0: 'Map', arg1: object) -> float:
        """public static <K> double org.apache.commons.collections4.MapUtils.getDoubleValue(java.util.Map<? super K, ?>,K)"""
        return float.__wrap(__MapUtils.getDoubleValue(arg0, arg1))

    @staticmethod
    @overload
    def transformedSortedMap(arg0: 'SortedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.transformedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return SortedMap.__wrap(__MapUtils.transformedSortedMap(arg0, arg1, arg2))

    @staticmethod
    @overload
    def putAll(arg0: 'Map', arg1: 'Object') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.MapUtils.putAll(java.util.Map<K, V>,java.lang.Object[])"""
        return Map.__wrap(__MapUtils.putAll(arg0, arg1))

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Transformer') -> 'IterableMap':
        """public static <K,V> org.apache.commons.collections4.IterableMap<K, V> org.apache.commons.collections4.MapUtils.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return IterableMap.__wrap(__MapUtils.lazyMap(arg0, arg1))

    @staticmethod
    @overload
    def predicatedSortedMap(arg0: 'SortedMap', arg1: 'Predicate', arg2: 'Predicate') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.MapUtils.predicatedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return SortedMap.__wrap(__MapUtils.predicatedSortedMap(arg0, arg1, arg2)) 
 
 
# CLASS: org.apache.commons.collections4.ListUtils
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.ListUtils as __ListUtils
__ListUtils = __ListUtils
import java.util.Collection as Collection
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ListUtils():
    """org.apache.commons.collections4.ListUtils"""
 
    @staticmethod
    def __wrap(java_value: __ListUtils) -> 'ListUtils':
        return ListUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListUtils):
        """
        Dynamic initializer for ListUtils.
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
    def longestCommonSubsequence(arg0: 'CharSequence', arg1: 'CharSequence') -> str:
        """public static java.lang.String org.apache.commons.collections4.ListUtils.longestCommonSubsequence(java.lang.CharSequence,java.lang.CharSequence)"""
        return str.__wrap(__ListUtils.longestCommonSubsequence(arg0, arg1))

    @staticmethod
    @overload
    def sum(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.sum(java.util.List<? extends E>,java.util.List<? extends E>)"""
        return List.__wrap(__ListUtils.sum(arg0, arg1))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'List') -> 'List':
        """public static <T> java.util.List<T> org.apache.commons.collections4.ListUtils.emptyIfNull(java.util.List<T>)"""
        return List.__wrap(__ListUtils.emptyIfNull(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hashCodeForList(arg0: 'Collection') -> int:
        """public static int org.apache.commons.collections4.ListUtils.hashCodeForList(java.util.Collection<?>)"""
        return int.__wrap(__ListUtils.hashCodeForList(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def indexOf(arg0: 'List', arg1: 'Predicate') -> int:
        """public static <E> int org.apache.commons.collections4.ListUtils.indexOf(java.util.List<E>,org.apache.commons.collections4.Predicate<E>)"""
        return int.__wrap(__ListUtils.indexOf(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def select(arg0: 'Collection', arg1: 'Predicate') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.select(java.util.Collection<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return List.__wrap(__ListUtils.select(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.unmodifiableList(java.util.List<? extends E>)"""
        return List.__wrap(__ListUtils.unmodifiableList(arg0))

    @staticmethod
    @overload
    def defaultIfNull(arg0: 'List', arg1: 'List') -> 'List':
        """public static <T> java.util.List<T> org.apache.commons.collections4.ListUtils.defaultIfNull(java.util.List<T>,java.util.List<T>)"""
        return List.__wrap(__ListUtils.defaultIfNull(arg0, arg1))

    @staticmethod
    @overload
    def removeAll(arg0: 'Collection', arg1: 'Collection') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.removeAll(java.util.Collection<E>,java.util.Collection<?>)"""
        return List.__wrap(__ListUtils.removeAll(arg0, arg1))

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Transformer') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.lazyList(java.util.List<E>,org.apache.commons.collections4.Transformer<java.lang.Integer, ? extends E>)"""
        return List.__wrap(__ListUtils.lazyList(arg0, arg1))

    @staticmethod
    @overload
    def union(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.union(java.util.List<? extends E>,java.util.List<? extends E>)"""
        return List.__wrap(__ListUtils.union(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def longestCommonSubsequence(arg0: 'List', arg1: 'List', arg2: 'Equator') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.longestCommonSubsequence(java.util.List<E>,java.util.List<E>,org.apache.commons.collections4.Equator<? super E>)"""
        return List.__wrap(__ListUtils.longestCommonSubsequence(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def lazyList(arg0: 'List', arg1: 'Factory') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.lazyList(java.util.List<E>,org.apache.commons.collections4.Factory<? extends E>)"""
        return List.__wrap(__ListUtils.lazyList(arg0, arg1))

    @staticmethod
    @overload
    def retainAll(arg0: 'Collection', arg1: 'Collection') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.retainAll(java.util.Collection<E>,java.util.Collection<?>)"""
        return List.__wrap(__ListUtils.retainAll(arg0, arg1))

    @staticmethod
    @overload
    def subtract(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.subtract(java.util.List<E>,java.util.List<? extends E>)"""
        return List.__wrap(__ListUtils.subtract(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def partition(arg0: 'List', arg1: int) -> 'List':
        """public static <T> java.util.List<java.util.List<T>> org.apache.commons.collections4.ListUtils.partition(java.util.List<T>,int)"""
        return List.__wrap(__ListUtils.partition(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def intersection(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.intersection(java.util.List<? extends E>,java.util.List<? extends E>)"""
        return List.__wrap(__ListUtils.intersection(arg0, arg1))

    @staticmethod
    @overload
    def selectRejected(arg0: 'Collection', arg1: 'Predicate') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.selectRejected(java.util.Collection<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return List.__wrap(__ListUtils.selectRejected(arg0, arg1))

    @staticmethod
    @overload
    def fixedSizeList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.fixedSizeList(java.util.List<E>)"""
        return List.__wrap(__ListUtils.fixedSizeList(arg0))

    @staticmethod
    @overload
    def isEqualList(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.ListUtils.isEqualList(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__ListUtils.isEqualList(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedList(arg0: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.synchronizedList(java.util.List<E>)"""
        return List.__wrap(__ListUtils.synchronizedList(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def longestCommonSubsequence(arg0: 'List', arg1: 'List') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.longestCommonSubsequence(java.util.List<E>,java.util.List<E>)"""
        return List.__wrap(__ListUtils.longestCommonSubsequence(arg0, arg1))

    @staticmethod
    @overload
    def predicatedList(arg0: 'List', arg1: 'Predicate') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.predicatedList(java.util.List<E>,org.apache.commons.collections4.Predicate<E>)"""
        return List.__wrap(__ListUtils.predicatedList(arg0, arg1))

    @staticmethod
    @overload
    def transformedList(arg0: 'List', arg1: 'Transformer') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.ListUtils.transformedList(java.util.List<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return List.__wrap(__ListUtils.transformedList(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.TrieUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.TrieUtils as __TrieUtils
__TrieUtils = __TrieUtils
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.Trie as __Trie
__Trie = __Trie
from builtins import int
 
class TrieUtils():
    """org.apache.commons.collections4.TrieUtils"""
 
    @staticmethod
    def __wrap(java_value: __TrieUtils) -> 'TrieUtils':
        return TrieUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TrieUtils):
        """
        Dynamic initializer for TrieUtils.
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
    def unmodifiableTrie(arg0: 'Trie') -> 'Trie':
        """public static <K,V> org.apache.commons.collections4.Trie<K, V> org.apache.commons.collections4.TrieUtils.unmodifiableTrie(org.apache.commons.collections4.Trie<K, ? extends V>)"""
        return Trie.__wrap(__TrieUtils.unmodifiableTrie(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.IteratorUtils
from pyquantum_helper import import_once as __import_once__
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import org.apache.commons.collections4.iterators.NodeListIterator as __NodeListIterator
__NodeListIterator = __NodeListIterator
import java.util.Enumeration as __Enumeration
__Enumeration = __Enumeration
from builtins import type
import org.apache.commons.collections4.OrderedIterator as __OrderedIterator
__OrderedIterator = __OrderedIterator
import org.apache.commons.collections4.ResettableListIterator as __ResettableListIterator
__ResettableListIterator = __ResettableListIterator
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import org.apache.commons.collections4.iterators.ZippingIterator as __ZippingIterator
__ZippingIterator = __ZippingIterator
import java.util.Collection as Collection
import org.apache.commons.collections4.ResettableIterator as __ResettableIterator
__ResettableIterator = __ResettableIterator
import org.apache.commons.collections4.iterators.BoundedIterator as __BoundedIterator
__BoundedIterator = __BoundedIterator
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import org.w3c.dom.NodeList as NodeList
import java.util.Enumeration as Enumeration
try:
    from pyapache.collections4 import iterators
except ImportError:
    iterators = __import_once__("pyapache.collections4.iterators")

from builtins import bool
import org.w3c.dom.Node as Node
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Iterable as Iterable
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.apache.commons.collections4.iterators.SkippingIterator as __SkippingIterator
__SkippingIterator = __SkippingIterator
import org.apache.commons.collections4.IteratorUtils as __IteratorUtils
__IteratorUtils = __IteratorUtils
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IteratorUtils():
    """org.apache.commons.collections4.IteratorUtils"""
 
    @staticmethod
    def __wrap(java_value: __IteratorUtils) -> 'IteratorUtils':
        return IteratorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IteratorUtils):
        """
        Dynamic initializer for IteratorUtils.
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
    def forEachButLast(arg0: 'Iterator', arg1: 'Closure') -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.forEachButLast(java.util.Iterator<E>,org.apache.commons.collections4.Closure<? super E>)"""
        return object.__wrap(__IteratorUtils.forEachButLast(arg0, arg1))

    @staticmethod
    @overload
    def emptyOrderedMapIterator() -> 'OrderedMapIterator':
        """public static <K,V> org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.IteratorUtils.emptyOrderedMapIterator()"""
        return OrderedMapIterator.__wrap(__IteratorUtils.emptyOrderedMapIterator())

    @staticmethod
    @overload
    def toArray(arg0: 'Iterator') -> List[object]:
        """public static java.lang.Object[] org.apache.commons.collections4.IteratorUtils.toArray(java.util.Iterator<?>)"""
        return List[object].__wrap(__IteratorUtils.toArray(arg0))

    @staticmethod
    @overload
    def arrayIterator(arg0: 'Object', arg1: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(E[],int)"""
        return ResettableIterator.__wrap(__IteratorUtils.arrayIterator(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def unmodifiableMapIterator(arg0: 'MapIterator') -> 'MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IteratorUtils.unmodifiableMapIterator(org.apache.commons.collections4.MapIterator<K, V>)"""
        return MapIterator.__wrap(__IteratorUtils.unmodifiableMapIterator(arg0))

    @staticmethod
    @overload
    def peekingIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.peekingIterator(java.util.Iterator<? extends E>)"""
        return Iterator.__wrap(__IteratorUtils.peekingIterator(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def first(arg0: 'Iterator') -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.first(java.util.Iterator<E>)"""
        return object.__wrap(__IteratorUtils.first(arg0))

    @staticmethod
    @overload
    def objectGraphIterator(arg0: object, arg1: 'Transformer') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.objectGraphIterator(E,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Iterator.__wrap(__IteratorUtils.objectGraphIterator(arg0, arg1))

    @staticmethod
    @overload
    def isEmpty(arg0: 'Iterator') -> bool:
        """public static boolean org.apache.commons.collections4.IteratorUtils.isEmpty(java.util.Iterator<?>)"""
        return bool.__wrap(__IteratorUtils.isEmpty(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toArray(arg0: 'Iterator', arg1: 'Class') -> List[object]:
        """public static <E> E[] org.apache.commons.collections4.IteratorUtils.toArray(java.util.Iterator<? extends E>,java.lang.Class<E>)"""
        return List[object].__wrap(__IteratorUtils.toArray(arg0, arg1))

    @staticmethod
    @overload
    def get(arg0: 'Iterator', arg1: int) -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.get(java.util.Iterator<E>,int)"""
        return object.__wrap(__IteratorUtils.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def size(arg0: 'Iterator') -> int:
        """public static int org.apache.commons.collections4.IteratorUtils.size(java.util.Iterator<?>)"""
        return int.__wrap(__IteratorUtils.size(arg0))

    @staticmethod
    @overload
    def nodeListIterator(arg0: 'NodeList') -> 'iterators.NodeListIterator':
        """public static org.apache.commons.collections4.iterators.NodeListIterator org.apache.commons.collections4.IteratorUtils.nodeListIterator(org.w3c.dom.NodeList)"""
        return iterators.NodeListIterator.__wrap(__IteratorUtils.nodeListIterator(arg0))

    @staticmethod
    @overload
    def contains(arg0: 'Iterator', arg1: object) -> bool:
        """public static <E> boolean org.apache.commons.collections4.IteratorUtils.contains(java.util.Iterator<E>,java.lang.Object)"""
        return bool.__wrap(__IteratorUtils.contains(arg0, arg1))

    @staticmethod
    @overload
    def collatedIterator(arg0: 'Comparator', arg1: 'Iterator', arg2: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.collatedIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return Iterator.__wrap(__IteratorUtils.collatedIterator(arg0, arg1, arg2))

    @staticmethod
    @overload
    def asIterator(arg0: 'Enumeration') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.asIterator(java.util.Enumeration<? extends E>)"""
        return Iterator.__wrap(__IteratorUtils.asIterator(arg0))

    @staticmethod
    @overload
    def skippingIterator(arg0: 'Iterator', arg1: int) -> 'iterators.SkippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.SkippingIterator<E> org.apache.commons.collections4.IteratorUtils.skippingIterator(java.util.Iterator<E>,long)"""
        return iterators.SkippingIterator.__wrap(__IteratorUtils.skippingIterator(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def zippingIterator(*arg0: 'Iterator') -> 'iterators.ZippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.ZippingIterator<E> org.apache.commons.collections4.IteratorUtils.zippingIterator(java.util.Iterator<? extends E>...)"""
        return iterators.ZippingIterator.__wrap(__IteratorUtils.zippingIterator(arg0))

    @staticmethod
    @overload
    def arrayListIterator(arg0: object, arg1: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(java.lang.Object,int)"""
        return ResettableListIterator.__wrap(__IteratorUtils.arrayListIterator(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def arrayListIterator(arg0: 'Object', arg1: int, arg2: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(E[],int,int)"""
        return ResettableListIterator.__wrap(__IteratorUtils.arrayListIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def arrayIterator(arg0: object, arg1: int, arg2: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(java.lang.Object,int,int)"""
        return ResettableIterator.__wrap(__IteratorUtils.arrayIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def arrayListIterator(arg0: 'Object', arg1: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(E[],int)"""
        return ResettableListIterator.__wrap(__IteratorUtils.arrayListIterator(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def asMultipleUseIterable(arg0: 'Iterator') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IteratorUtils.asMultipleUseIterable(java.util.Iterator<? extends E>)"""
        return Iterable.__wrap(__IteratorUtils.asMultipleUseIterable(arg0))

    @staticmethod
    @overload
    def matchesAny(arg0: 'Iterator', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IteratorUtils.matchesAny(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool.__wrap(__IteratorUtils.matchesAny(arg0, arg1))

    @staticmethod
    @overload
    def emptyIterator() -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.emptyIterator()"""
        return ResettableIterator.__wrap(__IteratorUtils.emptyIterator())

    @staticmethod
    @overload
    def emptyMapIterator() -> 'MapIterator':
        """public static <K,V> org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IteratorUtils.emptyMapIterator()"""
        return MapIterator.__wrap(__IteratorUtils.emptyMapIterator())

    @staticmethod
    @overload
    def asIterable(arg0: 'Iterator') -> 'Iterable':
        """public static <E> java.lang.Iterable<E> org.apache.commons.collections4.IteratorUtils.asIterable(java.util.Iterator<? extends E>)"""
        return Iterable.__wrap(__IteratorUtils.asIterable(arg0))

    @staticmethod
    @overload
    def arrayIterator(arg0: 'Object', arg1: int, arg2: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(E[],int,int)"""
        return ResettableIterator.__wrap(__IteratorUtils.arrayIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def find(arg0: 'Iterator', arg1: 'Predicate') -> object:
        """public static <E> E org.apache.commons.collections4.IteratorUtils.find(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return object.__wrap(__IteratorUtils.find(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def emptyOrderedIterator() -> 'OrderedIterator':
        """public static <E> org.apache.commons.collections4.OrderedIterator<E> org.apache.commons.collections4.IteratorUtils.emptyOrderedIterator()"""
        return OrderedIterator.__wrap(__IteratorUtils.emptyOrderedIterator())

    @staticmethod
    @overload
    def toString(arg0: 'Iterator', arg1: 'Transformer', arg2: str, arg3: str, arg4: str) -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IteratorUtils.toString(java.util.Iterator<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>,java.lang.String,java.lang.String,java.lang.String)"""
        return str.__wrap(__IteratorUtils.toString(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def indexOf(arg0: 'Iterator', arg1: 'Predicate') -> int:
        """public static <E> int org.apache.commons.collections4.IteratorUtils.indexOf(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return int.__wrap(__IteratorUtils.indexOf(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def unmodifiableListIterator(arg0: 'ListIterator') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.unmodifiableListIterator(java.util.ListIterator<E>)"""
        return ListIterator.__wrap(__IteratorUtils.unmodifiableListIterator(arg0))

    @staticmethod
    @overload
    def emptyListIterator() -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.emptyListIterator()"""
        return ResettableListIterator.__wrap(__IteratorUtils.emptyListIterator())

    @staticmethod
    @overload
    def matchesAll(arg0: 'Iterator', arg1: 'Predicate') -> bool:
        """public static <E> boolean org.apache.commons.collections4.IteratorUtils.matchesAll(java.util.Iterator<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return bool.__wrap(__IteratorUtils.matchesAll(arg0, arg1))

    @staticmethod
    @overload
    def loopingIterator(arg0: 'Collection') -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.loopingIterator(java.util.Collection<? extends E>)"""
        return ResettableIterator.__wrap(__IteratorUtils.loopingIterator(arg0))

    @staticmethod
    @overload
    def loopingListIterator(arg0: 'List') -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.loopingListIterator(java.util.List<E>)"""
        return ResettableListIterator.__wrap(__IteratorUtils.loopingListIterator(arg0))

    @staticmethod
    @overload
    def arrayIterator(arg0: object) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(java.lang.Object)"""
        return ResettableIterator.__wrap(__IteratorUtils.arrayIterator(arg0))

    @staticmethod
    @overload
    def nodeListIterator(arg0: 'Node') -> 'iterators.NodeListIterator':
        """public static org.apache.commons.collections4.iterators.NodeListIterator org.apache.commons.collections4.IteratorUtils.nodeListIterator(org.w3c.dom.Node)"""
        return iterators.NodeListIterator.__wrap(__IteratorUtils.nodeListIterator(arg0))

    @staticmethod
    @overload
    def getIterator(arg0: object) -> 'Iterator':
        """public static java.util.Iterator<?> org.apache.commons.collections4.IteratorUtils.getIterator(java.lang.Object)"""
        return Iterator.__wrap(__IteratorUtils.getIterator(arg0))

    @staticmethod
    @overload
    def arrayIterator(arg0: object, arg1: int) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(java.lang.Object,int)"""
        return ResettableIterator.__wrap(__IteratorUtils.arrayIterator(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def arrayListIterator(arg0: object) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(java.lang.Object)"""
        return ResettableListIterator.__wrap(__IteratorUtils.arrayListIterator(arg0))

    @staticmethod
    @overload
    def chainedIterator(arg0: 'Collection') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.chainedIterator(java.util.Collection<java.util.Iterator<? extends E>>)"""
        return Iterator.__wrap(__IteratorUtils.chainedIterator(arg0))

    @staticmethod
    @overload
    def pushbackIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.pushbackIterator(java.util.Iterator<? extends E>)"""
        return Iterator.__wrap(__IteratorUtils.pushbackIterator(arg0))

    @staticmethod
    @overload
    def zippingIterator(arg0: 'Iterator', arg1: 'Iterator', arg2: 'Iterator') -> 'iterators.ZippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.ZippingIterator<E> org.apache.commons.collections4.IteratorUtils.zippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return iterators.ZippingIterator.__wrap(__IteratorUtils.zippingIterator(arg0, arg1, arg2))

    @staticmethod
    @overload
    def toListIterator(arg0: 'Iterator') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.toListIterator(java.util.Iterator<? extends E>)"""
        return ListIterator.__wrap(__IteratorUtils.toListIterator(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def filteredListIterator(arg0: 'ListIterator', arg1: 'Predicate') -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.filteredListIterator(java.util.ListIterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return ListIterator.__wrap(__IteratorUtils.filteredListIterator(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: 'Iterator') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IteratorUtils.toString(java.util.Iterator<E>)"""
        return str.__wrap(__IteratorUtils.toString(arg0))

    @staticmethod
    @overload
    def collatedIterator(arg0: 'Comparator', *arg1: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.collatedIterator(java.util.Comparator<? super E>,java.util.Iterator<? extends E>...)"""
        return Iterator.__wrap(__IteratorUtils.collatedIterator(arg0, arg1))

    @staticmethod
    @overload
    def toList(arg0: 'Iterator') -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.IteratorUtils.toList(java.util.Iterator<? extends E>)"""
        return List.__wrap(__IteratorUtils.toList(arg0))

    @staticmethod
    @overload
    def arrayIterator(*arg0: object) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.arrayIterator(E...)"""
        return ResettableIterator.__wrap(__IteratorUtils.arrayIterator(arg0))

    @staticmethod
    @overload
    def collatedIterator(arg0: 'Comparator', arg1: 'Collection') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.collatedIterator(java.util.Comparator<? super E>,java.util.Collection<java.util.Iterator<? extends E>>)"""
        return Iterator.__wrap(__IteratorUtils.collatedIterator(arg0, arg1))

    @staticmethod
    @overload
    def boundedIterator(arg0: 'Iterator', arg1: int, arg2: int) -> 'iterators.BoundedIterator':
        """public static <E> org.apache.commons.collections4.iterators.BoundedIterator<E> org.apache.commons.collections4.IteratorUtils.boundedIterator(java.util.Iterator<? extends E>,long,long)"""
        return iterators.BoundedIterator.__wrap(__IteratorUtils.boundedIterator(arg0, __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def transformedIterator(arg0: 'Iterator', arg1: 'Transformer') -> 'Iterator':
        """public static <I,O> java.util.Iterator<O> org.apache.commons.collections4.IteratorUtils.transformedIterator(java.util.Iterator<? extends I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Iterator.__wrap(__IteratorUtils.transformedIterator(arg0, arg1))

    @staticmethod
    @overload
    def arrayListIterator(arg0: object, arg1: int, arg2: int) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(java.lang.Object,int,int)"""
        return ResettableListIterator.__wrap(__IteratorUtils.arrayListIterator(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def chainedIterator(*arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.chainedIterator(java.util.Iterator<? extends E>...)"""
        return Iterator.__wrap(__IteratorUtils.chainedIterator(arg0))

    @staticmethod
    @overload
    def boundedIterator(arg0: 'Iterator', arg1: int) -> 'iterators.BoundedIterator':
        """public static <E> org.apache.commons.collections4.iterators.BoundedIterator<E> org.apache.commons.collections4.IteratorUtils.boundedIterator(java.util.Iterator<? extends E>,long)"""
        return iterators.BoundedIterator.__wrap(__IteratorUtils.boundedIterator(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def asEnumeration(arg0: 'Iterator') -> 'Enumeration':
        """public static <E> java.util.Enumeration<E> org.apache.commons.collections4.IteratorUtils.asEnumeration(java.util.Iterator<? extends E>)"""
        return Enumeration.__wrap(__IteratorUtils.asEnumeration(arg0))

    @staticmethod
    @overload
    def forEach(arg0: 'Iterator', arg1: 'Closure'):
        """public static <E> void org.apache.commons.collections4.IteratorUtils.forEach(java.util.Iterator<E>,org.apache.commons.collections4.Closure<? super E>)"""
        __IteratorUtils.forEach(arg0, arg1)

    @staticmethod
    @overload
    def chainedIterator(arg0: 'Iterator', arg1: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.chainedIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return Iterator.__wrap(__IteratorUtils.chainedIterator(arg0, arg1))

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
    def toString(arg0: 'Iterator', arg1: 'Transformer') -> str:
        """public static <E> java.lang.String org.apache.commons.collections4.IteratorUtils.toString(java.util.Iterator<E>,org.apache.commons.collections4.Transformer<? super E, java.lang.String>)"""
        return str.__wrap(__IteratorUtils.toString(arg0, arg1))

    @staticmethod
    @overload
    def arrayListIterator(*arg0: object) -> 'ResettableListIterator':
        """public static <E> org.apache.commons.collections4.ResettableListIterator<E> org.apache.commons.collections4.IteratorUtils.arrayListIterator(E...)"""
        return ResettableListIterator.__wrap(__IteratorUtils.arrayListIterator(arg0))

    @staticmethod
    @overload
    def filteredIterator(arg0: 'Iterator', arg1: 'Predicate') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.filteredIterator(java.util.Iterator<? extends E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Iterator.__wrap(__IteratorUtils.filteredIterator(arg0, arg1))

    @staticmethod
    @overload
    def zippingIterator(arg0: 'Iterator', arg1: 'Iterator') -> 'iterators.ZippingIterator':
        """public static <E> org.apache.commons.collections4.iterators.ZippingIterator<E> org.apache.commons.collections4.IteratorUtils.zippingIterator(java.util.Iterator<? extends E>,java.util.Iterator<? extends E>)"""
        return iterators.ZippingIterator.__wrap(__IteratorUtils.zippingIterator(arg0, arg1))

    @staticmethod
    @overload
    def singletonIterator(arg0: object) -> 'ResettableIterator':
        """public static <E> org.apache.commons.collections4.ResettableIterator<E> org.apache.commons.collections4.IteratorUtils.singletonIterator(E)"""
        return ResettableIterator.__wrap(__IteratorUtils.singletonIterator(arg0))

    @staticmethod
    @overload
    def toList(arg0: 'Iterator', arg1: int) -> 'List':
        """public static <E> java.util.List<E> org.apache.commons.collections4.IteratorUtils.toList(java.util.Iterator<? extends E>,int)"""
        return List.__wrap(__IteratorUtils.toList(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def singletonListIterator(arg0: object) -> 'ListIterator':
        """public static <E> java.util.ListIterator<E> org.apache.commons.collections4.IteratorUtils.singletonListIterator(E)"""
        return ListIterator.__wrap(__IteratorUtils.singletonListIterator(arg0))

    @staticmethod
    @overload
    def asIterator(arg0: 'Enumeration', arg1: 'Collection') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.asIterator(java.util.Enumeration<? extends E>,java.util.Collection<? super E>)"""
        return Iterator.__wrap(__IteratorUtils.asIterator(arg0, arg1))

    @staticmethod
    @overload
    def unmodifiableIterator(arg0: 'Iterator') -> 'Iterator':
        """public static <E> java.util.Iterator<E> org.apache.commons.collections4.IteratorUtils.unmodifiableIterator(java.util.Iterator<E>)"""
        return Iterator.__wrap(__IteratorUtils.unmodifiableIterator(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.Get
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from abc import abstractmethod, ABC
 
class Get(ABC):
    """org.apache.commons.collections4.Get"""
 
    @staticmethod
    def __wrap(java_value: __Get) -> 'Get':
        return Get(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Get):
        """
        Dynamic initializer for Get.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MultiSetUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.MultiSetUtils as __MultiSetUtils
__MultiSetUtils = __MultiSetUtils
import java.lang.Long as __long
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MultiSetUtils():
    """org.apache.commons.collections4.MultiSetUtils"""
 
    @staticmethod
    def __wrap(java_value: __MultiSetUtils) -> 'MultiSetUtils':
        return MultiSetUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiSetUtils):
        """
        Dynamic initializer for MultiSetUtils.
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
    def predicatedMultiSet(arg0: 'MultiSet', arg1: 'Predicate') -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.predicatedMultiSet(org.apache.commons.collections4.MultiSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return MultiSet.__wrap(__MultiSetUtils.predicatedMultiSet(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedMultiSet(arg0: 'MultiSet') -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.synchronizedMultiSet(org.apache.commons.collections4.MultiSet<E>)"""
        return MultiSet.__wrap(__MultiSetUtils.synchronizedMultiSet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def unmodifiableMultiSet(arg0: 'MultiSet') -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.unmodifiableMultiSet(org.apache.commons.collections4.MultiSet<? extends E>)"""
        return MultiSet.__wrap(__MultiSetUtils.unmodifiableMultiSet(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def emptyMultiSet() -> 'MultiSet':
        """public static <E> org.apache.commons.collections4.MultiSet<E> org.apache.commons.collections4.MultiSetUtils.emptyMultiSet()"""
        return MultiSet.__wrap(__MultiSetUtils.emptyMultiSet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.ListValuedMap
import org.apache.commons.collections4.ListValuedMap as __ListValuedMap
__ListValuedMap = __ListValuedMap
import java.lang.Iterable as Iterable
import org.apache.commons.collections4.MultiValuedMap as __MultiValuedMap
__MultiValuedMap = __MultiValuedMap
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class ListValuedMap(ABC, __MultiValuedMap, MultiValuedMap):
    """org.apache.commons.collections4.ListValuedMap"""
 
    @staticmethod
    def __wrap(java_value: __ListValuedMap) -> 'ListValuedMap':
        return ListValuedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListValuedMap):
        """
        Dynamic initializer for ListValuedMap.
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
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.MultiValuedMap.mapIterator()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.util.List<V> org.apache.commons.collections4.ListValuedMap.get(K)"""
        pass

    @abstractmethod
    def putAll(self, arg0: object, arg1: 'Iterable'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(K,java.lang.Iterable<? extends V>)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.removeMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.MultiValuedMap.clear()"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.MultiValuedMap.values()"""
        pass

    @abstractmethod
    def containsMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsMapping(java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.isEmpty()"""
        pass

    @abstractmethod
    def keys(self, ):
        """public abstract org.apache.commons.collections4.MultiSet<K> org.apache.commons.collections4.MultiValuedMap.keys()"""
        pass

    @abstractmethod
    def entries(self, ):
        """public abstract java.util.Collection<java.util.Map$Entry<K, V>> org.apache.commons.collections4.MultiValuedMap.entries()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.put(K,V)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.MultiValuedMap.keySet()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'MultiValuedMap'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiValuedMap.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiValuedMap.size()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.util.List<V> org.apache.commons.collections4.ListValuedMap.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def asMap(self, ):
        """public abstract java.util.Map<K, java.util.Collection<V>> org.apache.commons.collections4.MultiValuedMap.asMap()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.Trie
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.lang.Object as __object
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
import java.util.SequencedCollection as SequencedCollection
import java.util.Map.Entry as Entry
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.util.SortedMap as SortedMap
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
import org.apache.commons.collections4.Trie as __Trie
__Trie = __Trie
 
class Trie(ABC, __IterableSortedMap, IterableSortedMap):
    """org.apache.commons.collections4.Trie"""
 
    @staticmethod
    def __wrap(java_value: __Trie) -> 'Trie':
        return Trie(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Trie):
        """
        Dynamic initializer for Trie.
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
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def tailMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.tailMap(K)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def prefixMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> org.apache.commons.collections4.Trie.prefixMap(K)"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K java.util.SortedMap.firstKey()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K java.util.SortedMap.lastKey()"""
        pass

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.SortedMap.entrySet()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.SortedMap.keySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def headMap(self, arg0: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.headMap(K)"""
        pass

    @abstractmethod
    def subMap(self, arg0: object, arg1: object):
        """public abstract java.util.SortedMap<K, V> java.util.SortedMap.subMap(K,K)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.SortedMap.values()"""
        pass

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def sequencedKeySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<K> java.util.SequencedMap.sequencedKeySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedKeySet())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def comparator(self, ):
        """public abstract java.util.Comparator<? super K> java.util.SortedMap.comparator()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.OrderedIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import org.apache.commons.collections4.OrderedIterator as __OrderedIterator
__OrderedIterator = __OrderedIterator
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class OrderedIterator(ABC, __Iterator, Iterator):
    """org.apache.commons.collections4.OrderedIterator"""
 
    @staticmethod
    def __wrap(java_value: __OrderedIterator) -> 'OrderedIterator':
        return OrderedIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedIterator):
        """
        Dynamic initializer for OrderedIterator.
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
    def hasPrevious(self, ):
        """public abstract boolean org.apache.commons.collections4.OrderedIterator.hasPrevious()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract E org.apache.commons.collections4.OrderedIterator.previous()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.Iterator.next()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.MultiSet
import java.util.function.Predicate as Predicate
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
import org.apache.commons.collections4.MultiSet as __MultiSet
__MultiSet = __MultiSet
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MultiSet(ABC, __Collection, Collection):
    """org.apache.commons.collections4.MultiSet"""
 
    @staticmethod
    def __wrap(java_value: __MultiSet) -> 'MultiSet':
        return MultiSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiSet):
        """
        Dynamic initializer for MultiSet.
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
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.MultiSet.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @abstractmethod
    def add(self, arg0: object, arg1: int):
        """public abstract int org.apache.commons.collections4.MultiSet.add(E,int)"""
        pass

    @abstractmethod
    def setCount(self, arg0: object, arg1: int):
        """public abstract int org.apache.commons.collections4.MultiSet.setCount(E,int)"""
        pass

    @abstractmethod
    def getCount(self, arg0: object):
        """public abstract int org.apache.commons.collections4.MultiSet.getCount(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object, arg1: int):
        """public abstract int org.apache.commons.collections4.MultiSet.remove(java.lang.Object,int)"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet.size()"""
        pass

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet.add(E)"""
        pass

    @abstractmethod
    def uniqueSet(self, ):
        """public abstract java.util.Set<E> org.apache.commons.collections4.MultiSet.uniqueSet()"""
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
    def iterator(self, ):
        """public abstract java.util.Iterator<E> org.apache.commons.collections4.MultiSet.iterator()"""
        pass

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.MultiSet.containsAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiSet.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.apache.commons.collections4.MultiSet.hashCode()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<org.apache.commons.collections4.MultiSet$Entry<E>> org.apache.commons.collections4.MultiSet.entrySet()"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.MultiSet.removeAll(java.util.Collection<?>)"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.SetUtils
from builtins import str
import java.util.NavigableSet as NavigableSet
from pyquantum_helper import override
import java.util.HashSet as HashSet
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.HashSet as __HashSet
__HashSet = __HashSet
import java.util.SortedSet as SortedSet
import java.util.Collection as Collection
from builtins import object
import java.util.Set as Set
import java.util.SortedSet as __SortedSet
__SortedSet = __SortedSet
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.SetUtils as __SetUtils_SetView
__SetView = __SetUtils_SetView.SetView
import java.lang.Integer as __int
import org.apache.commons.collections4.SetUtils as __SetUtils
__SetUtils = __SetUtils
from builtins import bool
from builtins import int
 
class SetUtils():
    """org.apache.commons.collections4.SetUtils"""
 
    @staticmethod
    def __wrap(java_value: __SetUtils) -> 'SetUtils':
        return SetUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetUtils):
        """
        Dynamic initializer for SetUtils.
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
    def predicatedNavigableSet(arg0: 'NavigableSet', arg1: 'Predicate') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.predicatedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return SortedSet.__wrap(__SetUtils.predicatedNavigableSet(arg0, arg1))

    @staticmethod
    @overload
    def hashSet(*arg0: object) -> 'HashSet':
        """public static <E> java.util.HashSet<E> org.apache.commons.collections4.SetUtils.hashSet(E...)"""
        return HashSet.__wrap(__SetUtils.hashSet(arg0))

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'Set') -> 'Set':
        """public static <T> java.util.Set<T> org.apache.commons.collections4.SetUtils.emptyIfNull(java.util.Set<T>)"""
        return Set.__wrap(__SetUtils.emptyIfNull(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def newIdentityHashSet() -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.newIdentityHashSet()"""
        return Set.__wrap(__SetUtils.newIdentityHashSet())

    @staticmethod
    @overload
    def predicatedSortedSet(arg0: 'SortedSet', arg1: 'Predicate') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.predicatedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return SortedSet.__wrap(__SetUtils.predicatedSortedSet(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def unmodifiableSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.unmodifiableSet(java.util.Set<? extends E>)"""
        return Set.__wrap(__SetUtils.unmodifiableSet(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Set.__wrap(__SetUtils.predicatedSet(arg0, arg1))

    @staticmethod
    @overload
    def transformedSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.transformedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return SortedSet.__wrap(__SetUtils.transformedSortedSet(arg0, arg1))

    @staticmethod
    @overload
    def synchronizedSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.synchronizedSortedSet(java.util.SortedSet<E>)"""
        return SortedSet.__wrap(__SetUtils.synchronizedSortedSet(arg0))

    @staticmethod
    @overload
    def unmodifiableSet(*arg0: object) -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.unmodifiableSet(E...)"""
        return Set.__wrap(__SetUtils.unmodifiableSet(arg0))

    @staticmethod
    @overload
    def emptySortedSet() -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.emptySortedSet()"""
        return SortedSet.__wrap(__SetUtils.emptySortedSet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def union(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.union(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView.__wrap(__SetUtils.union(arg0, arg1))

    @staticmethod
    @overload
    def disjunction(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.disjunction(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView.__wrap(__SetUtils.disjunction(arg0, arg1))

    @staticmethod
    @overload
    def intersection(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.intersection(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView.__wrap(__SetUtils.intersection(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def hashCodeForSet(arg0: 'Collection') -> int:
        """public static <T> int org.apache.commons.collections4.SetUtils.hashCodeForSet(java.util.Collection<T>)"""
        return int.__wrap(__SetUtils.hashCodeForSet(arg0))

    @staticmethod
    @overload
    def unmodifiableSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.unmodifiableSortedSet(java.util.SortedSet<E>)"""
        return SortedSet.__wrap(__SetUtils.unmodifiableSortedSet(arg0))

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set.__wrap(__SetUtils.transformedSet(arg0, arg1))

    @staticmethod
    @overload
    def isEqualSet(arg0: 'Collection', arg1: 'Collection') -> bool:
        """public static boolean org.apache.commons.collections4.SetUtils.isEqualSet(java.util.Collection<?>,java.util.Collection<?>)"""
        return bool.__wrap(__SetUtils.isEqualSet(arg0, arg1))

    @staticmethod
    @overload
    def orderedSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.orderedSet(java.util.Set<E>)"""
        return Set.__wrap(__SetUtils.orderedSet(arg0))

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
    def synchronizedSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.synchronizedSet(java.util.Set<E>)"""
        return Set.__wrap(__SetUtils.synchronizedSet(arg0))

    @staticmethod
    @overload
    def emptySet() -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.SetUtils.emptySet()"""
        return Set.__wrap(__SetUtils.emptySet())

    @staticmethod
    @overload
    def transformedNavigableSet(arg0: 'NavigableSet', arg1: 'Transformer') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.transformedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return SortedSet.__wrap(__SetUtils.transformedNavigableSet(arg0, arg1))

    @staticmethod
    @overload
    def difference(arg0: 'Set', arg1: 'Set') -> 'SetView':
        """public static <E> org.apache.commons.collections4.SetUtils$SetView<E> org.apache.commons.collections4.SetUtils.difference(java.util.Set<? extends E>,java.util.Set<? extends E>)"""
        return SetView.__wrap(__SetUtils.difference(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def unmodifiableNavigableSet(arg0: 'NavigableSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.SetUtils.unmodifiableNavigableSet(java.util.NavigableSet<E>)"""
        return SortedSet.__wrap(__SetUtils.unmodifiableNavigableSet(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.TransformerUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.TransformerUtils as __TransformerUtils
__TransformerUtils = __TransformerUtils
import java.lang.Integer as __int
import org.apache.commons.collections4.Transformer as __Transformer
__Transformer = __Transformer
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class TransformerUtils():
    """org.apache.commons.collections4.TransformerUtils"""
 
    @staticmethod
    def __wrap(java_value: __TransformerUtils) -> 'TransformerUtils':
        return TransformerUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformerUtils):
        """
        Dynamic initializer for TransformerUtils.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def cloneTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.cloneTransformer()"""
        return Transformer.__wrap(__TransformerUtils.cloneTransformer())

    @staticmethod
    @overload
    def invokerTransformer(arg0: str, arg1: 'Class', arg2: 'Object') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.invokerTransformer(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return Transformer.__wrap(__TransformerUtils.invokerTransformer(arg0, arg1, arg2))

    @staticmethod
    @overload
    def instantiateTransformer(arg0: 'Class', arg1: 'Object') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.TransformerUtils.instantiateTransformer(java.lang.Class<?>[],java.lang.Object[])"""
        return Transformer.__wrap(__TransformerUtils.instantiateTransformer(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def instantiateTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<java.lang.Class<? extends T>, T> org.apache.commons.collections4.TransformerUtils.instantiateTransformer()"""
        return Transformer.__wrap(__TransformerUtils.instantiateTransformer())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def exceptionTransformer() -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.exceptionTransformer()"""
        return Transformer.__wrap(__TransformerUtils.exceptionTransformer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def asTransformer(arg0: 'Closure') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.asTransformer(org.apache.commons.collections4.Closure<? super T>)"""
        return Transformer.__wrap(__TransformerUtils.asTransformer(arg0))

    @staticmethod
    @overload
    def constantTransformer(arg0: object) -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.constantTransformer(O)"""
        return Transformer.__wrap(__TransformerUtils.constantTransformer(arg0))

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.ifTransformer(org.apache.commons.collections4.Predicate<? super T>,org.apache.commons.collections4.Transformer<? super T, ? extends T>)"""
        return Transformer.__wrap(__TransformerUtils.ifTransformer(arg0, arg1))

    @staticmethod
    @overload
    def asTransformer(arg0: 'Predicate') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.Boolean> org.apache.commons.collections4.TransformerUtils.asTransformer(org.apache.commons.collections4.Predicate<? super T>)"""
        return Transformer.__wrap(__TransformerUtils.asTransformer(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def mapTransformer(arg0: 'Map') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.mapTransformer(java.util.Map<? super I, ? extends O>)"""
        return Transformer.__wrap(__TransformerUtils.mapTransformer(arg0))

    @staticmethod
    @overload
    def nopTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.nopTransformer()"""
        return Transformer.__wrap(__TransformerUtils.nopTransformer())

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Transformer.__wrap(__TransformerUtils.switchTransformer(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nullTransformer() -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.nullTransformer()"""
        return Transformer.__wrap(__TransformerUtils.nullTransformer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def chainedTransformer(*arg0: 'Transformer') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.chainedTransformer(org.apache.commons.collections4.Transformer<? super T, ? extends T>...)"""
        return Transformer.__wrap(__TransformerUtils.chainedTransformer(arg0))

    @staticmethod
    @overload
    def switchMapTransformer(arg0: 'Map') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchMapTransformer(java.util.Map<I, org.apache.commons.collections4.Transformer<I, O>>)"""
        return Transformer.__wrap(__TransformerUtils.switchMapTransformer(arg0))

    @staticmethod
    @overload
    def ifTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.ifTransformer(org.apache.commons.collections4.Predicate<? super I>,org.apache.commons.collections4.Transformer<? super I, ? extends O>,org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Transformer.__wrap(__TransformerUtils.ifTransformer(arg0, arg1, arg2))

    @staticmethod
    @overload
    def asTransformer(arg0: 'Factory') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.asTransformer(org.apache.commons.collections4.Factory<? extends O>)"""
        return Transformer.__wrap(__TransformerUtils.asTransformer(arg0))

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer', arg2: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>)"""
        return Transformer.__wrap(__TransformerUtils.switchTransformer(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stringValueTransformer() -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, java.lang.String> org.apache.commons.collections4.TransformerUtils.stringValueTransformer()"""
        return Transformer.__wrap(__TransformerUtils.stringValueTransformer())

    @staticmethod
    @overload
    def chainedTransformer(arg0: 'Collection') -> 'Transformer':
        """public static <T> org.apache.commons.collections4.Transformer<T, T> org.apache.commons.collections4.TransformerUtils.chainedTransformer(java.util.Collection<? extends org.apache.commons.collections4.Transformer<? super T, ? extends T>>)"""
        return Transformer.__wrap(__TransformerUtils.chainedTransformer(arg0))

    @staticmethod
    @overload
    def invokerTransformer(arg0: str) -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.invokerTransformer(java.lang.String)"""
        return Transformer.__wrap(__TransformerUtils.invokerTransformer(arg0))

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Map') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(java.util.Map<org.apache.commons.collections4.Predicate<I>, org.apache.commons.collections4.Transformer<I, O>>)"""
        return Transformer.__wrap(__TransformerUtils.switchTransformer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def switchTransformer(arg0: 'Predicate', arg1: 'Transformer') -> 'Transformer':
        """public static <I,O> org.apache.commons.collections4.Transformer<I, O> org.apache.commons.collections4.TransformerUtils.switchTransformer(org.apache.commons.collections4.Predicate<? super I>[],org.apache.commons.collections4.Transformer<? super I, ? extends O>[])"""
        return Transformer.__wrap(__TransformerUtils.switchTransformer(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.ResettableIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import org.apache.commons.collections4.ResettableIterator as __ResettableIterator
__ResettableIterator = __ResettableIterator
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class ResettableIterator(ABC, __Iterator, Iterator):
    """org.apache.commons.collections4.ResettableIterator"""
 
    @staticmethod
    def __wrap(java_value: __ResettableIterator) -> 'ResettableIterator':
        return ResettableIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResettableIterator):
        """
        Dynamic initializer for ResettableIterator.
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
    def reset(self, ):
        """public abstract void org.apache.commons.collections4.ResettableIterator.reset()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public default void java.util.Iterator.remove()"""
        super(Iterator, self).remove()

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.Iterator.next()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.Iterator.hasNext()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.ClosureUtils
import org.apache.commons.collections4.Closure as __Closure
__Closure = __Closure
from builtins import str
import org.apache.commons.collections4.ClosureUtils as __ClosureUtils
__ClosureUtils = __ClosureUtils
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Collection as Collection
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
from builtins import int
 
class ClosureUtils():
    """org.apache.commons.collections4.ClosureUtils"""
 
    @staticmethod
    def __wrap(java_value: __ClosureUtils) -> 'ClosureUtils':
        return ClosureUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClosureUtils):
        """
        Dynamic initializer for ClosureUtils.
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
    def switchClosure(arg0: 'Map') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchClosure(java.util.Map<org.apache.commons.collections4.Predicate<E>, org.apache.commons.collections4.Closure<E>>)"""
        return Closure.__wrap(__ClosureUtils.switchClosure(arg0))

    @staticmethod
    @overload
    def chainedClosure(*arg0: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.chainedClosure(org.apache.commons.collections4.Closure<? super E>...)"""
        return Closure.__wrap(__ClosureUtils.chainedClosure(arg0))

    @staticmethod
    @overload
    def invokerClosure(arg0: str) -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.invokerClosure(java.lang.String)"""
        return Closure.__wrap(__ClosureUtils.invokerClosure(arg0))

    @staticmethod
    @overload
    def doWhileClosure(arg0: 'Closure', arg1: 'Predicate') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.doWhileClosure(org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return Closure.__wrap(__ClosureUtils.doWhileClosure(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def exceptionClosure() -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.exceptionClosure()"""
        return Closure.__wrap(__ClosureUtils.exceptionClosure())

    @staticmethod
    @overload
    def switchClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[],org.apache.commons.collections4.Closure<? super E>)"""
        return Closure.__wrap(__ClosureUtils.switchClosure(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def forClosure(arg0: int, arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.forClosure(int,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure.__wrap(__ClosureUtils.forClosure(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure', arg2: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure.__wrap(__ClosureUtils.ifClosure(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def chainedClosure(arg0: 'Collection') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.chainedClosure(java.util.Collection<? extends org.apache.commons.collections4.Closure<? super E>>)"""
        return Closure.__wrap(__ClosureUtils.chainedClosure(arg0))

    @staticmethod
    @overload
    def ifClosure(arg0: 'Predicate', arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.ifClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure.__wrap(__ClosureUtils.ifClosure(arg0, arg1))

    @staticmethod
    @overload
    def switchClosure(arg0: 'Predicate', arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchClosure(org.apache.commons.collections4.Predicate<? super E>[],org.apache.commons.collections4.Closure<? super E>[])"""
        return Closure.__wrap(__ClosureUtils.switchClosure(arg0, arg1))

    @staticmethod
    @overload
    def invokerClosure(arg0: str, arg1: 'Class', arg2: 'Object') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.invokerClosure(java.lang.String,java.lang.Class<?>[],java.lang.Object[])"""
        return Closure.__wrap(__ClosureUtils.invokerClosure(arg0, arg1, arg2))

    @staticmethod
    @overload
    def switchMapClosure(arg0: 'Map') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.switchMapClosure(java.util.Map<? extends E, org.apache.commons.collections4.Closure<E>>)"""
        return Closure.__wrap(__ClosureUtils.switchMapClosure(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nopClosure() -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.nopClosure()"""
        return Closure.__wrap(__ClosureUtils.nopClosure())

    @staticmethod
    @overload
    def asClosure(arg0: 'Transformer') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.asClosure(org.apache.commons.collections4.Transformer<? super E, ?>)"""
        return Closure.__wrap(__ClosureUtils.asClosure(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def whileClosure(arg0: 'Predicate', arg1: 'Closure') -> 'Closure':
        """public static <E> org.apache.commons.collections4.Closure<E> org.apache.commons.collections4.ClosureUtils.whileClosure(org.apache.commons.collections4.Predicate<? super E>,org.apache.commons.collections4.Closure<? super E>)"""
        return Closure.__wrap(__ClosureUtils.whileClosure(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.ArrayStack
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
from builtins import bool
from builtins import str
import java.util.function.UnaryOperator as UnaryOperator
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
import java.util.Comparator as Comparator
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.ListIterator as ListIterator
import org.apache.commons.collections4.ArrayStack as __ArrayStack
__ArrayStack = __ArrayStack
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class ArrayStack(__ArrayList, ArrayList):
    """org.apache.commons.collections4.ArrayStack"""
 
    @staticmethod
    def __wrap(java_value: __ArrayStack) -> 'ArrayStack':
        return ArrayStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayStack):
        """
        Dynamic initializer for ArrayStack.
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
    def remove(self, arg0: int) -> object:
        """public E java.util.ArrayList.remove(int)"""
        return object.__wrap(super(__ArrayList, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.ArrayList.isEmpty()"""
        return bool.__wrap(super(ArrayList, self).isEmpty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @overload
    def subList(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<E> java.util.ArrayList.subList(int,int)"""
        return 'List'.__wrap(super(__ArrayList, self).subList(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.ArrayList.iterator()"""
        return 'Iterator'.__wrap(super(ArrayList, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.ArrayStack()"""
        val = __ArrayStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).retainAll(arg0))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void java.util.ArrayList.ensureCapacity(int)"""
        super(__ArrayList, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.add(E)"""
        return bool.__wrap(super(__ArrayList, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @overload
    def peek(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.ArrayStack.peek(int) throws java.util.EmptyStackException"""
        return object.__wrap(super(__ArrayStack, self).peek(__int.valueOf(arg0)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def sort(self, arg0: 'Comparator'):
        """public void java.util.ArrayList.sort(java.util.Comparator<? super E>)"""
        super(__ArrayList, self).sort(arg0)

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.ArrayList.toArray(T[])"""
        return List[object].__wrap(super(__ArrayList, self).toArray(arg0))

    @overload
    def set(self, arg0: int, arg1: object) -> object:
        """public E java.util.ArrayList.set(int,E)"""
        return object.__wrap(super(__ArrayList, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def removeFirst(self) -> object:
        """public E java.util.ArrayList.removeFirst()"""
        return object.__wrap(super(ArrayList, self).removeFirst())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.ArrayList.toArray()"""
        return List[object].__wrap(super(ArrayList, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean java.util.ArrayList.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__ArrayList, self).removeIf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.ArrayList.spliterator()"""
        return 'Spliterator'.__wrap(super(ArrayList, self).spliterator())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.ArrayList.size()"""
        return int.__wrap(super(ArrayList, self).size())

    @override
    @overload
    def add(self, arg0: int, arg1: object):
        """public void java.util.ArrayList.add(int,E)"""
        super(__ArrayList, self).add(__int.valueOf(arg0), arg1)

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.ArrayList.clone()"""
        return object.__wrap(super(ArrayList, self).clone())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.ArrayStack(int)"""
        val = __ArrayStack(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.indexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).indexOf(arg0))

    @overload
    def empty(self) -> bool:
        """public boolean org.apache.commons.collections4.ArrayStack.empty()"""
        return bool.__wrap(super(ArrayStack, self).empty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def listIterator(self, arg0: int) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator(int)"""
        return 'ListIterator'.__wrap(super(__ArrayList, self).listIterator(__int.valueOf(arg0)))

    @overload
    def pop(self) -> object:
        """public E org.apache.commons.collections4.ArrayStack.pop() throws java.util.EmptyStackException"""
        return object.__wrap(super(ArrayStack, self).pop())

    @overload
    def get(self, arg0: int) -> object:
        """public E java.util.ArrayList.get(int)"""
        return object.__wrap(super(__ArrayList, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.ArrayStack()"""
        val = __ArrayStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__ArrayList, self).removeAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public void java.util.ArrayList.addFirst(E)"""
        super(__ArrayList, self).addFirst(arg0)

    @override
    @overload
    def removeLast(self) -> object:
        """public E java.util.ArrayList.removeLast()"""
        return object.__wrap(super(ArrayList, self).removeLast())

    @override
    @overload
    def getFirst(self) -> object:
        """public E java.util.ArrayList.getFirst()"""
        return object.__wrap(super(ArrayList, self).getFirst())

    @override
    @overload
    def trimToSize(self):
        """public void java.util.ArrayList.trimToSize()"""
        super(ArrayList, self).trimToSize()

    @overload
    def peek(self) -> object:
        """public E org.apache.commons.collections4.ArrayStack.peek() throws java.util.EmptyStackException"""
        return object.__wrap(super(ArrayStack, self).peek())

    @overload
    def push(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.ArrayStack.push(E)"""
        return object.__wrap(super(__ArrayStack, self).push(arg0))

    @override
    @overload
    def clear(self):
        """public void java.util.ArrayList.clear()"""
        super(ArrayList, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.ArrayList.hashCode()"""
        return int.__wrap(super(ArrayList, self).hashCode())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.contains(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).contains(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean java.util.ArrayList.addAll(int,java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__ArrayList, self).addAll(__int.valueOf(arg0), arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'UnaryOperator'):
        """public void java.util.ArrayList.replaceAll(java.util.function.UnaryOperator<E>)"""
        super(__ArrayList, self).replaceAll(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public E java.util.ArrayList.getLast()"""
        return object.__wrap(super(ArrayList, self).getLast())

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
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.remove(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).remove(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public void java.util.ArrayList.addLast(E)"""
        super(__ArrayList, self).addLast(arg0)

    @overload
    def search(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.ArrayStack.search(java.lang.Object)"""
        return int.__wrap(super(__ArrayStack, self).search(arg0))

    @override
    @overload
    def reversed(self) -> 'List':
        """public default java.util.List<E> java.util.List.reversed()"""
        return 'List'.__wrap(super(List, self).reversed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.ArrayList.equals(java.lang.Object)"""
        return bool.__wrap(super(__ArrayList, self).equals(arg0))

    @overload
    def lastIndexOf(self, arg0: object) -> int:
        """public int java.util.ArrayList.lastIndexOf(java.lang.Object)"""
        return int.__wrap(super(__ArrayList, self).lastIndexOf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void java.util.ArrayList.forEach(java.util.function.Consumer<? super E>)"""
        super(__ArrayList, self).forEach(arg0)

    @override
    @overload
    def listIterator(self) -> 'ListIterator':
        """public java.util.ListIterator<E> java.util.ArrayList.listIterator()"""
        return 'ListIterator'.__wrap(super(ArrayList, self).listIterator()) 
 
 
# CLASS: org.apache.commons.collections4.BidiMap
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.lang.Object as __object
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.IterableGet as __IterableGet
__IterableGet = __IterableGet
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class BidiMap(ABC, __IterableMap, IterableMap):
    """org.apache.commons.collections4.BidiMap"""
 
    @staticmethod
    def __wrap(java_value: __BidiMap) -> 'BidiMap':
        return BidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BidiMap):
        """
        Dynamic initializer for BidiMap.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def getKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.getKey(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Set<V> org.apache.commons.collections4.BidiMap.values()"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V org.apache.commons.collections4.BidiMap.put(K,V)"""
        pass

    @abstractmethod
    def removeValue(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.removeValue(java.lang.Object)"""
        pass

    @abstractmethod
    def inverseBidiMap(self, ):
        """public abstract org.apache.commons.collections4.BidiMap<V, K> org.apache.commons.collections4.BidiMap.inverseBidiMap()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.MultiMap
import org.apache.commons.collections4.MultiMap as __MultiMap
__MultiMap = __MultiMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.lang.Object as __object
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.IterableGet as __IterableGet
__IterableGet = __IterableGet
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class MultiMap(ABC, __IterableMap, IterableMap):
    """org.apache.commons.collections4.MultiMap"""
 
    @staticmethod
    def __wrap(java_value: __MultiMap) -> 'MultiMap':
        return MultiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiMap):
        """
        Dynamic initializer for MultiMap.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.MultiMap.put(K,java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract java.lang.Object org.apache.commons.collections4.MultiMap.remove(java.lang.Object)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.MultiMap.size()"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.MultiMap.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def removeMapping(self, arg0: object, arg1: object):
        """public abstract boolean org.apache.commons.collections4.MultiMap.removeMapping(K,V)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract java.lang.Object org.apache.commons.collections4.MultiMap.get(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<java.lang.Object> org.apache.commons.collections4.MultiMap.values()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.MultiMapUtils
import org.apache.commons.collections4.SetValuedMap as __SetValuedMap
__SetValuedMap = __SetValuedMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.Bag as __Bag
__Bag = __Bag
import org.apache.commons.collections4.MultiValuedMap as __MultiValuedMap
__MultiValuedMap = __MultiValuedMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MultiMapUtils as __MultiMapUtils
__MultiMapUtils = __MultiMapUtils
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.ListValuedMap as __ListValuedMap
__ListValuedMap = __ListValuedMap
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class MultiMapUtils():
    """org.apache.commons.collections4.MultiMapUtils"""
 
    @staticmethod
    def __wrap(java_value: __MultiMapUtils) -> 'MultiMapUtils':
        return MultiMapUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiMapUtils):
        """
        Dynamic initializer for MultiMapUtils.
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
    def newListValuedHashMap() -> 'ListValuedMap':
        """public static <K,V> org.apache.commons.collections4.ListValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.newListValuedHashMap()"""
        return ListValuedMap.__wrap(__MultiMapUtils.newListValuedHashMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def emptyMultiValuedMap() -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.emptyMultiValuedMap()"""
        return MultiValuedMap.__wrap(__MultiMapUtils.emptyMultiValuedMap())

    @staticmethod
    @overload
    def transformedMultiValuedMap(arg0: 'MultiValuedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.transformedMultiValuedMap(org.apache.commons.collections4.MultiValuedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return MultiValuedMap.__wrap(__MultiMapUtils.transformedMultiValuedMap(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def isEmpty(arg0: 'MultiValuedMap') -> bool:
        """public static boolean org.apache.commons.collections4.MultiMapUtils.isEmpty(org.apache.commons.collections4.MultiValuedMap<?, ?>)"""
        return bool.__wrap(__MultiMapUtils.isEmpty(arg0))

    @staticmethod
    @overload
    def unmodifiableMultiValuedMap(arg0: 'MultiValuedMap') -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.unmodifiableMultiValuedMap(org.apache.commons.collections4.MultiValuedMap<? extends K, ? extends V>)"""
        return MultiValuedMap.__wrap(__MultiMapUtils.unmodifiableMultiValuedMap(arg0))

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
    def getValuesAsList(arg0: 'MultiValuedMap', arg1: object) -> 'List':
        """public static <K,V> java.util.List<V> org.apache.commons.collections4.MultiMapUtils.getValuesAsList(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return List.__wrap(__MultiMapUtils.getValuesAsList(arg0, arg1))

    @staticmethod
    @overload
    def getValuesAsBag(arg0: 'MultiValuedMap', arg1: object) -> 'Bag':
        """public static <K,V> org.apache.commons.collections4.Bag<V> org.apache.commons.collections4.MultiMapUtils.getValuesAsBag(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return Bag.__wrap(__MultiMapUtils.getValuesAsBag(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def newSetValuedHashMap() -> 'SetValuedMap':
        """public static <K,V> org.apache.commons.collections4.SetValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.newSetValuedHashMap()"""
        return SetValuedMap.__wrap(__MultiMapUtils.newSetValuedHashMap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def emptyIfNull(arg0: 'MultiValuedMap') -> 'MultiValuedMap':
        """public static <K,V> org.apache.commons.collections4.MultiValuedMap<K, V> org.apache.commons.collections4.MultiMapUtils.emptyIfNull(org.apache.commons.collections4.MultiValuedMap<K, V>)"""
        return MultiValuedMap.__wrap(__MultiMapUtils.emptyIfNull(arg0))

    @staticmethod
    @overload
    def getCollection(arg0: 'MultiValuedMap', arg1: object) -> 'Collection':
        """public static <K,V> java.util.Collection<V> org.apache.commons.collections4.MultiMapUtils.getCollection(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return Collection.__wrap(__MultiMapUtils.getCollection(arg0, arg1))

    @staticmethod
    @overload
    def getValuesAsSet(arg0: 'MultiValuedMap', arg1: object) -> 'Set':
        """public static <K,V> java.util.Set<V> org.apache.commons.collections4.MultiMapUtils.getValuesAsSet(org.apache.commons.collections4.MultiValuedMap<K, V>,K)"""
        return Set.__wrap(__MultiMapUtils.getValuesAsSet(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.OrderedBidiMap
import org.apache.commons.collections4.BidiMap as __BidiMap
__BidiMap = __BidiMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import org.apache.commons.collections4.OrderedBidiMap as __OrderedBidiMap
__OrderedBidiMap = __OrderedBidiMap
import java.lang.Object as __object
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class OrderedBidiMap(ABC, __BidiMap, BidiMap, __OrderedMap, OrderedMap):
    """org.apache.commons.collections4.OrderedBidiMap"""
 
    @staticmethod
    def __wrap(java_value: __OrderedBidiMap) -> 'OrderedBidiMap':
        return OrderedBidiMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrderedBidiMap):
        """
        Dynamic initializer for OrderedBidiMap.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def getKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.getKey(java.lang.Object)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def firstKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.firstKey()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.OrderedMap.mapIterator()"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @abstractmethod
    def nextKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.nextKey(K)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def inverseBidiMap(self, ):
        """public abstract org.apache.commons.collections4.OrderedBidiMap<V, K> org.apache.commons.collections4.OrderedBidiMap.inverseBidiMap()"""
        pass

    @abstractmethod
    def previousKey(self, arg0: object):
        """public abstract K org.apache.commons.collections4.OrderedMap.previousKey(K)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Set<V> org.apache.commons.collections4.BidiMap.values()"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V org.apache.commons.collections4.BidiMap.put(K,V)"""
        pass

    @abstractmethod
    def removeValue(self, arg0: object):
        """public abstract K org.apache.commons.collections4.BidiMap.removeValue(java.lang.Object)"""
        pass

    @abstractmethod
    def lastKey(self, ):
        """public abstract K org.apache.commons.collections4.OrderedMap.lastKey()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.ResettableListIterator
import java.util.ListIterator as __ListIterator
__ListIterator = __ListIterator
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import org.apache.commons.collections4.OrderedIterator as __OrderedIterator
__OrderedIterator = __OrderedIterator
import org.apache.commons.collections4.ResettableListIterator as __ResettableListIterator
__ResettableListIterator = __ResettableListIterator
from abc import abstractmethod, ABC
import org.apache.commons.collections4.ResettableIterator as __ResettableIterator
__ResettableIterator = __ResettableIterator
import java.util.function.Consumer as Consumer
 
class ResettableListIterator(ABC, __ListIterator, ListIterator, __ResettableIterator, ResettableIterator, __OrderedIterator, OrderedIterator):
    """org.apache.commons.collections4.ResettableListIterator"""
 
    @staticmethod
    def __wrap(java_value: __ResettableListIterator) -> 'ResettableListIterator':
        return ResettableListIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResettableListIterator):
        """
        Dynamic initializer for ResettableListIterator.
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
    def reset(self, ):
        """public abstract void org.apache.commons.collections4.ResettableIterator.reset()"""
        pass

    @abstractmethod
    def nextIndex(self, ):
        """public abstract int java.util.ListIterator.nextIndex()"""
        pass

    @abstractmethod
    def previousIndex(self, ):
        """public abstract int java.util.ListIterator.previousIndex()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract E java.util.ListIterator.previous()"""
        pass

    @abstractmethod
    def next(self, ):
        """public abstract E java.util.ListIterator.next()"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract void java.util.ListIterator.add(E)"""
        pass

    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean java.util.ListIterator.hasPrevious()"""
        pass

    @abstractmethod
    def hasNext(self, ):
        """public abstract boolean java.util.ListIterator.hasNext()"""
        pass

    @abstractmethod
    def hasPrevious(self, ):
        """public abstract boolean org.apache.commons.collections4.OrderedIterator.hasPrevious()"""
        pass

    @abstractmethod
    def previous(self, ):
        """public abstract E org.apache.commons.collections4.OrderedIterator.previous()"""
        pass

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @abstractmethod
    def set(self, arg0: object):
        """public abstract void java.util.ListIterator.set(E)"""
        pass

    @abstractmethod
    def remove(self, ):
        """public abstract void java.util.ListIterator.remove()"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.IterableMap
import org.apache.commons.collections4.IterableMap as __IterableMap
__IterableMap = __IterableMap
import org.apache.commons.collections4.Put as __Put
__Put = __Put
import java.lang.Object as __object
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.IterableGet as __IterableGet
__IterableGet = __IterableGet
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class IterableMap(ABC, __Map, Map, __Put, Put, __IterableGet, IterableGet):
    """org.apache.commons.collections4.IterableMap"""
 
    @staticmethod
    def __wrap(java_value: __IterableMap) -> 'IterableMap':
        return IterableMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IterableMap):
        """
        Dynamic initializer for IterableMap.
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
    def keySet(self, ):
        """public abstract java.util.Set<K> org.apache.commons.collections4.Get.keySet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract java.lang.Object org.apache.commons.collections4.Put.put(K,V)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.commons.collections4.Put.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.commons.collections4.Get.size()"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> org.apache.commons.collections4.Get.values()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsKey(java.lang.Object)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def mapIterator(self, ):
        """public abstract org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.IterableGet.mapIterator()"""
        pass

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V org.apache.commons.collections4.Get.get(java.lang.Object)"""
        pass

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.Get.entrySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.commons.collections4.Get.isEmpty()"""
        pass

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass