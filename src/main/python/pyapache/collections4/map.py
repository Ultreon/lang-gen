from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import org.apache.commons.collections4.map.UnmodifiableEntrySet as __UnmodifiableEntrySet
__UnmodifiableEntrySet = __UnmodifiableEntrySet
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
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableEntrySet(collections4.__AbstractSetDecorator, set.AbstractSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.map.UnmodifiableEntrySet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableEntrySet) -> 'UnmodifiableEntrySet':
        return UnmodifiableEntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableEntrySet):
        """
        Dynamic initializer for UnmodifiableEntrySet.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).remove(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

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

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.map.UnmodifiableEntrySet.toArray()"""
        return List[object].__wrap(super(UnmodifiableEntrySet, self).toArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(set.AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableEntrySet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableEntrySet, self).iterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @overload
    def add(self, arg0: 'Entry') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.add(java.util.Map$Entry<K, V>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).add(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.removeIf(java.util.function.Predicate<? super java.util.Map$Entry<K, V>>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).removeIf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__set.AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).retainAll(arg0))

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
        """public <T> T[] org.apache.commons.collections4.map.UnmodifiableEntrySet.toArray(T[])"""
        return List[object].__wrap(super(__UnmodifiableEntrySet, self).toArray(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).removeAll(arg0))

    @staticmethod
    @overload
    def unmodifiableEntrySet(arg0: 'Set') -> 'Set':
        """public static <K,V> java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableEntrySet.unmodifiableEntrySet(java.util.Set<java.util.Map$Entry<K, V>>)"""
        return Set.__wrap(__UnmodifiableEntrySet.unmodifiableEntrySet(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.addAll(java.util.Collection<? extends java.util.Map$Entry<K, V>>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).addAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableEntrySet.clear()"""
        super(UnmodifiableEntrySet, self).clear()

 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableEntrySet
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as __AbstractCollectionDecorator
__AbstractCollectionDecorator = __AbstractCollectionDecorator
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.set.AbstractSetDecorator as __AbstractSetDecorator
__AbstractSetDecorator = __AbstractSetDecorator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import org.apache.commons.collections4.map.UnmodifiableEntrySet as __UnmodifiableEntrySet
__UnmodifiableEntrySet = __UnmodifiableEntrySet
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
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class UnmodifiableEntrySet(collections4.__AbstractSetDecorator, set.AbstractSetDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable):
    """org.apache.commons.collections4.map.UnmodifiableEntrySet"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableEntrySet) -> 'UnmodifiableEntrySet':
        return UnmodifiableEntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableEntrySet):
        """
        Dynamic initializer for UnmodifiableEntrySet.
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
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool.__wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).remove(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).contains(arg0))

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

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int.__wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.map.UnmodifiableEntrySet.toArray()"""
        return List[object].__wrap(super(UnmodifiableEntrySet, self).toArray())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int.__wrap(super(set.AbstractSetDecorator, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableEntrySet.iterator()"""
        return 'Iterator'.__wrap(super(UnmodifiableEntrySet, self).iterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str.__wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'.__wrap(super(Set, self).spliterator())

    @overload
    def add(self, arg0: 'Entry') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.add(java.util.Map$Entry<K, V>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).add(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.removeIf(java.util.function.Predicate<? super java.util.Map$Entry<K, V>>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).removeIf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__set.AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).retainAll(arg0))

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
        """public <T> T[] org.apache.commons.collections4.map.UnmodifiableEntrySet.toArray(T[])"""
        return List[object].__wrap(super(__UnmodifiableEntrySet, self).toArray(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).removeAll(arg0))

    @staticmethod
    @overload
    def unmodifiableEntrySet(arg0: 'Set') -> 'Set':
        """public static <K,V> java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableEntrySet.unmodifiableEntrySet(java.util.Set<java.util.Map$Entry<K, V>>)"""
        return Set.__wrap(__UnmodifiableEntrySet.unmodifiableEntrySet(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.UnmodifiableEntrySet.addAll(java.util.Collection<? extends java.util.Map$Entry<K, V>>)"""
        return bool.__wrap(super(__UnmodifiableEntrySet, self).addAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableEntrySet.clear()"""
        super(UnmodifiableEntrySet, self).clear()

 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableEntrySet 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractIterableMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.apache.commons.collections4.Put as __Put
__Put = __Put
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
from abc import abstractmethod, ABC
import org.apache.commons.collections4.Get as __Get
__Get = __Get
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractIterableMap(ABC, pyapache.__IterableMap, collections4.IterableMap):
    """org.apache.commons.collections4.map.AbstractIterableMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractIterableMap) -> 'AbstractIterableMap':
        return AbstractIterableMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractIterableMap):
        """
        Dynamic initializer for AbstractIterableMap.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.AbstractIterableMap()"""
        val = __AbstractIterableMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.AbstractIterableMap()"""
        val = __AbstractIterableMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void org.apache.commons.collections4.Put.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def containsValue(self, arg0: object):
        """public abstract boolean org.apache.commons.collections4.Get.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
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
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$ValuesIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkIterator
__LinkIterator = __AbstractLinkedMap_LinkIterator.LinkIterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_ValuesIterator
__ValuesIterator = __AbstractLinkedMap_ValuesIterator.ValuesIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValuesIterator(__LinkIterator, LinkIterator, pyapache.__OrderedIterator, collections4.OrderedIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.map.AbstractLinkedMap.ValuesIterator"""
 
    @staticmethod
    def __wrap(java_value: __ValuesIterator) -> 'ValuesIterator':
        return ValuesIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValuesIterator):
        """
        Dynamic initializer for ValuesIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool.__wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool.__wrap(super(LinkIterator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str.__wrap(super(LinkIterator, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def previous(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$ValuesIterator.previous()"""
        return object.__wrap(super(ValuesIterator, self).previous())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def next(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$ValuesIterator.next()"""
        return object.__wrap(super(ValuesIterator, self).next())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength
import org.apache.commons.collections4.map.AbstractReferenceMap as __AbstractReferenceMap_ReferenceStrength
__ReferenceStrength = __AbstractReferenceMap_ReferenceStrength.ReferenceStrength
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class ReferenceStrength(__Enum, Enum):
    """org.apache.commons.collections4.map.AbstractReferenceMap.ReferenceStrength"""
 
    @staticmethod
    def __wrap(java_value: __ReferenceStrength) -> 'ReferenceStrength':
        return ReferenceStrength(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReferenceStrength):
        """
        Dynamic initializer for ReferenceStrength.
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
    def resolve(arg0: int) -> 'ReferenceStrength':
        """public static org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength.resolve(int)"""
        return ReferenceStrength.__wrap(__ReferenceStrength.resolve(__int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ReferenceStrength':
        """public static org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength.valueOf(java.lang.String)"""
        return ReferenceStrength.__wrap(__ReferenceStrength.valueOf(arg0))

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
    def values() -> List['ReferenceStrength']:
        """public static org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength[] org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength.values()"""
        return List[ReferenceStrength].__wrap(__ReferenceStrength.values())

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
 
 
# CLASS: org.apache.commons.collections4.map.DefaultedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.DefaultedMap as __DefaultedMap
__DefaultedMap = __DefaultedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class DefaultedMap(__AbstractMapDecorator, AbstractMapDecorator, __Serializable, Serializable):
    """org.apache.commons.collections4.map.DefaultedMap"""
 
    @staticmethod
    def __wrap(java_value: __DefaultedMap) -> 'DefaultedMap':
        return DefaultedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultedMap):
        """
        Dynamic initializer for DefaultedMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.collections4.map.DefaultedMap(V)"""
        val = __DefaultedMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @staticmethod
    @overload
    def defaultedMap(arg0: 'Map', arg1: object) -> 'DefaultedMap':
        """public static <K,V> org.apache.commons.collections4.map.DefaultedMap<K, V> org.apache.commons.collections4.map.DefaultedMap.defaultedMap(java.util.Map<K, V>,V)"""
        return DefaultedMap.__wrap(__DefaultedMap.defaultedMap(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def __init__(self, arg0: 'Transformer'):
        """public org.apache.commons.collections4.map.DefaultedMap(org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        val = __DefaultedMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @staticmethod
    @overload
    def defaultedMap(arg0: 'Map', arg1: 'Transformer') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.map.DefaultedMap.defaultedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return Map.__wrap(__DefaultedMap.defaultedMap(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @staticmethod
    @overload
    def defaultedMap(arg0: 'Map', arg1: 'Factory') -> 'DefaultedMap':
        """public static <K,V> org.apache.commons.collections4.map.DefaultedMap<K, V> org.apache.commons.collections4.map.DefaultedMap.defaultedMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return DefaultedMap.__wrap(__DefaultedMap.defaultedMap(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.DefaultedMap.get(java.lang.Object)"""
        return object.__wrap(super(__DefaultedMap, self).get(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashMapIterator
__HashMapIterator = __AbstractHashedMap_HashMapIterator.HashMapIterator
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashIterator
__HashIterator = __AbstractHashedMap_HashIterator.HashIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashMapIterator(__HashIterator, HashIterator, pyapache.__MapIterator, collections4.MapIterator):
    """org.apache.commons.collections4.map.AbstractHashedMap.HashMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __HashMapIterator) -> 'HashMapIterator':
        return HashMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashMapIterator):
        """
        Dynamic initializer for HashMapIterator.
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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.getKey()"""
        return object.__wrap(super(HashMapIterator, self).getKey())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.getValue()"""
        return object.__wrap(super(HashMapIterator, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str.__wrap(super(HashIterator, self).toString())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool.__wrap(super(HashIterator, self).hasNext())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.next()"""
        return object.__wrap(super(HashMapIterator, self).next())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashMapIterator.setValue(V)"""
        return object.__wrap(super(__HashMapIterator, self).setValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.CompositeMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.map.CompositeMap as __CompositeMap
__CompositeMap = __CompositeMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class CompositeMap(__AbstractIterableMap, AbstractIterableMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.CompositeMap"""
 
    @staticmethod
    def __wrap(java_value: __CompositeMap) -> 'CompositeMap':
        return CompositeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CompositeMap):
        """
        Dynamic initializer for CompositeMap.
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
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.CompositeMap.size()"""
        return int.__wrap(super(CompositeMap, self).size())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.CompositeMap.get(java.lang.Object)"""
        return object.__wrap(super(__CompositeMap, self).get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.isEmpty()"""
        return bool.__wrap(super(CompositeMap, self).isEmpty())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.CompositeMap.keySet()"""
        return 'Set'.__wrap(super(CompositeMap, self).keySet())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.CompositeMap.put(K,V)"""
        return object.__wrap(super(__CompositeMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__CompositeMap, self).containsValue(arg0))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def __init__(self, *arg0: 'Map'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>...)"""
        val = __CompositeMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__CompositeMap, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.CompositeMap.remove(java.lang.Object)"""
        return object.__wrap(super(__CompositeMap, self).remove(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.CompositeMap.entrySet()"""
        return 'Set'.__wrap(super(CompositeMap, self).entrySet())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.CompositeMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__CompositeMap, self).putAll(arg0)

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
    def __init__(self, arg0: 'Map', arg1: 'Map', arg2: 'MapMutator'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>,java.util.Map<K, V>,org.apache.commons.collections4.map.CompositeMap$MapMutator<K, V>)"""
        val = __CompositeMap(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def addComposited(self, arg0: 'Map'):
        """public synchronized void org.apache.commons.collections4.map.CompositeMap.addComposited(java.util.Map<K, V>) throws java.lang.IllegalArgumentException"""
        super(__CompositeMap, self).addComposited(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.CompositeMap.hashCode()"""
        return int.__wrap(super(CompositeMap, self).hashCode())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.CompositeMap.clear()"""
        super(CompositeMap, self).clear()

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
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Map', arg1: 'MapMutator'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>[],org.apache.commons.collections4.map.CompositeMap$MapMutator<K, V>)"""
        val = __CompositeMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.CompositeMap()"""
        val = __CompositeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setMutator(self, arg0: 'MapMutator'):
        """public void org.apache.commons.collections4.map.CompositeMap.setMutator(org.apache.commons.collections4.map.CompositeMap$MapMutator<K, V>)"""
        super(__CompositeMap, self).setMutator(arg0)

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.CompositeMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__CompositeMap, self).containsKey(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.CompositeMap.values()"""
        return 'Collection'.__wrap(super(CompositeMap, self).values())

    @overload
    def removeComposited(self, arg0: 'Map') -> 'Map':
        """public synchronized java.util.Map<K, V> org.apache.commons.collections4.map.CompositeMap.removeComposited(java.util.Map<K, V>)"""
        return 'Map'.__wrap(super(__CompositeMap, self).removeComposited(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.CompositeMap()"""
        val = __CompositeMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Map', arg1: 'Map'):
        """public org.apache.commons.collections4.map.CompositeMap(java.util.Map<K, V>,java.util.Map<K, V>)"""
        val = __CompositeMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$LinkEntry
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
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashEntry
__HashEntry = __AbstractHashedMap_HashEntry.HashEntry
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkEntry
__LinkEntry = __AbstractLinkedMap_LinkEntry.LinkEntry
from builtins import int
 
class LinkEntry(__HashEntry, HashEntry):
    """org.apache.commons.collections4.map.AbstractLinkedMap.LinkEntry"""
 
    @staticmethod
    def __wrap(java_value: __LinkEntry) -> 'LinkEntry':
        return LinkEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkEntry):
        """
        Dynamic initializer for LinkEntry.
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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.hashCode()"""
        return int.__wrap(super(HashEntry, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getValue()"""
        return object.__wrap(super(HashEntry, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getKey()"""
        return object.__wrap(super(HashEntry, self).getKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__HashEntry, self).equals(arg0))

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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.setValue(V)"""
        return object.__wrap(super(__HashEntry, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.toString()"""
        return str.__wrap(super(HashEntry, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.PredicatedSortedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import org.apache.commons.collections4.map.PredicatedMap as __PredicatedMap
__PredicatedMap = __PredicatedMap
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.PredicatedSortedMap as __PredicatedSortedMap
__PredicatedSortedMap = __PredicatedSortedMap
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class PredicatedSortedMap(__PredicatedMap, PredicatedMap, __SortedMap, SortedMap):
    """org.apache.commons.collections4.map.PredicatedSortedMap"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedSortedMap) -> 'PredicatedSortedMap':
        return PredicatedSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedSortedMap):
        """
        Dynamic initializer for PredicatedSortedMap.
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
    def predicatedMap(arg0: 'Map', arg1: 'Predicate', arg2: 'Predicate') -> 'PredicatedMap':
        """public static <K,V> org.apache.commons.collections4.map.PredicatedMap<K, V> org.apache.commons.collections4.map.PredicatedMap.predicatedMap(java.util.Map<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return PredicatedMap.__wrap(__PredicatedMap.predicatedMap(arg0, arg1, arg2))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__PredicatedSortedMap, self).tailMap(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

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

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__PredicatedSortedMap, self).headMap(arg0))

    @staticmethod
    @overload
    def predicatedSortedMap(arg0: 'SortedMap', arg1: 'Predicate', arg2: 'Predicate') -> 'PredicatedSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.PredicatedSortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.predicatedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return PredicatedSortedMap.__wrap(__PredicatedSortedMap.predicatedSortedMap(arg0, arg1, arg2))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.PredicatedSortedMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__PredicatedSortedMap, self).subMap(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.PredicatedSortedMap.firstKey()"""
        return object.__wrap(super(PredicatedSortedMap, self).firstKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.PredicatedMap.put(K,V)"""
        return object.__wrap(super(__PredicatedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.PredicatedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__PredicatedMap, self).putAll(arg0)

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.PredicatedSortedMap.comparator()"""
        return 'Comparator'.__wrap(super(PredicatedSortedMap, self).comparator())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.PredicatedSortedMap.lastKey()"""
        return object.__wrap(super(PredicatedSortedMap, self).lastKey()) 
 
 
# CLASS: org.apache.commons.collections4.map.FixedSizeMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.FixedSizeMap as __FixedSizeMap
__FixedSizeMap = __FixedSizeMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class FixedSizeMap(__AbstractMapDecorator, AbstractMapDecorator, pyapache.__BoundedMap, collections4.BoundedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.FixedSizeMap"""
 
    @staticmethod
    def __wrap(java_value: __FixedSizeMap) -> 'FixedSizeMap':
        return FixedSizeMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FixedSizeMap):
        """
        Dynamic initializer for FixedSizeMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @staticmethod
    @overload
    def fixedSizeMap(arg0: 'Map') -> 'FixedSizeMap':
        """public static <K,V> org.apache.commons.collections4.map.FixedSizeMap<K, V> org.apache.commons.collections4.map.FixedSizeMap.fixedSizeMap(java.util.Map<K, V>)"""
        return FixedSizeMap.__wrap(__FixedSizeMap.fixedSizeMap(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.FixedSizeMap.values()"""
        return 'Collection'.__wrap(super(FixedSizeMap, self).values())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeMap.put(K,V)"""
        return object.__wrap(super(__FixedSizeMap, self).put(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.FixedSizeMap.clear()"""
        super(FixedSizeMap, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.FixedSizeMap.entrySet()"""
        return 'Set'.__wrap(super(FixedSizeMap, self).entrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.FixedSizeMap.maxSize()"""
        return int.__wrap(super(FixedSizeMap, self).maxSize())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.FixedSizeMap.isFull()"""
        return bool.__wrap(super(FixedSizeMap, self).isFull())

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.FixedSizeMap.keySet()"""
        return 'Set'.__wrap(super(FixedSizeMap, self).keySet())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeMap.remove(java.lang.Object)"""
        return object.__wrap(super(__FixedSizeMap, self).remove(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.FixedSizeMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__FixedSizeMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.Flat3Map
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import org.apache.commons.collections4.map.Flat3Map as __Flat3Map
__Flat3Map = __Flat3Map
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class Flat3Map(pyapache.__IterableMap, collections4.IterableMap, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.Flat3Map"""
 
    @staticmethod
    def __wrap(java_value: __Flat3Map) -> 'Flat3Map':
        return Flat3Map(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Flat3Map):
        """
        Dynamic initializer for Flat3Map.
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
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.Flat3Map.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(Flat3Map, self).mapIterator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.Flat3Map.hashCode()"""
        return int.__wrap(super(Flat3Map, self).hashCode())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.Flat3Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__Flat3Map, self).putAll(arg0)

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.Flat3Map.remove(java.lang.Object)"""
        return object.__wrap(super(__Flat3Map, self).remove(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.Flat3Map()"""
        val = __Flat3Map()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.equals(java.lang.Object)"""
        return bool.__wrap(super(__Flat3Map, self).equals(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__Flat3Map, self).containsValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.isEmpty()"""
        return bool.__wrap(super(Flat3Map, self).isEmpty())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.Flat3Map.toString()"""
        return str.__wrap(super(Flat3Map, self).toString())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.Flat3Map.put(K,V)"""
        return object.__wrap(super(__Flat3Map, self).put(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.Flat3Map.size()"""
        return int.__wrap(super(Flat3Map, self).size())

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
    def clone(self) -> 'Flat3Map':
        """public org.apache.commons.collections4.map.Flat3Map<K, V> org.apache.commons.collections4.map.Flat3Map.clone()"""
        return 'Flat3Map'.__wrap(super(Flat3Map, self).clone())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.Flat3Map.clear()"""
        super(Flat3Map, self).clear()

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.Flat3Map.keySet()"""
        return 'Set'.__wrap(super(Flat3Map, self).keySet())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.Flat3Map(java.util.Map<? extends K, ? extends V>)"""
        val = __Flat3Map(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.Flat3Map()"""
        val = __Flat3Map()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.Flat3Map.get(java.lang.Object)"""
        return object.__wrap(super(__Flat3Map, self).get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.Flat3Map.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__Flat3Map, self).containsKey(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.Flat3Map.values()"""
        return 'Collection'.__wrap(super(Flat3Map, self).values())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.Flat3Map.entrySet()"""
        return 'Set'.__wrap(super(Flat3Map, self).entrySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.map.PassiveExpiringMap as __PassiveExpiringMap_ConstantTimeToLiveExpirationPolicy
__ConstantTimeToLiveExpirationPolicy = __PassiveExpiringMap_ConstantTimeToLiveExpirationPolicy.ConstantTimeToLiveExpirationPolicy
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
 
class ConstantTimeToLiveExpirationPolicy(__ExpirationPolicy, ExpirationPolicy):
    """org.apache.commons.collections4.map.PassiveExpiringMap.ConstantTimeToLiveExpirationPolicy"""
 
    @staticmethod
    def __wrap(java_value: __ConstantTimeToLiveExpirationPolicy) -> 'ConstantTimeToLiveExpirationPolicy':
        return ConstantTimeToLiveExpirationPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantTimeToLiveExpirationPolicy):
        """
        Dynamic initializer for ConstantTimeToLiveExpirationPolicy.
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
    def __init__(self):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy()"""
        val = __ConstantTimeToLiveExpirationPolicy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy(long)"""
        val = __ConstantTimeToLiveExpirationPolicy(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def expirationTime(self, arg0: object, arg1: object) -> int:
        """public long org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy.expirationTime(K,V)"""
        return int.__wrap(super(__ConstantTimeToLiveExpirationPolicy, self).expirationTime(arg0, arg1))

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
    def __init__(self, arg0: int, arg1: 'TimeUnit'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy(long,java.util.concurrent.TimeUnit)"""
        val = __ConstantTimeToLiveExpirationPolicy(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.PassiveExpiringMap$ConstantTimeToLiveExpirationPolicy()"""
        val = __ConstantTimeToLiveExpirationPolicy()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.collections4.map.SingletonMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.map.SingletonMap as __SingletonMap
__SingletonMap = __SingletonMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class SingletonMap(pyapache.__OrderedMap, collections4.OrderedMap, pyapache.__BoundedMap, collections4.BoundedMap, pyapache.__KeyValue, collections4.KeyValue, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.SingletonMap"""
 
    @staticmethod
    def __wrap(java_value: __SingletonMap) -> 'SingletonMap':
        return SingletonMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SingletonMap):
        """
        Dynamic initializer for SingletonMap.
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
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.lastKey()"""
        return object.__wrap(super(SingletonMap, self).lastKey())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.firstKey()"""
        return object.__wrap(super(SingletonMap, self).firstKey())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.setValue(V)"""
        return object.__wrap(super(__SingletonMap, self).setValue(arg0))

    @overload
    def __init__(self, arg0: 'Entry'):
        """public org.apache.commons.collections4.map.SingletonMap(java.util.Map$Entry<? extends K, ? extends V>)"""
        val = __SingletonMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.SingletonMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(SingletonMap, self).mapIterator())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.getValue()"""
        return object.__wrap(super(SingletonMap, self).getValue())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.SingletonMap.keySet()"""
        return 'Set'.__wrap(super(SingletonMap, self).keySet())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.get(java.lang.Object)"""
        return object.__wrap(super(__SingletonMap, self).get(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.SingletonMap.clear()"""
        super(SingletonMap, self).clear()

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.maxSize()"""
        return int.__wrap(super(SingletonMap, self).maxSize())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.SingletonMap.entrySet()"""
        return 'Set'.__wrap(super(SingletonMap, self).entrySet())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.getKey()"""
        return object.__wrap(super(SingletonMap, self).getKey())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.SingletonMap()"""
        val = __SingletonMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.size()"""
        return int.__wrap(super(SingletonMap, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.SingletonMap.hashCode()"""
        return int.__wrap(super(SingletonMap, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.SingletonMap(java.util.Map<? extends K, ? extends V>)"""
        val = __SingletonMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.SingletonMap.toString()"""
        return str.__wrap(super(SingletonMap, self).toString())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.put(K,V)"""
        return object.__wrap(super(__SingletonMap, self).put(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.isEmpty()"""
        return bool.__wrap(super(SingletonMap, self).isEmpty())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.SingletonMap()"""
        val = __SingletonMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.SingletonMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__SingletonMap, self).putAll(arg0)

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def clone(self) -> 'SingletonMap':
        """public org.apache.commons.collections4.map.SingletonMap<K, V> org.apache.commons.collections4.map.SingletonMap.clone()"""
        return 'SingletonMap'.__wrap(super(SingletonMap, self).clone())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.SingletonMap.remove(java.lang.Object)"""
        return object.__wrap(super(__SingletonMap, self).remove(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def __init__(self, arg0: 'KeyValue'):
        """public org.apache.commons.collections4.map.SingletonMap(org.apache.commons.collections4.KeyValue<K, V>)"""
        val = __SingletonMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.SingletonMap.values()"""
        return 'Collection'.__wrap(super(SingletonMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__SingletonMap, self).containsValue(arg0))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.previousKey(K)"""
        return object.__wrap(super(__SingletonMap, self).previousKey(arg0))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public org.apache.commons.collections4.map.SingletonMap(K,V)"""
        val = __SingletonMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__SingletonMap, self).containsKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__SingletonMap, self).equals(arg0))

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
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.SingletonMap.isFull()"""
        return bool.__wrap(super(SingletonMap, self).isFull())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.SingletonMap.nextKey(K)"""
        return object.__wrap(super(__SingletonMap, self).nextKey(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.LazySortedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.map.LazyMap as __LazyMap
__LazyMap = __LazyMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import org.apache.commons.collections4.map.LazySortedMap as __LazySortedMap
__LazySortedMap = __LazySortedMap
import java.util.Map as Map
from builtins import int
 
class LazySortedMap(__LazyMap, LazyMap, __SortedMap, SortedMap):
    """org.apache.commons.collections4.map.LazySortedMap"""
 
    @staticmethod
    def __wrap(java_value: __LazySortedMap) -> 'LazySortedMap':
        return LazySortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazySortedMap):
        """
        Dynamic initializer for LazySortedMap.
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
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.LazySortedMap.lastKey()"""
        return object.__wrap(super(LazySortedMap, self).lastKey())

    @override
    @overload
    def pollFirstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollFirstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollFirstEntry())

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Factory') -> 'LazyMap':
        """public static <K,V> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return LazyMap.__wrap(__LazyMap.lazyMap(arg0, arg1))

    @override
    @overload
    def lastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.lastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).lastEntry())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__LazySortedMap, self).headMap(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Factory') -> 'LazySortedMap':
        """public static <K,V> org.apache.commons.collections4.map.LazySortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return LazySortedMap.__wrap(__LazySortedMap.lazySortedMap(arg0, arg1))

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Transformer') -> 'LazyMap':
        """public static <V,K> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return LazyMap.__wrap(__LazyMap.lazyMap(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__LazySortedMap, self).subMap(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.LazySortedMap.firstKey()"""
        return object.__wrap(super(LazySortedMap, self).firstKey())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

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

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def firstEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.firstEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).firstEntry())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__LazySortedMap, self).tailMap(arg0))

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

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.LazyMap.get(java.lang.Object)"""
        return object.__wrap(super(__LazyMap, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.LazySortedMap.comparator()"""
        return 'Comparator'.__wrap(super(LazySortedMap, self).comparator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @staticmethod
    @overload
    def lazySortedMap(arg0: 'SortedMap', arg1: 'Transformer') -> 'LazySortedMap':
        """public static <K,V> org.apache.commons.collections4.map.LazySortedMap<K, V> org.apache.commons.collections4.map.LazySortedMap.lazySortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return LazySortedMap.__wrap(__LazySortedMap.lazySortedMap(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMapDecorator, self).putAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractOrderedMapDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import org.apache.commons.collections4.map.AbstractOrderedMapDecorator as __AbstractOrderedMapDecorator
__AbstractOrderedMapDecorator = __AbstractOrderedMapDecorator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractOrderedMapDecorator(ABC, __AbstractMapDecorator, AbstractMapDecorator, pyapache.__OrderedMap, collections4.OrderedMap):
    """org.apache.commons.collections4.map.AbstractOrderedMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractOrderedMapDecorator) -> 'AbstractOrderedMapDecorator':
        return AbstractOrderedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractOrderedMapDecorator):
        """
        Dynamic initializer for AbstractOrderedMapDecorator.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractOrderedMapDecorator, self).firstKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self, arg0: 'OrderedMap'):
        """public org.apache.commons.collections4.map.AbstractOrderedMapDecorator(org.apache.commons.collections4.OrderedMap<K, V>)"""
        val = __AbstractOrderedMapDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractOrderedMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractOrderedMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractOrderedMapDecorator, self).lastKey())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractOrderedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractOrderedMapDecorator, self).mapIterator())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter as __EntrySetToMapIteratorAdapter
__EntrySetToMapIteratorAdapter = __EntrySetToMapIteratorAdapter
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Set as Set
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntrySetToMapIteratorAdapter(pyapache.__MapIterator, collections4.MapIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter"""
 
    @staticmethod
    def __wrap(java_value: __EntrySetToMapIteratorAdapter) -> 'EntrySetToMapIteratorAdapter':
        return EntrySetToMapIteratorAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySetToMapIteratorAdapter):
        """
        Dynamic initializer for EntrySetToMapIteratorAdapter.
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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getKey()"""
        return object.__wrap(super(EntrySetToMapIteratorAdapter, self).getKey())

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
    def reset(self):
        """public synchronized void org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.reset()"""
        super(EntrySetToMapIteratorAdapter, self).reset()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.hasNext()"""
        return bool.__wrap(super(EntrySetToMapIteratorAdapter, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.remove()"""
        super(EntrySetToMapIteratorAdapter, self).remove()

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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getValue()"""
        return object.__wrap(super(EntrySetToMapIteratorAdapter, self).getValue())

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.next()"""
        return object.__wrap(super(EntrySetToMapIteratorAdapter, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def __init__(self, arg0: 'Set'):
        """public org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter(java.util.Set<java.util.Map$Entry<K, V>>)"""
        val = __EntrySetToMapIteratorAdapter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.setValue(V)"""
        return object.__wrap(super(__EntrySetToMapIteratorAdapter, self).setValue(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$ValuesIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_ValuesIterator
__ValuesIterator = __AbstractHashedMap_ValuesIterator.ValuesIterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashIterator
__HashIterator = __AbstractHashedMap_HashIterator.HashIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValuesIterator(__HashIterator, HashIterator, __Iterator, Iterator):
    """org.apache.commons.collections4.map.AbstractHashedMap.ValuesIterator"""
 
    @staticmethod
    def __wrap(java_value: __ValuesIterator) -> 'ValuesIterator':
        return ValuesIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValuesIterator):
        """
        Dynamic initializer for ValuesIterator.
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

    @override
    @overload
    def next(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$ValuesIterator.next()"""
        return object.__wrap(super(ValuesIterator, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str.__wrap(super(HashIterator, self).toString())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool.__wrap(super(HashIterator, self).hasNext())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.ReferenceIdentityMap
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.collections4.map.ReferenceIdentityMap as __ReferenceIdentityMap
__ReferenceIdentityMap = __ReferenceIdentityMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.AbstractReferenceMap as __AbstractReferenceMap
__AbstractReferenceMap = __AbstractReferenceMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class ReferenceIdentityMap(__AbstractReferenceMap, AbstractReferenceMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.ReferenceIdentityMap"""
 
    @staticmethod
    def __wrap(java_value: __ReferenceIdentityMap) -> 'ReferenceIdentityMap':
        return ReferenceIdentityMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReferenceIdentityMap):
        """
        Dynamic initializer for ReferenceIdentityMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: bool):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,boolean)"""
        val = __ReferenceIdentityMap(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.isEmpty()"""
        return bool.__wrap(super(AbstractReferenceMap, self).isEmpty())

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float, arg4: bool):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float,boolean)"""
        val = __ReferenceIdentityMap(arg0, arg1, __int.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength'):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength)"""
        val = __ReferenceIdentityMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractReferenceMap.keySet()"""
        return 'Set'.__wrap(super(AbstractReferenceMap, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractReferenceMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float)"""
        val = __ReferenceIdentityMap(arg0, arg1, __int.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractReferenceMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractReferenceMap, self).entrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap()"""
        val = __ReferenceIdentityMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public org.apache.commons.collections4.map.ReferenceIdentityMap()"""
        val = __ReferenceIdentityMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractReferenceMap.values()"""
        return 'Collection'.__wrap(super(AbstractReferenceMap, self).values())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap.size()"""
        return int.__wrap(super(AbstractReferenceMap, self).size())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractReferenceMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractReferenceMap, self).mapIterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractReferenceMap, self).remove(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractReferenceMap, self).containsValue(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractReferenceMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractReferenceMap.clear()"""
        super(AbstractReferenceMap, self).clear()

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.put(K,V)"""
        return object.__wrap(super(__AbstractReferenceMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.FixedSizeSortedMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.map.FixedSizeSortedMap as __FixedSizeSortedMap
__FixedSizeSortedMap = __FixedSizeSortedMap
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as __AbstractSortedMapDecorator
__AbstractSortedMapDecorator = __AbstractSortedMapDecorator
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class FixedSizeSortedMap(__AbstractSortedMapDecorator, AbstractSortedMapDecorator, pyapache.__BoundedMap, collections4.BoundedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.FixedSizeSortedMap"""
 
    @staticmethod
    def __wrap(java_value: __FixedSizeSortedMap) -> 'FixedSizeSortedMap':
        return FixedSizeSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FixedSizeSortedMap):
        """
        Dynamic initializer for FixedSizeSortedMap.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeSortedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__FixedSizeSortedMap, self).remove(arg0))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__FixedSizeSortedMap, self).headMap(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractSortedMapDecorator, self).firstKey())

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @staticmethod
    @overload
    def fixedSizeSortedMap(arg0: 'SortedMap') -> 'FixedSizeSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.FixedSizeSortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.fixedSizeSortedMap(java.util.SortedMap<K, V>)"""
        return FixedSizeSortedMap.__wrap(__FixedSizeSortedMap.fixedSizeSortedMap(arg0))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.FixedSizeSortedMap.clear()"""
        super(FixedSizeSortedMap, self).clear()

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def pollLastEntry(self) -> 'Entry.Map$Entry':
        """public default java.util.Map$Entry<K, V> java.util.SequencedMap.pollLastEntry()"""
        return 'Entry.Map$Entry'.__wrap(super(SequencedMap, self).pollLastEntry())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.FixedSizeSortedMap.keySet()"""
        return 'Set'.__wrap(super(FixedSizeSortedMap, self).keySet())

    @override
    @overload
    def sequencedValues(self) -> 'SequencedCollection':
        """public default java.util.SequencedCollection<V> java.util.SequencedMap.sequencedValues()"""
        return 'SequencedCollection'.__wrap(super(SequencedMap, self).sequencedValues())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractSortedMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractSortedMapDecorator, self).lastKey())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.FixedSizeSortedMap.entrySet()"""
        return 'Set'.__wrap(super(FixedSizeSortedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedMapDecorator, self).comparator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__FixedSizeSortedMap, self).subMap(arg0, arg1))

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.FixedSizeSortedMap.maxSize()"""
        return int.__wrap(super(FixedSizeSortedMap, self).maxSize())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.FixedSizeSortedMap.put(K,V)"""
        return object.__wrap(super(__FixedSizeSortedMap, self).put(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractSortedMapDecorator, self).previousKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.FixedSizeSortedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__FixedSizeSortedMap, self).putAll(arg0)

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.FixedSizeSortedMap.isFull()"""
        return bool.__wrap(super(FixedSizeSortedMap, self).isFull())

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

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.FixedSizeSortedMap.values()"""
        return 'Collection'.__wrap(super(FixedSizeSortedMap, self).values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.FixedSizeSortedMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__FixedSizeSortedMap, self).tailMap(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractSortedMapDecorator, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.PredicatedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.map.PredicatedMap as __PredicatedMap
__PredicatedMap = __PredicatedMap
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class PredicatedMap(__AbstractInputCheckedMapDecorator, AbstractInputCheckedMapDecorator, __Serializable, Serializable):
    """org.apache.commons.collections4.map.PredicatedMap"""
 
    @staticmethod
    def __wrap(java_value: __PredicatedMap) -> 'PredicatedMap':
        return PredicatedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredicatedMap):
        """
        Dynamic initializer for PredicatedMap.
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
    def predicatedMap(arg0: 'Map', arg1: 'Predicate', arg2: 'Predicate') -> 'PredicatedMap':
        """public static <K,V> org.apache.commons.collections4.map.PredicatedMap<K, V> org.apache.commons.collections4.map.PredicatedMap.predicatedMap(java.util.Map<K, V>,org.apache.commons.collections4.Predicate<? super K>,org.apache.commons.collections4.Predicate<? super V>)"""
        return PredicatedMap.__wrap(__PredicatedMap.predicatedMap(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.PredicatedMap.put(K,V)"""
        return object.__wrap(super(__PredicatedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.PredicatedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__PredicatedMap, self).putAll(arg0)

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.collections4.map.AbstractReferenceMap as __AbstractReferenceMap_ReferenceEntry
__ReferenceEntry = __AbstractReferenceMap_ReferenceEntry.ReferenceEntry
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashEntry
__HashEntry = __AbstractHashedMap_HashEntry.HashEntry
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReferenceEntry(__HashEntry, HashEntry):
    """org.apache.commons.collections4.map.AbstractReferenceMap.ReferenceEntry"""
 
    @staticmethod
    def __wrap(java_value: __ReferenceEntry) -> 'ReferenceEntry':
        return ReferenceEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReferenceEntry):
        """
        Dynamic initializer for ReferenceEntry.
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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.setValue(V)"""
        return object.__wrap(super(__ReferenceEntry, self).setValue(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.getValue()"""
        return object.__wrap(super(ReferenceEntry, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.toString()"""
        return str.__wrap(super(HashEntry, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'AbstractReferenceMap', arg1: 'HashEntry', arg2: int, arg3: object, arg4: object):
        """public org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry(org.apache.commons.collections4.map.AbstractReferenceMap<K, V>,org.apache.commons.collections4.map.AbstractHashedMap$HashEntry<K, V>,int,K,V)"""
        val = __ReferenceEntry(arg0, arg1, __int.valueOf(arg2), arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.hashCode()"""
        return int.__wrap(super(ReferenceEntry, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.getKey()"""
        return object.__wrap(super(ReferenceEntry, self).getKey())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__ReferenceEntry, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$HashIterator
from builtins import str
import java.lang.Long as __long
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashIterator
__HashIterator = __AbstractHashedMap_HashIterator.HashIterator
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashIterator(ABC):
    """org.apache.commons.collections4.map.AbstractHashedMap.HashIterator"""
 
    @staticmethod
    def __wrap(java_value: __HashIterator) -> 'HashIterator':
        return HashIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashIterator):
        """
        Dynamic initializer for HashIterator.
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
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool.__wrap(super(HashIterator, self).hasNext())

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
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str.__wrap(super(HashIterator, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.LazyMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.map.LazyMap as __LazyMap
__LazyMap = __LazyMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class LazyMap(__AbstractMapDecorator, AbstractMapDecorator, __Serializable, Serializable):
    """org.apache.commons.collections4.map.LazyMap"""
 
    @staticmethod
    def __wrap(java_value: __LazyMap) -> 'LazyMap':
        return LazyMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazyMap):
        """
        Dynamic initializer for LazyMap.
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
    def lazyMap(arg0: 'Map', arg1: 'Factory') -> 'LazyMap':
        """public static <K,V> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Factory<? extends V>)"""
        return LazyMap.__wrap(__LazyMap.lazyMap(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @staticmethod
    @overload
    def lazyMap(arg0: 'Map', arg1: 'Transformer') -> 'LazyMap':
        """public static <V,K> org.apache.commons.collections4.map.LazyMap<K, V> org.apache.commons.collections4.map.LazyMap.lazyMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends V>)"""
        return LazyMap.__wrap(__LazyMap.lazyMap(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.LazyMap.get(java.lang.Object)"""
        return object.__wrap(super(__LazyMap, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

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
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$EntrySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_EntrySetIterator
__EntrySetIterator = __AbstractLinkedMap_EntrySetIterator.EntrySetIterator
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkIterator
__LinkIterator = __AbstractLinkedMap_LinkIterator.LinkIterator
import java.util.Map.Entry as Entry
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
 
class EntrySetIterator(__LinkIterator, LinkIterator, pyapache.__OrderedIterator, collections4.OrderedIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.map.AbstractLinkedMap.EntrySetIterator"""
 
    @staticmethod
    def __wrap(java_value: __EntrySetIterator) -> 'EntrySetIterator':
        return EntrySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySetIterator):
        """
        Dynamic initializer for EntrySetIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool.__wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool.__wrap(super(LinkIterator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str.__wrap(super(LinkIterator, self).toString())

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
    def previous(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.map.AbstractLinkedMap$EntrySetIterator.previous()"""
        return 'Entry.Map$Entry'.__wrap(super(EntrySetIterator, self).previous())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.map.AbstractLinkedMap$EntrySetIterator.next()"""
        return 'Entry.Map$Entry'.__wrap(super(EntrySetIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.TransformedSortedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import org.apache.commons.collections4.map.TransformedSortedMap as __TransformedSortedMap
__TransformedSortedMap = __TransformedSortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import org.apache.commons.collections4.map.TransformedMap as __TransformedMap
__TransformedMap = __TransformedMap
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class TransformedSortedMap(__TransformedMap, TransformedMap, __SortedMap, SortedMap):
    """org.apache.commons.collections4.map.TransformedSortedMap"""
 
    @staticmethod
    def __wrap(java_value: __TransformedSortedMap) -> 'TransformedSortedMap':
        return TransformedSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedSortedMap):
        """
        Dynamic initializer for TransformedSortedMap.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

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

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.TransformedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__TransformedMap, self).putAll(arg0)

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.TransformedSortedMap.lastKey()"""
        return object.__wrap(super(TransformedSortedMap, self).lastKey())

    @staticmethod
    @overload
    def transformingSortedMap(arg0: 'SortedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedSortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.transformingSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedSortedMap.__wrap(__TransformedSortedMap.transformingSortedMap(arg0, arg1, arg2))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.TransformedMap.put(K,V)"""
        return object.__wrap(super(__TransformedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__TransformedSortedMap, self).subMap(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @staticmethod
    @overload
    def transformedSortedMap(arg0: 'SortedMap', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedSortedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedSortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.transformedSortedMap(java.util.SortedMap<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedSortedMap.__wrap(__TransformedSortedMap.transformedSortedMap(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__TransformedSortedMap, self).tailMap(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap.__wrap(__TransformedMap.transformingMap(arg0, arg1, arg2))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.TransformedSortedMap.comparator()"""
        return 'Comparator'.__wrap(super(TransformedSortedMap, self).comparator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @staticmethod
    @overload
    def transformedMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap.__wrap(__TransformedMap.transformedMap(arg0, arg1, arg2))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.TransformedSortedMap.firstKey()"""
        return object.__wrap(super(TransformedSortedMap, self).firstKey())

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.TransformedSortedMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__TransformedSortedMap, self).headMap(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$Values
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
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.util.function.IntFunction as IntFunction
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_Values
__Values = __AbstractHashedMap_Values.Values
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Values(__AbstractCollection, AbstractCollection):
    """org.apache.commons.collections4.map.AbstractHashedMap.Values"""
 
    @staticmethod
    def __wrap(java_value: __Values) -> 'Values':
        return Values(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Values):
        """
        Dynamic initializer for Values.
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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$Values.contains(java.lang.Object)"""
        return bool.__wrap(super(__Values, self).contains(arg0))

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<V> org.apache.commons.collections4.map.AbstractHashedMap$Values.iterator()"""
        return 'Iterator'.__wrap(super(Values, self).iterator())

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

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).removeAll(arg0))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$Values.clear()"""
        super(Values, self).clear()

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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.AbstractCollection.toArray()"""
        return List[object].__wrap(super(AbstractCollection, self).toArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.AbstractCollection.isEmpty()"""
        return bool.__wrap(super(AbstractCollection, self).isEmpty())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$Values.size()"""
        return int.__wrap(super(Values, self).size())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.collections4.map.ListOrderedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.map.ListOrderedMap as __ListOrderedMap
__ListOrderedMap = __ListOrderedMap
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class ListOrderedMap(__AbstractMapDecorator, AbstractMapDecorator, pyapache.__OrderedMap, collections4.OrderedMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.ListOrderedMap"""
 
    @staticmethod
    def __wrap(java_value: __ListOrderedMap) -> 'ListOrderedMap':
        return ListOrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ListOrderedMap):
        """
        Dynamic initializer for ListOrderedMap.
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
    def listOrderedMap(arg0: 'Map') -> 'ListOrderedMap':
        """public static <K,V> org.apache.commons.collections4.map.ListOrderedMap<K, V> org.apache.commons.collections4.map.ListOrderedMap.listOrderedMap(java.util.Map<K, V>)"""
        return ListOrderedMap.__wrap(__ListOrderedMap.listOrderedMap(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.remove(int)"""
        return object.__wrap(super(__ListOrderedMap, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.ListOrderedMap.values()"""
        return 'Collection'.__wrap(super(ListOrderedMap, self).values())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.nextKey(java.lang.Object)"""
        return object.__wrap(super(__ListOrderedMap, self).nextKey(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.ListOrderedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__ListOrderedMap, self).putAll(arg0)

    @overload
    def valueList(self) -> 'List':
        """public java.util.List<V> org.apache.commons.collections4.map.ListOrderedMap.valueList()"""
        return 'List'.__wrap(super(ListOrderedMap, self).valueList())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.lastKey()"""
        return object.__wrap(super(ListOrderedMap, self).lastKey())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def getValue(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.getValue(int)"""
        return object.__wrap(super(__ListOrderedMap, self).getValue(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.ListOrderedMap()"""
        val = __ListOrderedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__ListOrderedMap, self).remove(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.ListOrderedMap.toString()"""
        return str.__wrap(super(ListOrderedMap, self).toString())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.map.ListOrderedMap.indexOf(java.lang.Object)"""
        return int.__wrap(super(__ListOrderedMap, self).indexOf(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.ListOrderedMap.clear()"""
        super(ListOrderedMap, self).clear()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.put(K,V)"""
        return object.__wrap(super(__ListOrderedMap, self).put(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.ListOrderedMap.keySet()"""
        return 'Set'.__wrap(super(ListOrderedMap, self).keySet())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def put(self, arg0: int, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.put(int,K,V)"""
        return object.__wrap(super(__ListOrderedMap, self).put(__int.valueOf(arg0), arg1, arg2))

    @overload
    def putAll(self, arg0: int, arg1: 'Map'):
        """public void org.apache.commons.collections4.map.ListOrderedMap.putAll(int,java.util.Map<? extends K, ? extends V>)"""
        super(__ListOrderedMap, self).putAll(__int.valueOf(arg0), arg1)

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.firstKey()"""
        return object.__wrap(super(ListOrderedMap, self).firstKey())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def asList(self) -> 'List':
        """public java.util.List<K> org.apache.commons.collections4.map.ListOrderedMap.asList()"""
        return 'List'.__wrap(super(ListOrderedMap, self).asList())

    @overload
    def get(self, arg0: int) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.get(int)"""
        return object.__wrap(super(__ListOrderedMap, self).get(__int.valueOf(arg0)))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.ListOrderedMap.previousKey(java.lang.Object)"""
        return object.__wrap(super(__ListOrderedMap, self).previousKey(arg0))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.ListOrderedMap.entrySet()"""
        return 'Set'.__wrap(super(ListOrderedMap, self).entrySet())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.ListOrderedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(ListOrderedMap, self).mapIterator())

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
    def setValue(self, arg0: int, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.ListOrderedMap.setValue(int,V)"""
        return object.__wrap(super(__ListOrderedMap, self).setValue(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.ListOrderedMap()"""
        val = __ListOrderedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def keyList(self) -> 'List':
        """public java.util.List<K> org.apache.commons.collections4.map.ListOrderedMap.keyList()"""
        return 'List'.__wrap(super(ListOrderedMap, self).keyList()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkIterator
__LinkIterator = __AbstractLinkedMap_LinkIterator.LinkIterator
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinkIterator(ABC):
    """org.apache.commons.collections4.map.AbstractLinkedMap.LinkIterator"""
 
    @staticmethod
    def __wrap(java_value: __LinkIterator) -> 'LinkIterator':
        return LinkIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkIterator):
        """
        Dynamic initializer for LinkIterator.
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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool.__wrap(super(LinkIterator, self).hasNext())

    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool.__wrap(super(LinkIterator, self).hasPrevious())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str.__wrap(super(LinkIterator, self).toString())

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
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

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
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$KeySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashIterator
__HashIterator = __AbstractHashedMap_HashIterator.HashIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_KeySetIterator
__KeySetIterator = __AbstractHashedMap_KeySetIterator.KeySetIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KeySetIterator(__HashIterator, HashIterator, __Iterator, Iterator):
    """org.apache.commons.collections4.map.AbstractHashedMap.KeySetIterator"""
 
    @staticmethod
    def __wrap(java_value: __KeySetIterator) -> 'KeySetIterator':
        return KeySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeySetIterator):
        """
        Dynamic initializer for KeySetIterator.
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
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$KeySetIterator.next()"""
        return object.__wrap(super(KeySetIterator, self).next())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str.__wrap(super(HashIterator, self).toString())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool.__wrap(super(HashIterator, self).hasNext())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$HashEntry
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
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashEntry
__HashEntry = __AbstractHashedMap_HashEntry.HashEntry
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HashEntry(Map.__Map_Entry, Entry.Map$Entry, pyapache.__KeyValue, collections4.KeyValue):
    """org.apache.commons.collections4.map.AbstractHashedMap.HashEntry"""
 
    @staticmethod
    def __wrap(java_value: __HashEntry) -> 'HashEntry':
        return HashEntry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashEntry):
        """
        Dynamic initializer for HashEntry.
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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.hashCode()"""
        return int.__wrap(super(HashEntry, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getValue()"""
        return object.__wrap(super(HashEntry, self).getValue())

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.getKey()"""
        return object.__wrap(super(HashEntry, self).getKey())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.equals(java.lang.Object)"""
        return bool.__wrap(super(__HashEntry, self).equals(arg0))

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
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.setValue(V)"""
        return object.__wrap(super(__HashEntry, self).setValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashEntry.toString()"""
        return str.__wrap(super(HashEntry, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.HashedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.map.HashedMap as __HashedMap
__HashedMap = __HashedMap
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class HashedMap(__AbstractHashedMap, AbstractHashedMap, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.HashedMap"""
 
    @staticmethod
    def __wrap(java_value: __HashedMap) -> 'HashedMap':
        return HashedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashedMap):
        """
        Dynamic initializer for HashedMap.
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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.HashedMap(int,float)"""
        val = __HashedMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool.__wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object.__wrap(super(__AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int.__wrap(super(AbstractHashedMap, self).size())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractHashedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractHashedMap, self).mapIterator())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.HashedMap()"""
        val = __HashedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.HashedMap(int)"""
        val = __HashedMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public org.apache.commons.collections4.map.HashedMap()"""
        val = __HashedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clone(self) -> 'HashedMap':
        """public org.apache.commons.collections4.map.HashedMap<K, V> org.apache.commons.collections4.map.HashedMap.clone()"""
        return 'HashedMap'.__wrap(super(HashedMap, self).clone())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.clear()"""
        super(AbstractHashedMap, self).clear()

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'.__wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).keySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.HashedMap(java.util.Map<? extends K, ? extends V>)"""
        val = __HashedMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.StaticBucketMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.map.StaticBucketMap as __StaticBucketMap
__StaticBucketMap = __StaticBucketMap
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.lang.Runnable as Runnable
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class StaticBucketMap(__AbstractIterableMap, AbstractIterableMap):
    """org.apache.commons.collections4.map.StaticBucketMap"""
 
    @staticmethod
    def __wrap(java_value: __StaticBucketMap) -> 'StaticBucketMap':
        return StaticBucketMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StaticBucketMap):
        """
        Dynamic initializer for StaticBucketMap.
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
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.StaticBucketMap.remove(java.lang.Object)"""
        return object.__wrap(super(__StaticBucketMap, self).remove(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__StaticBucketMap, self).containsValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__StaticBucketMap, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.StaticBucketMap.clear()"""
        super(StaticBucketMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.StaticBucketMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__StaticBucketMap, self).putAll(arg0)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.isEmpty()"""
        return bool.__wrap(super(StaticBucketMap, self).isEmpty())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.StaticBucketMap.get(java.lang.Object)"""
        return object.__wrap(super(__StaticBucketMap, self).get(arg0))

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
    def atomic(self, arg0: 'Runnable'):
        """public void org.apache.commons.collections4.map.StaticBucketMap.atomic(java.lang.Runnable)"""
        super(__StaticBucketMap, self).atomic(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.StaticBucketMap(int)"""
        val = __StaticBucketMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.StaticBucketMap.size()"""
        return int.__wrap(super(StaticBucketMap, self).size())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.StaticBucketMap.entrySet()"""
        return 'Set'.__wrap(super(StaticBucketMap, self).entrySet())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.StaticBucketMap()"""
        val = __StaticBucketMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.StaticBucketMap.put(K,V)"""
        return object.__wrap(super(__StaticBucketMap, self).put(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.StaticBucketMap.hashCode()"""
        return int.__wrap(super(StaticBucketMap, self).hashCode())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.StaticBucketMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__StaticBucketMap, self).containsKey(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.StaticBucketMap.keySet()"""
        return 'Set'.__wrap(super(StaticBucketMap, self).keySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.StaticBucketMap.values()"""
        return 'Collection'.__wrap(super(StaticBucketMap, self).values())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.StaticBucketMap()"""
        val = __StaticBucketMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.map.UnmodifiableMap as __UnmodifiableMap
__UnmodifiableMap = __UnmodifiableMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableMap(__AbstractMapDecorator, AbstractMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable, __Serializable, Serializable):
    """org.apache.commons.collections4.map.UnmodifiableMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableMap) -> 'UnmodifiableMap':
        return UnmodifiableMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableMap):
        """
        Dynamic initializer for UnmodifiableMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.UnmodifiableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(UnmodifiableMap, self).mapIterator())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.UnmodifiableMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableMap, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableMap.put(K,V)"""
        return object.__wrap(super(__UnmodifiableMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableMap.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableMap, self).entrySet())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @staticmethod
    @overload
    def unmodifiableMap(arg0: 'Map') -> 'Map':
        """public static <K,V> java.util.Map<K, V> org.apache.commons.collections4.map.UnmodifiableMap.unmodifiableMap(java.util.Map<? extends K, ? extends V>)"""
        return Map.__wrap(__UnmodifiableMap.unmodifiableMap(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableMap.clear()"""
        super(UnmodifiableMap, self).clear()

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableMap.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableMap, self).remove(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.UnmodifiableMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableMap, self).putAll(arg0)

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.UnmodifiableMap.values()"""
        return 'Collection'.__wrap(super(UnmodifiableMap, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
from builtins import object
import java.util.function.BiFunction as BiFunction
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractHashedMap(__AbstractMap, AbstractMap, pyapache.__IterableMap, collections4.IterableMap):
    """org.apache.commons.collections4.map.AbstractHashedMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractHashedMap) -> 'AbstractHashedMap':
        return AbstractHashedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractHashedMap):
        """
        Dynamic initializer for AbstractHashedMap.
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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsValue(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool.__wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object.__wrap(super(__AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int.__wrap(super(AbstractHashedMap, self).size())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractHashedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractHashedMap, self).mapIterator())

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

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.clear()"""
        super(AbstractHashedMap, self).clear()

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'.__wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).keySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.LinkedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.map.LinkedMap as __LinkedMap
__LinkedMap = __LinkedMap
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap
__AbstractLinkedMap = __AbstractLinkedMap
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
import java.util.List as List
 
class LinkedMap(__AbstractLinkedMap, AbstractLinkedMap, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.LinkedMap"""
 
    @staticmethod
    def __wrap(java_value: __LinkedMap) -> 'LinkedMap':
        return LinkedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkedMap):
        """
        Dynamic initializer for LinkedMap.
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
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.LinkedMap(java.util.Map<? extends K, ? extends V>)"""
        val = __LinkedMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.firstKey()"""
        return object.__wrap(super(AbstractLinkedMap, self).firstKey())

    @overload
    def remove(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.LinkedMap.remove(int)"""
        return object.__wrap(super(__LinkedMap, self).remove(__int.valueOf(arg0)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool.__wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.map.LinkedMap.indexOf(java.lang.Object)"""
        return int.__wrap(super(__LinkedMap, self).indexOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object.__wrap(super(__AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractLinkedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractLinkedMap, self).mapIterator())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int.__wrap(super(AbstractHashedMap, self).size())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsKey(arg0))

    @overload
    def clone(self) -> 'LinkedMap':
        """public org.apache.commons.collections4.map.LinkedMap<K, V> org.apache.commons.collections4.map.LinkedMap.clone()"""
        return 'LinkedMap'.__wrap(super(LinkedMap, self).clone())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap.clear()"""
        super(AbstractLinkedMap, self).clear()

    @overload
    def getValue(self, arg0: int) -> object:
        """public V org.apache.commons.collections4.map.LinkedMap.getValue(int)"""
        return object.__wrap(super(__LinkedMap, self).getValue(__int.valueOf(arg0)))

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
    def __init__(self):
        """public org.apache.commons.collections4.map.LinkedMap()"""
        val = __LinkedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedMap, self).containsValue(arg0))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.LinkedMap()"""
        val = __LinkedMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.previousKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractLinkedMap, self).previousKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: int) -> object:
        """public K org.apache.commons.collections4.map.LinkedMap.get(int)"""
        return object.__wrap(super(__LinkedMap, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.nextKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractLinkedMap, self).nextKey(arg0))

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'.__wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.LinkedMap(int)"""
        val = __LinkedMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def asList(self) -> 'List':
        """public java.util.List<K> org.apache.commons.collections4.map.LinkedMap.asList()"""
        return 'List'.__wrap(super(LinkedMap, self).asList())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.LinkedMap(int,float)"""
        val = __LinkedMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.lastKey()"""
        return object.__wrap(super(AbstractLinkedMap, self).lastKey())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.CompositeMap$MapMutator
import org.apache.commons.collections4.map.CompositeMap as __CompositeMap_MapMutator
__MapMutator = __CompositeMap_MapMutator.MapMutator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class MapMutator(ABC, __Serializable, Serializable):
    """org.apache.commons.collections4.map.CompositeMap.MapMutator"""
 
    @staticmethod
    def __wrap(java_value: __MapMutator) -> 'MapMutator':
        return MapMutator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapMutator):
        """
        Dynamic initializer for MapMutator.
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
    def resolveCollision(self, arg0: 'CompositeMap', arg1: 'Map', arg2: 'Map', arg3: 'Collection'):
        """public abstract void org.apache.commons.collections4.map.CompositeMap$MapMutator.resolveCollision(org.apache.commons.collections4.map.CompositeMap<K, V>,java.util.Map<K, V>,java.util.Map<K, V>,java.util.Collection<K>)"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'CompositeMap', arg1: 'Map', arg2: 'Map'):
        """public abstract void org.apache.commons.collections4.map.CompositeMap$MapMutator.putAll(org.apache.commons.collections4.map.CompositeMap<K, V>,java.util.Map<K, V>[],java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def put(self, arg0: 'CompositeMap', arg1: 'Map', arg2: object, arg3: object):
        """public abstract V org.apache.commons.collections4.map.CompositeMap$MapMutator.put(org.apache.commons.collections4.map.CompositeMap<K, V>,java.util.Map<K, V>[],K,V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.map.MultiKeyMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.MultiKeyMap as __MultiKeyMap
__MultiKeyMap = __MultiKeyMap
import java.lang.Class as __Class
__Class = __Class
try:
    from pyapache.collections4 import keyvalue
except ImportError:
    keyvalue = __import_once__("pyapache.collections4.keyvalue")

from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class MultiKeyMap(__AbstractMapDecorator, AbstractMapDecorator, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.MultiKeyMap"""
 
    @staticmethod
    def __wrap(java_value: __MultiKeyMap) -> 'MultiKeyMap':
        return MultiKeyMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiKeyMap):
        """
        Dynamic initializer for MultiKeyMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).get(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,K,K,V)"""
        return object.__wrap(super(__MultiKeyMap, self).put(arg0, arg1, arg2, arg3, arg4))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.MultiKeyMap()"""
        val = __MultiKeyMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeAll(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).removeAll(arg0, arg1, arg2))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).get(arg0, arg1, arg2))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def clone(self) -> 'MultiKeyMap':
        """public org.apache.commons.collections4.map.MultiKeyMap<K, V> org.apache.commons.collections4.map.MultiKeyMap.clone()"""
        return 'MultiKeyMap'.__wrap(super(MultiKeyMap, self).clone())

    @staticmethod
    @overload
    def multiKeyMap(arg0: 'AbstractHashedMap') -> 'MultiKeyMap':
        """public static <K,V> org.apache.commons.collections4.map.MultiKeyMap<K, V> org.apache.commons.collections4.map.MultiKeyMap.multiKeyMap(org.apache.commons.collections4.map.AbstractHashedMap<org.apache.commons.collections4.keyvalue.MultiKey<? extends K>, V>)"""
        return MultiKeyMap.__wrap(__MultiKeyMap.multiKeyMap(arg0))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object, arg3: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,K,V)"""
        return object.__wrap(super(__MultiKeyMap, self).put(arg0, arg1, arg2, arg3))

    @overload
    def removeAll(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).removeAll(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def containsKey(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).containsKey(arg0, arg1, arg2, arg3, arg4))

    @overload
    def get(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).get(arg0, arg1, arg2, arg3, arg4))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @overload
    def containsKey(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).containsKey(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @overload
    def removeAll(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).removeAll(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object, arg1: object, arg2: object, arg3: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.get(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).get(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeAll(self, arg0: object, arg1: object, arg2: object, arg3: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.removeAll(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).removeAll(arg0, arg1, arg2, arg3))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).removeMultiKey(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.MultiKeyMap()"""
        val = __MultiKeyMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).removeMultiKey(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,K,K,K,V)"""
        return object.__wrap(super(__MultiKeyMap, self).put(arg0, arg1, arg2, arg3, arg4, arg5))

    @overload
    def containsKey(self, arg0: object, arg1: object, arg2: object, arg3: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).containsKey(arg0, arg1, arg2, arg3))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def containsKey(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiKeyMap.containsKey(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiKeyMap, self).containsKey(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<org.apache.commons.collections4.keyvalue.MultiKey<? extends K>, V> org.apache.commons.collections4.map.MultiKeyMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(MultiKeyMap, self).mapIterator())

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
    def put(self, arg0: 'MultiKey', arg1: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(org.apache.commons.collections4.keyvalue.MultiKey<? extends K>,V)"""
        return object.__wrap(super(__MultiKeyMap, self).put(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.MultiKeyMap.putAll(java.util.Map<? extends org.apache.commons.collections4.keyvalue.MultiKey<? extends K>, ? extends V>)"""
        super(__MultiKeyMap, self).putAll(arg0)

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @overload
    def put(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.put(K,K,V)"""
        return object.__wrap(super(__MultiKeyMap, self).put(arg0, arg1, arg2))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object, arg2: object, arg3: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).removeMultiKey(arg0, arg1, arg2, arg3))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def removeMultiKey(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object:
        """public V org.apache.commons.collections4.map.MultiKeyMap.removeMultiKey(java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__MultiKeyMap, self).removeMultiKey(arg0, arg1, arg2, arg3, arg4)) 
 
 
# CLASS: org.apache.commons.collections4.map.PassiveExpiringMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
import org.apache.commons.collections4.map.PassiveExpiringMap as __PassiveExpiringMap
__PassiveExpiringMap = __PassiveExpiringMap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class PassiveExpiringMap(__AbstractMapDecorator, AbstractMapDecorator, __Serializable, Serializable):
    """org.apache.commons.collections4.map.PassiveExpiringMap"""
 
    @staticmethod
    def __wrap(java_value: __PassiveExpiringMap) -> 'PassiveExpiringMap':
        return PassiveExpiringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PassiveExpiringMap):
        """
        Dynamic initializer for PassiveExpiringMap.
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
    def __init__(self, arg0: 'ExpirationPolicy', arg1: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy<K, V>,java.util.Map<K, V>)"""
        val = __PassiveExpiringMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.PassiveExpiringMap()"""
        val = __PassiveExpiringMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.PassiveExpiringMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__PassiveExpiringMap, self).putAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.PassiveExpiringMap.get(java.lang.Object)"""
        return object.__wrap(super(__PassiveExpiringMap, self).get(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.PassiveExpiringMap()"""
        val = __PassiveExpiringMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'TimeUnit'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long,java.util.concurrent.TimeUnit)"""
        val = __PassiveExpiringMap(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long)"""
        val = __PassiveExpiringMap(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'TimeUnit', arg2: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long,java.util.concurrent.TimeUnit,java.util.Map<K, V>)"""
        val = __PassiveExpiringMap(__long.valueOf(arg0), arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.PassiveExpiringMap.isEmpty()"""
        return bool.__wrap(super(PassiveExpiringMap, self).isEmpty())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(java.util.Map<K, V>)"""
        val = __PassiveExpiringMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ExpirationPolicy'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy<K, V>)"""
        val = __PassiveExpiringMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.PassiveExpiringMap.remove(java.lang.Object)"""
        return object.__wrap(super(__PassiveExpiringMap, self).remove(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.PassiveExpiringMap.keySet()"""
        return 'Set'.__wrap(super(PassiveExpiringMap, self).keySet())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.PassiveExpiringMap.entrySet()"""
        return 'Set'.__wrap(super(PassiveExpiringMap, self).entrySet())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.PassiveExpiringMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__PassiveExpiringMap, self).containsValue(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'Map'):
        """public org.apache.commons.collections4.map.PassiveExpiringMap(long,java.util.Map<K, V>)"""
        val = __PassiveExpiringMap(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.PassiveExpiringMap.put(K,V)"""
        return object.__wrap(super(__PassiveExpiringMap, self).put(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.PassiveExpiringMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__PassiveExpiringMap, self).containsKey(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.PassiveExpiringMap.size()"""
        return int.__wrap(super(PassiveExpiringMap, self).size())

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
    def clear(self):
        """public void org.apache.commons.collections4.map.PassiveExpiringMap.clear()"""
        super(PassiveExpiringMap, self).clear()

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.PassiveExpiringMap.values()"""
        return 'Collection'.__wrap(super(PassiveExpiringMap, self).values())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableOrderedMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.map.UnmodifiableOrderedMap as __UnmodifiableOrderedMap
__UnmodifiableOrderedMap = __UnmodifiableOrderedMap
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import org.apache.commons.collections4.map.AbstractOrderedMapDecorator as __AbstractOrderedMapDecorator
__AbstractOrderedMapDecorator = __AbstractOrderedMapDecorator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.collections4.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableOrderedMap(__AbstractOrderedMapDecorator, AbstractOrderedMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable, __Serializable, Serializable):
    """org.apache.commons.collections4.map.UnmodifiableOrderedMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableOrderedMap) -> 'UnmodifiableOrderedMap':
        return UnmodifiableOrderedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableOrderedMap):
        """
        Dynamic initializer for UnmodifiableOrderedMap.
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
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.UnmodifiableOrderedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(UnmodifiableOrderedMap, self).mapIterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableOrderedMap.clear()"""
        super(UnmodifiableOrderedMap, self).clear()

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.UnmodifiableOrderedMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableOrderedMap, self).keySet())

    @staticmethod
    @overload
    def unmodifiableOrderedMap(arg0: 'OrderedMap') -> 'collections4.OrderedMap':
        """public static <K,V> org.apache.commons.collections4.OrderedMap<K, V> org.apache.commons.collections4.map.UnmodifiableOrderedMap.unmodifiableOrderedMap(org.apache.commons.collections4.OrderedMap<? extends K, ? extends V>)"""
        return collections4.OrderedMap.__wrap(__UnmodifiableOrderedMap.unmodifiableOrderedMap(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractOrderedMapDecorator, self).firstKey())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableOrderedMap.put(K,V)"""
        return object.__wrap(super(__UnmodifiableOrderedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.UnmodifiableOrderedMap.values()"""
        return 'Collection'.__wrap(super(UnmodifiableOrderedMap, self).values())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableOrderedMap.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableOrderedMap, self).entrySet())

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.UnmodifiableOrderedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableOrderedMap, self).putAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractOrderedMapDecorator, self).previousKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractOrderedMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractOrderedMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractOrderedMapDecorator, self).lastKey())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableOrderedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableOrderedMap, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter as __EntrySetToMapIteratorAdapter
__EntrySetToMapIteratorAdapter = __EntrySetToMapIteratorAdapter
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as __AbstractSortedMapDecorator_SortedMapIterator
__SortedMapIterator = __AbstractSortedMapDecorator_SortedMapIterator.SortedMapIterator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SortedMapIterator(__EntrySetToMapIteratorAdapter, EntrySetToMapIteratorAdapter, pyapache.__OrderedMapIterator, collections4.OrderedMapIterator):
    """org.apache.commons.collections4.map.AbstractSortedMapDecorator.SortedMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __SortedMapIterator) -> 'SortedMapIterator':
        return SortedMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedMapIterator):
        """
        Dynamic initializer for SortedMapIterator.
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
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getKey()"""
        return object.__wrap(super(EntrySetToMapIteratorAdapter, self).getKey())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def previous(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator.previous()"""
        return object.__wrap(super(SortedMapIterator, self).previous())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public synchronized void org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator.reset()"""
        super(SortedMapIterator, self).reset()

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.hasNext()"""
        return bool.__wrap(super(EntrySetToMapIteratorAdapter, self).hasNext())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.remove()"""
        super(EntrySetToMapIteratorAdapter, self).remove()

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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.getValue()"""
        return object.__wrap(super(EntrySetToMapIteratorAdapter, self).getValue())

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractSortedMapDecorator$SortedMapIterator.hasPrevious()"""
        return bool.__wrap(super(SortedMapIterator, self).hasPrevious())

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
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.next()"""
        return object.__wrap(super(EntrySetToMapIteratorAdapter, self).next())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.EntrySetToMapIteratorAdapter.setValue(V)"""
        return object.__wrap(super(__EntrySetToMapIteratorAdapter, self).setValue(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.LRUMap
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap
__AbstractLinkedMap = __AbstractLinkedMap
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.LRUMap as __LRUMap
__LRUMap = __LRUMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class LRUMap(__AbstractLinkedMap, AbstractLinkedMap, pyapache.__BoundedMap, collections4.BoundedMap, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.LRUMap"""
 
    @staticmethod
    def __wrap(java_value: __LRUMap) -> 'LRUMap':
        return LRUMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LRUMap):
        """
        Dynamic initializer for LRUMap.
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
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.firstKey()"""
        return object.__wrap(super(AbstractLinkedMap, self).firstKey())

    @overload
    def __init__(self, arg0: 'Map', arg1: bool):
        """public org.apache.commons.collections4.map.LRUMap(java.util.Map<? extends K, ? extends V>,boolean)"""
        val = __LRUMap(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object, arg1: bool) -> object:
        """public V org.apache.commons.collections4.map.LRUMap.get(java.lang.Object,boolean)"""
        return object.__wrap(super(__LRUMap, self).get(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool.__wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.LRUMap()"""
        val = __LRUMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.LRUMap(int)"""
        val = __LRUMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractLinkedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractLinkedMap, self).mapIterator())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsKey(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.LRUMap(int,float)"""
        val = __LRUMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.previousKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractLinkedMap, self).previousKey(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.collections4.map.LRUMap(int,int)"""
        val = __LRUMap(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.LRUMap.get(java.lang.Object)"""
        return object.__wrap(super(__LRUMap, self).get(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'.__wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def isFull(self) -> bool:
        """public boolean org.apache.commons.collections4.map.LRUMap.isFull()"""
        return bool.__wrap(super(LRUMap, self).isFull())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def maxSize(self) -> int:
        """public int org.apache.commons.collections4.map.LRUMap.maxSize()"""
        return int.__wrap(super(LRUMap, self).maxSize())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: bool):
        """public org.apache.commons.collections4.map.LRUMap(int,float,boolean)"""
        val = __LRUMap(__int.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object.__wrap(super(__AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: bool):
        """public org.apache.commons.collections4.map.LRUMap(int,int,float,boolean)"""
        val = __LRUMap(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.LRUMap(java.util.Map<? extends K, ? extends V>)"""
        val = __LRUMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.LRUMap()"""
        val = __LRUMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int.__wrap(super(AbstractHashedMap, self).size())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap.clear()"""
        super(AbstractLinkedMap, self).clear()

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(__Map, self).forEach(arg0)

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public org.apache.commons.collections4.map.LRUMap(int,boolean)"""
        val = __LRUMap(__int.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedMap, self).containsValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.nextKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractLinkedMap, self).nextKey(arg0))

    @overload
    def isScanUntilRemovable(self) -> bool:
        """public boolean org.apache.commons.collections4.map.LRUMap.isScanUntilRemovable()"""
        return bool.__wrap(super(LRUMap, self).isScanUntilRemovable())

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
    def clone(self) -> 'LRUMap':
        """public org.apache.commons.collections4.map.LRUMap<K, V> org.apache.commons.collections4.map.LRUMap.clone()"""
        return 'LRUMap'.__wrap(super(LRUMap, self).clone())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).keySet())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public org.apache.commons.collections4.map.LRUMap(int,int,float)"""
        val = __LRUMap(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.lastKey()"""
        return object.__wrap(super(AbstractLinkedMap, self).lastKey()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractMapDecorator
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractMapDecorator(ABC, __AbstractIterableMap, AbstractIterableMap):
    """org.apache.commons.collections4.map.AbstractMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMapDecorator) -> 'AbstractMapDecorator':
        return AbstractMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMapDecorator):
        """
        Dynamic initializer for AbstractMapDecorator.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMapDecorator, self).putAll(arg0)

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$EntrySetIterator
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_EntrySetIterator
__EntrySetIterator = __AbstractHashedMap_EntrySetIterator.EntrySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.function.Consumer as Consumer
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_HashIterator
__HashIterator = __AbstractHashedMap_HashIterator.HashIterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntrySetIterator(__HashIterator, HashIterator, __Iterator, Iterator):
    """org.apache.commons.collections4.map.AbstractHashedMap.EntrySetIterator"""
 
    @staticmethod
    def __wrap(java_value: __EntrySetIterator) -> 'EntrySetIterator':
        return EntrySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySetIterator):
        """
        Dynamic initializer for EntrySetIterator.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.toString()"""
        return str.__wrap(super(HashIterator, self).toString())

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
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.hasNext()"""
        return bool.__wrap(super(HashIterator, self).hasNext())

    @override
    @overload
    def next(self) -> 'Entry.Map$Entry':
        """public java.util.Map$Entry<K, V> org.apache.commons.collections4.map.AbstractHashedMap$EntrySetIterator.next()"""
        return 'Entry.Map$Entry'.__wrap(super(EntrySetIterator, self).next())

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
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$HashIterator.remove()"""
        super(HashIterator, self).remove()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractSortedMapDecorator
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as __AbstractSortedMapDecorator
__AbstractSortedMapDecorator = __AbstractSortedMapDecorator
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractSortedMapDecorator(ABC, __AbstractMapDecorator, AbstractMapDecorator, pyapache.__IterableSortedMap, collections4.IterableSortedMap):
    """org.apache.commons.collections4.map.AbstractSortedMapDecorator"""
 
    @staticmethod
    def __wrap(java_value: __AbstractSortedMapDecorator) -> 'AbstractSortedMapDecorator':
        return AbstractSortedMapDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractSortedMapDecorator):
        """
        Dynamic initializer for AbstractSortedMapDecorator.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.firstKey()"""
        return object.__wrap(super(AbstractSortedMapDecorator, self).firstKey())

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

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
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractSortedMapDecorator, self).nextKey(arg0))

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.lastKey()"""
        return object.__wrap(super(AbstractSortedMapDecorator, self).lastKey())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractMapDecorator.entrySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).entrySet())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.AbstractSortedMapDecorator.comparator()"""
        return 'Comparator'.__wrap(super(AbstractSortedMapDecorator, self).comparator())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractSortedMapDecorator, self).tailMap(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @overload
    def __init__(self, arg0: 'SortedMap'):
        """public org.apache.commons.collections4.map.AbstractSortedMapDecorator(java.util.SortedMap<K, V>)"""
        val = __AbstractSortedMapDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__AbstractSortedMapDecorator, self).subMap(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.headMap(K)"""
        return 'SortedMap'.__wrap(super(__AbstractSortedMapDecorator, self).headMap(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractSortedMapDecorator, self).previousKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.put(K,V)"""
        return object.__wrap(super(__AbstractMapDecorator, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractSortedMapDecorator, self).mapIterator())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractMapDecorator, self).putAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy
import org.apache.commons.collections4.map.PassiveExpiringMap as __PassiveExpiringMap_ExpirationPolicy
__ExpirationPolicy = __PassiveExpiringMap_ExpirationPolicy.ExpirationPolicy
from abc import abstractmethod, ABC
 
class ExpirationPolicy(ABC, __Serializable, Serializable):
    """org.apache.commons.collections4.map.PassiveExpiringMap.ExpirationPolicy"""
 
    @staticmethod
    def __wrap(java_value: __ExpirationPolicy) -> 'ExpirationPolicy':
        return ExpirationPolicy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExpirationPolicy):
        """
        Dynamic initializer for ExpirationPolicy.
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
    def expirationTime(self, arg0: object, arg1: object):
        """public abstract long org.apache.commons.collections4.map.PassiveExpiringMap$ExpirationPolicy.expirationTime(K,V)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractReferenceMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.AbstractReferenceMap as __AbstractReferenceMap
__AbstractReferenceMap = __AbstractReferenceMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractReferenceMap(ABC, __AbstractHashedMap, AbstractHashedMap):
    """org.apache.commons.collections4.map.AbstractReferenceMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractReferenceMap) -> 'AbstractReferenceMap':
        return AbstractReferenceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractReferenceMap):
        """
        Dynamic initializer for AbstractReferenceMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.isEmpty()"""
        return bool.__wrap(super(AbstractReferenceMap, self).isEmpty())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractReferenceMap.keySet()"""
        return 'Set'.__wrap(super(AbstractReferenceMap, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractReferenceMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractReferenceMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractReferenceMap, self).entrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractReferenceMap.values()"""
        return 'Collection'.__wrap(super(AbstractReferenceMap, self).values())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap.size()"""
        return int.__wrap(super(AbstractReferenceMap, self).size())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractReferenceMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractReferenceMap, self).mapIterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractReferenceMap, self).remove(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractReferenceMap, self).containsValue(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractReferenceMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractReferenceMap.clear()"""
        super(AbstractReferenceMap, self).clear()

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.put(K,V)"""
        return object.__wrap(super(__AbstractReferenceMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$KeySetIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkIterator
__LinkIterator = __AbstractLinkedMap_LinkIterator.LinkIterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_KeySetIterator
__KeySetIterator = __AbstractLinkedMap_KeySetIterator.KeySetIterator
from builtins import int
 
class KeySetIterator(__LinkIterator, LinkIterator, pyapache.__OrderedIterator, collections4.OrderedIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.map.AbstractLinkedMap.KeySetIterator"""
 
    @staticmethod
    def __wrap(java_value: __KeySetIterator) -> 'KeySetIterator':
        return KeySetIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeySetIterator):
        """
        Dynamic initializer for KeySetIterator.
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
    def previous(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$KeySetIterator.previous()"""
        return object.__wrap(super(KeySetIterator, self).previous())

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool.__wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool.__wrap(super(LinkIterator, self).hasPrevious())

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$KeySetIterator.next()"""
        return object.__wrap(super(KeySetIterator, self).next())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str.__wrap(super(LinkIterator, self).toString())

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
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$EntrySet
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_EntrySet
__EntrySet = __AbstractHashedMap_EntrySet.EntrySet
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
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class EntrySet(__AbstractSet, AbstractSet):
    """org.apache.commons.collections4.map.AbstractHashedMap.EntrySet"""
 
    @staticmethod
    def __wrap(java_value: __EntrySet) -> 'EntrySet':
        return EntrySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntrySet):
        """
        Dynamic initializer for EntrySet.
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

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.clear()"""
        super(EntrySet, self).clear()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.iterator()"""
        return 'Iterator'.__wrap(super(EntrySet, self).iterator())

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
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.contains(java.lang.Object)"""
        return bool.__wrap(super(__EntrySet, self).contains(arg0))

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

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__EntrySet, self).remove(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

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
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$EntrySet.size()"""
        return int.__wrap(super(EntrySet, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractHashedMap$KeySet
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
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.function.IntFunction as IntFunction
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap_KeySet
__KeySet = __AbstractHashedMap_KeySet.KeySet
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class KeySet(__AbstractSet, AbstractSet):
    """org.apache.commons.collections4.map.AbstractHashedMap.KeySet"""
 
    @staticmethod
    def __wrap(java_value: __KeySet) -> 'KeySet':
        return KeySet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeySet):
        """
        Dynamic initializer for KeySet.
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

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap$KeySet.clear()"""
        super(KeySet, self).clear()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<K> org.apache.commons.collections4.map.AbstractHashedMap$KeySet.iterator()"""
        return 'Iterator'.__wrap(super(KeySet, self).iterator())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$KeySet.contains(java.lang.Object)"""
        return bool.__wrap(super(__KeySet, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap$KeySet.size()"""
        return int.__wrap(super(KeySet, self).size())

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap$KeySet.remove(java.lang.Object)"""
        return bool.__wrap(super(__KeySet, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.AbstractCollection.toArray(T[])"""
        return List[object].__wrap(super(__AbstractCollection, self).toArray(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode()) 
 
 
# CLASS: org.apache.commons.collections4.map.ReferenceMap
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.commons.collections4.map.ReferenceMap as __ReferenceMap
__ReferenceMap = __ReferenceMap
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.AbstractReferenceMap as __AbstractReferenceMap
__AbstractReferenceMap = __AbstractReferenceMap
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class ReferenceMap(__AbstractReferenceMap, AbstractReferenceMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.ReferenceMap"""
 
    @staticmethod
    def __wrap(java_value: __ReferenceMap) -> 'ReferenceMap':
        return ReferenceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReferenceMap):
        """
        Dynamic initializer for ReferenceMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.isEmpty()"""
        return bool.__wrap(super(AbstractReferenceMap, self).isEmpty())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractReferenceMap.keySet()"""
        return 'Set'.__wrap(super(AbstractReferenceMap, self).keySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.ReferenceMap()"""
        val = __ReferenceMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float)"""
        val = __ReferenceMap(arg0, arg1, __int.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractReferenceMap, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractReferenceMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractReferenceMap, self).entrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength'):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength)"""
        val = __ReferenceMap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractReferenceMap.values()"""
        return 'Collection'.__wrap(super(AbstractReferenceMap, self).values())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractReferenceMap.size()"""
        return int.__wrap(super(AbstractReferenceMap, self).size())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.ReferenceMap()"""
        val = __ReferenceMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: int, arg3: float, arg4: bool):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,int,float,boolean)"""
        val = __ReferenceMap(arg0, arg1, __int.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractReferenceMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractReferenceMap, self).mapIterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractReferenceMap, self).remove(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: 'ReferenceStrength', arg1: 'ReferenceStrength', arg2: bool):
        """public org.apache.commons.collections4.map.ReferenceMap(org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,org.apache.commons.collections4.map.AbstractReferenceMap$ReferenceStrength,boolean)"""
        val = __ReferenceMap(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractReferenceMap, self).containsValue(arg0))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractReferenceMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractReferenceMap, self).containsKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractReferenceMap.clear()"""
        super(AbstractReferenceMap, self).clear()

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractReferenceMap.put(K,V)"""
        return object.__wrap(super(__AbstractReferenceMap, self).put(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.map.MultiValueMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Iterator as Iterator
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
import org.apache.commons.collections4.map.MultiValueMap as __MultiValueMap
__MultiValueMap = __MultiValueMap
from builtins import int
 
class MultiValueMap(__AbstractMapDecorator, AbstractMapDecorator, pyapache.__MultiMap, collections4.MultiMap, __Serializable, Serializable):
    """org.apache.commons.collections4.map.MultiValueMap"""
 
    @staticmethod
    def __wrap(java_value: __MultiValueMap) -> 'MultiValueMap':
        return MultiValueMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiValueMap):
        """
        Dynamic initializer for MultiValueMap.
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
    def containsValue(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.containsValue(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiValueMap, self).containsValue(arg0, arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.MultiValueMap()"""
        val = __MultiValueMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Class') -> 'MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.map.MultiValueMap.multiValueMap(java.util.Map<K, ? super C>,java.lang.Class<C>)"""
        return MultiValueMap.__wrap(__MultiValueMap.multiValueMap(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__MultiValueMap, self).containsValue(arg0))

    @overload
    def getCollection(self, arg0: object) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.MultiValueMap.getCollection(java.lang.Object)"""
        return 'Collection'.__wrap(super(__MultiValueMap, self).getCollection(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.MultiValueMap.iterator()"""
        return 'Iterator'.__wrap(super(MultiValueMap, self).iterator())

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map') -> 'MultiValueMap':
        """public static <K,V> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.map.MultiValueMap.multiValueMap(java.util.Map<K, ? super java.util.Collection<V>>)"""
        return MultiValueMap.__wrap(__MultiValueMap.multiValueMap(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, java.lang.Object>> org.apache.commons.collections4.map.MultiValueMap.entrySet()"""
        return 'Set'.__wrap(super(MultiValueMap, self).entrySet())

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.MultiValueMap.clear()"""
        super(MultiValueMap, self).clear()

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def removeMapping(self, arg0: object, arg1: object) -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.removeMapping(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__MultiValueMap, self).removeMapping(arg0, arg1))

    @overload
    def iterator(self, arg0: object) -> 'Iterator':
        """public java.util.Iterator<V> org.apache.commons.collections4.map.MultiValueMap.iterator(java.lang.Object)"""
        return 'Iterator'.__wrap(super(__MultiValueMap, self).iterator(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def totalSize(self) -> int:
        """public int org.apache.commons.collections4.map.MultiValueMap.totalSize()"""
        return int.__wrap(super(MultiValueMap, self).totalSize())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public java.lang.Object org.apache.commons.collections4.map.MultiValueMap.put(K,java.lang.Object)"""
        return object.__wrap(super(__MultiValueMap, self).put(arg0, arg1))

    @overload
    def putAll(self, arg0: object, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.map.MultiValueMap.putAll(K,java.util.Collection<V>)"""
        return bool.__wrap(super(__MultiValueMap, self).putAll(arg0, arg1))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def size(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.map.MultiValueMap.size(java.lang.Object)"""
        return int.__wrap(super(__MultiValueMap, self).size(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.MultiValueMap.putAll(java.util.Map<? extends K, ?>)"""
        super(__MultiValueMap, self).putAll(arg0)

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
    def __init__(self):
        """public org.apache.commons.collections4.map.MultiValueMap()"""
        val = __MultiValueMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<java.lang.Object> org.apache.commons.collections4.map.MultiValueMap.values()"""
        return 'Collection'.__wrap(super(MultiValueMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @staticmethod
    @overload
    def multiValueMap(arg0: 'Map', arg1: 'Factory') -> 'MultiValueMap':
        """public static <K,V,C extends java.util.Collection<V>> org.apache.commons.collections4.map.MultiValueMap<K, V> org.apache.commons.collections4.map.MultiValueMap.multiValueMap(java.util.Map<K, ? super C>,org.apache.commons.collections4.Factory<C>)"""
        return MultiValueMap.__wrap(__MultiValueMap.multiValueMap(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.UnmodifiableSortedMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.map.AbstractSortedMapDecorator as __AbstractSortedMapDecorator
__AbstractSortedMapDecorator = __AbstractSortedMapDecorator
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map_Entry
__Entry = __Map_Entry.Entry
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.SequencedCollection as SequencedCollection
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Map.Entry as Entry
import java.lang.Class as __Class
__Class = __Class
import java.util.SortedMap as SortedMap
import java.util.SequencedCollection as __SequencedCollection
__SequencedCollection = __SequencedCollection
import java.util.SequencedSet as SequencedSet
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.SortedMap as __SortedMap
__SortedMap = __SortedMap
import org.apache.commons.collections4.map.UnmodifiableSortedMap as __UnmodifiableSortedMap
__UnmodifiableSortedMap = __UnmodifiableSortedMap
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.SequencedMap as __SequencedMap
__SequencedMap = __SequencedMap
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.SequencedSet as __SequencedSet
__SequencedSet = __SequencedSet
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class UnmodifiableSortedMap(__AbstractSortedMapDecorator, AbstractSortedMapDecorator, pyapache.__Unmodifiable, collections4.Unmodifiable, __Serializable, Serializable):
    """org.apache.commons.collections4.map.UnmodifiableSortedMap"""
 
    @staticmethod
    def __wrap(java_value: __UnmodifiableSortedMap) -> 'UnmodifiableSortedMap':
        return UnmodifiableSortedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnmodifiableSortedMap):
        """
        Dynamic initializer for UnmodifiableSortedMap.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.UnmodifiableSortedMap.clear()"""
        super(UnmodifiableSortedMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sequencedEntrySet(self) -> 'SequencedSet':
        """public default java.util.SequencedSet<java.util.Map$Entry<K, V>> java.util.SequencedMap.sequencedEntrySet()"""
        return 'SequencedSet'.__wrap(super(SequencedMap, self).sequencedEntrySet())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @override
    @overload
    def reversed(self) -> 'SortedMap':
        """public default java.util.SortedMap<K, V> java.util.SortedMap.reversed()"""
        return 'SortedMap'.__wrap(super(SortedMap, self).reversed())

    @overload
    def putFirst(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putFirst(K,V)"""
        return object.__wrap(super(__SortedMap, self).putFirst(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableSortedMap.put(K,V)"""
        return object.__wrap(super(__UnmodifiableSortedMap, self).put(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object.__wrap(super(__Map, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.UnmodifiableSortedMap.entrySet()"""
        return 'Set'.__wrap(super(UnmodifiableSortedMap, self).entrySet())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.UnmodifiableSortedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__UnmodifiableSortedMap, self).remove(arg0))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

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
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.nextKey(K)"""
        return object.__wrap(super(__AbstractSortedMapDecorator, self).nextKey(arg0))

    @overload
    def subMap(self, arg0: object, arg1: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.subMap(K,K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableSortedMap, self).subMap(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super K> org.apache.commons.collections4.map.UnmodifiableSortedMap.comparator()"""
        return 'Comparator'.__wrap(super(UnmodifiableSortedMap, self).comparator())

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.UnmodifiableSortedMap.lastKey()"""
        return object.__wrap(super(UnmodifiableSortedMap, self).lastKey())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def putLast(self, arg0: object, arg1: object) -> object:
        """public default V java.util.SortedMap.putLast(K,V)"""
        return object.__wrap(super(__SortedMap, self).putLast(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractSortedMapDecorator.previousKey(K)"""
        return object.__wrap(super(__AbstractSortedMapDecorator, self).previousKey(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

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
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.UnmodifiableSortedMap.firstKey()"""
        return object.__wrap(super(UnmodifiableSortedMap, self).firstKey())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def tailMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.tailMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableSortedMap, self).tailMap(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

    @overload
    def headMap(self, arg0: object) -> 'SortedMap':
        """public java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.headMap(K)"""
        return 'SortedMap'.__wrap(super(__UnmodifiableSortedMap, self).headMap(arg0))

    @staticmethod
    @overload
    def unmodifiableSortedMap(arg0: 'SortedMap') -> 'SortedMap':
        """public static <K,V> java.util.SortedMap<K, V> org.apache.commons.collections4.map.UnmodifiableSortedMap.unmodifiableSortedMap(java.util.SortedMap<K, ? extends V>)"""
        return SortedMap.__wrap(__UnmodifiableSortedMap.unmodifiableSortedMap(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.UnmodifiableSortedMap.keySet()"""
        return 'Set'.__wrap(super(UnmodifiableSortedMap, self).keySet())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.UnmodifiableSortedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__UnmodifiableSortedMap, self).putAll(arg0)

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractSortedMapDecorator.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractSortedMapDecorator, self).mapIterator())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.UnmodifiableSortedMap.values()"""
        return 'Collection'.__wrap(super(UnmodifiableSortedMap, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.apache.commons.collections4.OrderedMapIterator as __OrderedMapIterator
__OrderedMapIterator = __OrderedMapIterator
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap
__AbstractLinkedMap = __AbstractLinkedMap
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class AbstractLinkedMap(ABC, __AbstractHashedMap, AbstractHashedMap, pyapache.__OrderedMap, collections4.OrderedMap):
    """org.apache.commons.collections4.map.AbstractLinkedMap"""
 
    @staticmethod
    def __wrap(java_value: __AbstractLinkedMap) -> 'AbstractLinkedMap':
        return AbstractLinkedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractLinkedMap):
        """
        Dynamic initializer for AbstractLinkedMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @override
    @overload
    def firstKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.firstKey()"""
        return object.__wrap(super(AbstractLinkedMap, self).firstKey())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool.__wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).remove(arg0))

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object.__wrap(super(__AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def mapIterator(self) -> 'collections4.OrderedMapIterator':
        """public org.apache.commons.collections4.OrderedMapIterator<K, V> org.apache.commons.collections4.map.AbstractLinkedMap.mapIterator()"""
        return 'collections4.OrderedMapIterator'.__wrap(super(AbstractLinkedMap, self).mapIterator())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int.__wrap(super(AbstractHashedMap, self).size())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap.clear()"""
        super(AbstractLinkedMap, self).clear()

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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractLinkedMap, self).containsValue(arg0))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def previousKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.previousKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractLinkedMap, self).previousKey(arg0))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @overload
    def nextKey(self, arg0: object) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.nextKey(java.lang.Object)"""
        return object.__wrap(super(__AbstractLinkedMap, self).nextKey(arg0))

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'.__wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).keySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @override
    @overload
    def lastKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap.lastKey()"""
        return object.__wrap(super(AbstractLinkedMap, self).lastKey())

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.CaseInsensitiveMap
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.collections4.map.CaseInsensitiveMap as __CaseInsensitiveMap
__CaseInsensitiveMap = __CaseInsensitiveMap
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import org.apache.commons.collections4.map.AbstractHashedMap as __AbstractHashedMap
__AbstractHashedMap = __AbstractHashedMap
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Float as __float
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class CaseInsensitiveMap(__AbstractHashedMap, AbstractHashedMap, __Serializable, Serializable, __Cloneable, Cloneable):
    """org.apache.commons.collections4.map.CaseInsensitiveMap"""
 
    @staticmethod
    def __wrap(java_value: __CaseInsensitiveMap) -> 'CaseInsensitiveMap':
        return CaseInsensitiveMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CaseInsensitiveMap):
        """
        Dynamic initializer for CaseInsensitiveMap.
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
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsValue(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap()"""
        val = __CaseInsensitiveMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Map'):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap(java.util.Map<? extends K, ? extends V>)"""
        val = __CaseInsensitiveMap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.isEmpty()"""
        return bool.__wrap(super(AbstractHashedMap, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractHashedMap.toString()"""
        return str.__wrap(super(AbstractHashedMap, self).toString())

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).remove(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap(int,float)"""
        val = __CaseInsensitiveMap(__int.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.put(K,V)"""
        return object.__wrap(super(__AbstractHashedMap, self).put(arg0, arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap()"""
        val = __CaseInsensitiveMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.size()"""
        return int.__wrap(super(AbstractHashedMap, self).size())

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractHashedMap.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractHashedMap, self).containsKey(arg0))

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractHashedMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractHashedMap, self).mapIterator())

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

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__AbstractHashedMap, self).putAll(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractHashedMap.hashCode()"""
        return int.__wrap(super(AbstractHashedMap, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractHashedMap.clear()"""
        super(AbstractHashedMap, self).clear()

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
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> org.apache.commons.collections4.map.AbstractHashedMap.entrySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).entrySet())

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @overload
    def __init__(self, arg0: int):
        """public org.apache.commons.collections4.map.CaseInsensitiveMap(int)"""
        val = __CaseInsensitiveMap(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractHashedMap.values()"""
        return 'Collection'.__wrap(super(AbstractHashedMap, self).values())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractHashedMap.keySet()"""
        return 'Set'.__wrap(super(AbstractHashedMap, self).keySet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @overload
    def clone(self) -> 'CaseInsensitiveMap':
        """public org.apache.commons.collections4.map.CaseInsensitiveMap<K, V> org.apache.commons.collections4.map.CaseInsensitiveMap.clone()"""
        return 'CaseInsensitiveMap'.__wrap(super(CaseInsensitiveMap, self).clone())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractHashedMap.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractHashedMap, self).get(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.map.TransformedMap
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import org.apache.commons.collections4.MapIterator as __MapIterator
__MapIterator = __MapIterator
import java.util.Collection as __Collection
__Collection = __Collection
import org.apache.commons.collections4.map.AbstractIterableMap as __AbstractIterableMap
__AbstractIterableMap = __AbstractIterableMap
import java.lang.Class as __Class
__Class = __Class
from builtins import bool
import org.apache.commons.collections4.map.AbstractMapDecorator as __AbstractMapDecorator
__AbstractMapDecorator = __AbstractMapDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
import org.apache.commons.collections4.map.TransformedMap as __TransformedMap
__TransformedMap = __TransformedMap
import java.util.function.BiFunction as BiFunction
try:
    from pyapache import collections4
except ImportError:
    collections4 = __import_once__("pyapache.collections4")

import java.util.Set as Set
import java.lang.Long as __long
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import int
 
class TransformedMap(__AbstractInputCheckedMapDecorator, AbstractInputCheckedMapDecorator, __Serializable, Serializable):
    """org.apache.commons.collections4.map.TransformedMap"""
 
    @staticmethod
    def __wrap(java_value: __TransformedMap) -> 'TransformedMap':
        return TransformedMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformedMap):
        """
        Dynamic initializer for TransformedMap.
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).equals(arg0))

    @overload
    def remove(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.remove(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).remove(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.hashCode()"""
        return int.__wrap(super(AbstractMapDecorator, self).hashCode())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.map.AbstractMapDecorator.size()"""
        return int.__wrap(super(AbstractMapDecorator, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object.__wrap(super(__Map, self).getOrDefault(arg0, arg1))

    @staticmethod
    @overload
    def transformingMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformingMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap.__wrap(__TransformedMap.transformingMap(arg0, arg1, arg2))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object.__wrap(super(__Map, self).replace(arg0, arg1))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractMapDecorator.toString()"""
        return str.__wrap(super(AbstractMapDecorator, self).toString())

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object.__wrap(super(__Map, self).compute(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.isEmpty()"""
        return bool.__wrap(super(AbstractMapDecorator, self).isEmpty())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsKey(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.map.AbstractMapDecorator.clear()"""
        super(AbstractMapDecorator, self).clear()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object.__wrap(super(__Map, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public void org.apache.commons.collections4.map.TransformedMap.putAll(java.util.Map<? extends K, ? extends V>)"""
        super(__TransformedMap, self).putAll(arg0)

    @overload
    def get(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractMapDecorator.get(java.lang.Object)"""
        return object.__wrap(super(__AbstractMapDecorator, self).get(arg0))

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
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Map, self).remove(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> org.apache.commons.collections4.map.AbstractMapDecorator.keySet()"""
        return 'Set'.__wrap(super(AbstractMapDecorator, self).keySet())

    @override
    @overload
    def mapIterator(self) -> 'collections4.MapIterator':
        """public org.apache.commons.collections4.MapIterator<K, V> org.apache.commons.collections4.map.AbstractIterableMap.mapIterator()"""
        return 'collections4.MapIterator'.__wrap(super(AbstractIterableMap, self).mapIterator())

    @staticmethod
    @overload
    def transformedMap(arg0: 'Map', arg1: 'Transformer', arg2: 'Transformer') -> 'TransformedMap':
        """public static <K,V> org.apache.commons.collections4.map.TransformedMap<K, V> org.apache.commons.collections4.map.TransformedMap.transformedMap(java.util.Map<K, V>,org.apache.commons.collections4.Transformer<? super K, ? extends K>,org.apache.commons.collections4.Transformer<? super V, ? extends V>)"""
        return TransformedMap.__wrap(__TransformedMap.transformedMap(arg0, arg1, arg2))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractMapDecorator.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__AbstractMapDecorator, self).containsValue(arg0))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public V org.apache.commons.collections4.map.TransformedMap.put(K,V)"""
        return object.__wrap(super(__TransformedMap, self).put(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool.__wrap(super(__Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> org.apache.commons.collections4.map.AbstractMapDecorator.values()"""
        return 'Collection'.__wrap(super(AbstractMapDecorator, self).values())

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(__Map, self).replaceAll(arg0) 
 
 
# CLASS: org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.function.Consumer as Consumer
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkIterator
__LinkIterator = __AbstractLinkedMap_LinkIterator.LinkIterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.collections4.map.AbstractLinkedMap as __AbstractLinkedMap_LinkMapIterator
__LinkMapIterator = __AbstractLinkedMap_LinkMapIterator.LinkMapIterator
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LinkMapIterator(__LinkIterator, LinkIterator, pyapache.__OrderedMapIterator, collections4.OrderedMapIterator, pyapache.__ResettableIterator, collections4.ResettableIterator):
    """org.apache.commons.collections4.map.AbstractLinkedMap.LinkMapIterator"""
 
    @staticmethod
    def __wrap(java_value: __LinkMapIterator) -> 'LinkMapIterator':
        return LinkMapIterator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinkMapIterator):
        """
        Dynamic initializer for LinkMapIterator.
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
    def getValue(self) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.getValue()"""
        return object.__wrap(super(LinkMapIterator, self).getValue())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hasNext(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasNext()"""
        return bool.__wrap(super(LinkIterator, self).hasNext())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getKey(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.getKey()"""
        return object.__wrap(super(LinkMapIterator, self).getKey())

    @override
    @overload
    def reset(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.reset()"""
        super(LinkIterator, self).reset()

    @override
    @overload
    def hasPrevious(self) -> bool:
        """public boolean org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.hasPrevious()"""
        return bool.__wrap(super(LinkIterator, self).hasPrevious())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.toString()"""
        return str.__wrap(super(LinkIterator, self).toString())

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
    def previous(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.previous()"""
        return object.__wrap(super(LinkMapIterator, self).previous())

    @overload
    def setValue(self, arg0: object) -> object:
        """public V org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.setValue(V)"""
        return object.__wrap(super(__LinkMapIterator, self).setValue(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def remove(self):
        """public void org.apache.commons.collections4.map.AbstractLinkedMap$LinkIterator.remove()"""
        super(LinkIterator, self).remove()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachRemaining(self, arg0: 'Consumer'):
        """public default void java.util.Iterator.forEachRemaining(java.util.function.Consumer<? super E>)"""
        super(__Iterator, self).forEachRemaining(arg0)

    @override
    @overload
    def next(self) -> object:
        """public K org.apache.commons.collections4.map.AbstractLinkedMap$LinkMapIterator.next()"""
        return object.__wrap(super(LinkMapIterator, self).next())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))