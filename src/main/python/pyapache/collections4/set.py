from __future__ import annotations
from overload import overload


 
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.set.MapBackedSet as _MapBackedSet
_MapBackedSet = _MapBackedSet
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
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
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapBackedSet():
    """org.apache.commons.collections4.set.MapBackedSet"""
 
    @staticmethod
    def _wrap(java_value: _MapBackedSet) -> 'MapBackedSet':
        return MapBackedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapBackedSet):
        """
        Dynamic initializer for MapBackedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapBackedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapBackedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.remove(java.lang.Object)"""
        return bool._wrap(super(_MapBackedSet, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.MapBackedSet.hashCode()"""
        return int._wrap(super(MapBackedSet, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.MapBackedSet.clear()"""
        super(MapBackedSet, self).clear()

    @staticmethod
    @overload
    def mapBackedSet(arg0: 'Map') -> 'MapBackedSet':
        """public static <E,V> org.apache.commons.collections4.set.MapBackedSet<E, V> org.apache.commons.collections4.set.MapBackedSet.mapBackedSet(java.util.Map<E, ? super V>)"""
        return MapBackedSet._wrap(_MapBackedSet.mapBackedSet(arg0))

    @staticmethod
    @overload
    def mapBackedSet(arg0: 'Map', arg1: object) -> 'MapBackedSet':
        """public static <E,V> org.apache.commons.collections4.set.MapBackedSet<E, V> org.apache.commons.collections4.set.MapBackedSet.mapBackedSet(java.util.Map<E, ? super V>,V)"""
        return MapBackedSet._wrap(_MapBackedSet.mapBackedSet(arg0, arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.add(E)"""
        return bool._wrap(super(_MapBackedSet, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.MapBackedSet.iterator()"""
        return 'Iterator'._wrap(super(MapBackedSet, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MapBackedSet, self).containsAll(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MapBackedSet, self).retainAll(arg0))

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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.MapBackedSet.toArray()"""
        return List[object]._wrap(super(MapBackedSet, self).toArray())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.set.MapBackedSet.size()"""
        return int._wrap(super(MapBackedSet, self).size())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.MapBackedSet.toArray(T[])"""
        return List[object]._wrap(super(_MapBackedSet, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_MapBackedSet, self).addAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_MapBackedSet, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.contains(java.lang.Object)"""
        return bool._wrap(super(_MapBackedSet, self).contains(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MapBackedSet, self).removeAll(arg0))

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

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.isEmpty()"""
        return bool._wrap(super(MapBackedSet, self).isEmpty())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_MapBackedSet, self).removeIf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.set.MapBackedSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import org.apache.commons.collections4.set.MapBackedSet as _MapBackedSet
_MapBackedSet = _MapBackedSet
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
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
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapBackedSet():
    """org.apache.commons.collections4.set.MapBackedSet"""
 
    @staticmethod
    def _wrap(java_value: _MapBackedSet) -> 'MapBackedSet':
        return MapBackedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapBackedSet):
        """
        Dynamic initializer for MapBackedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapBackedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapBackedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.remove(java.lang.Object)"""
        return bool._wrap(super(_MapBackedSet, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.MapBackedSet.hashCode()"""
        return int._wrap(super(MapBackedSet, self).hashCode())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.MapBackedSet.clear()"""
        super(MapBackedSet, self).clear()

    @staticmethod
    @overload
    def mapBackedSet(arg0: 'Map') -> 'MapBackedSet':
        """public static <E,V> org.apache.commons.collections4.set.MapBackedSet<E, V> org.apache.commons.collections4.set.MapBackedSet.mapBackedSet(java.util.Map<E, ? super V>)"""
        return MapBackedSet._wrap(_MapBackedSet.mapBackedSet(arg0))

    @staticmethod
    @overload
    def mapBackedSet(arg0: 'Map', arg1: object) -> 'MapBackedSet':
        """public static <E,V> org.apache.commons.collections4.set.MapBackedSet<E, V> org.apache.commons.collections4.set.MapBackedSet.mapBackedSet(java.util.Map<E, ? super V>,V)"""
        return MapBackedSet._wrap(_MapBackedSet.mapBackedSet(arg0, arg1))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.add(E)"""
        return bool._wrap(super(_MapBackedSet, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.MapBackedSet.iterator()"""
        return 'Iterator'._wrap(super(MapBackedSet, self).iterator())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MapBackedSet, self).containsAll(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MapBackedSet, self).retainAll(arg0))

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
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.MapBackedSet.toArray()"""
        return List[object]._wrap(super(MapBackedSet, self).toArray())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.set.MapBackedSet.size()"""
        return int._wrap(super(MapBackedSet, self).size())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.MapBackedSet.toArray(T[])"""
        return List[object]._wrap(super(_MapBackedSet, self).toArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_MapBackedSet, self).addAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_MapBackedSet, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.contains(java.lang.Object)"""
        return bool._wrap(super(_MapBackedSet, self).contains(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MapBackedSet, self).removeAll(arg0))

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

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.isEmpty()"""
        return bool._wrap(super(MapBackedSet, self).isEmpty())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.MapBackedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_MapBackedSet, self).removeIf(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

 
 
 
# CLASS: org.apache.commons.collections4.set.MapBackedSet 
 
 
# CLASS: org.apache.commons.collections4.set.TransformedSortedSet
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.set.TransformedSortedSet as _TransformedSortedSet
_TransformedSortedSet = _TransformedSortedSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.set.TransformedSet as _TransformedSet
_TransformedSet = _TransformedSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedSortedSet():
    """org.apache.commons.collections4.set.TransformedSortedSet"""
 
    @staticmethod
    def _wrap(java_value: _TransformedSortedSet) -> 'TransformedSortedSet':
        return TransformedSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedSortedSet):
        """
        Dynamic initializer for TransformedSortedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedSortedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedSortedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object._wrap(super(SortedSet, self).removeFirst())

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.last()"""
        return object._wrap(super(TransformedSortedSet, self).last())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @staticmethod
    @overload
    def transformedSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet._wrap(_TransformedSortedSet.transformedSortedSet(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.headSet(E)"""
        return 'SortedSet'._wrap(super(_TransformedSortedSet, self).headSet(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.TransformedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformedSet, self).equals(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.TransformedSortedSet.comparator()"""
        return 'Comparator'._wrap(super(TransformedSortedSet, self).comparator())

    @staticmethod
    @overload
    def transformingSet(arg0: 'Set', arg1: 'Transformer') -> 'TransformedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSet<E> org.apache.commons.collections4.set.TransformedSet.transformingSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSet._wrap(_TransformedSet.transformingSet(arg0, arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

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
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_TransformedSortedSet, self).subSet(arg0, arg1))

    @staticmethod
    @overload
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.TransformedCollection, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.TransformedSet.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set._wrap(_TransformedSet.transformedSet(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.tailSet(E)"""
        return 'SortedSet'._wrap(super(_TransformedSortedSet, self).tailSet(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformingCollection(arg0, arg1))

    @staticmethod
    @overload
    def transformingSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformingSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet._wrap(_TransformedSortedSet.transformingSortedSet(arg0, arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object._wrap(super(SortedSet, self).removeLast())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.TransformedSet.hashCode()"""
        return int._wrap(super(TransformedSet, self).hashCode())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.first()"""
        return object._wrap(super(TransformedSortedSet, self).first())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'._wrap(super(SortedSet, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractSetDecorator
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSetDecorator():
    """org.apache.commons.collections4.set.AbstractSetDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSetDecorator) -> 'AbstractSetDecorator':
        return AbstractSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSetDecorator):
        """
        Dynamic initializer for AbstractSetDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSetDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSetDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractSerializableSetDecorator
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import org.apache.commons.collections4.set.AbstractSerializableSetDecorator as _AbstractSerializableSetDecorator
_AbstractSerializableSetDecorator = _AbstractSerializableSetDecorator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSerializableSetDecorator():
    """org.apache.commons.collections4.set.AbstractSerializableSetDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSerializableSetDecorator) -> 'AbstractSerializableSetDecorator':
        return AbstractSerializableSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSerializableSetDecorator):
        """
        Dynamic initializer for AbstractSerializableSetDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSerializableSetDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSerializableSetDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.TransformedSet
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.set.TransformedSet as _TransformedSet
_TransformedSet = _TransformedSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedSet():
    """org.apache.commons.collections4.set.TransformedSet"""
 
    @staticmethod
    def _wrap(java_value: _TransformedSet) -> 'TransformedSet':
        return TransformedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedSet):
        """
        Dynamic initializer for TransformedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.TransformedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformedSet, self).equals(arg0))

    @staticmethod
    @overload
    def transformingSet(arg0: 'Set', arg1: 'Transformer') -> 'TransformedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSet<E> org.apache.commons.collections4.set.TransformedSet.transformingSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSet._wrap(_TransformedSet.transformingSet(arg0, arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

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
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.TransformedCollection, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.TransformedSet.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set._wrap(_TransformedSet.transformedSet(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformingCollection(arg0, arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.TransformedSet.hashCode()"""
        return int._wrap(super(TransformedSet, self).hashCode())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractNavigableSetDecorator
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as _AbstractSortedSetDecorator
_AbstractSortedSetDecorator = _AbstractSortedSetDecorator
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.NavigableSet as NavigableSet
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
import java.util.NavigableSet as _NavigableSet
_NavigableSet = _NavigableSet
from typing import List
import java.util.Comparator as Comparator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.collections4.set.AbstractNavigableSetDecorator as _AbstractNavigableSetDecorator
_AbstractNavigableSetDecorator = _AbstractNavigableSetDecorator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractNavigableSetDecorator():
    """org.apache.commons.collections4.set.AbstractNavigableSetDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractNavigableSetDecorator) -> 'AbstractNavigableSetDecorator':
        return AbstractNavigableSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractNavigableSetDecorator):
        """
        Dynamic initializer for AbstractNavigableSetDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractNavigableSetDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractNavigableSetDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollFirst()"""
        return object._wrap(super(AbstractNavigableSetDecorator, self).pollFirst())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object._wrap(super(NavigableSet, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object._wrap(super(NavigableSet, self).removeFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.ceiling(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).ceiling(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_AbstractSortedSetDecorator, self).subSet(arg0, arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.descendingIterator()"""
        return 'Iterator'._wrap(super(AbstractNavigableSetDecorator, self).descendingIterator())

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.floor(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).floor(arg0))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.headSet(E)"""
        return 'SortedSet'._wrap(super(_AbstractSortedSetDecorator, self).headSet(arg0))

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.descendingSet()"""
        return 'NavigableSet'._wrap(super(AbstractNavigableSetDecorator, self).descendingSet())

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).last())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.tailSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_AbstractNavigableSetDecorator, self).tailSet(arg0, _boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.tailSet(E)"""
        return 'SortedSet'._wrap(super(_AbstractSortedSetDecorator, self).tailSet(arg0))

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.higher(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).higher(arg0))

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'._wrap(super(NavigableSet, self).reversed())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.headSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_AbstractNavigableSetDecorator, self).headSet(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.lower(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).lower(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedSetDecorator, self).comparator())

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollLast()"""
        return object._wrap(super(AbstractNavigableSetDecorator, self).pollLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.AbstractNavigableSetDecorator.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'._wrap(super(_AbstractNavigableSetDecorator, self).subSet(arg0, _boolean.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).first())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.AbstractSortedSetDecorator
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as _AbstractSortedSetDecorator
_AbstractSortedSetDecorator = _AbstractSortedSetDecorator
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractSortedSetDecorator():
    """org.apache.commons.collections4.set.AbstractSortedSetDecorator"""
 
    @staticmethod
    def _wrap(java_value: _AbstractSortedSetDecorator) -> 'AbstractSortedSetDecorator':
        return AbstractSortedSetDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractSortedSetDecorator):
        """
        Dynamic initializer for AbstractSortedSetDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractSortedSetDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractSortedSetDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object._wrap(super(SortedSet, self).removeFirst())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.tailSet(E)"""
        return 'SortedSet'._wrap(super(_AbstractSortedSetDecorator, self).tailSet(arg0))

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
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_AbstractSortedSetDecorator, self).subSet(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedSetDecorator, self).comparator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).first())

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.headSet(E)"""
        return 'SortedSet'._wrap(super(_AbstractSortedSetDecorator, self).headSet(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).last())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).addAll(arg0))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object._wrap(super(SortedSet, self).removeLast())

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
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'._wrap(super(SortedSet, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.add(E)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).add(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.TransformedNavigableSet
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.set.TransformedSortedSet as _TransformedSortedSet
_TransformedSortedSet = _TransformedSortedSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.TransformedCollection as _TransformedCollection
_TransformedCollection = _TransformedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.NavigableSet as NavigableSet
import org.apache.commons.collections4.set.TransformedNavigableSet as _TransformedNavigableSet
_TransformedNavigableSet = _TransformedNavigableSet
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
import java.util.NavigableSet as _NavigableSet
_NavigableSet = _NavigableSet
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.set.TransformedSet as _TransformedSet
_TransformedSet = _TransformedSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TransformedNavigableSet():
    """org.apache.commons.collections4.set.TransformedNavigableSet"""
 
    @staticmethod
    def _wrap(java_value: _TransformedNavigableSet) -> 'TransformedNavigableSet':
        return TransformedNavigableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformedNavigableSet):
        """
        Dynamic initializer for TransformedNavigableSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformedNavigableSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformedNavigableSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.tailSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_TransformedNavigableSet, self).tailSet(arg0, _boolean.valueOf(arg1)))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.add(E)"""
        return bool._wrap(super(_collection.TransformedCollection, self).add(arg0))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object._wrap(super(NavigableSet, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object._wrap(super(NavigableSet, self).removeFirst())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.ceiling(E)"""
        return object._wrap(super(_TransformedNavigableSet, self).ceiling(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.TransformedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_TransformedSet, self).equals(arg0))

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
    def transformedCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformedCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformedCollection(arg0, arg1))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.TransformedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.TransformedCollection, self).addAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @staticmethod
    @overload
    def transformedSet(arg0: 'Set', arg1: 'Transformer') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.TransformedSet.transformedSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return Set._wrap(_TransformedSet.transformedSet(arg0, arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'._wrap(super(_TransformedNavigableSet, self).subSet(arg0, _boolean.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.pollLast()"""
        return object._wrap(super(TransformedNavigableSet, self).pollLast())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.tailSet(E)"""
        return 'SortedSet'._wrap(super(_TransformedSortedSet, self).tailSet(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.higher(E)"""
        return object._wrap(super(_TransformedNavigableSet, self).higher(arg0))

    @staticmethod
    @overload
    def transformedNavigableSet(arg0: 'NavigableSet', arg1: 'Transformer') -> 'TransformedNavigableSet':
        """public static <E> org.apache.commons.collections4.set.TransformedNavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.transformedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedNavigableSet._wrap(_TransformedNavigableSet.transformedNavigableSet(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.last()"""
        return object._wrap(super(TransformedSortedSet, self).last())

    @staticmethod
    @overload
    def transformedSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet._wrap(_TransformedSortedSet.transformedSortedSet(arg0, arg1))

    @staticmethod
    @overload
    def transformingNavigableSet(arg0: 'NavigableSet', arg1: 'Transformer') -> 'TransformedNavigableSet':
        """public static <E> org.apache.commons.collections4.set.TransformedNavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.transformingNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedNavigableSet._wrap(_TransformedNavigableSet.transformingNavigableSet(arg0, arg1))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.headSet(E)"""
        return 'SortedSet'._wrap(super(_TransformedSortedSet, self).headSet(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.TransformedSortedSet.comparator()"""
        return 'Comparator'._wrap(super(TransformedSortedSet, self).comparator())

    @staticmethod
    @overload
    def transformingSet(arg0: 'Set', arg1: 'Transformer') -> 'TransformedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSet<E> org.apache.commons.collections4.set.TransformedSet.transformingSet(java.util.Set<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSet._wrap(_TransformedSet.transformingSet(arg0, arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.pollFirst()"""
        return object._wrap(super(TransformedNavigableSet, self).pollFirst())

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'._wrap(super(NavigableSet, self).reversed())

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.headSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_TransformedNavigableSet, self).headSet(arg0, _boolean.valueOf(arg1)))

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_TransformedSortedSet, self).subSet(arg0, arg1))

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.floor(E)"""
        return object._wrap(super(_TransformedNavigableSet, self).floor(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.TransformedNavigableSet.descendingSet()"""
        return 'NavigableSet'._wrap(super(TransformedNavigableSet, self).descendingSet())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.TransformedNavigableSet.descendingIterator()"""
        return 'Iterator'._wrap(super(TransformedNavigableSet, self).descendingIterator())

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @staticmethod
    @overload
    def transformingCollection(arg0: 'Collection', arg1: 'Transformer') -> 'collection.TransformedCollection':
        """public static <E> org.apache.commons.collections4.collection.TransformedCollection<E> org.apache.commons.collections4.collection.TransformedCollection.transformingCollection(java.util.Collection<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return collection.TransformedCollection._wrap(_TransformedCollection.transformingCollection(arg0, arg1))

    @staticmethod
    @overload
    def transformingSortedSet(arg0: 'SortedSet', arg1: 'Transformer') -> 'TransformedSortedSet':
        """public static <E> org.apache.commons.collections4.set.TransformedSortedSet<E> org.apache.commons.collections4.set.TransformedSortedSet.transformingSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Transformer<? super E, ? extends E>)"""
        return TransformedSortedSet._wrap(_TransformedSortedSet.transformingSortedSet(arg0, arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.TransformedNavigableSet.lower(E)"""
        return object._wrap(super(_TransformedNavigableSet, self).lower(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.TransformedSet.hashCode()"""
        return int._wrap(super(TransformedSet, self).hashCode())

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.TransformedSortedSet.first()"""
        return object._wrap(super(TransformedSortedSet, self).first())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableSet
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import org.apache.commons.collections4.set.UnmodifiableSet as _UnmodifiableSet
_UnmodifiableSet = _UnmodifiableSet
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableSet():
    """org.apache.commons.collections4.set.UnmodifiableSet"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableSet) -> 'UnmodifiableSet':
        return UnmodifiableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableSet):
        """
        Dynamic initializer for UnmodifiableSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableSet, self).retainAll(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableSet.clear()"""
        super(UnmodifiableSet, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableSet, self).remove(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableSet, self).removeAll(arg0))

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
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.add(E)"""
        return bool._wrap(super(_UnmodifiableSet, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableSet, self).addAll(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @staticmethod
    @overload
    def unmodifiableSet(arg0: 'Set') -> 'Set':
        """public static <E> java.util.Set<E> org.apache.commons.collections4.set.UnmodifiableSet.unmodifiableSet(java.util.Set<? extends E>)"""
        return Set._wrap(_UnmodifiableSet.unmodifiableSet(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableSet, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableSet.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableSet, self).iterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.set.PredicatedSortedSet
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection
_PredicatedCollection = _PredicatedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.set.PredicatedSet as _PredicatedSet
_PredicatedSet = _PredicatedSet
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection_Builder
_Builder = _PredicatedCollection_Builder.Builder
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.set.PredicatedSortedSet as _PredicatedSortedSet
_PredicatedSortedSet = _PredicatedSortedSet
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedSortedSet():
    """org.apache.commons.collections4.set.PredicatedSortedSet"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedSortedSet) -> 'PredicatedSortedSet':
        return PredicatedSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedSortedSet):
        """
        Dynamic initializer for PredicatedSortedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedSortedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedSortedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object._wrap(super(SortedSet, self).removeFirst())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.PredicatedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedSet, self).equals(arg0))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.headSet(E)"""
        return 'SortedSet'._wrap(super(_PredicatedSortedSet, self).headSet(arg0))

    @staticmethod
    @overload
    def predicatedSortedSet(arg0: 'SortedSet', arg1: 'Predicate') -> 'PredicatedSortedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.predicatedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSortedSet._wrap(_PredicatedSortedSet.predicatedSortedSet(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'PredicatedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSet<E> org.apache.commons.collections4.set.PredicatedSet.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSet._wrap(_PredicatedSet.predicatedSet(arg0, arg1))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.first()"""
        return object._wrap(super(PredicatedSortedSet, self).first())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_PredicatedSortedSet, self).subSet(arg0, arg1))

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
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.last()"""
        return object._wrap(super(PredicatedSortedSet, self).last())

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.notNullBuilder())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection._wrap(_PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.PredicatedSet.hashCode()"""
        return int._wrap(super(PredicatedSet, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object._wrap(super(SortedSet, self).removeLast())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.PredicatedSortedSet.comparator()"""
        return 'Comparator'._wrap(super(PredicatedSortedSet, self).comparator())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.builder(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'._wrap(super(SortedSet, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.tailSet(E)"""
        return 'SortedSet'._wrap(super(_PredicatedSortedSet, self).tailSet(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.CompositeSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.set.CompositeSet as _CompositeSet
_CompositeSet = _CompositeSet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class CompositeSet():
    """org.apache.commons.collections4.set.CompositeSet"""
 
    @staticmethod
    def _wrap(java_value: _CompositeSet) -> 'CompositeSet':
        return CompositeSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CompositeSet):
        """
        Dynamic initializer for CompositeSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CompositeSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CompositeSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.add(E)"""
        return bool._wrap(super(_CompositeSet, self).add(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_CompositeSet, self).addAll(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.set.CompositeSet()"""
        val = _CompositeSet()
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.isEmpty()"""
        return bool._wrap(super(CompositeSet, self).isEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addComposited(self, arg0: 'Set'):
        """public synchronized void org.apache.commons.collections4.set.CompositeSet.addComposited(java.util.Set<E>)"""
        super(_CompositeSet, self).addComposited(arg0)

    @overload
    def removeComposited(self, arg0: 'Set'):
        """public void org.apache.commons.collections4.set.CompositeSet.removeComposited(java.util.Set<E>)"""
        super(_CompositeSet, self).removeComposited(arg0)

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.CompositeSet.iterator()"""
        return 'Iterator'._wrap(super(CompositeSet, self).iterator())

    @overload
    def toSet(self) -> 'Set':
        """public java.util.Set<E> org.apache.commons.collections4.set.CompositeSet.toSet()"""
        return 'Set'._wrap(super(CompositeSet, self).toSet())

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
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CompositeSet, self).containsAll(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_CompositeSet, self).removeIf(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CompositeSet, self).retainAll(arg0))

    @overload
    def __init__(self, arg0: 'Set'):
        """public org.apache.commons.collections4.set.CompositeSet(java.util.Set<E>)"""
        val = _CompositeSet(arg0)
        self.__wrapper = val

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.contains(java.lang.Object)"""
        return bool._wrap(super(_CompositeSet, self).contains(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.CompositeSet.clear()"""
        super(CompositeSet, self).clear()

    @overload
    def getSets(self) -> 'List':
        """public java.util.List<java.util.Set<E>> org.apache.commons.collections4.set.CompositeSet.getSets()"""
        return 'List'._wrap(super(CompositeSet, self).getSets())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addComposited(self, arg0: 'Set', arg1: 'Set'):
        """public void org.apache.commons.collections4.set.CompositeSet.addComposited(java.util.Set<E>,java.util.Set<E>)"""
        super(_CompositeSet, self).addComposited(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, *arg0: 'Set'):
        """public org.apache.commons.collections4.set.CompositeSet(java.util.Set<E>...)"""
        val = _CompositeSet(arg0)
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.set.CompositeSet.size()"""
        return int._wrap(super(CompositeSet, self).size())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.equals(java.lang.Object)"""
        return bool._wrap(super(_CompositeSet, self).equals(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.CompositeSet.toArray(T[])"""
        return List[object]._wrap(super(_CompositeSet, self).toArray(arg0))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_CompositeSet, self).removeAll(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addComposited(self, *arg0: 'Set'):
        """public void org.apache.commons.collections4.set.CompositeSet.addComposited(java.util.Set<E>...)"""
        super(_CompositeSet, self).addComposited(arg0)

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.CompositeSet.toArray()"""
        return List[object]._wrap(super(CompositeSet, self).toArray())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.set.CompositeSet()"""
        val = _CompositeSet()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.CompositeSet.hashCode()"""
        return int._wrap(super(CompositeSet, self).hashCode())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.CompositeSet.remove(java.lang.Object)"""
        return bool._wrap(super(_CompositeSet, self).remove(arg0))

    @overload
    def setMutator(self, arg0: 'SetMutator'):
        """public void org.apache.commons.collections4.set.CompositeSet.setMutator(org.apache.commons.collections4.set.CompositeSet$SetMutator<E>)"""
        super(_CompositeSet, self).setMutator(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableSortedSet
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import org.apache.commons.collections4.set.UnmodifiableSortedSet as _UnmodifiableSortedSet
_UnmodifiableSortedSet = _UnmodifiableSortedSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as _AbstractSortedSetDecorator
_AbstractSortedSetDecorator = _AbstractSortedSetDecorator
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
import java.util.Comparator as Comparator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableSortedSet():
    """org.apache.commons.collections4.set.UnmodifiableSortedSet"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableSortedSet) -> 'UnmodifiableSortedSet':
        return UnmodifiableSortedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableSortedSet):
        """
        Dynamic initializer for UnmodifiableSortedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableSortedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableSortedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.SortedSet.removeFirst()"""
        return object._wrap(super(SortedSet, self).removeFirst())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableSortedSet, self).removeAll(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableSortedSet, self).retainAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableSortedSet.clear()"""
        super(UnmodifiableSortedSet, self).clear()

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
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableSortedSet, self).remove(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @staticmethod
    @overload
    def unmodifiableSortedSet(arg0: 'SortedSet') -> 'SortedSet':
        """public static <E> java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.unmodifiableSortedSet(java.util.SortedSet<E>)"""
        return SortedSet._wrap(_UnmodifiableSortedSet.unmodifiableSortedSet(arg0))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableSortedSet, self).removeIf(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedSetDecorator, self).comparator())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableSortedSet, self).iterator())

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableSortedSet, self).addAll(arg0))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).first())

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).last())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableSortedSet.add(E)"""
        return bool._wrap(super(_UnmodifiableSortedSet, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.SortedSet.removeLast()"""
        return object._wrap(super(SortedSet, self).removeLast())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_UnmodifiableSortedSet, self).subSet(arg0, arg1))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.headSet(E)"""
        return 'SortedSet'._wrap(super(_UnmodifiableSortedSet, self).headSet(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reversed(self) -> 'SortedSet':
        """public default java.util.SortedSet<E> java.util.SortedSet.reversed()"""
        return 'SortedSet'._wrap(super(SortedSet, self).reversed())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableSortedSet.tailSet(E)"""
        return 'SortedSet'._wrap(super(_UnmodifiableSortedSet, self).tailSet(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.PredicatedSet
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection
_PredicatedCollection = _PredicatedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.set.PredicatedSet as _PredicatedSet
_PredicatedSet = _PredicatedSet
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection_Builder
_Builder = _PredicatedCollection_Builder.Builder
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedSet():
    """org.apache.commons.collections4.set.PredicatedSet"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedSet) -> 'PredicatedSet':
        return PredicatedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedSet):
        """
        Dynamic initializer for PredicatedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.PredicatedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedSet, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'PredicatedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSet<E> org.apache.commons.collections4.set.PredicatedSet.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSet._wrap(_PredicatedSet.predicatedSet(arg0, arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

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
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.notNullBuilder())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection._wrap(_PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.PredicatedSet.hashCode()"""
        return int._wrap(super(PredicatedSet, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.builder(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.PredicatedNavigableSet
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection
_PredicatedCollection = _PredicatedCollection
import java.util.Collection as Collection
try:
    from pyapache.collections4 import collection
except ImportError:
    collection = _import_once("pyapache.collections4.collection")

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import org.apache.commons.collections4.set.PredicatedSet as _PredicatedSet
_PredicatedSet = _PredicatedSet
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.NavigableSet as NavigableSet
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
import java.util.NavigableSet as _NavigableSet
_NavigableSet = _NavigableSet
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Comparator as Comparator
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.commons.collections4.collection.PredicatedCollection as _PredicatedCollection_Builder
_Builder = _PredicatedCollection_Builder.Builder
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import org.apache.commons.collections4.set.PredicatedSortedSet as _PredicatedSortedSet
_PredicatedSortedSet = _PredicatedSortedSet
import org.apache.commons.collections4.set.PredicatedNavigableSet as _PredicatedNavigableSet
_PredicatedNavigableSet = _PredicatedNavigableSet
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PredicatedNavigableSet():
    """org.apache.commons.collections4.set.PredicatedNavigableSet"""
 
    @staticmethod
    def _wrap(java_value: _PredicatedNavigableSet) -> 'PredicatedNavigableSet':
        return PredicatedNavigableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredicatedNavigableSet):
        """
        Dynamic initializer for PredicatedNavigableSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredicatedNavigableSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredicatedNavigableSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.headSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_PredicatedNavigableSet, self).headSet(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object._wrap(super(NavigableSet, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object._wrap(super(NavigableSet, self).removeFirst())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.PredicatedSet.equals(java.lang.Object)"""
        return bool._wrap(super(_PredicatedSet, self).equals(arg0))

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.higher(E)"""
        return object._wrap(super(_PredicatedNavigableSet, self).higher(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def predicatedSet(arg0: 'Set', arg1: 'Predicate') -> 'PredicatedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSet<E> org.apache.commons.collections4.set.PredicatedSet.predicatedSet(java.util.Set<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSet._wrap(_PredicatedSet.predicatedSet(arg0, arg1))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.first()"""
        return object._wrap(super(PredicatedSortedSet, self).first())

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_PredicatedSortedSet, self).subSet(arg0, arg1))

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
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'._wrap(super(_PredicatedNavigableSet, self).subSet(arg0, _boolean.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).retainAll(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedSortedSet.last()"""
        return object._wrap(super(PredicatedSortedSet, self).last())

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeAll(arg0))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @staticmethod
    @overload
    def notNullBuilder() -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.notNullBuilder()"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.notNullBuilder())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).removeIf(arg0))

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.floor(E)"""
        return object._wrap(super(_PredicatedNavigableSet, self).floor(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.PredicatedSet.hashCode()"""
        return int._wrap(super(PredicatedSet, self).hashCode())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.add(E)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).add(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.ceiling(E)"""
        return object._wrap(super(_PredicatedNavigableSet, self).ceiling(arg0))

    @overload
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.headSet(E)"""
        return 'SortedSet'._wrap(super(_PredicatedSortedSet, self).headSet(arg0))

    @staticmethod
    @overload
    def predicatedSortedSet(arg0: 'SortedSet', arg1: 'Predicate') -> 'PredicatedSortedSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedSortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.predicatedSortedSet(java.util.SortedSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedSortedSet._wrap(_PredicatedSortedSet.predicatedSortedSet(arg0, arg1))

    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.pollFirst()"""
        return object._wrap(super(PredicatedNavigableSet, self).pollFirst())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.pollLast()"""
        return object._wrap(super(PredicatedNavigableSet, self).pollLast())

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'._wrap(super(NavigableSet, self).reversed())

    @staticmethod
    @overload
    def predicatedNavigableSet(arg0: 'NavigableSet', arg1: 'Predicate') -> 'PredicatedNavigableSet':
        """public static <E> org.apache.commons.collections4.set.PredicatedNavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.predicatedNavigableSet(java.util.NavigableSet<E>,org.apache.commons.collections4.Predicate<? super E>)"""
        return PredicatedNavigableSet._wrap(_PredicatedNavigableSet.predicatedNavigableSet(arg0, arg1))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.collection.AbstractCollectionDecorator.clear()"""
        super(collection.AbstractCollectionDecorator, self).clear()

    @staticmethod
    @overload
    def predicatedCollection(arg0: 'Collection', arg1: 'Predicate') -> 'collection.PredicatedCollection':
        """public static <T> org.apache.commons.collections4.collection.PredicatedCollection<T> org.apache.commons.collections4.collection.PredicatedCollection.predicatedCollection(java.util.Collection<T>,org.apache.commons.collections4.Predicate<? super T>)"""
        return collection.PredicatedCollection._wrap(_PredicatedCollection.predicatedCollection(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.PredicatedNavigableSet.descendingIterator()"""
        return 'Iterator'._wrap(super(PredicatedNavigableSet, self).descendingIterator())

    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.tailSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_PredicatedNavigableSet, self).tailSet(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.collection.AbstractCollectionDecorator.iterator()"""
        return 'Iterator'._wrap(super(collection.AbstractCollectionDecorator, self).iterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.PredicatedNavigableSet.lower(E)"""
        return object._wrap(super(_PredicatedNavigableSet, self).lower(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.PredicatedSortedSet.comparator()"""
        return 'Comparator'._wrap(super(PredicatedSortedSet, self).comparator())

    @staticmethod
    @overload
    def builder(arg0: 'Predicate') -> 'collection.PredicatedCollection$Builder':
        """public static <E> org.apache.commons.collections4.collection.PredicatedCollection$Builder<E> org.apache.commons.collections4.collection.PredicatedCollection.builder(org.apache.commons.collections4.Predicate<? super E>)"""
        return collection.PredicatedCollection$Builder._wrap(_PredicatedCollection.builder(arg0))

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.PredicatedNavigableSet.descendingSet()"""
        return 'NavigableSet'._wrap(super(PredicatedNavigableSet, self).descendingSet())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.remove(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).remove(arg0))

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.PredicatedSortedSet.tailSet(E)"""
        return 'SortedSet'._wrap(super(_PredicatedSortedSet, self).tailSet(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.PredicatedCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_collection.PredicatedCollection, self).addAll(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.set.CompositeSet$SetMutator
import java.util.Set as Set
import org.apache.commons.collections4.set.CompositeSet as _CompositeSet_SetMutator
_SetMutator = _CompositeSet_SetMutator.SetMutator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import java.util.List as List
 
class SetMutator():
    """org.apache.commons.collections4.set.CompositeSet.SetMutator"""
 
    @staticmethod
    def _wrap(java_value: _SetMutator) -> 'SetMutator':
        return SetMutator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetMutator):
        """
        Dynamic initializer for SetMutator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetMutator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetMutator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def addAll(self, arg0: 'CompositeSet', arg1: 'List', arg2: 'Collection'):
        """public abstract boolean org.apache.commons.collections4.set.CompositeSet$SetMutator.addAll(org.apache.commons.collections4.set.CompositeSet<E>,java.util.List<java.util.Set<E>>,java.util.Collection<? extends E>)"""
        pass

    @abstractmethod
    def add(self, arg0: 'CompositeSet', arg1: 'List', arg2: object):
        """public abstract boolean org.apache.commons.collections4.set.CompositeSet$SetMutator.add(org.apache.commons.collections4.set.CompositeSet<E>,java.util.List<java.util.Set<E>>,E)"""
        pass

    @abstractmethod
    def resolveCollision(self, arg0: 'CompositeSet', arg1: 'Set', arg2: 'Set', arg3: 'Collection'):
        """public abstract void org.apache.commons.collections4.set.CompositeSet$SetMutator.resolveCollision(org.apache.commons.collections4.set.CompositeSet<E>,java.util.Set<E>,java.util.Set<E>,java.util.Collection<E>)"""
        pass 
 
 
# CLASS: org.apache.commons.collections4.set.UnmodifiableNavigableSet
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.set.AbstractSortedSetDecorator as _AbstractSortedSetDecorator
_AbstractSortedSetDecorator = _AbstractSortedSetDecorator
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.util.SortedSet as _SortedSet
_SortedSet = _SortedSet
from builtins import str
from pyquantum_helper import override
import java.util.NavigableSet as NavigableSet
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.SortedSet as SortedSet
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
import java.util.Iterator as Iterator
import java.util.NavigableSet as _NavigableSet
_NavigableSet = _NavigableSet
from typing import List
import java.util.Comparator as Comparator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import org.apache.commons.collections4.set.AbstractNavigableSetDecorator as _AbstractNavigableSetDecorator
_AbstractNavigableSetDecorator = _AbstractNavigableSetDecorator
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import org.apache.commons.collections4.set.UnmodifiableNavigableSet as _UnmodifiableNavigableSet
_UnmodifiableNavigableSet = _UnmodifiableNavigableSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnmodifiableNavigableSet():
    """org.apache.commons.collections4.set.UnmodifiableNavigableSet"""
 
    @staticmethod
    def _wrap(java_value: _UnmodifiableNavigableSet) -> 'UnmodifiableNavigableSet':
        return UnmodifiableNavigableSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnmodifiableNavigableSet):
        """
        Dynamic initializer for UnmodifiableNavigableSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnmodifiableNavigableSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnmodifiableNavigableSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def pollFirst(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollFirst()"""
        return object._wrap(super(AbstractNavigableSetDecorator, self).pollFirst())

    @override
    @overload
    def removeLast(self) -> object:
        """public default E java.util.NavigableSet.removeLast()"""
        return object._wrap(super(NavigableSet, self).removeLast())

    @override
    @overload
    def addLast(self, arg0: object):
        """public default void java.util.SortedSet.addLast(E)"""
        super(_SortedSet, self).addLast(arg0)

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_UnmodifiableNavigableSet, self).removeIf(arg0))

    @override
    @overload
    def removeFirst(self) -> object:
        """public default E java.util.NavigableSet.removeFirst()"""
        return object._wrap(super(NavigableSet, self).removeFirst())

    @overload
    def tailSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.tailSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_UnmodifiableNavigableSet, self).tailSet(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.UnmodifiableNavigableSet.clear()"""
        super(UnmodifiableNavigableSet, self).clear()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def ceiling(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.ceiling(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).ceiling(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_UnmodifiableNavigableSet, self).addAll(arg0))

    @override
    @overload
    def addFirst(self, arg0: object):
        """public default void java.util.SortedSet.addFirst(E)"""
        super(_SortedSet, self).addFirst(arg0)

    @overload
    def subSet(self, arg0: object, arg1: bool, arg2: object, arg3: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.subSet(E,boolean,E,boolean)"""
        return 'NavigableSet'._wrap(super(_UnmodifiableNavigableSet, self).subSet(arg0, _boolean.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

    @override
    @overload
    def getLast(self) -> object:
        """public default E java.util.SortedSet.getLast()"""
        return object._wrap(super(SortedSet, self).getLast())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.iterator()"""
        return 'Iterator'._wrap(super(UnmodifiableNavigableSet, self).iterator())

    @override
    @overload
    def descendingSet(self) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.descendingSet()"""
        return 'NavigableSet'._wrap(super(UnmodifiableNavigableSet, self).descendingSet())

    @overload
    def floor(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.floor(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).floor(arg0))

    @override
    @overload
    def last(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.last()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).last())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableNavigableSet, self).retainAll(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.SortedSet.spliterator()"""
        return 'Spliterator'._wrap(super(SortedSet, self).spliterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_UnmodifiableNavigableSet, self).removeAll(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @staticmethod
    @overload
    def unmodifiableNavigableSet(arg0: 'NavigableSet') -> 'NavigableSet':
        """public static <E> java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.unmodifiableNavigableSet(java.util.NavigableSet<E>)"""
        return NavigableSet._wrap(_UnmodifiableNavigableSet.unmodifiableNavigableSet(arg0))

    @overload
    def subSet(self, arg0: object, arg1: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.subSet(E,E)"""
        return 'SortedSet'._wrap(super(_UnmodifiableNavigableSet, self).subSet(arg0, arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def higher(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.higher(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).higher(arg0))

    @override
    @overload
    def reversed(self) -> 'NavigableSet':
        """public default java.util.NavigableSet<E> java.util.NavigableSet.reversed()"""
        return 'NavigableSet'._wrap(super(NavigableSet, self).reversed())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.add(E)"""
        return bool._wrap(super(_UnmodifiableNavigableSet, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray(T[])"""
        return List[object]._wrap(super(_collection.AbstractCollectionDecorator, self).toArray(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.collection.AbstractCollectionDecorator.toString()"""
        return str._wrap(super(collection.AbstractCollectionDecorator, self).toString())

    @overload
    def headSet(self, arg0: object, arg1: bool) -> 'NavigableSet':
        """public java.util.NavigableSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.headSet(E,boolean)"""
        return 'NavigableSet'._wrap(super(_UnmodifiableNavigableSet, self).headSet(arg0, _boolean.valueOf(arg1)))

    @overload
    def lower(self, arg0: object) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.lower(E)"""
        return object._wrap(super(_AbstractNavigableSetDecorator, self).lower(arg0))

    @override
    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<? super E> org.apache.commons.collections4.set.AbstractSortedSetDecorator.comparator()"""
        return 'Comparator'._wrap(super(AbstractSortedSetDecorator, self).comparator())

    @override
    @overload
    def pollLast(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractNavigableSetDecorator.pollLast()"""
        return object._wrap(super(AbstractNavigableSetDecorator, self).pollLast())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFirst(self) -> object:
        """public default E java.util.SortedSet.getFirst()"""
        return object._wrap(super(SortedSet, self).getFirst())

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.UnmodifiableNavigableSet.remove(java.lang.Object)"""
        return bool._wrap(super(_UnmodifiableNavigableSet, self).remove(arg0))

    @override
    @overload
    def first(self) -> object:
        """public E org.apache.commons.collections4.set.AbstractSortedSetDecorator.first()"""
        return object._wrap(super(AbstractSortedSetDecorator, self).first())

    @override
    @overload
    def descendingIterator(self) -> 'Iterator':
        """public java.util.Iterator<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.descendingIterator()"""
        return 'Iterator'._wrap(super(UnmodifiableNavigableSet, self).descendingIterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.collection.AbstractCollectionDecorator.toArray()"""
        return List[object]._wrap(super(collection.AbstractCollectionDecorator, self).toArray())

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
    def headSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.headSet(E)"""
        return 'SortedSet'._wrap(super(_UnmodifiableNavigableSet, self).headSet(arg0))

    @overload
    def tailSet(self, arg0: object) -> 'SortedSet':
        """public java.util.SortedSet<E> org.apache.commons.collections4.set.UnmodifiableNavigableSet.tailSet(E)"""
        return 'SortedSet'._wrap(super(_UnmodifiableNavigableSet, self).tailSet(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.commons.collections4.set.ListOrderedSet
from pyquantum_helper import import_once as _import_once
import org.apache.commons.collections4.set.AbstractSetDecorator as _AbstractSetDecorator
_AbstractSetDecorator = _AbstractSetDecorator
import java.util.function.Predicate as Predicate
import org.apache.commons.collections4.set.ListOrderedSet as _ListOrderedSet
_ListOrderedSet = _ListOrderedSet
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import org.apache.commons.collections4.OrderedIterator as _OrderedIterator
_OrderedIterator = _OrderedIterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.collections4.collection.AbstractCollectionDecorator as _AbstractCollectionDecorator
_AbstractCollectionDecorator = _AbstractCollectionDecorator
from typing import List
try:
    from pyapache import collections4
except ImportError:
    collections4 = _import_once("pyapache.collections4")

import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class ListOrderedSet():
    """org.apache.commons.collections4.set.ListOrderedSet"""
 
    @staticmethod
    def _wrap(java_value: _ListOrderedSet) -> 'ListOrderedSet':
        return ListOrderedSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ListOrderedSet):
        """
        Dynamic initializer for ListOrderedSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ListOrderedSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ListOrderedSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def add(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.add(E)"""
        return bool._wrap(super(_ListOrderedSet, self).add(arg0))

    @override
    @overload
    def clear(self):
        """public void org.apache.commons.collections4.set.ListOrderedSet.clear()"""
        super(ListOrderedSet, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def indexOf(self, arg0: object) -> int:
        """public int org.apache.commons.collections4.set.ListOrderedSet.indexOf(java.lang.Object)"""
        return int._wrap(super(_ListOrderedSet, self).indexOf(arg0))

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ListOrderedSet, self).addAll(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def asList(self) -> 'List':
        """public java.util.List<E> org.apache.commons.collections4.set.ListOrderedSet.asList()"""
        return 'List'._wrap(super(ListOrderedSet, self).asList())

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] org.apache.commons.collections4.set.ListOrderedSet.toArray(T[])"""
        return List[object]._wrap(super(_ListOrderedSet, self).toArray(arg0))

    @staticmethod
    @overload
    def listOrderedSet(arg0: 'List') -> 'ListOrderedSet':
        """public static <E> org.apache.commons.collections4.set.ListOrderedSet<E> org.apache.commons.collections4.set.ListOrderedSet.listOrderedSet(java.util.List<E>)"""
        return ListOrderedSet._wrap(_ListOrderedSet.listOrderedSet(arg0))

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
    def listOrderedSet(arg0: 'Set', arg1: 'List') -> 'ListOrderedSet':
        """public static <E> org.apache.commons.collections4.set.ListOrderedSet<E> org.apache.commons.collections4.set.ListOrderedSet.listOrderedSet(java.util.Set<E>,java.util.List<E>)"""
        return ListOrderedSet._wrap(_ListOrderedSet.listOrderedSet(arg0, arg1))

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ListOrderedSet, self).removeAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.collections4.set.AbstractSetDecorator.hashCode()"""
        return int._wrap(super(AbstractSetDecorator, self).hashCode())

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_ListOrderedSet, self).retainAll(arg0))

    @overload
    def get(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.set.ListOrderedSet.get(int)"""
        return object._wrap(super(_ListOrderedSet, self).get(_int.valueOf(arg0)))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).containsAll(arg0))

    @staticmethod
    @overload
    def listOrderedSet(arg0: 'Set') -> 'ListOrderedSet':
        """public static <E> org.apache.commons.collections4.set.ListOrderedSet<E> org.apache.commons.collections4.set.ListOrderedSet.listOrderedSet(java.util.Set<E>)"""
        return ListOrderedSet._wrap(_ListOrderedSet.listOrderedSet(arg0))

    @overload
    def remove(self, arg0: int) -> object:
        """public E org.apache.commons.collections4.set.ListOrderedSet.remove(int)"""
        return object._wrap(super(_ListOrderedSet, self).remove(_int.valueOf(arg0)))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_ListOrderedSet, self).removeIf(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.remove(java.lang.Object)"""
        return bool._wrap(super(_ListOrderedSet, self).remove(arg0))

    @overload
    def addAll(self, arg0: int, arg1: 'Collection') -> bool:
        """public boolean org.apache.commons.collections4.set.ListOrderedSet.addAll(int,java.util.Collection<? extends E>)"""
        return bool._wrap(super(_ListOrderedSet, self).addAll(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'collections4.OrderedIterator':
        """public org.apache.commons.collections4.OrderedIterator<E> org.apache.commons.collections4.set.ListOrderedSet.iterator()"""
        return 'collections4.OrderedIterator'._wrap(super(ListOrderedSet, self).iterator())

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.set.ListOrderedSet()"""
        val = _ListOrderedSet()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.collections4.set.ListOrderedSet.toString()"""
        return str._wrap(super(ListOrderedSet, self).toString())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.contains(java.lang.Object)"""
        return bool._wrap(super(_collection.AbstractCollectionDecorator, self).contains(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.commons.collections4.collection.AbstractCollectionDecorator.size()"""
        return int._wrap(super(collection.AbstractCollectionDecorator, self).size())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.set.ListOrderedSet()"""
        val = _ListOrderedSet()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.commons.collections4.set.ListOrderedSet.toArray()"""
        return List[object]._wrap(super(ListOrderedSet, self).toArray())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.commons.collections4.collection.AbstractCollectionDecorator.isEmpty()"""
        return bool._wrap(super(collection.AbstractCollectionDecorator, self).isEmpty())

    @overload
    def add(self, arg0: int, arg1: object):
        """public void org.apache.commons.collections4.set.ListOrderedSet.add(int,E)"""
        super(_ListOrderedSet, self).add(_int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.collections4.set.AbstractSetDecorator.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSetDecorator, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)